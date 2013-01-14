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

##Auto start

If you want to have this start after logging in copy this file to `~/Libary/LaunchAgents` LaunchAgents are start only after a user logs in.

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
This file is included in this repo as `org.ipython.plist`

##ToDo

* Figure out how to get py2app to launch ipython and package this as an .app
* Find a way to hide the Python Laucher from the dock
