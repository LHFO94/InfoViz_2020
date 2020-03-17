from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from cluster import final_cluster
import pandas as pd
import json
import os

SQLALCHEMY_TRACK_MODIFICATIONS = False

def create_image_list(path):
    image_list = os.listdir(path)
    return image_list

def read_csv(name):
    csv_path = "./static/attributes/csv/" + name + '.csv'
    json_path = "./static/attributes/json/" + name + ".json"
    df = pd.read_csv(csv_path, sep=';')
    df.set_index('Name', inplace=True)
    df.to_json(json_path)

def get_images(n):
    image_paths = []
    image_names = []
    for file in os.listdir("./static/pictures/")[:n]:
        if file.endswith(".jpg"):
            s = '../static/pictures/' + file
            image_paths.append(s)
            image_names.append(file[:-4])
    return image_paths, image_names

def csv_to_json(name):
    csv_path = "./static/attributes/csv/" + name + '.csv'
    json_path = "./static/attributes/json/"+ name + ".json"
    df = pd.read_csv(csv_path, sep = ';')
    df.set_index("Name", inplace=True)
    df.to_json(json_path, orient='index')

app = Flask(__name__)
app.config['image_name'] = 'swan'
app.config['image_list'] = create_image_list('./static/pictures/')
app.config['attributes'] = pd.read_csv("./static/attributes/NOWHERE_DATASET.csv", header=[0, 1], index_col=0)
app.config['geo_data'] = pd.read_csv("./static/attributes/Geo.csv", header=[0])
app.config['data'] =pd.read_csv("./static/attributes/results_TSNE_3d.csv", header=[0])


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == "POST":
        app.config['image_name'] = request.form["content"]
        return redirect('/')

    else:
        image_name = app.config['image_name']
        PEOPLE_FOLDER = os.path.join('static', 'pictures')
        picture_filename = image_name + '.jpg'
        full_filename = os.path.join(PEOPLE_FOLDER, picture_filename)
        print(full_filename)
        image_list = app.config['image_list']
        db_attributes = app.config['attributes']

        return render_template('index.html', image=image_name, user_image=full_filename, image_list=image_list)


@app.route('/graph/', methods=['POST', 'GET'])
def graph():

    if request.method == 'POST':
        try:
            return redirect('/')

        except:
            return "There was an issue updating your task"

    else:
        get_d3_data()
        get_d3_attributes()
        db_attributes = app.config['geo_data']
        json_list = os.path.join('..', 'static', 'Attributes', 'json', '')
        return render_template('intro_page.html',  db_attr = db_attributes , json_list = json_list )

        image_name = app.config['image_name']


        return render_template('graph.html', user_image=full_filename, image_list=image_list, db_attr=db_attributes)

@app.route('/graph/parallel', methods=['POST','GET'])
def parallel():
    if request.method == 'POST':
        try :
            return  redirect('/')
        except :
            return "There was an issue updating your task"
    else :
        csv_file = request.args.get("csv_file")
        PEOPLE_FOLDER = os.path.join('..', 'static')
        full_filename = os.path.join(PEOPLE_FOLDER, 'pictures')
        image_list = app.config['image_list']
        db_attributes = app.config['attributes']
        json_list = os.path.join(PEOPLE_FOLDER, 'Attributes', 'csv', '')

        return render_template('parallel.html', user_image = full_filename,
        image_list = image_list, csv_file = csv_file,
        json_list = json_list )


@app.route('/quiz/', methods=['POST','GET'])
def quiz():
    if request.method == 'POST':
        try :
            return  redirect('/')
        except :
            return "There was an issue updating your task"
    else :
        return render_template('quiz.html' )



@app.route('/graph/data/TSNE')
def get_d3_data():
    df = app.config['data']
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
        images = results[0]
        names = results[1]
        PEOPLE_FOLDER = os.path.join('..', 'static')
        csv_file = request.args.get("csv_file")
        json_list = os.path.join(PEOPLE_FOLDER, 'Attributes', 'csv', '')
        print(names)
        return render_template('sequence.html', images=images, image_names = names,
        csv_file = csv_file, json_list = json_list)

        # csv_file = request.args.get("csv_file")
        # PEOPLE_FOLDER = os.path.join('..', 'static')
        # full_filename = os.path.join(PEOPLE_FOLDER, 'pictures')
        # image_list = app.config['image_list']
        # db_attributes = app.config['attributes']
        # json_list = os.path.join(PEOPLE_FOLDER, 'Attributes', 'csv', '')
        #
        # return render_template('sequence.html', images=images,
        # user_image = full_filename, image_list = image_list,
        # csv_file = csv_file, json_list = json_list,
        # image_names = json.dumps(image_names))

if __name__ == "__main__":
    app.run(debug=True)
