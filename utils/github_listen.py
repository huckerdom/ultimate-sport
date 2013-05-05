from os.path import abspath, dirname, join
import os
import shlex
import subprocess
import traceback

from flask import Flask, request

app = Flask(__name__)

commands = ['git stash', 'git checkout master', 'git pull origin master',
            'nikola build', 'nikola deploy']

GITHUB_IPS = ['207.97.227.253', '50.57.128.197', '108.171.174.178', '50.57.231.61',
              '204.232.175.65-204.232.175.94', '192.30.252.1-192.30.255.254']

def ip_in_range(ip_range, ip):
    start, end = ip_range.split('-')
    process = lambda x: [int(s) for s in x.split('.')]
    start, end, ip = process(start), process(end), process(ip)
    for i in range(4):
        if not start[i] <= ip[i] <= end[i]:
            return False
    return True

def is_github_ip(our_ip):
    for ip in GITHUB_IPS:
        if '-' in ip and ip_in_range(ip, our_ip):
            return True
        elif '-' not in ip and ip == our_ip:
            return True
    return False

def is_acceptable_ip(our_ip):
    return (our_ip == '127.0.0.1') or is_github_ip(our_ip)

def publish_site():
    print 'Publishing site'
    directory = dirname(dirname(abspath(__file__)))
    old_dir = os.getcwd()
    os.chdir(directory)
    for command in commands:
        subprocess.call(shlex.split(command))
    os.chdir(old_dir)
    return 'Success'

@app.route('/status.png', methods=['GET'])
def send_status_img():
    return (open(join(dirname(dirname(abspath(__file__))), 'files', 'images', 'deployer_up.png'), 'rb').read(),
            200, {'content-type':'image/png'})

@app.route('/', methods=['POST'])
def listen():
    if is_acceptable_ip(request.remote_addr):
        try:
            return publish_site()
        except:
            traceback.print_exc()
            return 'Internal Error', 500
    else:
        print 'Received request from %s. Ignored.' % request.remote_addr
        return 'Forbidden', 403


if __name__ == '__main__':
    # Debug is set to true for the auto-reloading functionality
    app.run(host='0.0.0.0', port=8008, debug=True)
