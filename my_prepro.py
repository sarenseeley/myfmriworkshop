#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:54:02 2017

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
    #do something cool
    print('Hello data in the path '+basedir)
    for item in
    
    
def main():
    #load in all the global variables prepro needs, right now just path to data
    basedir='/Users/sarenseeley/Desktop/data/subjects'
    prepro(basedir) #call prepro to do cool things
    #basedir is global variable
    
main()
    

## Let's start with skull stripping using fsl's BET function.
# This is a linux based command so we are going to need to use a module to python to understand it.
# Normally at the command line we would run something like this:
# bet input output [options]
## In python we can use the os module to run linux commands
# os.system(bet input output -F)    
    

print(os.system('echo $FSLDIR'))

input='/Users/sarenseeley/Desktop/data/subjects/<subject number>/func/<nifiti_file>'

# Each time we run this command the only things we really need to change are the subject number and 
# the name of the nifti fileOur subject numbers and nifti files use a predictable pattern!
# We can use the glob module to find everything with a similar pattern.
# Here we are going to use a wildcard character (*) to represent the portions of the 
# subject number that differ.

input=glob.glob('/Users/sarenseeley/Desktop/data/subjects/sub-*/func/sub-*_task-bart*.nii.gz')
print(input[0:10])


# glob has created a list with everything matching our pattern criteria. 
# We can use any of python's list comprehension tools to further explore the list
len(input)
input[-1]

# We can also take any element from the list and make it a string. 
# By making a string we can grab IDs or other parts of interest

x=input[1]
print('my path is '+x)
y=x.split('/')
print (y)
whatcomp=y[2]
sub=y[6]
print sub

sub=input[1].split('/')[6]
print(sub)

# Let's make this look a little nicer
sub=input[1].split('/')[6]
print(sub)

# Now we have the subject number but it looks like we have multiple tasks. 
# How can we split an element from the list to get the task information and 
# the subject information?

# so this takes the second input, splits it on the dot
subtask=input[1].split('/')[8].split('.')[0]
#subtask=subtask.strip('.nii.gz')
print(subtask)

output=subtask+'_brain'
print(output)

# Lets go back to our bet command in the os wrapper. 
# We now have all the elements we need to execute it.

os.system('bet' x output '-F')
print(x)
print(output)
os.system('bet %s %s -F'%(x, output))

# The %s is a placeholder for string variable
# The % lets python know to look to the % sign outside the string for the variable of 
# interest. We could also use this to pass integers and floats using %i and %f respectively.

#Now we have the ability to run bet through python on one subject.... but what about all the other scans.... ?
# for loops!

input=glob.glob('/Users/sarenseeley/Desktop/data/subjects/sub-*/func/sub-*.nii.gz')
#print input

#this is a little long to type each time, and it is really easy to mess up the / formating
# os.path.join( ) is super useful to quickly define paths. 
# It will format strings into paths and allows us to use the %s

#input=glob.glob('/Users/sarenseeley/Desktop/data/sub-*/func/sub-*.nii.gz')
basedir='/Users/sarenseeley/Desktop/data/subjects'
path=os.path.join(basedir,'sub-*','func','sub-*.nii.gz')
#print(path)
#input=glob.glob(path)
#len(input[1:5])
os.path.exists(basedir)

# Let's put this altogether into our function prepro( ) with a loop
# just grab barts: 'sub-*_task-bart_bold.nii.gz'

# pdb.set_trace() = python debug
# helps you locate where something broke

def prepro(basedir):
    for item in glob.glob(os.path.join(basedir,'sub-*','func','sub-*.nii.gz')):
        input=item
        output_path=item.strip('.nii.gz')
        output=output_path+('_brain')
        os.system("/usr/local/fsl/bin/bet %s %s -F"%(input, output))
        pdb.set_trace()
def main():
    basedir='/Users/sarenseeley/Desktop/data/subjects'
    prepro(basedir)
    
main()