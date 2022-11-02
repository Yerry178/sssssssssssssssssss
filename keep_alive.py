from flask import Flask
from typing import Literal
from threading import Thread

app = Flask('')

@app.route('/')
def home() -> str:
    return "I'm alive baby :)"

def run() -> Literal[None]:
  app.run(host='0.0.0.0',port=8000)

def keep_alive() -> Literal[None]:  
    t = Thread(target=run)
    t.daemon = True
    t.start()
