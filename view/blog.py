from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for, session
from controller.user_mgmt import User
from controller.session_mgmt import BlogSession
from flask_login import login_user,current_user,logout_user
import datetime

blog_link = Blueprint('blog', __name__)


@blog_link.route('/set_email', methods=['GET', 'POST'])
def set_email():
    if request.method == 'GET':
        # print('set_email', request.headers)
        print('set_email', request.args.get('user_email'))
        return redirect(url_for('blog.set_blog'))
        # return redirect('/blog/set_blog')
        # return make_response(jsonify(success=True), 200)
    else:
        # print('set_email', request.headers)
        # if content type is application/json
        # print('set_email', request.get_json())
        # print('set_email', request.form['user_email'])
        user = User.create(request.form['user_email'], request.form['blog_id'])
        login_user(user, remember=True, duration=datetime.timedelta(days=365))
        
        return redirect(url_for('blog.set_blog'))
    
    
@blog_link.route('/logout')
def logout():
    User.delete(current_user.id)
    logout_user()
    return redirect(url_for('blog.set_blog'))
    
@blog_link.route('/set_blog')
def set_blog():
    if current_user.is_authenticated:
        webpage_name = BlogSession.get_blog_page(current_user.blog_id)
        BlogSession.save_session_info(session['client_id'], current_user.user_email, webpage_name)
        return render_template(webpage_name, user_email=current_user.user_email)
    else:
        webpage_name = BlogSession.get_blog_page()
        BlogSession.save_session_info(session['client_id'], 'anonymous', webpage_name)
        return render_template(webpage_name)
