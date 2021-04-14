import json
from flask import Flask
from data import db_session, REST_service


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_pass123'


def main():
    db_session.global_init("db/works.db")
    app.register_blueprint(REST_service.blueprint)
    app.run()


if __name__ == '__main__':
    main()
