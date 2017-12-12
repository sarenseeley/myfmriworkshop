#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:54:02 2017

@author: sarenseeley
"""

import glob
import os
import pdb
import subprocess
import argparse
import datetime
import shutil

def prepro(basedir):
    #do something cool
    print('Hello data in the path '+basedir)
    
def main():
    #load in all the global variables prepro needs, right now just path to data
    basedir='/Users/sarenseeley/Desktop/data'
    prepro(basedir) #call prepro to do cool things
    
main()
    
    
    
    