from flask import Flask, render_template, url_for
from rpi_rf import RFDevice
import rfModule

app = Flask (__name__)
con = rfModule.lightController()

@app.route("/")
def index():
    return render_template('index.html')

# background process happening without any refreshing
@app.route('/light_one_on')
def light_one_on():
    con.light1.toggle()
    return "nothing"

# background process happening without any refreshing
@app.route('/light_one_off')
def light_one_off():
    con.light1.toggle()
    return "nothing"

# background process happening without any refreshing
@app.route('/light_two_on')
def light_two_on():
    con.light2.toggle()
    return "nothing"

# background process happening without any refreshing
@app.route('/light_two_off')
def light_two_off():
    con.light2.toggle()
    return "nothing"

if __name__ == '__main__':
    app.run(debug=true)