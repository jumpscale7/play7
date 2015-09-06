from JumpScale import j


def _create_docker_machine(name, image='despiegk/mc'):
    ports = "8086:8086 8083:8083 28017:28017 27017:27017 5544:5544 82:82"
    vols = "/opt/jumpscale/var/influxdb:/var/mydocker/influxdb # /opt/jumpscale/var/mongodb:/var/mydocker/mongodb"
    j.tools.docker.destroy(name)
    j.tools.docker.create(
        name=name,
        ports=ports,
        vols=vols,
        volsro='',
        stdout=True,
        base=image,
        nameserver=['8.8.8.8'],
        replace=True,
        cpu=None,
        mem=0,
        jumpscale=True
    )


def docker_create_machine(name='master', reset=False, image='despiegk/mc'):
    containers = j.tools.docker.list()
    if name not in containers or reset:
        _create_docker_machine(name, image)

    return j.tools.docker.getSSH(name)


def install_portal(ssh):
    """
    install portal
    """

    ssh.run('ays install -n singlenode_portal')
    ssh.run('ays start')


###################################################################################
if __name__ == '__main__':
    name = 'master'
    ssh = docker_create_machine(name=name, reset=True)

    install_portal(ssh)

    info = j.tools.docker.inspect(name)

    port = info['NetworkSettings']['Ports']['22/tcp'][0]['HostPort']
    print "SSH port of docker is: %s" % port
