"""
This module defines crud operations to work with profile table
"""
from Messanger.models.UserProfile import Profile
from Messanger import database


def get_profiles(identifier: int) -> list:
    """
    This function is used to select all records from hospital table
    :return: the list of all departments of hospital
    """
    profiles = Profile.query.filter_by(identifier=identifier).first()
    return profiles.json() if profiles is not None else None


def add_profile(name: str, lastname: str, avatar, location: str, email: str) -> None:
    """
    this module updates user profile
    :param name: user name
    :param lastname: user last name
    :param avatar: user avatar
    :param location: user location
    :param email: user email
    """
    profile = Profile(name=name, lastname=lastname, avatar=avatar, location=location, email=email)
    database.session.add(profile)
    database.session.commit()


def update_profile(id: int, name: str, lastname: str, avatar, location: str, email: str) -> None:
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
    profile.avatar = avatar
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
