#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import Tk
from utils import window

def main():
    root = Tk()
    root.geometry("585x490+500+200")
    root.resizable(False, False)
    window.DockerInterface()
    root.mainloop()

if __name__ == '__main__':
    main()