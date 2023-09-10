#!/usr/bin/python3

#sudo apt install python3-tk
#sudo apt install python3-ttkthemes
#sudo apt install python3-psutil
#sudo apt install xterm


from tkinter import *
from tkinter import ttk
import tkinter as tk
from os import popen
#from PIL import ImageTk, Image



class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        """defines the basic look of the app"""
        # Window Basics
        self.title("Prima Di Tutto (Surface on Ubuntu)")

        app_width = 755
        app_height = 755
        global screen_width
        screen_width = self.winfo_screenwidth()
        global screen_height
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")


        # Notebook Theming
        global noteStyler
        noteStyler = ttk.Style(self)
        noteStyler.theme_use('yaru')
        noteStyler.configure(
            "TNotebook",
            borderwidth=0,
            tabposition="w",
            highlightthickness=0,
        )


        main_frame = ttk.Frame(self,padding=20)
        main_frame.pack(fill="both",expand=TRUE)

        read_first = ttk.Label(main_frame, text="This Application adds the Surface Custom Kernel, The Camera Driver and some usefull Tool and Fixes to\nUbuntu. To learn more go to the Developers's Github.")
        read_first.pack()

        surface_core = ttk.LabelFrame(main_frame,text="Surface Patch",padding=5)
        surface_core.pack(pady=10,fill="x")

        apps_core = ttk.LabelFrame(main_frame,text="Aplications",padding=5)
        apps_core.pack(pady=10,fill="x")

        fixes_core = ttk.LabelFrame(main_frame,text="Tweaks & Fixes",padding=5)
        fixes_core.pack(pady=10,fill="x")

        terminal_core = ttk.Label(main_frame,padding=5)
        terminal_core.pack(pady=10,fill="x")


        def surf_action(text):
            """Passes commands du auto generated buttons"""
            if text == "Install Surface Kernel":
                popen(
                    f'xterm -into %d -bg Grey11 -geometry 1000x500 -e "~/primo-di-tutto/scripts/debian_surface_kernel_install.sh && sleep 3 && exit ; exec bash"' % wid)
            if text == "Install Camera Driver":
                popen(
                    f'xterm -into %d -bg Grey11 -geometry 1000x500 -e "~/primo-di-tutto/scripts/debian_surface_cam_install.sh && sleep 3 && exit ; exec bash"' % wid)



        # Button list
        surface_button_list = [
            "Install Surface Kernel",
            "Install Camera Driver",
        ]

        surface_button_list1 = []
        conf_row = 0
        conf_column = 0
        for surf_button in surface_button_list:
            # Generates buttons from list with grid
            self.surface_button_x = ttk.Button(
                surface_core,
                width=25,
                text=surf_button,
                command=lambda text=surf_button: surf_action(text),
            )
            self.surface_button_x.grid(row=conf_row, column=conf_column, padx=5, pady=5)
            surface_button_list1.append(self.surface_button_x)
            conf_column = conf_column + 1
            if conf_column == 3:
                conf_row = conf_row + 1
                conf_column = 0


        def app_action(text):
            """Passes commands du auto generated buttons"""
            if text == "Install Flatpak":
                popen(
                    f'xterm -into %d -bg Grey11 -geometry 1000x500 -e "~/primo-di-tutto/scripts/debian_flatpak_install.sh && sleep 3 && exit ; exec bash"' % wid)
            if text == "Install Chrome-Gnome-Shell":
                popen(
                    f'xterm -into %d -bg Grey11 -geometry 1000x500 -e "pkexec apt install chrome-gnome-shell && sleep 3 && exit ; exec bash"' % wid)
            if text == "Install Gnome Tweaks":
                popen(
                    f'xterm -into %d -bg Grey11 -geometry 1000x500 -e "pkexec apt install gnome-tweaks && sleep 3 && exit ; exec bash"' % wid)
            if text == "Install Gnome Software":
                popen(
                    f'xterm -into %d -bg Grey11 -geometry 1000x500 -e "sudo apt install gnome-software && sleep 3 && exit ; exec bash"' % wid)
            if text == "Install Gnome Extesions App":
                popen(
                    f'xterm -into %d -bg Grey11 -geometry 1000x500 -e "pkexec apt install gnome-shell-extensions && sleep 3 && exit ; exec bash"' % wid)
            if text == "Install Paprirus + Folders":
                popen(
                    f'xterm -into %d -bg Grey11 -geometry 1000x500 -e "~/primo-di-tutto/scripts/ubuntu_papirus_+_papirus_folder_install.sh && sleep 3 && exit ; exec bash"' % wid)



        # Button list
        ubuntu_button_list = [
            
            "Install Flatpak",
            "Install Chrome-Gnome-Shell",
            "Install Gnome Tweaks",
            "Install Gnome Software",
            "Install Gnome Extesions App",
            "Install Paprirus + Folders",
        ]

        ubuntu_button_list1 = []
        conf_row = 0
        conf_column = 0
        for app_button in ubuntu_button_list:
            # Generates buttons from list with grid
            self.ubuntu_button_x = ttk.Button(
                apps_core,
                width=25,
                text=app_button,
                command=lambda text=app_button: app_action(text),


            )
            self.ubuntu_button_x.grid(row=conf_row, column=conf_column, padx=5, pady=5)
            ubuntu_button_list1.append(self.ubuntu_button_x)
            conf_column = conf_column + 1
            if conf_column == 3:
                conf_row = conf_row + 1
                conf_column = 0


        def fix_action(text):
            """Passes commands du auto generated buttons"""
            if text == "Install Firefox PPA":
                popen(
                    f'xterm -into %d -bg Grey11 -geometry 1000x500 -e "~/primo-di-tutto/scripts/ubuntu_firefox_snapt_to_ppa && sleep 3 && exit ; exec bash"' % wid)
            if text == "Install GS Flatpak PlugIn":
                popen(
                    f'xterm -into %d -bg Grey11 -geometry 1000x500 -e "pkexec apt install gnome-software-plugin-flatpak && sleep 3 && exit ; exec bash"' % wid)
            if text == "Install MS Fonts":
                popen(
                    f'xterm -into %d -bg Grey11 -geometry 1000x500 -e "~/primo-di-tutto/scripts/ubuntu_ms_font_install && sleep 3 && exit ; exec bash"' % wid)
            if text == "Dock Minimizer App":
                popen(
                    f'xterm -into %d -bg Grey11 -geometry 1000x500 -e "~/primo-di-tutto/scripts/ubuntu_minimize_by_dock.sh && sleep 3 && exit ; exec bash"' % wid)
            if text == "Dock Minimizer Reset":
                popen(
                    f'xterm -into %d -bg Grey11 -geometry 1000x500 -e "~/primo-di-tutto/scripts/ubuntu_minimize_by_dock_reset.sh && sleep 3 && exit ; exec bash"' % wid)
            if text == "Flatpak Cursor Fix":
                popen(
                    f'xterm -into %d -bg Grey11 -geometry 1000x500 -e "~/primo-di-tutto/scripts/debian_flatpak_cursor_fix.sh && sleep 3 && exit ; exec bash"' % wid)


        # Button list
        fix_button_list = [
            "Install Firefox PPA",
            "Install GS Flatpak PlugIn",
            "Install MS Fonts",
            "Dock Minimizer App",
            "Dock Minimizer Reset",
            "Flatpak Cursor Fix",
        ]

        fix_button_list1 = []
        conf_row = 0
        conf_column = 0
        for fix_button in fix_button_list:
            # Generates buttons from list with grid
            self.fix_button_x = ttk.Button(
                fixes_core,
                #justify="left",
                #compound="left",
                width=25,
                #anchor="w",
                text=fix_button,
                command=lambda text=fix_button: fix_action(text),
                #highlightthickness=0,
                #borderwidth=0,
                #font=(font_12),
                #background=ext_btn

            )
            self.fix_button_x.grid(row=conf_row, column=conf_column, padx=5, pady=5)
            fix_button_list1.append(self.fix_button_x)
            conf_column = conf_column + 1
            if conf_column == 3:
                conf_row = conf_row + 1
                conf_column = 0


        self.termf = ttk.Frame(
            terminal_core,
            height=600,
            width=960,
        )

        wid = self.termf.winfo_id()
    

        self.termf.pack(fill=BOTH, expand=True, padx=5)
        #self.termf.pack_propagate(0)


# [End Of The Line]
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()