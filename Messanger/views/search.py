"""
This module to create live search
"""
from flask import request, jsonify
from sqlalchemy.orm import load_only
from Messanger.views.homepage import messanger
from Messanger.models.UserProfile import Profile


@messanger.route('/search', methods=['POST', "GET"])
def livesearch():
    searchbox = request.form.get('text')
    if searchbox.strip() != '':
        search = "%{}%".format(searchbox)
        fields = ['name', 'lastname']
        ajax = Profile.query.filter(Profile.name.like(search)).options(load_only(*fields)).all()
        if ajax:
            return jsonify([ajax.json() for ajax in ajax])
        return jsonify([None])
    return jsonify([None])
