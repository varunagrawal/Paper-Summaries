import os
from os.path import isfile, join

path = 'papers/'

papers_list = [join(path, f) for f in os.listdir(path) if isfile(join(path, f))]

for p in papers_list:
    with open(p) as f:
        title = f.readline()[3:].strip()
        print("- [{0}]({1})".format(title, p))

