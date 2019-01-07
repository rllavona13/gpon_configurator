from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def gpon_form():

    if 'submit' in request.form:
        return render_template('config.html')


if __name__ == '__main__':
    app.run()
