# -*- coding: utf-8 -*-
"""Project views."""
from flask import Blueprint, render_template
from flask_login import login_required

blueprint = Blueprint('project', __name__, url_prefix='/projects', static_folder='../static')


@blueprint.route('/')
def projects():
    """List projects."""
    return render_template('projects/list.html')
