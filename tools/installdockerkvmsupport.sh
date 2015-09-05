apt-get update
apt-get upgrade
apt-get install mc curl git ssh python2.7 python-requests resolvconf -y
set -ex
rm -f /tmp/install.py
curl https://github.com/Jumpscale/jumpscale_core7/blob/master/install/install.sh > /tmp/install.py
cd /tmp
python /tmp/install.py

ays install -n docker
echo 'DOCKER DONE' >> /opt/jumpscale7/done.txt

ays install -n kvm
echo 'KVM DONE' >> /opt/jumpscale7/done.txt

#WHEN OVH
#apt-get install linux-image-generic -f -y
#echo 'APT KERNEL DONE' >> /opt/jumpscale7/done.txt
#sudo rm -rf /etc/grub.d/06_OVHkernel
#sudo update-grub
#echo 'GRUB DONE' >> /opt/jumpscale7/done.txt
#sudo apt-get install linux-headers-generic -f -y

echo INSTALL DONE

echo 'INSTALL DONE' >> /opt/jumpscale7/done.txt

#reboot

