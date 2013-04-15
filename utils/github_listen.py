from os.path import abspath, dirname
import os
import shlex
import subprocess

from flask import Flask, request

app = Flask(__name__)

commands = ['git stash', 'git checkout master', 'git pull origin master',
            'nikola build', 'nikola deploy']

@app.route('/', methods=['POST'])
def listen():
    if request.remote_addr == '204.232.175.75':
        return publish_site()

def publish_site():
    print 'Publishing site'
    directory = dirname(dirname(abspath(__file__)))
    print 'cd into', directory
    os.chdir(directory)
    for command in commands:
        subprocess.call(shlex.split(command))
    return 'Success'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)
