import os
from flask import Flask, url_for, request, redirect, flash
from sqlalchemy.orm import Query
from werkzeug.utils import secure_filename

from ftree.database import start_db, db_session
from ftree.models.person import Member

UPLOAD_FOLDER = './images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["SECRET_KEY"] = "Dormykey"


@app.route('/')
def main():
    start_db()
    fammember = db_session.query(Member).filter(Member.first_name == 'John').first()

    family = {'name': 'john', 'sibling': 'cousin'}
    return f"{fammember}"


@app.get('/upload')
def upload_get():
    upload_form = f"""
    <form action="{url_for("upload_post")}" method="POST" enctype="multipart/form-data">
    <title>Fill the form  and Upload your picture</title>
    <label for="fname">First name:</label>
    <input required type="text" id="fname" name="fname"><br><br>
    <label for="lname">Last name:</label>
    <input required type="text" id="lname" name="lname"><br><br>
    <input required type=file name=file>
    <input type="submit" value="Upload">
</form>
    """

    return upload_form

@app.post('/upload')
def upload_post():
    # SAVING THE FILE TO HARDDRIVE
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        flash("file uploaded successfully")
        # SAVING THE MEMBER TO DB
        start_db()
        form_info = request.form.to_dict()
        example_member = Member(form_info["fname"], form_info["lname"], filepath)
        db_session.add(example_member)
        db_session.commit()
        return redirect(url_for('upload_get'))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS