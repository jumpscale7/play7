
from JumpScale import j
from fabric.api import *

import JumpScale.baselib.remote.cuisine
import JumpScale.lib.docker
import JumpScale.baselib.redis

# codedirFromHost=""  #to not map the code dir
codedirFromHost="# /opt/code:/opt/code"

redis=j.clients.redis.getRedisClient("localhost",9999)

def docker_create_machine(reset=False,image='despiegk/mc'):
    name='master'
    key="play:docker:%s:%s"%(name,image)
    if reset or not redis.exists(key):
        port=j.tools.docker.create(name=name, base=image, nameserver='8.8.8.8', replace=True, cpu=None, mem=0,jumpscale=True)
        redis.set(key,str(port))
    return int(redis.get(key))

def portal():
    """
    install osis    
    """
    run=ssh.run

    #install redis
    cmd="jpackage install -n redis --data='name=mem#port=9999#mem=100#disk=1' -i mem"
    run(cmd)
    return

    #install mongodb (if local install)    
    cmd="""
jpackage install -n mongodb -i main -r --data="\
mongodb.host=127.0.0.1 #\
mongodb.port=27017 #\
mongodb.replicaset=EMPTY #\
mongodb.name=main"
"""
    run(cmd)

    cmd="""
jpackage install -n mongodb_client -i main -r --data="\
mongodb.client.addr=localhost #\
mongodb.client.port=27017 #\
mongodb.client.login= #\
mongodb.client.passwd=EMPTY"
"""
    run(cmd)

    cmd="""
#install influxdb (if local install)
jpackage install -n influxdb -i main -r --data="influxdb.seedservers:"
"""
    run(cmd)

    cmd="""
#install influxdb client
jpackage install -n influxdb_client -i main -r --data="\
influxdb.client.addr=localhost #\
influxdb.client.port=8086 #\
influxdb.client.login=root #\
influxdb.client.passwd=root"
"""
    run(cmd)

    cmd="""
#install osis (if local install)
jpackage install -n osis -i main -r --data="\
osis.key= EMPTY#\
osis.connection=mongodb:main influxdb:main #\
osis.superadmin.passwd=rooter"
"""
    run(cmd)

    cmd="""
#install osis client (if remote install, then no mongodb client nor server required)
jpackage install -n osis_client -i main -r --data="\
osis.client.addr=localhost #\
osis.client.port=5544 #\
osis.client.login=root #\
osis.client.passwd=rooter"
"""
    run(cmd)

    cmd="""
#create admin user for e.g. portal
jsuser set --hrd="\
user.name=admin #\
user.domain=incubaid.com #\
user.passwd=admin #\
user.roles=admin #\
user.active=1 #\
user.description=EMPTY #\
user.emails=kristof@incubaid.com #\
user.xmpp=EMPTY #\
user.mobile=+??? #\
user.authkeys=2354345345,436346346 #\
user.groups=admin"
"""
    run(cmd)

    cmd="""
#install portal (depends on osis)
jpackage install -n portal -i main -r --data="\
portal.port=82 #\
portal.ipaddr=localhost #\
portal.admin.passwd=admin #\
portal.name=main #\
osis.connection=main"
"""
    run(cmd)

    cmd="""
#install portal for jumpscale docs
jpackage install -n doc_jumpscale -r --data="\
portal.instance=main #\
"
"""
    run(cmd)


    run("jpackage install -n grafana")   

    cmd="""
#install portal for jumpscale docs
jpackage install -n grafana_portal -r --data="\
influxdb.connection=main#\
"
"""
    run(cmd)

    run("jsprocess restart -n portal")


###################################################################################

port=docker_create_machine(False)

ssh=j.remote.cuisine.connect("localhost",port)
#check all commands available on ssh.  (there are lots of)

portal()
print "port of docker is: %s"%port


