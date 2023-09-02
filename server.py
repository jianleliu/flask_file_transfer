"""Server, processes all the data."""

from io import BytesIO

from flask import render_template, request, jsonify, send_file

from lib.sql.query import get_all, get_file_by_id, insert

def page_home():
    """returns the home page html"""
    return render_template('home.html')

def page_upload():
    """returns the upload page html"""
    return render_template('upload.html')

def upload():
    """handles the user file upload, redirect user to the result page
    """
    file = None
    username = 'No Name'
    result = None
    #Check if the request is POST.
    if request.method == 'POST':
        #Check if the file is actually selected.
        if 'file' in request.files:
            file = request.files['file']
            #Check if username is entered
            if request.form['username'].strip() != '':
                username = request.form['username']
            #Process a query
            insert(file, username)
            result = 'success'
        else:
            result = 'failed'
    return page_result(result)

def return_file(file_name, file_type, id_):
    """Generates a encrypted temporary url for user to download from."""
    data = get_file_by_id(id_)[0]
    # If file is found, return it, else redirect to another page.
    if data:
        return send_file(BytesIO(data),
                         download_name=f'{file_name}.{file_type}',
                         as_attachment=True)
    return page_result('file not found.')

def return_table_data():
    """Loads a table of downloadables, requested by js."""
    data = get_all()
    print(data)
    return jsonify([{"date": t[0].strftime("%H:%M, %m/%d/%Y"),
                    "username": t[1], "file_type": t[2],
                     "file_size": t[3], "unit": t[4], "file_name": t[5],
                     "id": t[6]} for t in data])

def page_result(result):
    """Display the result/message based on the param

    @param result: the message to display"""

    return f'<p>{result}</p>'
