apt-get update
apt-get upgrade
apt-get install mc curl git ssh python2.7 python-requests resolvconf -y
set -ex
rm -f /tmp/bootstrap_web.py
curl https://raw.githubusercontent.com/Jumpscale/jumpscale_core7/@ys/install/web/bootstrap_web.py > /tmp/bootstrap_web.py
cd /tmp
python /tmp/bootstrap_web.py

##NEED TO FIX
#jsconfig hrdset -n whoami.email -v ''
#jsconfig hrdset -n whoami.fullname -v ''
#jsconfig hrdset -n whoami.git.login -v ''
#jsconfig hrdset -n whoami.git.passwd -v ''

#echo 'email =' > /opt/jumpscale7/hrd/system/whoami.hrd
#echo 'fullname =' >> /opt/jumpscale7/hrd/system/whoami.hrd
#echo 'git.login =' >> /opt/jumpscale7/hrd/system/whoami.hrd
#echo 'git.passwd =' >> /opt/jumpscale7/hrd/system/whoami.hrd

#echo 'HRD SET' >> /opt/jumpscale7/done.txt

#ays install -n docker
echo 'DOCKER DONE' >> /opt/jumpscale7/done.txt
#ays install -n kvm
echo 'KVM DONE' >> /opt/jumpscale7/done.txt

#apt-get install linux-image-generic -f -y
#echo 'APT KERNEL DONE' >> /opt/jumpscale7/done.txt
#sudo rm -rf /etc/grub.d/06_OVHkernel
#sudo update-grub
#echo 'GRUB DONE' >> /opt/jumpscale7/done.txt
#sudo apt-get install linux-headers-generic -f -y

echo INSTALL DONE

echo 'INSTALL DONE' >> /opt/jumpscale7/done.txt

#reboot

