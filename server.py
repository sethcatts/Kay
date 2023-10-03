from flask import Flask, render_template, url_for
from rpi_rf import RFDevice
import rfModule

app = Flask (__name__)
RFC = rfModule.rfController()

@app.route("/")
def index():
    return render_template('index.html')

# background process happening without any refreshing
@app.route('/light_one_on')
def light_one_on():
    RFC.sendSignal(11097756)
    return "nothing"

# background process happening without any refreshing
@app.route('/light_one_off')
def light_one_off():
    RFC.sendSignal(11097748)
    return "nothing"

# background process happening without any refreshing
@app.route('/light_two_on')
def light_two_on():
    RFC.sendSignal(11097754)
    return "nothing"

# background process happening without any refreshing
@app.route('/light_two_off')
def light_two_off():
    RFC.sendSignal(11097746)
    return "nothing"

if __name__ == '__main__':
    app.run(debug=true)