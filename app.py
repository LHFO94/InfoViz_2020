from flask import Flask, render_template , url_for, request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd
import os

SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)
app.config['attributes'] = pd.read_csv("./static/attributes/NOWHERE_DATASET.csv", header=[0, 1], index_col=0)
app.config['data'] = pd.read_csv("./static/attributes/results_TSNE_3d.csv", header=[0])



@app.route('/', methods=['POST','GET'])
def graph():
    if request.method == 'POST':
        try :
            return  redirect('/')
        except :
            return "There was an issue updating your task"
    else :

        get_d3_data()

        full_filename = os.path.join('..', 'static', 'pictures')
        db_attributes = app.config['attributes']
        json_list = os.path.join('..', 'static', 'Attributes', 'json', '')

        return render_template('Front_page_scatter.html', user_image = full_filename,  db_attr = db_attributes, json_list = json_list)


@app.route('/parallel', methods=['POST','GET'])
def parallel():
    if request.method == 'POST':
        try :
            return  redirect('/')
        except :
            return "There was an issue updating your task"
    else :
        PEOPLE_FOLDER = os.path.join('..', 'static')
        full_filename = os.path.join(PEOPLE_FOLDER, 'pictures')
        db_attributes = app.config['attributes']
        json_list = os.path.join(PEOPLE_FOLDER, 'Attributes', 'csv', '')

        return render_template('parallel.html', user_image = full_filename , db_attr = db_attributes, json_list = json_list )




@app.route('/data/attributes')
def get_d3_data():
    df = app.config['data']
    return df.to_csv()


if __name__ == "__main__":
    app.run(debug = True)
