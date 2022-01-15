"""
This module defines crud operations to work with profile table
"""
from flask import url_for

from Messanger.models.UserProfile import Profile
from Messanger import database, create_app


def get_profiles(identifier: int) -> list:
    """
    This function is used to select all records from hospital table
    :return: the list of all departments of hospital
    """
    profiles = Profile.query.filter_by(identifier=identifier).first()
    return profiles.json() if profiles is not None else None


def add_profile(name: str, lastname: str, location: str, email: str, identifier: int) -> None:
    """
    this module updates user profile
    :param name: user name
    :param lastname: user last name
    :param location: user location
    :param email: user email
    """
    profile = Profile(name=name, lastname=lastname, location=location, email=email, identifier=identifier)
    database.session.add(profile)
    database.session.commit()


def update_profile(id: int, name: str, lastname: str, location: str, email: str) -> None:
    """
    this module updates user profile
    :param: id: user identifier
    :param name: user name
    :param lastname: user last name
    :param avatar: user avatar
    :param location: user location
    :param email: user email
    """
    profile = Profile.query.get_or_404(id)
    profile.name = name
    profile.lastname = lastname
    profile.location = location
    profile.email = email
    database.session.add(profile)
    database.session.commit()


def delete_profile(id: int) -> None:
    """
    This function is used to delete an existing department
    :param id: the id of the profile to delete
    """
    profile = Profile.query.get_or_404(id)
    database.session.delete(profile)
    database.session.commit()


def get_avatar(identifier: int):
    """
    This function get admin avatar
    :return: avatar of admin account
    """
    user_profile = Profile.query.filter_by(identifier=identifier).first()
    if user_profile is None or not user_profile.avatar:
        with create_app().open_resource(create_app().root_path + url_for('static', filename='images/default.png'),
                                        "rb") as img:
            avatar = img.read()
    else:
        avatar = user_profile.avatar
    return avatar


def update_avatar(avatar, identifier: int) -> bool:
    """
    This bodule updates admin's avatar
    :param avatar: file
    :param username: str
    :return: bool
    """
    if not avatar:
        return False
    try:
        profile = Profile.query.filter_by(identifier=identifier).first()
        profile.avatar = avatar
        database.session.add(profile)
        database.session.commit()
    except Exception:
        return False
    return True


def check_if_is_available(filename) -> bool:
    """
    this module checks if format of file is available
    :param filename: file
    :return: bool
    """
    file = filename.rsplit('.', 1)[1]
    if file == "png" or file == "PNG":
        return True
    return False
