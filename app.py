from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "<p>what is ur name?</p> <form action = '/home/runner/swati-sample-1/home.py'> <input type = 'text'>&nbsp; <input type='submit' value='Submit'> </form>"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
