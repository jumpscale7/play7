apt-get update
apt-get upgrade
apt-get install mc curl git ssh python2.7 python-requests  -y
set -ex
curl https://raw.githubusercontent.com/Jumpscale/jumpscale_core7/master/install/web/bootstrap_web.py > /tmp/bootstrap_web.py
cd /tmp
python /tmp/bootstrap_web.py

