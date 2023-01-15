from flask import Flask, render_template



app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

def run_app():
    return app.run(host='127.0.0.1:5500')

if __name__ == '__main__':
    app.run()
