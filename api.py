"""Checks incoming requests, error handling. """
from app import web
import server

@web.route('/')
def page_home():
    """handles user request to a page."""
    return server.page_home()

@web.route('/upload')
def page_upload():
    """handles user request to a page."""
    return server.page_upload()

@web.route('/upload', methods=['GET', 'POST'])
def upload():
    """handles user POST request to upload."""
    return server.upload()

@web.route('/result')
def page_result(result):
    """display the result/message based on the param

    @param result: the message to display"""
    return server.page_result(result)


@web.route('/api/downloadable')
def return_table_data():
    """Loads a table of downloadables, requested by js."""
    return server.return_table_data()

@web.route('/api/download/<file_name>.<file_type>@ID=<id_>')
def return_file(file_name, file_type, id_):
    """Retrieves data file from DB and return it."""
    return server.return_file(file_name, file_type, id_)
