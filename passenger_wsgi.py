# import imp
from importlib.machinery import SourceFileLoader
import os
import sys


sys.path.insert(0, os.path.dirname(__file__))

# wsgi = imp.load_source('wsgi', 'run.py')
wsgi = SourceFileLoader('wsgi', 'run.py').load_module()
application = wsgi.app
#hwefiuhwriefhewirughiuwrhefiuwh