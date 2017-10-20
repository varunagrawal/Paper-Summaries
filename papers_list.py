"""
Script to generate index of papers for each area.
Usage:
    # In the root of the repo
    `python papers_list.py`
"""

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

def get_papers():
    # `dict` of various research areas. 
    # Each key is an area string and the value is the list of papers.
    areas = {}

    for root, dirs, files in os.walk(base_path):
        # Get all the subdirectories in the base_path as the different areas
        if root == base_path:
            for area in dirs:
                areas[area] = []

        if files:
            area = root.split('/')[-1]
            for file in files:
                if "README" in file:
                    continue
                areas[area].append(osp.join(root, file))
        
    # pretty_print_areas(areas)
    return areas


def generate_index(area, papers):
    papers.sort(key=human_sort_keys)

    with open(osp.join(base_path, area, "README.md"), 'w+') as op:
        op.write("## " + area.title() + "\n\n")
        for paper in papers:
            with open(paper) as f:
                title = f.readline()[3:].strip()
                paper_link = osp.basename(paper)
                paper_no = paper.split('/')[-1][:-3]
                op.write("{2}. [{0}]({1})\n".format(title, paper_link, paper_no))


def main():
    areas = get_papers()
    for k, v in areas.items():
        generate_index(k, v)
        

if  __name__ == "__main__":
    main()
