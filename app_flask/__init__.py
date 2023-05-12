from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dsgsgergsggsdgg6erw1g6erw1g'

from app_flask import routes