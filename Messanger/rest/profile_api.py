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
parser.add_argument('avatar')


class AllProfiles(Resource):
    """
     This is the class for AllDepartments Resource available at /hospital url
    """

    @staticmethod
    def get(identifier):
        return jsonify(profile_service.get_profiles(identifier))

    @staticmethod
    def post():
        """
        This method is called when POST request is sent
        :return: the 'Department added' response with status code 201
        """

        args = parser.parse_args()
        if args['name'] is None or args['lastname'] is None or args['email'] is None:
            abort(Response("Couldn't add department of hospital. Check insert data", 400))
        elif args['name'].strip() == '' or args['lastname'].strip() == '' or args['email'].strip() == '':
            abort(Response("Couldn't edit department. Missing data", 400))
        elif args['name'] == '' or args['lastname'] == '' or args['email'] == '':
            abort(Response("Couldn't add department of hospital. Check insert data", 400))
        else:
            profile_service.add_profile(args['name'], args['lastname'], args['avatar'], args['location'], args['email'])
        return "Profile added", 201

    @staticmethod
    def delete(identifier: int):
        """
        This method is called when DELETE request is sent
        :return: the empty response with status code 204
        """
        profile_service.delete_profile(identifier)
        return 'Profile deleted', 200

    @staticmethod
    def put(identifier):
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
            profile_service.update_profile(identifier, args['name'], args['lastname'], args['avatar'], args['location'],
                                           args['email'])
        return "Profile updated", 200
