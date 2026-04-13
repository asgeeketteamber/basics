import os
from flask import Flask 

def create_app(test_config=None):
    #create and configure the app
    app=Flask(__name__,instance_relative_config=True) #essentially the entire web application 
     #creates flask instance
       #name= name of the current python module(the app needs to know where it's located to set up some paths and __name__ is th eway to do that )
       #instannce_relative_configuration=true-tells the app that the configuration files are relative to the instance folder
       #instance folder- located outside flaskr and holds local data that shouldnt be comitted to version control
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path,'flaskr.sqlite')
    )
    #app.congig.from_mapping()-sets so default configuration that the app will use 
    #secret key-used by flask and extensions to keep data save it is set to dev to provide convinient value during development but it should be overriden with a random value while deploying
    #database- the path where sqlite database file will be saved. it is under app_instance_path 
    if test_config is None:
        #load the instance config, if it exists, when not testing 
        app.config.from_pyfile('config.py',silent=True)
    else:
        #load the test config if passed in 
        app.config.from_mapping(test_config)
    #app.config.from_pyfile()-

    #ensure that the instance folder exists 
    os.makedirs(app.instance_path,exist_ok=True)
    #os.makedirs()-ensure that app.instance_path exists
    from . import db 
    db.init_app(app)
    #a neat package that connects all the database related setup to the 
    #Flask app once it has been created


    #a simplepage that says hello 
    @app.route('/hello')
    def hello():
        return "hello homies <3"
        #simple route that allows user to see application i swokring byt saying hello 

    return app