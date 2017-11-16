# -*- coding: utf-8 -*-
from lxml import html
import requests
from houselists import *

timeList = []
outputList = []
h_list = []
h_url = ""
n_rooms = {}

def getOutputList(timeList):

    for element in timeList:
        outputList.append("06:00 - " + element[0:5] + ", " + element[6:11] + " - 21:00")

    
def getOutputList3():
    i_2 = 0
    while i_2 < len(h_list):
        for element in n_rooms:
            if element == h_list[i_2]:
                n_rooms[element].append(outputList[i_2])
        i_2 += 1

def scaleDownList(a_list):
    t_l = []
    for test in a_list:
        t_l.append(test[0:5])
        t_l.append(test[8:13])
        t_l.append(test[15:20])
        t_l.append(test[23:28])
    return t_l

def getOutputListReturn(h_l, h_u):
    
    output_string = ""
    n_rooms = h_l
    page = requests.get(h_u)
    tree = html.fromstring(page.content)
    i_4 = 0
    
    for link in tree.xpath("//a/text()"):
        if len(link) == 5:
            h_list.append(link)
            
    getOutputList(tree.xpath("//nobr/text()"))
    getOutputList3()

    for output in n_rooms:
        if not n_rooms[output]:
            output_string += output + " : Obokad" + "\n"
        elif len(n_rooms[output]) == 1:
            output_string += output + " : " + n_rooms[output][0] + "\n"
        else:
            i_3 = 0
            t_os = ""
            a_l2 = sorted(list(set(scaleDownList(n_rooms[output]))))
            while i_3 < len(a_l2):
                t_os += a_l2[i_3] + " - " + a_l2[i_3 + 1] + ", "
                i_3 += 2

                t_os = t_os[:-2]
                output_string += output + " : " + t_os + "\n"

    return output_string
