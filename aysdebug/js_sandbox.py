import sys
from JumpScale import j

j.do.createDir("/usr/local/lib/python3.5/site-packages")
j.do.symlink("/opt/jumpscale7/lib/JumpScale/","/usr/local/lib/python3.5/site-packages/JumpScale/")
j.do.symlink("/opt/jumpscale7/lib/JumpScale/","/root/.ipython/JumpScale/")


def sandbox1():

    paths=[]
    paths.append("/usr/lib/python3.5/")
    paths.append("/usr/local/lib/python3.5/dist-packages")



    excludeFileRegex=["/xml/","-tk/","/xml","/lib2to3"]
    excludeDirRegex=["/JumpScale","\.dist-info","config-x86_64-linux-gnu"]

    dest = "/opt/jumpscale7/lib"

    for path in paths:
        j.tools.sandboxer.copyTo(path,dest,excludeFileRegex=excludeFileRegex,excludeDirRegex=excludeDirRegex)

    try:
        j.do.copyFile("/usr/bin/python","/opt/jumpscale7/bin/python")
    except Exception as e:
        print (e)
        
    j.tools.sandboxer.copyLibsTo(dest,"/opt/jumpscale7/bin/",recursive=True)
    print ("SANDBOXING DONE")

# sandbox1()



d=j.atyourservice.debug.get("mytest")
d.setHost("192.168.0.140")
d.addPath("/opt/jumpscale7/")
d.upload()


sys.exit()