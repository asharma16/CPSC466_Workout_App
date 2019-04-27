# CPSC466_Workout_App

Source: https://scotch.io/tutorials/authentication-and-authorization-with-flask-login
Three main packages needed to run the project:
1. Flask
2. Flask-Login
3. Flask-SQLAlchemy
In order to run the application on virtualenv:
export FLASK_APP=project name
export FLASK_DEBUG
flask run

********************************************************************

For Windows OS, assume the repository is on Desktop:

    Powershell:
        Open Powershell (no need to run as administrator).
        Its default path should be at the user folder, so run command " cd ./Desktop/CPSC466_Workout_App " or " cd ./Your_download_folder/CPSC466_Workout_App ", you can use "Tab" key to automatically complete the file/folder name.
        Next run command " $env:FLASK_APP = "project" " (must have quotation marks around the word project, "project" indicates to the project folder inside our repository root folder; also 'FLASK_APP' can be all lowercases and no spaces around '=' is OK).
        Finally you can run command " flask run ", the " FLASK_DEBUG = 1 " command is optional.

    Command Prompt, CMD:
        Open CMD (no need to run as administrator).
        Its default path should also be at the user folder, so again, run command " cd ./Desktop/CPSC466_Workout_App " or " cd ./Your_download_folder/CPSC466_Workout_App ".
        Next run command " set FLASK_APP=project " (must have no spaces around '=').
        Finally you can run command " flask run ", the " set FLASK_DEBUG=1 " command is also optional.
