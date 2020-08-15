packs = []
with open('rs', 'r') as f:
    lines = f.readlines()
    for l in lines:
        packs.extend(l.split())

installed = []
with open('temp', 'r') as g:
    lines = g.readlines()
    for l in lines:
        installed.extend(l.split())

todo = []
for p in packs:
    if not p in installed:
        todo.append(p)

print(todo)


# with open("rss", 'w') as ff:
#    for p in packs:
#         s = "install.packages(\"{}\")\n".format(p)
#        ff.write(s)

