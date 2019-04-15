#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import Tk
from utils import window

def main():
    root = Tk()
    root.geometry("750x645+500+200")
    window.DockerInterface()
    root.mainloop()

if __name__ == '__main__':
    main()