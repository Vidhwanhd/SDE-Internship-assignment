from flask import Flask
from controllers.auth_controller import auth_blueprint
from controllers.user_controller import user_blueprint

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(user_blueprint, url_prefix='/user')   # for /user/<id>
app.register_blueprint(user_blueprint, url_prefix='/users')  # for /users

app.register_blueprint(auth_blueprint, url_prefix='/auth')

@app.route('/')
def home():
    return "User Management System"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
