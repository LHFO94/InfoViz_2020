from flask import Flask, render_template , url_for, request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd
import os

SQLALCHEMY_TRACK_MODIFICATIONS = False


def create_image_list(path) :
    image_list = os.listdir(path)
    return image_list

app = Flask(__name__)
app.config['image_name'] = 'Room_2005'
app.config['image_list'] = create_image_list('./static/pictures/')
app.config['attributes'] = pd.read_csv("./static/attributes/NOWHERE_DATASET.csv", header=[0, 1], index_col=0)
app.config['geo_data'] = pd.read_csv("./static/attributes/Geo.csv", header=[0])
app.config['data'] =pd.read_csv("./static/attributes/results_TSNE_2d.csv", header=[0])
app.config['image_hover'] = 'Room_2005'



@app.route('/', methods=['POST','GET'])
def intro():

    if request.method == 'POST':
        try :
            return  redirect('/images/')

        except :
            return "There was an issue updating your task"

    else :
        return render_template('intro_page.html')

@app.route('/graph/', methods=['POST','GET'])
def graph():
    if request.method == 'POST':
        try :
            print (request.form['myData'])
            app.config['image_hover'] = request.form['myData']

            return  redirect('/graph/')
        except :
            return "There was an issue updating your task"
    else :
        get_d3_data()
        get_d3_attributes()
        db_attributes = app.config['geo_data']
        image_hover = app.config['image_hover']
        return render_template('graph.html',  db_attr = db_attributes , image_hover = image_hover )


@app.route('/graph/data/TSNE')
def get_d3_data():
    df = app.config['data']
    return df.to_csv()

@app.route('/graph/data/attributes')
def get_d3_attributes():
    df = app.config['attributes']
    return df.to_csv()


if __name__ == "__main__":
    app.run(debug = True)
