from flask import Blueprint, Response, request, redirect, render_template, send_from_directory
routes = Blueprint('routes', __name__)
import os
import functions
import settings


#
#   All the routes in the API
#
@routes.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(routes.root_path, 'static/img'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@routes.route('/')
def home():
    return render_template('page_index.html')


@routes.route('/contact')
def contact():
    return render_template('page_contact.html')


@routes.route('/rule/')
def rules():
    return render_template('page_rules.html')