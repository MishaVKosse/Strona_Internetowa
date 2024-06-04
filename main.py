from flask import Flask,render_template

import random
import os
import sys

app = Flask(__name__)

imagepath = os.path.join("static","image")
app.config["UPLOAD_FOLDER"] = imagepath


@app.route("/")
def hello_world():
    return rendermain()


 #"główna strona na której wszysko jest"
@app.route('/index')
def rendermain():
    images = ["image/" + i for i in os.listdir(imagepath)]
    return render_template("index.html", imagelist=images)

# "Privet " + "Ya iz internet" => "Privet Ya iz internet"
# "image/" + "OIP.jfif" => "image/OIP.jfif"
# [i for i in range (0,10)] => [0,1,2,3,4,5,6,7,8,9]
# ["image/" + i for i in ilist] => [image/Adiccion1.jpg,image/OIP.jfif]

#rzut monety
@app.route("/moneta")
def moneta():
    coinresult = ""
    coin = random.randint(1,2)
    if coin == 1:
        coinresult = 'orzeł'
    elif coin == 2:
        coinresult = 'reszka'
    return render_template('moneta.html', moneta_coinresult=coinresult)
    

app.run(debug=True)
