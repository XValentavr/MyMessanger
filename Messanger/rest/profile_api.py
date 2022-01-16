"""
This module defines a rest interface to work with departments of hospital
"""
from flask import abort, jsonify, Response
from flask_restful import reqparse, Resource

# local imports
from ..service import profile_service

# get the request parser
parser = reqparse.RequestParser()

# define the arguments which will be in a request query
parser.add_argument('name')
parser.add_argument('lastname')
parser.add_argument('email')
parser.add_argument('location')
parser.add_argument('identifier')


def abort_of_already_exists(identifier: int):
    """
    this module forbid adding user if user already exists
    :param identifier: user identifier
    :return: None
    """
    if profile_service.get_profiles(identifier):
        abort(Response("Department of hosptital {} already exist".format(identifier), 404))


class AllProfiles(Resource):
    """
     This is the class for AllProfiles Resource available at /profile url
    """

    @staticmethod
    def get(identifier):
        return jsonify(profile_service.get_profiles(identifier))

    @staticmethod
    def post():
        """
        This method is called when POST request is sent
        :return: the 'user added' response with status code 201
        """

        args = parser.parse_args()
        abort_of_already_exists(args['identifier'])
        if args['name'] is None or args['lastname'] is None or args['email'] is None:
            abort(Response("Couldn't add department of hospital. Check insert data", 400))
        elif args['name'].strip() == '' or args['lastname'].strip() == '' or args['email'].strip() == '':
            abort(Response("Couldn't edit department. Missing data", 400))
        elif args['name'] == '' or args['lastname'] == '' or args['email'] == '':
            abort(Response("Couldn't add department of hospital. Check insert data", 400))
        else:
            profile_service.add_profile(args['name'], args['lastname'], args['location'], args['email'],
                                        (args['identifier'].strip()))
        return "Profile added", 201

    @staticmethod
    def delete():
        """
        This method is called when DELETE request is sent
        :return: the empty response with status code 204
        """
        args = parser.parse_args()
        profile_service.delete_profile(args['identifier'].strip())
        return 'Profile deleted', 204

    @staticmethod
    def put():
        """
        This method is called when PUT request is sent
        :return: the 'Profile updated' response with status code 200
        """
        args = parser.parse_args()
        if args['name'] is None or args['lastname'] is None or args['email'] is None:
            abort(Response("Couldn't add department of hospital. Check insert data", 400))
        elif args['name'].strip() == '' or args['lastname'].strip() == '' or args['email'].strip() == '':
            abort(Response("Couldn't edit department. Missing data", 400))
        elif args['name'] == '' or args['lastname'] == '' or args['email'] == '':
            abort(Response("Couldn't add department of hospital. Check insert data", 400))
        else:
            profile_service.update_profile((args['identifier'].strip()), args['name'], args['lastname'],
                                           args['location'],
                                           args['email'])
        return "Profile updated", 200
