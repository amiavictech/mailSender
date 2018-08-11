# mailSender - AMIA Mail Sender App #

## Install python virtual environment
>virtualenv -p path-to-python-bin-folder venv

## To activate
>source venv/bin/activate

## Following are the python dependencies of this project
install using pip install command
> pip install openpyxl google-api-python-client oauth2client

## To run the app activate the virtual environment and issue 
> python init.py

## To create binary file for windows or macos, issue the following commands
>pip install pyinstaller

>pyinstaller --onefile init.py
