from flask_login import UserMixin

from Messanger import database


class Authorize(UserMixin, database.Model):
    __tablename__ = 'user'

    #: user identifier
    id = database.Column(database.Integer(), primary_key=True)

    #: user password
    password = database.Column(database.String(length=255), nullable=False, unique=True)

    #: user login
    login = database.Column(database.String(length=255), nullable=False)

    #: user phone
    phone = database.Column(database.String(length=255), nullable=False, unique=True)

    #: user UUID
    UUID = database.Column(database.String(length=255))

    def __init__(self,password, login, phone, UUID):
        self.password = password
        self.login = login
        self.phone = phone
        self.UUID = UUID

    def json(self):
        """
        This method is used to return the employee in json format
        :return: the employee in json format
        """
        # pylint: disable=no-member
        return {
            'password': self.password,
            'login': self.login,
            'phone': self.phone,
        }
