"""
This module defines crud operations to work with admin table
"""
from Messanger.models.User import Authorize
from Messanger import database


def get_user_by_name(login: str) -> str:
    """
    This function is used to get the single user by UUID
    :param login: the username of the user to get
    :return: the user  with the specified username
    """
    user = Authorize.query.filter_by(login=login).first()
    return user if user else None


def get_user_by_phone(phone: str) -> str:
    """
    This function is used to get the single user by UUID
    :param phone: the username of the user to get
    :return: the user  with the specified username
    """
    user = Authorize.query.filter_by(phone=phone).first()
    return user if user else None


def authorize_user(password: str, login: str, UUID, phone: str):
    """
    This function authorize user in database
    :param password: user password to register
    :param login: user password
    :param UUID: uuid identifier of user
    :return: None
    """
    user = Authorize(password=password, login=login, UUID=UUID, phone=phone)
    database.session.add(user)
    database.session.commit()


def delete_user(id: str):
    """
    This function deletes all user info
    :param id: user identifier
    """
    user = Authorize.query.filter_by(UUID=id).first()
    database.session.delete(user)
    database.session.commit()
