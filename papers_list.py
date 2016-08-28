import os
from os.path import isfile, join
import re

path = 'papers/'

def atoi(text):
    return int(text) if text.isdigit() else text
    
def human_sort_keys(text):
    """
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    """
    return [ atoi(c) for c in re.split('(\d+)', text) ]

papers_list = [join(path, f) for f in os.listdir(path) if isfile(join(path, f))]
papers_list.sort(key=human_sort_keys)

for p in papers_list:
    with open(p) as f:
        title = f.readline()[3:].strip()
        print("- [{0}]({1})".format(title, p))
