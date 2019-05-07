from flask import flask, request, url_for, make_response
from flask_cqlalchemy import CQLAlchemy
from test import imageprepare
import datetime

app = Flask(__name__)

app.config['CASSANDRA_HOSTS'] = ['127.0.0.1']
app.config['CASSANDRA_KEYSPACE'] = "cqlengine"
db = CQLAlchemy(app)

class InputList(db.Model):
    Input_id = db.columns(db.Integer, primary_key=True)
    predict = db.columns.Integer(required=False)
    accesstime = db.columns.timestamp(required=True)


@app.route('/')
def index():
    return 'Welcome'

@app.route('/inputlist',methods=['GET'])
def get_inputs():
    inputs=InputList.query.all()
    for inp in inputs:
        print(inp.Input_id, inp.predict, inp.accesstime)

@app.route('/predict',methods=['POST'])
def predict():
    img = request.files()
    im = list(img.getdata())
    predictlabel=imageprepare(im)
    print(predictable)
    count = random.randint(1.10000)
    entry=InputList(Input_id=count,predict=predictable,accesstime=datetime.now())
    db.session.add(entry)
    db.session.commit()

@app.route('/inputlist/<int:input_id>',methods=['GET'])
def get_input(input_id):
    i = input_id
    entry = InputList.query.get(i)
    print(entry.input_id, entry.predict, entry.accesstime)

# @app.route('/inputlist/<int:input_id>',methods=['DELETE'])
# def delete_entry(input_id):


@app.errorhandler(404)
def not_found(error):
    return make_response({'Not Found'},404)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=80)