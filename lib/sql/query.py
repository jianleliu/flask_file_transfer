"""All sql queries goes here."""

from cgi import FieldStorage
import subprocess
import mysql.connector
from werkzeug.utils import secure_filename

from config import DatabaseConfig, SuperUser

#Start a connect with mysql.
mydb = mysql.connector.connect(
                            user=DatabaseConfig.USER,
                            database=DatabaseConfig.DATABASE,
                            password=DatabaseConfig.PASSWORD,
                            host=DatabaseConfig.HOST,
                        )

def read_file(file: FieldStorage) -> tuple:
    """reads the filestorage object.
    ! can be improved with better readability.
    @param file: filestorage object to be read.

    @return: a tuple(bytes -> hex object, file_size of bytes, units -> B, KB, MB).
    """
    data = file.read()
    file_size = len(data)
    unit = 'B'
    # 1000 bytes = 1 KB.
    if file_size >= 1000:
        # if it's over 1 mil bytes
        if file_size >= 1000 * 1000:
            unit = 'MB'
            file_size = round(file_size/(1000*1000), 2)
        #if over 1000 bytes -> KB
        else:
            unit = 'KB'
            file_size = round(file_size/1000, 2)
    return (data.hex(), file_size, unit)

def get_max_allowed_packet() -> int:
    """Get the max_allowed_packet parameter in mysql DB.

    @return the value INT.
    """
    cursor = mydb.cursor()
    cursor.execute('show variables like "max_allowed_packet"')
    data = cursor.fetchall()[0][1]
    cursor.close()
    mydb.commit()
    print(data)
    return int(data)

def max_allowed_packet(bytes_):
    """Change the max_allowed_packet parameter through sql coection.

    @bytes value changed to.
    """
    #Execute SQL query.
    cursor = mydb.cursor()
    cursor.execute(f'set global max_allowed_packet={bytes_}')
    cursor.close()
    mydb.commit()
    #Restart mySQL server connection.
    cursor = mydb.cursor()
    cursor.execute('show variables like "max_allowed_packet"')
    cursor.close()
    mydb.commit()
    subprocess.call([
        'echo', SuperUser.PASSWORD,
        '|',
        'sudo', '-S', 'service', 'mysql', 'restart']
        )
    mydb.close()

def insert(file: FieldStorage, username='No Name'):
    """insert one row into the database

    @param File: fieldstorage object
    @param username: str, default is 'No Name'
    """
    #Process the file
    result_tuple = read_file(file)  # returns a tuple
    lis = secure_filename(file.filename).split(
        '.')  # splits the filename and format type

    #Variables
    data = str(result_tuple[0])
    filesize = result_tuple[1]
    unit = result_tuple[2]
    filename = lis[0]
    filetype = lis[-1]
    user = username
    print(username)
    #Query
    cursor = mydb.cursor()
    query = "insert into FileRecord (Date, Data, UserName, FileType, \
            FileSize, Unit, FileName) values (now(), unhex(%s), %s, %s, %s, %s, %s);"
    val = (data, user, filetype, filesize, unit, filename)
    cursor.execute(query, val)
    mydb.commit()
    cursor.close()

def get_all() -> list:
    """retrieve all the rows in the table without data column

    @return a list of tuple (Date, UserName, FileType, FileSize, Unit, 
        FileName, ID)
    """
    cursor = mydb.cursor()
    query = "select Date, UserName, FileType, FileSize, Unit, FileName,\
          ID from FileRecord;"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

def get_all_data() -> list:
    """retrieve all the rows in the table

    @return a list of tuple (Date, Data, UserName, FileType,
                             FileSize, Unit, FileName, ID)
    """
    cursor = mydb.cursor()
    query = "select * from FileRecord;"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

def get_row_by_id(id_):
    """retrieve a row from files based on the file ID

    @param id_: ID of the file, stored in the database
    @return a tuple (Date, Data, UserName, FileType, FileSize, Unit, 
        FileName, ID)
    """
    cursor = mydb.cursor()
    query = f"select * from FileRecord where ID = {id_};"
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    return result

def get_file_by_id(id_):
    """retrieve a file's byte string with its given ID

    @param id_: unique ID given to every file in a DB
    @return the file in byte string format
        None, if not found
    """
    cursor = mydb.cursor()
    query = f'select Data from FileRecord where ID = {id_};'
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    return result

def get_file(filename, file_type: str, id_):
    """retrieve a file's byte string with @filename, @file_type, @id
    !!!unusable, unable to locate specific row in the db
    *try not to use f string and use val instead(look at other function).

    @param filename: the filename in the database
    @param file_type: the file extension
    @param id_: the file id in the db

    @return byte string
        None, if not found
    """
    cursor = mydb.cursor()
    query = (f"select Data from FileRecord where (ID = {id_} AND",
                f"FileName = {filename} AND FileType = {file_type});")
    cursor.execute(query)
    data = cursor.fetchone()
    cursor.close()
    return data

def get_table_data():
    """retrieve all column except for Data in files DB

    @return a tuple (Date, UserName, FileType, FileSize, Unit, FileName, ID)
    """
    cursor = mydb.cursor()
    query = 'select (Date, UserName, FileType, FileSize, Unit, FileName, ID) \
            from FileRecord;'
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result
