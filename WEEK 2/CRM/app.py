
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
import csv

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.secret_key = 'super_secret_key'

def get_uploaded_filename():
    uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
    if uploaded_files:
        return uploaded_files[0]  # Assume the first file is the uploaded file
    else:
        return None

def get_headers(filename):
    if os.path.exists(filename):
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            return next(reader, [])
    else:
        return []

@app.route('/')
def index():
    uploaded_filename = get_uploaded_filename()
    if uploaded_filename:
        headers = get_headers(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_filename))
    else:
        headers = []
    return render_template('index.html', headers=headers)

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'append_header':
            new_header = request.form.get('new_header')
            if new_header:
                uploaded_filename = get_uploaded_filename()
                if uploaded_filename:
                    try:
                        with open(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_filename), 'r', newline='') as csvfile:
                            reader = csv.reader(csvfile)
                            existing_content = list(reader)
                        if existing_content:
                            existing_content[0].append(new_header)
                            with open(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_filename), 'w', newline='') as csvfile:
                                writer = csv.writer(csvfile)
                                writer.writerows(existing_content)
                            flash("Header appended successfully.")
                        else:
                            flash("No data found in the CSV file.")
                    except Exception as e:
                        flash("Error occurred while processing the file: {}".format(str(e)))
                else:
                    flash("No file uploaded yet.")
            else:
                flash("Please enter a new header.")
        else:
            file = request.files['file']
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                flash("File uploaded successfully.")
            else:
                flash("No file selected.")
    return redirect(url_for('index'))

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
