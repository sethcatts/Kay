from flask import Flask, render_template, url_for
from rpi_rf import RFDevice
import schedule
import time
import rfModule

app = Flask (__name__)
con = rfModule.lightController()


@app.route("/")
def index():
    return render_template('index.html')

# background process happening without any refreshing
@app.route('/light_one_toggle')
def light_one_toggle():
    con.light1.toggle()
    return "nothing"

# background process happening without any refreshing
@app.route('/light_two_toggle')
def light_two_toggle():
    con.light2.toggle()
    return "nothing"

# background process happening without any refreshing
@app.route('/light_three_toggle')
def light_three_toggle():
    con.light3.toggle()
    return "nothing"

# background process happening without any refreshing
@app.route('/plant_light_toggle')
def  plant_light_toggle():
    con.light4.toggle()
    return "nothing"


if __name__ == '__main__':
    print("Starting server")
    app.run(debug=True)

