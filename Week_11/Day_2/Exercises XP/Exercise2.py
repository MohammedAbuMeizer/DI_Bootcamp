import flask

app = flask.Flask(__name__)

@app.route("/cv")
def CV():
    return flask.render_template('cv.html')

app.run(port=5000, debug=True)