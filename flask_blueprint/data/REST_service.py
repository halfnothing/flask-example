import flask
from flask import jsonify, request
from . import db_session
from .works import Work


blueprint = flask.Blueprint(
    'REST_service',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/works', methods=['GET'])
def get_news():
    db_sess = db_session.create_session()
    works = db_sess.query(Work).all()
    return jsonify(
        {
            'works':
                [item.to_dict(only=('name', 'about'))
                 for item in works]
        }
    )


@blueprint.route('/api/works', methods=['POST'])
def create_news():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['name', 'about']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    work = Work(
        name=request.json['name'],
        about=request.json['about']
    )
    db_sess.add(work)
    db_sess.commit()
    return jsonify({'success': 'OK'})
