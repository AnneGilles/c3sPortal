#!/bin/bash

# make a virtual python environment
virtualenv env

# if you experience problems an older version of setuptools:
#env/bin/pip install --upgrade 

# set it up for development/resolve dependencies
env/bin/python setup.py develop

# run it
env/bin/pserve development.ini --reload
