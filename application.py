from flask import Flask
import os

application = Flask(__name__)


@application.route('/')
def hello():
    return 'HELLO FROM ELI TO HEROKU'

if __name__ == '__main__':
    application.run(host=os.getenv('HOST', '0.0.0.0'), port=os.getenv('PORT', '8888'))
