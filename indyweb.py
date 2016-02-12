import flask

from subprocess import Popen, PIPE
import sys

app = flask.Flask(__name__)

@app.route('/think/<qbn>')
def think(qbn):
	p = Popen(sys.argv[1], stdin=PIPE, stdout=PIPE)
	p.stdin.write(qbn);
	p.stdin.flush()
	p.wait()
	qmn =p.stdout.readline().strip()

	r = flask.Response('{"qmn": "%s"}' % qmn)
	r.headers['Content-Type'] = 'application/json'
	r.headers['Access-Control-Allow-Origin'] = '*'
	return r
	
app.run(debug=True)
