# flask_file_transfer
A simple flask file storing/retrieving web application using MySQL as database and jQuery for web end rendering. 

# Instructions
1. **Setup MySQL**
   - Download MySQL from the official website.
     - Run it, either with command line or GUI(workbench)
     - Execute the "flask_project_FileRecord.sql" schema.
2. **Setup venv**
    - globally: 
        1. pip install -r requirements.txt
        2. python3 /path/to/run.py
     - virtual environment: 
        1. python3 -m venv "Replace with a name with no double quotes"
        2. Source path/to/venv/bin/activate
        3. path/to/venv/bin/pip install -r requirements.txt 
        4. path/to/venv/bin/python3 run.py

  # Improvements
  1. Containerize the entire application, preferably a multistage dockerfile including MySQL.
  2. Add a user login feature and database table.
  3. Write tests.
  4. Implement dashboard.
  5. Implement try-except blocks.
