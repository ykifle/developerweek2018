# -*- coding: utf-8 -*-
"""Project views."""
from flask import Blueprint, render_template
from flask_login import login_required
import os

blueprint = Blueprint('project', __name__, url_prefix='/projects', static_folder='../static')


@blueprint.route('/')
def projects():
    """List projects."""
    projects = os.listdir('workspace')
    return render_template('projects/list.html', projects= projects)

@blueprint.route('/1')
def project():
    """Show project."""
    return render_template('projects/show.html')