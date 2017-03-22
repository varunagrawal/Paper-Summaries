import os
import os.path as osp
import re


base_path = 'papers/'

def atoi(text):
    return int(text) if text.isdigit() else text
    
def human_sort_keys(text):
    """
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    """
    return [ atoi(c) for c in re.split('(\d+)', text) ]

def pretty_print_areas(areas):
    for k in areas.keys():
        print("{0}\t\t{1}".format(k, areas[k]))

areas = {}

for root, dirs, files in os.walk(base_path):
    # Get all the subdirectories in the base_path as the different areas
    if root == base_path:
        for area in dirs:
            areas[area] = []

    if files:
        area = root.split('/')[-1]
        for file in files:
            areas[area].append(osp.join(root, file))
    
# pretty_print_areas(areas)

for k in areas.keys():
    areas[k].sort(key=human_sort_keys)
    print("## " + k.title())
    for p in areas[k]:
        with open(p) as f:
            title = f.readline()[3:].strip()
            print("- [{0}]({1})".format(title, p))
    
    print()
