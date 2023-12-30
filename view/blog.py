from flask import Flask, Blueprint, request, render_template, make_response, jsonify

blog_link = Blueprint('blog', __name__)


@blog_link.route('/set_email', methods=['GET'])
def set_email():
    print('set_email', request.args.get('user_email'))
    return make_response(jsonify(success=True), 200)
    
@blog_link.route('/set_blog')
def set_blog():
    return render_template('blog_A.html')
