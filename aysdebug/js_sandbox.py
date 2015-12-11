import sys
from JumpScale import j

j.do.createDir("/usr/local/lib/python3.5/site-packages")
j.do.symlink("/opt/jumpscale8/lib/JumpScale/","/usr/local/lib/python3.5/site-packages/JumpScale/")
j.do.symlink("/opt/jumpscale8/lib/JumpScale/","/root/.ipython/JumpScale/")


# import sys,base64
# r=sys.stdin.read()
# r=r.encode("ascii")
# base64.b64encode(r)

# from IPython import embed
# embed()


def sandbox1():

    paths=[]
    paths.append("/usr/lib/python3.5/")
    paths.append("/usr/local/lib/python3.5/dist-packages")



    excludeFileRegex=["/xml/","-tk/","/xml","/lib2to3"]
    excludeDirRegex=["/JumpScale","\.dist-info","config-x86_64-linux-gnu"]

    dest = "/opt/jumpscale8/lib"

    for path in paths:
        j.tools.sandboxer.copyTo(path,dest,excludeFileRegex=excludeFileRegex,excludeDirRegex=excludeDirRegex)

    try:
        j.do.copyFile("/usr/bin/python3.5","/opt/jumpscale8/bin/python")
    except Exception as e:
        print (e)

    try:
        j.do.copyFile("/usr/bin/python3.5","/opt/jumpscale8/bin/python3")
    except Exception as e:
        print (e)

        
    j.tools.sandboxer.copyLibsTo(dest,"/opt/jumpscale8/bin/",recursive=True)
    print ("SANDBOXING DONE")

# sandbox1()



d=j.atyourservice.debug.get("mytest")
d.setHost("192.168.0.105")
d.setCache("192.168.0.140")
# d.setNamespace("dedupe")
d.addPath("/opt/jumpscale8/")


d.upload(tocache=True,bootstrap=True)
# d.installAYSFS()


sys.exit()