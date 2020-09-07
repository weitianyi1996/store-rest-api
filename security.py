from models.user import UserModel



def authenticate(username, password):
    user = UserModel.find_by_username(username)  # create user instance using sql data
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload["identity"]  # use return JW token to get user id, check if JWT token is correct
    return UserModel.find_by_userid(user_id)


