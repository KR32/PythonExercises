import os
import sys
from pathlib import Path
from shutil import copyfile, copy
from pkgutil import walk_packages
from importlib import import_module
from traceback import print_tb

root_path = './app/app/db_models'

acronym_list = ['uemae', 'demo1', 'hmgsa']
file_list = ['uemae.py', 'demo1.py', 'hmgsa.py']

def import_sa_models():
    def onerror(name):
        print('=' * 100)
        print("Error importing module %s" % name)
        type, value, traceback = sys.exc_info()
        print_tb(traceback)
        print('=' * 100)
    import app.app.db_models
    modules = walk_packages(path=app.app.db_models.__path__, prefix='app.app.db_models.', onerror=onerror)
    for (a, module, b) in modules:
        print((a, module, b))

import_sa_models()
# for items in acronym_list:
#     path = os.path.join(root_path, items)
#     if os.path.isdir(path):
#         pass
#     else:
#         os.mkdir(path)

# for fldr,file in zip(acronym_list, file_list):
#     acronym_root_path = os.path.join(root_path,fldr)
#     path = os.path.join(acronym_root_path, file)
#     if os.path.isfile(path):
#         pass
#     else:
#         open(path, 'w+')
