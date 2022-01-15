'''
This moduke describes user profile
'''
from Messanger import database


class Profile(database.Model):
    __tablename__ = 'userprofile'

    #: user identifier
    id = database.Column(database.Integer(), primary_key=True)

    #: user Name
    name = database.Column(database.String(length=255), nullable=False)

    #: user Surname
    surname = database.Column(database.String(length=255), nullable=False)

    #: user avatar
    avatar = database.Column(database.BLOB())

    #: user location
    location = database.Column(database.String(length=255))

    #: user email
    email = database.Column(database.String(length=255), nullable=False)

    #: user info
    identifier = database.Column(database.Integer, database.ForeignKey('user.id'))

    def json(self):
        """
        This method is used to return the employee in json format
        :return: the employee in json format
        """
        # pylint: disable=no-member
        return {
            'name': self.name,
            'surname': self.surname,
            'avatar': self.avatar,
            'location': self.location,
            'email': self.email,
            'identifier': self.identifier
        }
