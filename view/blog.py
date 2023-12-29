from flask import Flask, Blueprint, request, render_template

blog_link = Blueprint('blog', __name__)


@blog_link.route('/test')
def test():
    return render_template('blog_A.html')
