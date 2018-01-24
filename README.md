## OSMHIC SEARCH HELPER for LINUX
#### Python and GTK3/GObject version
###### by Robert Knight


This is the readme for the Osmhic Search Helper.  This application
originally appeared on Windows Desktop and then on the Universal Windows
Platform (Windows store).  Those versions were written in C#.  This
version is written in Python and uses GTK 3. The original window source
came from the text entry and checkbox examples available at The Python
GTK+ 3 Tutorial website.

To use the application save the searchhelper.py into a folder of your
choice. From a terminal, launch it via the command 'searchelper'

Run ./install.sh from the directory where the zip file is extracted.
The installation script will remove existing the searchhelper directory
in /opt.  It will then copy the application files to opt/searchhelper.

After doing this, it will copy the .desktop to /usr/share/applications.
Then, it will create a launch script at /usr/bin/searchhelper and set
that script as an executable. It will copy the main searchhelper
application icon to /usr/share/pixmaps/ and will copy the individually
scaled icons to the local highcolor directories.  It copies 16x16,
32x32, 48x48, 128x128, and 256x256.

After this, the application can be run from the command line via searchhelper or
from the applications list in Gnome 3.








