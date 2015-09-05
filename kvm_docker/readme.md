test

```
# install jumpscale, docker, kvm support
sh ../tools/installdockerkvmsupport.sh
```

create jumpscript which
```!python
# install ubuntu 15.10 KVM machine
#use our ays functionality to install KVM vmachine (see Christophe for example)

#drive all the ays from central (over ssh)

# use ays rewrite of
##../docker_jumpscale_development/do.py
## deploy in the KVM machine

# ssh into the KVM machine, do some test e.g. write/read a file into it
# do this from the top driver file

# destroy the docker
## check docker is gone

# destroy the vm
## check VM is gone

```
