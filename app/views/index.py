from flask import Blueprint, render_template

bp = Blueprint('index', __name__)

@bp.route('/')
def index():
    return render_template('index.html', id=0)

@bp.route("/<int:id>")
def index_id(id):
    return render_template("index.html", id=id)