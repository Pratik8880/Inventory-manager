from flask import Blueprint
from controllers.user_controller import login_user,logout_user   #actual logic for handling the login/logout from user_controller.py

user_routes = Blueprint('user',__name__) # for crating a blueprint object named user

@user_routes.route('/login', methods=['GET','POST']) #defining a route login for both GET and POST request
def login():
    return login_user()

@user_routes.route('/logout')  #logouts and clear the session to redirect them 
def logout():
    return logout_user()



