from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sklearn.cluster import KMeans
from scipy.spatial import distance
from sklearn.manifold import TSNE
from datetime import datetime
import pandas as pd
import numpy as np
from cluster import *
from attribute_mapping import *
import json
import os


app = Flask(__name__)
app.config['image_name'] = 'swan'
app.config['attributes'] = pd.read_csv("./static/attributes/NOWHERE_DATASET.csv", header=[0, 1], index_col=0)
app.config['geo_data'] = pd.read_csv("./static/attributes/Geo.csv", header=[0])
app.config['data'] =pd.read_csv("./static/attributes/results_TSNE_3d.csv", header=[0])
app.config['sequence_list'] = []



@app.route('/', methods=['POST','GET'])
def intro():

    if request.method == 'POST':
        try :
            return  redirect('/images/')

        except :
            return "There was an issue updating your task"

    else :
        get_d3_data()
        get_d3_attributes()
        db_attributes = app.config['geo_data']
        json_list = os.path.join('..', 'static', 'Attributes', 'json', '')
        return render_template('intro_page.html',  db_attr = db_attributes , json_list = json_list )

@app.route('/quiz/', methods=['POST','GET'])
def quiz():
    if request.method == 'POST':
        print (request.form.getlist('col_filter[]'))
        input_array_string  =  request.form.getlist('col_filter[]')
        input_array = []
        for loop in input_array_string:
            input_array.append(int(loop))

        print (input_array)




        file_path = "./static/Quiz/quiz_attributes_commas.csv"
        attribute_map = pd.read_csv(file_path, index_col = 0)
        output_list = map_attributes(input_array,attribute_map)

        print (output_list)
        print ('and now length:')
        print (len(output_list))

        app.config['sequence_list'] = final_cluster(output_list[:145])

        print (app.config['sequence_list'])
        try :
            return  redirect('/')
        except :
            return "There was an issue updating your task"
    else :
        print (app.config['sequence_list'])
        return render_template('quiz.html' )



@app.route('/graph/data/TSNE')
def get_d3_data():
    df = app.config['data']
    return df.to_csv()

@app.route('/graph/data/attributes')
def get_d3_attributes():
    df = app.config['attributes']
    return df.to_csv()


@app.route('/sequence', methods=['POST', 'GET'])
def sequence():

    if request.method == 'POST':
        try:
            return redirect('/')

        except:
            return "There was an issue updating your task"
    else:
        results = app.config['sequence_list']
        print (results)
        images = results[0]
        names = results[1]
        PEOPLE_FOLDER = os.path.join('..', 'static')
        csv_file = request.args.get("csv_file")
        json_list = os.path.join(PEOPLE_FOLDER, 'Attributes', 'csv', '')
        print(names)
        return render_template('sequence.html', images=images, image_names = names,
        csv_file = csv_file, json_list = json_list)


if __name__ == "__main__":
    app.run(debug=True)
