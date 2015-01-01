apt-get update
apt-get upgrade
apt-get install mc curl git ssh python2.7 python-requests resolvconf -y
set -ex
curl https://raw.githubusercontent.com/Jumpscale/jumpscale_core7/master/install/web/bootstrap_web.py > /tmp/bootstrap_web.py
cd /tmp
python /tmp/bootstrap_web.py

##NEED TO FIX
#jsconfig hrdset -n whoami.email -v ''
#jsconfig hrdset -n whoami.fullname -v ''
#jsconfig hrdset -n whoami.git.login -v ''
#jsconfig hrdset -n whoami.git.passwd -v ''

echo 'whoami.email =' > /opt/jumpscale7/hrd/system/whoami.hrd
echo 'whoami.fullname =' >> /opt/jumpscale7/hrd/system/whoami.hrd
echo 'whoami.git.login =' >> /opt/jumpscale7/hrd/system/whoami.hrd
echo 'whoami.git.passwd =' >> /opt/jumpscale7/hrd/system/whoami.hrd

echo 'HRD SET' >> /opt/jumpscale7/done.txt

jpackage install -n docker
echo 'DOCKER DONE' >> /opt/jumpscale7/done.txt
jpackage install -n kvm
echo 'KVM DONE' >> /opt/jumpscale7/done.txt

apt-get install linux-image-generic -f -y
echo 'APT KERNEL DONE' >> /opt/jumpscale7/done.txt
mkdir -p ~/ovh.d/
sudo mv /etc/grub.d/06_OVHkernel ~/ovh.d
sudo update-grub
echo 'GRUB DONE' >> /opt/jumpscale7/done.txt
sudo apt-get install linux-headers-generic -f -y

echo INSTALL DONE

echo 'INSTALL DONE' >> /opt/jumpscale7/done.txt
