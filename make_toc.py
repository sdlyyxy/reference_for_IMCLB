import os
_root = os.getcwd()
for root, dirs, files in os.walk(_root):
    if root != _root:
        break
    for name in dirs:
        if name == '.git' or name == '.vscode':
            continue
        print "* %s" % name
        for _root_, _dirs, mdfiles in os.walk(os.path.join(root, name)):
            for mdfile in mdfiles:
                if mdfile == '.DS_Store':
                    continue
                print "\t* [%s](%s)" % (mdfile[:-3], os.path.join(_root_, mdfile).replace(_root, ''))
