from JumpScale import j


def docker_create_machine(name, reinstall=False, image='despiegk/mc'):
    docker = j.atyourservice.findTemplates(name='node.docker')[0]
    ports = "8086:8086 8083:8083 28017:28017 27017:27017 5544:5544 82:82"
    vols = "/opt/jumpscale/var/influxdb:/var/mydocker/influxdb # /opt/jumpscale/var/mongodb:/var/mydocker/mongodb"
    args = {
        'instance.param.name': name,
        'instance.param.image': image,
        'instance.param.portsforwards': ports,
        'instance.param.volumes': vols,
    }

    docker.install(name, reinstall=reinstall, args=args)

###################################################################################
if __name__ == '__main__':
    name = 'master'
    docker_create_machine(name=name, reinstall=True)
    instance = j.atyourservice.findServices(name='node.docker', instance=name)[0]

    portal = j.atyourservice.findTemplates(name='singlenode_portal')[0]
    portal.install(parent=instance)

    info = j.tools.docker.inspect(name)

    port = info['NetworkSettings']['Ports']['22/tcp'][0]['HostPort']
    print "SSH port of docker is: %s" % port
