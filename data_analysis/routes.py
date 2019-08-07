import os
import secrets
from flask import render_template, redirect, url_for, flash, request
from data_analysis import app, db
from werkzeug.utils import secure_filename
from data_analysis.forms import TextUpload
from data_analysis.models import RawText


def save_text(form_text):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_text.filename)
    text_fn = random_hex + f_ext
    text_path = os.path.join(app.root_path, 'texts', text_fn)

    with app.open_resource(form_text) as t:
        t.save(text_path)

    return text_fn


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/getfile', methods=["GET", "POST"])
def getfile():
    form = TextUpload()
    if request.method == 'POST':
        # for secure filenames. Read the documentation.
        if form.validate_on_submit():
            file = form.text.data
            filename = secure_filename(file.filename)
            # os.path.join is used so that paths work in every operating system
            file.save(os.path.join(app.root_path, "files", filename))
            # You should use os.path.join here too.
            with open(os.path.join(app.root_path, "files", filename), "r") as f:
                file_content = f.read()
                raw_text = RawText(text=file_content, filename=filename)
                db.session.add(raw_text)
                db.session.commit()
            return file_content
        else:
            flash("File already exists", "danger")
    else:
        return render_template("getfile.html", form=form)


@app.route('/files')
def files():
    all_files = RawText.query.all()
    return render_template("file.html", files=all_files)



#   form = TextUpload()
#    if form.validate_on_submit():
#        if form.text.data:
#            text_file = save_text(form.text.data)
#            db.session.add(text_file)
#            db.session.commit()
#            flash('Yay!', 'success')
#        return redirect(url_for('files'))
#    elif request.method == 'GET':
#        return render_template('getfile.html', form=form)


#    if request.method == 'POST':
 #       # check if the post request has the file part
  #      if 'file' not in request.files:
   #         flash('No file part')
    #        return redirect(request.url)
     #   file = request.files['file']
      #  # if user does not select file, browser also
       # # submit an empty part without filename
 #       if file.filename == '':
  #          flash('No selected file')
   #         return redirect(request.url)
    #    if file and allowed_file(file.filename):
     #       filename = secure_filename(file.filename)
      #      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
       #     return render_template("file.html", file_content=file)




###    form = TextUpload(request.form)
###    if form.validate_on_submit():
###        file = form.text
###        file_content = file.read()
###        return render_template("file.html", file_content=file_content)
