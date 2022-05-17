from flask import Flask
import uuid

# create flask application
app = Flask(__name__)
my_id = str(uuid.uuid4())

# create root route
@app.route("/")
def hello_world():
    return '<p>Hello, World '+my_id+'</p>'

@app.route("/bye")
def bye():
    return '<p>bye, World</p> '

app.run(debug=True,port=5000,host='0.0.0.0')