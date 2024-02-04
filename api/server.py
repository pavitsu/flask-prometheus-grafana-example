import logging
from flask import Flask, Response
from flask import jsonify
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter, make_asgi_app, multiprocess, generate_latest, CollectorRegistry, CONTENT_TYPE_LATEST, Summary
import os 
import shutil

# ensure variable exists, and ensure defined folder is clean on start
prome_stats = os.environ["PROMETHEUS_MULTIPROC_DIR"]
if os.path.exists(prome_stats):
    shutil.rmtree(prome_stats)
os.mkdir(prome_stats)

from markupsafe import escape
import random

logging.basicConfig(level=logging.INFO)
logging.info("Setting LOGLEVEL to INFO")

api = Flask(__name__)
metrics = PrometheusMetrics(api)
metrics.info("app_info", "App Info, this can be anything you want", version="1.0.0")
c = Counter('counter_model_predict_probability', 'Probability of Model (Counter)')
s = Summary('summary_model_predict_probability', 'Probability of Model (Summary)')
# s.observe(4.7)  

from markupsafe import escape 

@api.route("/metrics")
def metrics():
    registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)
    data = generate_latest(registry)
    return Response(data, mimetype=CONTENT_TYPE_LATEST)

@api.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!" # avoiding injection attack like  <script>alert("bad")</script>

@api.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@api.route("/")
def index():
    return "Hello, this is my homepage."

@api.route("/predict/<text>")
def predict(text):
    predict = random.random()
    c.inc(predict)  
    s.observe(predict)  
    return jsonify({"text" : text, "predict": predict})
