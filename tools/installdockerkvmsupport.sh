apt-get update
apt-get upgrade
apt-get install mc curl git ssh python2.7 python-requests  -y
set -ex
curl https://raw.githubusercontent.com/Jumpscale/jumpscale_core7/master/install/web/bootstrap_web.py > /tmp/bootstrap_web.py
cd /tmp
python /tmp/bootstrap_web.py

jpackage install -n docker
jpackage install -n kvm

apt-get install linux-image-generic -f
mkdir ~/ovh.d/
sudo mv /etc/grub.d/06_OVHkernel ~/ovh.d
sudo update-grub
sudo apt-get install linux-headers-generic -f


