[app]

# (required) Display name of your application
title = MyPythonApp

# (required) Package name
package.name = mypythonapp

# (optional) Package version
package.version = 1.0

# (required) Package domain (needed for android/ios packaging)
package.domain = org.cccs.com

# (required) Source code where the main.py live
source.dir = .

# (optional) Application version code
version.code = 1

# (optional) Application version name
version.name = 1.0

# (optional) Icon of the application
#icon.filename = icon.png

# (optional) Presplash of the application
#presplash.filename = presplash.png

# (optional) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (optional) List of comma-separated permissions
android.permissions = INTERNET

# (optional) List of Java dependencies
android.add_src = java_src

# (optional) List of Python dependencies
requirements = kivy
