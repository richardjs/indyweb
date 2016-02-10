from flask import Flask

app = Flask(__name__)

@app.route('/think/<qbn>')
def think(qbn):
	return qbn
	
app.run(debug=True)
