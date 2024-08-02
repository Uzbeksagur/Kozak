from flask import Flask,render_template
from threading import Thread
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=3, x_proto=3, x_host=3, x_prefix=3
  )

@app.route('/')

def index():
    return "Alive"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()
