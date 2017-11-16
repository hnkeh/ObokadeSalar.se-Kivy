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
    outputList = []
    for element in timeList:
        outputList.append("06:00 - " + element[0:5] + ", " + element[6:11] + " - 21:00")
    return outputList

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
    page = requests.get(h_u)
    tree = html.fromstring(page.content)

    for c_cell in tree.xpath('td[td[@class="commonCell"]]/text()'):
        if len(c_cell) <= 5:
            print('öpö')

    h_list = []
    for link in tree.xpath("//a/text()"):

        if len(link) <= 5 and link[1:2].isdigit():

                h_list.append(link)

    o_list = getOutputList(tree.xpath("//nobr/text()"))
    i_2 = 0
    while i_2 < len(h_list):
        for room in h_l:
            if room == h_list[i_2]:
                h_l[room].append(o_list[i_2])
        i_2 += 1

    for output in h_l:
        if not h_l[output]:
            output_string += output + " : Obokad" + "\n"
        elif len(h_l[output]) == 1:
            output_string += output + " : " + h_l[output][0] + "\n"
        else:
            i_3 = 0
            t_os = ""
            a_l2 = []
            a_l2 = sorted(list(set(scaleDownList(h_l[output]))))
            while i_3 < len(a_l2):
                t_os += a_l2[i_3] + " - " + a_l2[i_3 + 1] + ", "
                i_3 += 2

            t_os = t_os[:-2]
            output_string += output + " : " + t_os + "\n"

    return output_string
