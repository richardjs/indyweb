import flask

from subprocess import Popen, PIPE
import sys

app = flask.Flask(__name__)

@app.route('/think/<qbn>')
def think(qbn):
	p = Popen((sys.argv[1], qbn), stdin=PIPE, stdout=PIPE, shell=False)
	p.wait()
	qmn = p.stdout.readline().strip()

	print qbn, qmn

	r = flask.Response('{"qmn": "%s"}' % qmn)
	r.headers['Content-Type'] = 'application/json'
	r.headers['Access-Control-Allow-Origin'] = '*'
	return r
	
app.run()
