"""This is the __init__.py file of rest module.
Imports the department_of_hospital_api and employee_api submodules and registers the api links
"""
# standard library imports
from flask_restful import Api

# local imports
from . import profile_api


def create_api(application):
    api = Api(application)

    # adding the department resources
    api.add_resource(profile_api.AllProfiles, '/api/profiles/<identifier>')

    return api
