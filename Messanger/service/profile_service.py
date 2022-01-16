"""
This module defines crud operations to work with profile table
"""
from flask import url_for

from Messanger.models.User import Authorize
from Messanger.models.UserProfile import Profile
from Messanger import database, create_app
from Messanger.service.user_service import delete_user


def get_profiles(UUID: str) -> list:
    """
    This function is used to select all records from hospital table
    :return: the list of all departments of hospital
    """
    profiles = Profile.query.filter_by(identifier=UUID).first()
    return profiles.json() if profiles is not None else None


def get_foreign_values(UUID: str) -> list:
    """
    This function is used to select all records from hospital table
    :return: the list of all departments of hospital
    """
    profiles = Authorize.query.filter_by(UUID=Profile.identifier).first()
    return profiles.json() if profiles is not None else None


def add_profile(name: str, lastname: str, location: str, email: str, UUID: str) -> None:
    """
    this module updates user profile
    :param name: user name
    :param lastname: user last name
    :param location: user location
    :param email: user email
    """
    profile = Profile(name=name, lastname=lastname, location=location, email=email, identifier=UUID)
    database.session.add(profile)
    database.session.commit()


def update_profile(UUID: str, name: str, lastname: str, location: str, email: str) -> None:
    """
    this module updates user profile
    :param UUID: user identifier
    :param name: user name
    :param lastname: user last name
    :param location: user location
    :param email: user email
    """
    profile = Profile.query.filter_by(identifier=UUID).first()
    profile.name = name
    profile.lastname = lastname
    profile.location = location
    profile.email = email
    database.session.add(profile)
    database.session.commit()


def delete_profile(UUID: str) -> None:
    """
    This function is used to delete an existing department
    :param UUID: the id of the profile to delete
    """
    profile = Profile.query.filter_by(identifier=UUID).first()
    database.session.delete(profile)
    database.session.commit()
    delete_user(UUID)


def get_avatar(UUID: str):
    """
    This function get admin avatar
    :return: avatar of admin account
    """
    user_profile = Profile.query.filter_by(identifier=UUID).first()
    if user_profile is None or not user_profile.avatar:
        with create_app().open_resource(create_app().root_path + url_for('static', filename='images/default.png'),
                                        "rb") as img:
            avatar = img.read()
    else:
        avatar = user_profile.avatar
    return avatar


def update_avatar(avatar, UUID: str) -> bool:
    """
    This bodule updates admin's avatar
    :param avatar: file
    :return: bool
    """
    if not avatar:
        return False
    try:
        profile = Profile.query.filter_by(identifier=UUID).first()
        profile.avatar = avatar
        database.session.add(profile)
        database.session.commit()
    except Exception:
        return False
    return True
