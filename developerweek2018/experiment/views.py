# -*- coding: utf-8 -*-
"""Project views."""
from flask import Blueprint, render_template

blueprint = Blueprint('experiment', __name__, url_prefix='/experiments', static_folder='../static')


@blueprint.route('/1')
def experiment():
    """Show experiment."""
    return render_template('experiments/show.html')
