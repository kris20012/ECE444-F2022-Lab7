import flask
from flask import json, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Model loading
loaded_model = None
with open('basic_classifier.pkl', 'rb') as fid:
    loaded_model = pickle.load(fid)

vectorizer = None
with open('count_vectorizer.pkl', 'rb') as vd:
    vectorizer = pickle.load(vd)

# test model if it works
# prediction = loaded_model.predict(vectorizer.transform(['This is true news']))[0]
# print(prediction)


# FLASK APP - will be used for determining if news (entered by the user) is fake or not
#
# Reference: https://medium.com/swlh/deploy-a-machine-learning-model-with-aws-elasticbeanstalk-dfcc47b6043e

application = flask.Flask(__name__)

# Friendly welcome page for user
@application.route('/')
def welcomePage():
    return "Welcome to the Fake News Detector Tool"

@application.route('/ping', methods=['GET'])
def ping():
    status = 200
    return flask.Response(response='\n', status=status, mimetype='application/json')

@application.route('/fake-news-detector', methods=['GET','POST'])
def fakeNewsDetector():
    # Get text data from user.
    data = None
    text = request.args['text']

    # use model to predict whether the input data is real or not
    prediction = loaded_model.predict(vectorizer.transform([text]))[0]
    prediction = "Analysis of text: " + prediction 

    # return feedback with JSON
    return flask.Response(response=json.dumps(prediction), status=200, mimetype='application/json')


if __name__ == '__main__':
    application.run()    