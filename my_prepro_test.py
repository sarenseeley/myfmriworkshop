#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 13:06:38 2017

@author: sarenseeley
"""


import sys
sys.path
sys.path.append("/usr/local/fsl/bin/fsl")

import glob
import os
import pdb
import subprocess
import argparse
import datetime
import shutil

def prepro(basedir):
    for item in glob.glob(os.path.join(basedir,'sub-*','func','sub*bart*bold.nii.gz')):
        input=item
        output_path=item.strip('.nii.gz')
        output=output_path+('_brain')
        os.system("/usr/local/fsl/bin/bet %s %s -F"%(input, output))
        #pdb.set_trace()
def main():
    basedir='/Users/sarenseeley/Desktop/data/subjects'
    prepro(basedir)
    
main()