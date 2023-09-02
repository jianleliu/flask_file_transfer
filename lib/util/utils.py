"""A module to store reusable functions."""

from cgi import FieldStorage
from json import dump

from flask import url_for

def to_bin(file):
    """converts a input file to bytes.
    
    @param file filedescriptor or path.
    
    @return a binary buffer.
    """
    file_data = None
    #Read input and convert into bytes.
    with open(file, 'rb') as f:
        file_data = f.read()
    return file_data

def to_file(file_name, file_data: bytes, file_extension):
    """convert the byte object to file.
    
    @param name: the name of the output file.
    @param bin: bytes object as input.
    @param type: filetype.
    """
    #writes bytes to specific file
    with open(f'{file_name}.{file_extension}', 'wb') as f:
        f.write(file_data)

def read_file(file: FieldStorage) -> tuple:
    """reads the filestorage object.
    
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

def create_json(data, filename):
    """dumps the data into a json object.
    
    @data dumpable data structure.
    """
    with open(url_for('static', filename=f'json/{filename}'), 'wb') as f:
        dump(data, f)
