from tkinter import Tk as tk, Text, BOTH, W, N, E, S, Listbox, messagebox
from tkinter.ttk import Frame, Button, Label, Style

from utils.utils import getDirs
from utils.utils import getContainers
from utils.utils import getWarnings
from utils.utils import sysPrune
from utils.utils import inspectProject
from utils.utils import checkIfComposerExists
from utils.utils import checkIfComposerExistsBool
from utils.utils import getDockerfiles
from utils.utils import buildDockerfiles
from utils.utils import _run
from utils.utils import stackRM

class DockerInterface(Frame):
    """
    Docker interface visual class
    @TODO: to refactor
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.master.title("Py Docker Interface Manager")

        ####################
        # used functions
        ####################

        def getDirectories(event):
            # current directory that we are looking for
            information.see("end")

        def systemprune():
            message = messagebox.askokcancel("Warning", "Would you like to perform a system prune?")
            if message:
                sysPrune(information)

        def inspect():
            if getWarnings():
                for message in getWarnings():
                    information.insert("end", message, "warning")

            index = area.curselection()
            inspectProject(information, area.get(index))

            # checking if composer exists
            information.insert("end", checkIfComposerExists(area.get(index)), "notice")

            information.see("end")

        def clearConsole():
            message = messagebox.askokcancel("Warning", "Clear the console?")
            if message:
                information.delete(1.0, "end")

        def buildProject():
            index = area.curselection()
            if len(getDockerfiles(area.get(index))) > 1:
                message = messagebox.askokcancel("Attention!", "More than one Dockerfiles found. Build all?")
                if message:
                    buildDockerfiles(information, getDockerfiles(area.get(index)), area.get(index), True)
                else:
                    buildDockerfiles(information, getDockerfiles(area.get(index)), area.get(index), False)
            else:
                buildDockerfiles(information, getDockerfiles(area.get(index)), area.get(index), False)

        def runProject():
            message = messagebox.askokcancel("Attention!", "Start the current project?")
            if message:
                index = area.curselection()
                foldername = area.get(index)
                _run(information, foldername, checkIfComposerExistsBool(foldername))

        def removeStack():
            message = messagebox.askokcancel("Attention!", "Removing the stack for the current project?")
            project = area.get(area.curselection())
            if message:
                stackRM(information, project)

        ####################
        # sidebar area
        ####################

        sidebar = Frame(self.master, width=200, height=500, relief='flat', borderwidth=2)
        sidebar.pack(expand=False, fill='both', side='right', anchor='ne')

        ### Inspect Button
        abtn = Button(sidebar, text="Inspect", command=inspect)
        abtn.grid(row=0, column=0, pady=2)

        ### Build button
        abtn = Button(sidebar, text="Build", command=buildProject)
        abtn.grid(row=1, column=0, pady=2)

        ### Run button
        cbtn = Button(sidebar, text="Run", command=runProject)
        cbtn.grid(row=2, column=0, pady=2)

        ### System Prune button
        cbtn = Button(sidebar, text="Prune", command=systemprune)
        cbtn.grid(row=3, column=0, pady=2)

        ### Stack rm button
        settingsbtn = Button(sidebar, text="Remove", command=removeStack)
        settingsbtn.grid(row=4, column=0, pady=2)

        ### Close button
        obtn = Button(sidebar, text="Close", command=self.closeWindow)
        obtn.grid(row=7, column=0, pady=2)

        ####################
        # main content area
        ####################
        main_content = Frame(self.master, relief='groove')
        main_content.pack(expand=True, fill='both', side='left')

        lbl = Label(main_content, text="Projects")
        lbl.grid(sticky=W, pady=4, padx=5)

        ### Directories list
        area = Listbox(main_content, width=60)
        for directory in getDirs("../"):
            area.insert(1, directory)

        area.select_set(0)

        area.grid(row=1, column=0, rowspan=4,
                  padx=5, sticky=E + W + N + S)

        area.bind('<ButtonRelease-1>', getDirectories)

        #information area
        information = Text(main_content, width=60, height=15)
        information.tag_config('warning', foreground="red")
        information.tag_config('notice', foreground="white", background="blue")
        information.tag_config('inspect', foreground="black", background="lightgray")
        information.tag_config('danger', foreground="white", background="red")
        information.grid(row=6, column=0,
                  pady=10, padx=5, sticky=E + W + S + N)

        #### Output area
        lb2 = Label(main_content, text="Output >>>")
        lb2.grid(sticky=W, row=7, column=0, pady=4, padx=5)

    def closeWindow(self):
        message = messagebox.askokcancel("Closing application", "Would you really want to exit the application?")
        if message == True:
            self.master.destroy()