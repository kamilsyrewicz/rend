from flask import Blueprint, render_template

feature = Blueprint('feature', __name__, url_prefix="/feature")


@feature.route('/')
def index():
    return render_template('templates/.html')

