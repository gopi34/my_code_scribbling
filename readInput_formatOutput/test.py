#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 18:50:52 2017

@author: gopi34
"""

def read_file():
    line_list = []
    newfile = open('test.txt')
    for i,line in enumerate(newfile):
        line_list.append(str(i+1 )+ '. ' + line.strip() + ' \n')
    writestream = open('Useful_sites.txt', 'w')
    for i in line_list:
        writestream.writelines(i)
    writestream.close()
    newfile.close()
    print(line_list)
read_file()

