from distutils.core import setup
import py2app

NAME = 'menu'
SCRIPT = 'menu.py'
VERSION = '0.1'
ID = 'menu'

"""
python setup.py py2app -A -r beaker.png
python setup.py py2app -r beaker.png
OPTIONS = {
    'iconfile':'icon.icns',
    'plist': {'CFBundleShortVersionString':'0.1.0',}
}
get icons http://stackoverflow.com/questions/5608080/how-to-specify-py2app-icon
"""

plist = dict(
     CFBundleName                = NAME,
     CFBundleShortVersionString  = ' '.join([NAME, VERSION]),
     CFBundleGetInfoString       = NAME,
     CFBundleExecutable          = NAME,
     CFBundleIdentifier          = 'org.ipython.%s' % ID,
     LSUIElement                 = '0', #makes it not appear in cmd-tab task list etc.
)


app_data = dict(script=SCRIPT, plist=plist)

setup(
   app = [app_data],
   options = {
       'py2app':{
           'resources':[
               ],
           'excludes':[
               ]
           }
       }
)