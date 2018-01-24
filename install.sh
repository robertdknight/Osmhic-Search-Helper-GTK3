#!/usr/bin/env bash

sudo rm -rf /opt/searchhelper
sudo mkdir /opt/searchhelper
sudo cp *.* /opt/searchhelper
sudo rm -f /usr/bin/searchhelper
sudo cp -v searchhelper.desktop /usr/share/applications
sudo cp -v searchhelper /usr/bin/searchhelper
sudo chmod +x /usr/bin/searchhelper
sudo cp -v icon.png /usr/share/pixmaps/searchhelper.png

# The icons need to be in the local share folder for the icon to appear properly
# in the Dock when using Wayland in Fedora 25.   This may be because of the
# limited number of them presented, only 5, while the /usr/share/icons has 15
# different sizes.  The specific reason warrants further research.

cp -v icons/16x16/searchhelper.png ~/.local/share/icons/hicolor/16x16/apps/searchhelper.png
cp -v icons/32x32/searchhelper.png ~/.local/share/icons/hicolor/32x32/apps/searchhelper.png
cp -v icons/48x48/searchhelper.png ~/.local/share/icons/hicolor/48x48/apps/searchhelper.png
cp -v icons/128x128/searchhelper.png ~/.local/share/icons/hicolor/128x128/apps/searchhelper.png
cp -v icons/256x256/searchhelper.png ~/.local/share/icons/hicolor/256x256/apps/searchhelper.png


