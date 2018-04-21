import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
# from gi.repository.GdkPixbuf import Pixbuf
import os
import sys

# by Robert Knight - June 2017
# https://rdknight.org/blog
# Use the contact page on that site to report any issues.

# Where [1] or [2] appear in comments with someone's name and a Thanks, this
# references the URL 'works cited' type comment at the bottom of the file.


icon = ("searchhelper")

class SearchHelperWindow(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title="Search Helper", parent=None)

        """ A search bar for Linux """
        # save the default browser option in case this is the first time the
        # program is launched
        """
        The following section is for the application icon on Gnome 3
        """

        GLib.set_prgname('searchhelper')  # For Wayland only
        # Thanks to Tomas Kaluza [1]

        pixbuf16 = Gtk.IconTheme.get_default().load_icon(icon, 16, 0)
        pixbuf32 = Gtk.IconTheme.get_default().load_icon(icon, 32, 0)
        pixbuf48 = Gtk.IconTheme.get_default().load_icon(icon, 48, 0)
        pixbuf128 = Gtk.IconTheme.get_default().load_icon(icon, 128, 0)
        pixbuf256 = Gtk.IconTheme.get_default().load_icon(icon, 256, 0)
        self.set_icon_list([pixbuf16, pixbuf32, pixbuf48, pixbuf128, pixbuf256])
        # Thanks to morningbird [1]

        self.save_browser_options('firefox')
        # save the default edu filter strings and option in case this is the
        # first time the program is launched
        self.save_filter_strings()
        self.save_filter_options("False")

        # Create a default window and add a grid control to it
        self.set_border_width(1)
        self.set_default_size(200, 70)

        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.add(self.grid)

        self.entry = Gtk.Entry()
        self.entry.set_text("Input Search Text")
        self.grid.attach(self.entry, 0, 0, 4, 1)

        self.button0 = Gtk.Button.new_with_mnemonic("Bing")
        self.button0.connect("clicked", self.on_button0_clicked)
        self.grid.attach_next_to(self.button0, self.entry,
                                 Gtk.PositionType.BOTTOM, 1, 1)
        # these are how many spaces the button takes up, w, & h

        self.button1 = Gtk.Button.new_with_mnemonic("Ecosia")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.grid.attach_next_to(self.button1, self.button0, Gtk.PositionType.
                                 RIGHT, 1, 1)

        self.button2 = Gtk.Button.new_with_mnemonic("Google")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.grid.attach_next_to(self.button2, self.button1, Gtk.PositionType.
                                 RIGHT, 1, 1)

        self.button3 = Gtk.Button.new_with_mnemonic("Duck Duck Go")
        self.button3.connect("clicked", self.on_button3_clicked)
        self.grid.attach_next_to(self.button3, self.button2, Gtk.PositionType.
                                 RIGHT, 1, 1)

        self.check_firefox = Gtk.CheckButton("Firefox")
        self.check_firefox.connect("toggled", self.on_firefox_toggled)
        self.check_firefox.set_active(True)
        self.grid.attach_next_to(self.check_firefox, self.button0, Gtk.
                                 PositionType.BOTTOM, 1, 1)

        self.check_chrome = Gtk.CheckButton("Chrome")
        self.check_chrome.connect("toggled", self.on_chrome_toggled)
        self.check_chrome.set_active(False)
        self.grid.attach_next_to(self.check_chrome, self.button1, Gtk.
                                 PositionType.BOTTOM, 1, 1)

        self.check_edu = Gtk.CheckButton("Filtered .EDU")
        self.check_edu.connect("toggled", self.on_edu_toggled)
        self.check_edu.set_active(False)
        self.grid.attach_next_to(self.check_edu, self.button2, Gtk.PositionType.BOTTOM, 1, 1)

        self.link_button = Gtk.LinkButton("http://rdknight.org/blog",
                                          "Visit the blog")
        self.grid.attach_next_to(self.link_button, self.button3, Gtk.
                                 PositionType.BOTTOM, 1, 1)

        self.button4 = Gtk.Button.new_with_mnemonic("Nullege")
        self.button4.connect("clicked", self.on_nullege_clicked)
        self.grid.attach_next_to(self.button4, self.link_button,
                                 Gtk.PositionType.BOTTOM, 1, 1)

        self.button5 = Gtk.Button.new_with_mnemonic("Stack Overflow")
        self.button5.connect("clicked", self.on_stackoverflow_clicked)
        self.grid.attach_next_to(self.button5, self.check_edu,
                                 Gtk.PositionType.BOTTOM, 1, 1)
        self.button6 = Gtk.Button.new_with_mnemonic("Program Creek")
        self.button6.connect("clicked", self.on_programcreek_clicked)
        self.grid.attach_next_to(self.button6, self.check_chrome,
                                 Gtk.PositionType.BOTTOM, 1, 1)
    # Save the browser selection to a text file.  As of 2017-06-18, this is
    # limited to Firefox and Chrome only

    def save_browser_options(self, browser):
        """ Save browser name to a string in a text file """
        base_path_name = os.getenv("HOME")
        data_path_name = base_path_name + '/.SearchHelper'
        filename = data_path_name + '/browser.txt'
        try:
            os.mkdir(data_path_name)
        except Exception, err:
            print ' Directory Already Exists '
            print sys.stderr.write('ERROR: %sn' % str(err))
            print
        pass
        with open(filename, mode='w+') as opened_file:
            opened_file.write(browser)
        print("Write operation complete")

    def read_browser_options(self):
        """ Read browser name from a string in a text file """
        print
        base_path_name = os.getenv("HOME")
        data_path_name = base_path_name + '/.SearchHelper'
        filename = data_path_name + '/browser.txt'
        with open(filename) as file_object:
            contents = file_object.read()
            print(contents)
        return contents

    def save_filter_options(self, filter):
        """ Save filter option status to a string in a text file """
        base_path_name = os.getenv("HOME")
        data_path_name = base_path_name + '/.SearchHelper'
        filename = data_path_name + '/filter.txt'
        try:
            os.mkdir(data_path_name)
        except Exception, err:
            print ' Directory Already Exists '
            print sys.stderr.write('ERROR: %sn' % str(err))
            print
        pass
        with open(filename, mode='w+') as file:
            file.write(filter)
        print("Write operation complete")

    def read_filter_options(self):
        """ Read filter name from a string in a text file """
        print
        base_path_name = os.getenv("HOME")
        data_path_name = base_path_name + '/.SearchHelper'
        filename = data_path_name + '/filter.txt'
        with open(filename) as file_object:
            contents = file_object.read()
            print(contents)
            return contents

    def save_filter_strings(self):
        """ Save filter option strings to a string in a text file """
        base_path_name = os.getenv("HOME")
        data_path_name = base_path_name + '/.SearchHelper'
        bing_filename = data_path_name + '/bingfilter.txt'
        bing_filter = "%20-academia%20(site:.edu)"
        qrobe_filename = data_path_name + '/qrobefilter.txt'
        qrobe_filter = "%20-academia%20-princeton%20/.edu"
        google_filename = data_path_name + '/googlefilter.txt'
        google_filter = "%20-academia%20(site:.edu)"
        duckduckgo_filename = data_path_name + '/duckduckgofilter.txt'
        duckduckgo_filter = "%20-academia%20!edu"
        try:
            os.mkdir(data_path_name)
        except Exception, err:
            print ' Directory Already Exists '
            print sys.stderr.write('ERROR: %sn' % str(err))
            print
        pass
        with open(bing_filename, mode='w+') as file:
            file.write(bing_filter)
        with open(qrobe_filename, mode='w+') as file:
            file.write(qrobe_filter)
        with open(google_filename, mode='w+') as file:
            file.write(google_filter)
        with open(duckduckgo_filename, mode='w+') as file:
            file.write(duckduckgo_filter)
        print("Write operation complete")

    def read_filter_string(self, engine):
        """ Save filter option status to a string in a text file """
        base_path_name = os.getenv("HOME")
        data_path_name = base_path_name + '/.SearchHelper'
        if engine == "bing":
            filename = data_path_name + '/bingfilter.txt'
            filter_string = "%20-academia%20(site:.edu)"
        elif engine == "qrobe":
            filename = data_path_name + '/qrobefilter.txt'
            filter_string = "%20-academia%20-princeton%20/.edu"
        elif engine == "google":
            filename = data_path_name + '/googlefilter.txt'
            filter_string = "%20-academia%20(site:.edu)"
        elif engine == "duckduckgo":
            filename = data_path_name + '/duckduckgofilter.txt'
            filter_string = "%20-academia%20!edu"
        return filter_string

    def on_firefox_toggled(self, button):
        value = button.get_active()
        self.entry.set_editable(value)
        if value == True:
            print("Firefox On\True")
            self.check_chrome.set_active(False)
            self.save_browser_options('firefox')
        else:
            print("Firefox Off\False")
            self.check_chrome.set_active(True)
            self.save_browser_options('google-chrome')
    def on_chrome_toggled(self, button):
        value = button.get_active()
        self.entry.set_editable(value)
        if value == True:
            self.check_firefox.set_active(False)
            print("Chrome On\True")
            self.save_browser_options('google-chrome')
        else:
            self.check_firefox.set_active(True)
            print("Chrome Off\False")
            self.save_browser_options('firefox')

    def on_edu_toggled(self, button):
        value = button.get_active()
        self.entry.set_editable(value)
        if value == True:
            print("Edu site filter YES")
            self.save_filter_options("True")
        else:
            print("Edu site filter No")
            self.save_filter_options("False")

    def on_button0_clicked(self, button):
        print("\"Bing\" button was clicked")
        browser = self.read_browser_options()
        filter_options = self.read_filter_options()
        try:
            search_text = self.entry.get_text()
            if filter_options == "True":
                print(browser + ' ' + "\"http://www.bing.com/search?q=" +
                      search_text + self.read_filter_string("bing") + '\"')
                os.system(browser + ' ' + "\"http://www.bing.com/search?q=" +
                          search_text + self.read_filter_string("bing") + '\"'
                          + ' &')
            else:
                print(browser + ' ' + "\"http://www.bing.com/search?q=" +
                      search_text + '\"')
                os.system(browser + ' ' + "\"http://www.bing.com/search?q=" +
                          search_text + '\"' + ' &')
        except Exception, err:
            print ' Failed on_button0_clicked '
            print sys.stderr.write('ERROR: %sn' % str(err))
            print
        pass

    def on_button1_clicked(self, button):
        print("\"Ecosia\" button was clicked")
        browser = self.read_browser_options()
        filter_options = self.read_filter_options()
        try:
            search_text = self.entry.get_text()
            if filter_options == "True":
                print(browser + ' ' + "\"https://www.ecosia.org/search?q=" +
                      search_text + self.read_filter_string("bing") + '\"')
                os.system(browser + ' ' + "\"https://www.ecosia.org/search?q=" +
                          search_text + self.read_filter_string("bing") + '\"'
                          + ' &')
            else:
                print(browser + ' ' + "\"https://www.ecosia.org/search?q=" +
                      search_text + '\"')
                os.system(browser + ' ' + "\"https://www.ecosia.org/search?q=" +
                          search_text + '\"' + ' &')
        except Exception, err:
            print ' Failed on_button1_clicked '
            print sys.stderr.write('ERROR: %sn' % str(err))
            print
        pass

    def on_button2_clicked(self, button):
        print("\"Google\" button was clicked")
        browser = self.read_browser_options()
        filter_options = self.read_filter_options()
        try:
            search_text = self.entry.get_text()
            if filter_options == "True":
                print(browser + ' ' + "\"https://www.google.com/?gws_rd=ssl#q="
                      + search_text + self.read_filter_string("bing") + '\"')
                os.system(browser + ' ' +
                          "\"https://www.google.com/?gws_rd=ssl#q=" +
                          search_text + self.read_filter_string("bing")
                          + '\"' + ' &')
            else:
                print(browser + ' ' +
                      "\"https://www.google.com/?gws_rd=ssl#q=" + search_text +
                      '\"')
                os.system(browser + ' ' +
                          "\"https://www.google.com/?gws_rd=ssl#q=" +
                          search_text + '\"' + ' &')
        except Exception, err:
            print ' Failed on_button2_clicked '
            print sys.stderr.write('ERROR: %sn' % str(err))
            print
        pass

    def on_button3_clicked(self, button):
        print("\"Duck Duck Go\" button was clicked")
        browser = self.read_browser_options()
        filter_options = self.read_filter_options()
        try:
            search_text = self.entry.get_text()
            if filter_options == "True":
                print(browser + ' ' + "\"https://duckduckgo.com/?q=" +
                      search_text + self.read_filter_string("bing") + '\"')
                os.system(browser + ' ' + "\"https://duckduckgo.com/?q=" +
                          search_text + self.read_filter_string("bing") + '\"'
                          + ' &')
            else:
                print(browser + ' ' + "\"https://duckduckgo.com/?q=" +
                      search_text + '\"')
                os.system(browser + ' ' + "\"https://duckduckgo.com/?q=" +
                          search_text + '\"' + ' &')
        except Exception, err:
            print ' Failed on_button3_clicked '
            print sys.stderr.write('ERROR: %sn' % str(err))
            print
        pass

    def on_nullege_clicked(self, button):
        print("\"Nullege\" was clicked")
        browser = self.read_browser_options()
        filter_options = self.read_filter_options()
        try:
            search_text = self.entry.get_text()
            if filter_options == "True":
                print(browser + ' ' + "\"http://nullege.com/codes/search/" +
                      search_text + self.read_filter_string("bing") + '\"')
                os.system(browser + ' ' + "\"http://nullege.com/codes/search/"
                          + search_text + self.read_filter_string("bing") + '\"'
                          + ' &')
            else:
                print(browser + ' ' + "\"http://nullege.com/codes/search/"
                      + search_text + '\"')
                os.system(browser + ' ' + "\"http://nullege.com/codes/search/"
                          + search_text + '\"' + ' &')
        except Exception, err:
            print ' Failed on_nullege_clicked '
            print sys.stderr.write('ERROR: %sn' % str(err))
            print
        pass

    def on_stackoverflow_clicked(self, button):
        print("\"stackoverflow\" was clicked")
        browser = self.read_browser_options()
        filter_options = self.read_filter_options()
        try:
            search_text = self.entry.get_text()
            if filter_options == "True":
                print(browser + ' '
                      + "\"https://stackoverflow.com/search?q=" + search_text
                      + self.read_filter_string("bing") + '\"')
                os.system(browser + ' '
                          + "\"https://stackoverflow.com/search?q="
                          + search_text + self.read_filter_string("bing")
                          + '\"' + ' &')
            else:
                print(browser + ' ' + "\"https://stackoverflow.com/search?q="
                      + search_text + '\"')
                os.system(browser + ' '
                          + "\"https://stackoverflow.com/search?q="
                          + search_text + '\"' + ' &')
        except Exception, err:
            print ' Failed on_nullege_clicked '
            print sys.stderr.write('ERROR: %sn' % str(err))
            print
        pass

    def on_programcreek_clicked(self, button):
        print("\"programcreek\" was clicked")
        browser = self.read_browser_options()
        filter_options = self.read_filter_options()
        try:
            search_text = self.entry.get_text()
            if filter_options == "True":
                print(browser + ' '
                      + "\"https://www.bing.com/search?q=" + search_text
                      + self.read_filter_string("bing") + ' (site%3Aprogramcreek.com)\"')
                os.system(browser + ' '
                          + "\"https://www.bing.com/search?q="
                          + search_text + self.read_filter_string("bing")
                          + ' (site%3Aprogramcreek.com)\"' + ' &')
            else:
                print(browser + ' ' + "\"https://www.bing.com/search?q="
                      + search_text + ' (site%3Aprogramcreek.com)\"')
                os.system(browser + ' '
                          + "\"https://www.bing.com/search?q="
                          + search_text + ' (site%3Aprogramcreek.com)\"' + ' &')
        except Exception, err:
            print ' Failed on_nullege_clicked '
            print sys.stderr.write('ERROR: %sn' % str(err))
            print
        pass

win = SearchHelperWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()



# [1] "https://stackoverflow.com/questions/45162862/how-do-i-set-an-icon-for-the-whole-application-using-pygobject"