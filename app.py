from flask import Flask, render_template

app = Flask(__name__)


@app.route('/distrib_wag')
def hello():
    return render_template('./distrib-wag.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
