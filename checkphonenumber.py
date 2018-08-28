#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os

def check():

    num_a = "1"

    phone_number = raw_input("请输入一个电话号码:\n")

#    if phone_number.isdigit() == True:
#        pass
#    else:
#        print "Error Number!"

    if len( phone_number ) == 11 :
        pass
    else:
        print "Error Number!"
        sys.exit(0)

    if ( phone_number[0] is num_a ) :
        pass
    else:
        print "Error Number!"
        sys.exit(0)
    return;

run = check()

