from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['POST'])
def listen():
    if request.remote_addr == '204.232.175.75':
        print 'Publishing site'
        print request.data

if __name__ == '__main__':
    app.run(host='0.0.0.0')
