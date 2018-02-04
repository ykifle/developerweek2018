# -*- coding: utf-8 -*-
"""Project views."""
from flask import Blueprint, render_template, redirect, session
import os
import shutil

blueprint = Blueprint('experiment', __name__, url_prefix='/experiments', static_folder='../static')


@blueprint.route('/1')
def experiment():
    """Show experiment."""
    return render_template('experiments/show.html', id=1)

@blueprint.route('/4')
def experiment4():
    """Show experiment."""
    return render_template('experiments/show.html', id=4)

@blueprint.route('/1/fork')
def fork_experiment():
    """Show experiment."""
    shutil.copytree('/red/notebook/experiment-1', '/red/notebook/experiment-4')
    session['forked'] = True
    return redirect('/experiments/4')
