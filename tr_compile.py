#!flask/bin/python

import os


pybabel = 'pybabel'
os.system(pybabel + ' compile -d app/translations')