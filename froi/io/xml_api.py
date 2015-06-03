# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:

import os
import xml.dom.minidom
import nibabel as nib

def xmlread_label(xmlname, tagname, index):
    """
    read specific label from xml file according to tag and index.

    """
    parent_path = os.path.dirname(os.getcwd())
    tar_path = parent_path+'/froi/data/atlas/'
    dom=xml.dom.minidom.parse(tar_path + xmlname)
    root = dom.documentElement
    tags = root.getElementsByTagName(tagname)
    tag = tags[index]
    return tag.firstChild.data

def xmlread_labellist(xmlname, tagname):
    """
    read specific label list from xml file according to tag.

    """
    labellist = []
    path = os.getcwd()
    parent_path = os.path.dirname(path)
    tar_path = parent_path+'/froi/data/atlas/'
    dom=xml.dom.minidom.parse(tar_path + xmlname)
    root = dom.documentElement
    tags = root.getElementsByTagName(tagname)
    for i in range(len(tags)):
        labellist.append(tags[i].firstChild.data)
    return labellist

def extract_atlasprob(image, x, y, z):
    """
    extract atlas probability values according to coordinate.

    """
    path = os.getcwd()
    parent_path = os.path.dirname(path)
    tar_path = parent_path+'/froi/data/atlas/'
    atlas = nib.load(tar_path + image)
    atlasdata = atlas.get_data()
    problist = atlasdata[x, y, z, :]/100.0
    return problist

def sorting(labellist, problist):
    """
    sorting the label according to probability value.

    """
    if (len(labellist)!=len(problist)):
        raise 'the length of label and value can not match'
    result = ''
    for i in range(len(problist)):
        if (problist[i] != 0):
            result += (str(problist[i])+' '+labellist[i]+'\n')
    return result