#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This script is part of the docker interface python script

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.

@author Alexandru Dumitru
@website https://www.webdal.ro
"""

from tkinter import Tk
from utils import window

def main():
    root = Tk()
    root.geometry("585x490+500+200")
    root.resizable(False, False)
    root.wm_iconbitmap('docker-interface.ico')
    window.DockerInterface()
    root.mainloop()

if __name__ == '__main__':
    main()