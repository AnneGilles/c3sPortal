#!/bin/bash

#domain="c3sPortal"

# activate the virtualenv 
#. ../env/bin/activate

# extract messages: 
# adds message strings found in code and templates to c3sPortal.pot
python setup.py extract_messages

# update catalog:
# will update the language specific catalog (.po) with entries from .pot
python setup.py update_catalog

# compile catalog:
# will compile the language specific catalog to the relevant .mo
#python setup.py compile_catalog

