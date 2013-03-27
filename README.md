ipython-osx-menu
================

![Alt text](http://labs.radiantmachines.com/ipython.png "In action")

![Alt text](http://labs.radiantmachines.com/notebook.png "Open in browser")

Easily spawn and the access IPython notebook from the OS X Menu bar. 

This is super alpha.

just run it with 

``python menu.py``

##Requirements

* PyObjC
* IPython

##Auto start

To have this auto-start copy the below to a file in  `~/Libary/LaunchAgents` 

Make sure to change the `<string>/Users/josh/Desktop/imenu/menu.py</string>` to your scripts path.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">

<plist version="1.0">
<dict>
    <key>Label</key>
    <string>org.ipython</string>
    <key>ProgramArguments</key>
    <array>
        <string>/Users/josh/Desktop/imenu/menu.py</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
```
This file is included in this repo as `org.ipython.plist` which would be a good for your own.

##ToDo

* Figure out how to get py2app to launch ipython and package this as an .app
* Find a way to hide the Python Laucher from the dock
* Find a way to list active notebooks on the launcher menu, and go directly to their pages


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/gourneau/ipython-osx-menu/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

