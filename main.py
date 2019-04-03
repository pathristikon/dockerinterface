#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Text, BOTH, W, N, E, S, Listbox, messagebox
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

import json

class DockerInterface(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

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
            index = area.curselection()
            foldername = area.get(index)
            _run(information, foldername, checkIfComposerExistsBool(foldername))

        self.master.title("Py Docker Interface Manager")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        lbl = Label(self, text="Projects")
        lbl.grid(sticky=W, pady=4, padx=5)

        ### Directories list
        area = Listbox(self)
        for directory in getDirs("../"):
            area.insert(1, directory)

        area.select_set(0)

        area.grid(row=1, column=0, columnspan=2, rowspan=4,
                  padx=5, sticky=E + W + N)

        area.bind('<ButtonRelease-1>', getDirectories)

        ### Inspect Button
        abtn = Button(self, text="Inspect", command=inspect)
        abtn.grid(row=1, column=3)

        ### Build button
        abtn = Button(self, text="Build", command=buildProject)
        abtn.grid(row=1, column=4)

        ### Run button
        cbtn = Button(self, text="Run", command=runProject)
        cbtn.grid(row=2, column=3)

        ### System Prune button
        cbtn = Button(self, text="Prune", command=systemprune)
        cbtn.grid(row=2, column=4)

        #### Output area
        lb2 = Label(self, text="Output >>>")
        lb2.grid(sticky=W, row=4, column=0, pady=4, padx=5)

        information = Text(self)
        information.tag_config('warning', foreground="red")
        information.tag_config('notice', foreground="white", background="blue")
        information.tag_config('inspect', foreground="black", background="lightgray")
        information.tag_config('danger', foreground="white", background="red")
        information.grid(row=3, column=0, columnspan=3,
                  padx=5, sticky=E + W + S)

        ### test button
        settingsbtn = Button(self, text="TEST")
        settingsbtn.grid(row=4, column=3)

        ### test button
        settingsbtn = Button(self, text="TEST")
        settingsbtn.grid(row=4, column=4)

        ### Help Button
        hbtn = Button(self, text="Clear", command=clearConsole)
        hbtn.grid(row=5, column=0, padx=5)

        ### Close button
        obtn = Button(self, text="Close", command=self.closeWindow)
        obtn.grid(row=5, column=4)

        ### Settings button
        settingsbtn = Button(self, text="Settings", command=self.closeWindow)
        settingsbtn.grid(row=5, column=3)

    def closeWindow(self):
        message = messagebox.askokcancel("Closing application", "Would you really want to exit the application?")
        if message == True:
            self.master.destroy()

def main():
    root = Tk()
    root.geometry("750x645+500+200")
    DockerInterface()
    root.mainloop()

if __name__ == '__main__':
    main()