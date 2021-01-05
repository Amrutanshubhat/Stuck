from flask import Flask,render_template,url_for,request,flash,redirect
from werkzeug.utils import secure_filename
from nsetools import Nse
import csv
import os
nse=Nse()

import functions


UPLOAD_FOLDER = './'
ALLOWED_EXTENSIONS = {'csv'}
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

holding = 0

@app.route('/holding',methods=['POST'])
def set_holding():
    global holding
    holding = float(request.form['holding'])
    return redirect('/')

@app.route('/',methods=['GET','POST'])
def home():
    global holding
    lst=functions.total_csv(holding)
    if(len(lst)==0):
        return render_template('upload_file.html')
    return render_template('root.html',lst=lst)


@app.route('/market')
def market():
    lst=nse.get_index_list()[1:24]
    return render_template('home.html',lst=lst)

@app.route("/index/<index>")
def get_detail(index):
    lst = nse.get_index_quote(index)
    lst.popitem()
    return render_template('index.html',lst=lst)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods = ['POST'])  
def upload():  
    if request.method == 'POST':  
        f = request.files['file']
        if(allowed_file(f.filename)):
            filename='ledger.csv'  
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  
            flash("Uploaded Successfully")
        else:
            flash('Invalid File')
    return redirect("/")