from flask import Flask, jsonify, request, render_template, make_response
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
from view import blog
from controller.user_mgmt import User
import os

# 인증서 비활성, 안정되지 않은 전송허용 https만 지원기능을 http에서 테스트할 경우
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__, static_url_path='/static')
CORS(app)
app.secret_key = 'test_server'  # os.urandom(24)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'

app.register_blueprint(blog.blog_link, url_prefix='/blog')


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)


if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug=True)
