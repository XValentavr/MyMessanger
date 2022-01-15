'''
This moduke describes user profile
'''
from Messanger import database


class Profile(database.Model):
    __tablename__ = 'userprofile'

    #: user identifier
    id = database.Column(database.Integer(), primary_key=True)

    #: user Name
    Name = database.Column(database.String(length=255), nullable=False)

    #: user Surname
    Surname = database.Column(database.String(length=255), nullable=False)

    #: user avatar
    Avatar = database.Column(database.BLOB(), nullable=False)
