from db import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def validate_api_user(user):


    check_user = User.query.filter_by(username=user).first()
    if (check_user == 0):
            return None
    else:
        result = check_user
        return result
    
def validate_api_password(user, password):

    userdata = User.query.filter_by(username=user).first()


    if userdata:
        pass2 = userdata.password
        if bcrypt.check_password_hash(pass2, password):
            result = 'login succesful'
            return result
        else:
            
            return None

     