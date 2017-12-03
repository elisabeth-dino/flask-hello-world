from flask import Flask

application = Flask(__name__)


@application.route('/')
def hello():
    return 'Hola, alumno del curso cloud y devops de verano!'

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)
