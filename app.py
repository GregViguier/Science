from flask import Flask
import flask
import saxsAnalyzer
from nvd3 import lineWithFocusChart
app = Flask(__name__)


@app.route("/")
def root():
    return flask.render_template('index.html')


def indexOLD():
    chart = lineWithFocusChart(
        height=600, width='800', show_legend=False, name='lineWithFocusChart')
    data = saxsAnalyzer.getdata(5)
    for index, saxsdata in enumerate(data):
        chart.add_serie(name="Serie " + str(index),
                        y=saxsdata[1], x=range(len(saxsdata[1])))
    chart.buildhtml()
    return chart.htmlcontent


def get_json_data():
    data = saxsAnalyzer.getdata(5)
    json_data = "["
    for index, saxsdata in enumerate(data):
        I = saxsdata[1]
        Q = saxsdata[0]
        for ivalue, qvalue in zip(I, Q):
            json_data += "{\"name\": \"Azimuthal " + str(index) + "\"" + ", \"Q\" :" + str(
                qvalue) + ", \"I\" :" + str(ivalue) + "},"
    json_data = json_data[:-1]
    json_data += "]"
    return json_data


@app.route("/saxs")
def saxs_data():
    return get_json_data()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
