from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def gpon_form():

    if 'submit' in request.form:
        slot = (request.form['SlotPosition'])
        olt = (request.form['OLTPosition'])
        ont = (request.form['ONTPosition'])
        sernoid = (request.form['SernoID'])
        customername = (request.form['CustomerName'])
        pppoeusername = (request.form['pppoeusername'])
        pppoepassword = (request.form['pppoepassword'])
        sipuser1 = (request.form['sipuser1'])
        sippassword1 = (request.form['sippassword1'])
        sipuser2 = (request.form['sipuser2'])
        sippassword2 = (request.form['sippassword2'])

        gpon_lines = slot, olt, ont, sernoid, customername, pppoeusername, pppoepassword, sipuser1, sippassword1, \
            sipuser2, sippassword2
        return render_template('config.html', lines=gpon_lines)

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8080, debug=True)
