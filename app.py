from flask import Flask, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename
import os
import ig
import mimetypes
from flask import Flask,render_template, Response

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/marks',methods=['GET','POST'])
def marks():
    if request.method == 'POST':
        result = ig.pre()
        return redirect('/total')
    return render_template('marks.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect(url_for('total'))

@app.route('/total')
def total():
    result = ig.pre()
    return render_template('total.html',result=result)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/classdetails')
def classdetails():
    return render_template('classdetails.html')


@app.route('/all_stud')
def all_stud():
    return render_template('all_stud.html')

@app.route('/add_stud')
def add_stud():
    return render_template('add_stud.html')

@app.route('/del_stud')
def del_stud():
    return render_template('del_stud.html')

@app.route('/filter_stud')
def filter_stud():
    return render_template('filter_stud.html')

@app.route('/camera')
def camera():
    return render_template('camera.html')
    

if __name__ == '__main__':
    app.run(debug=True)


    # http_server = WSGIServer(('0.0.0.0', 5000), app)
    # http_server.serve_forever()