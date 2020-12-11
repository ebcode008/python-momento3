from flask import Flask, render_template
from flask.wrappers import Response
import requests

#import requests
app = Flask(__name__)

# ruta inicial


@app.route('/index')
def api():
    url = 'https://quotes-moviles-app.herokuapp.com/'
    esp_url = 'getQuotesAll/'
    res = requests.request("GET", url + esp_url)
    if res.status_code == 200:
        body = res.json()
        return render_template('/index.html', records=body['quotesDB'])
    else:
        return "Error de servidor"


@app.route('/detail/<id>')
def detail(id):
    url = 'https://quotes-moviles-app.herokuapp.com/getQuotesById/'
    esp_url = id
    res = requests.request("GET", url + esp_url)
    if res.status_code == 200:
        body = res.json()
        return render_template('detail.html', records=body['quotesDB'])
    else:
        return "Error de servidor"


if __name__ == __name__:
    app.run(debug=True)

# python -m flask run
