from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["GET"])
def root():
  return "welcome to the Nikhil's app Version-V22	"

app.run(host="0.0.0.0", port=3000, debug=True)
