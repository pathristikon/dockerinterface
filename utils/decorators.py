"""
This script is part of the docker interface python script

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.

@author Alexandru Dumitru
@website https://www.webdal.ro
"""

import datetime, os
import subprocess, shlex, sys
from subprocess import CalledProcessError
import _thread

def executeCommand(description):
    """
    Decorator for executing bash commands
    :param description:
    :return:
    """
    def wrap(func):
        def wrapped_f(*args):
            command = func(*args)
            text = "\n[NOTICE] " + str(datetime.datetime.now())
            text += " " + description + "\n"
            args[0].insert("end", text, "inspect")
            try:
                _thread.start_new_thread(run_command, (command, args,))
            except:
                print ("Error: unable to start thread")
        return wrapped_f
    return wrap

def run_command(command, args):
    """
    Execute command in new thread
    :param command:
    :param args:
    :return:
    """
    try:
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

    except subprocess.CalledProcessError as err:
        print("Status : FAIL", err.returncode, err.output)

    else:
        proc = process.stdout

        while process.poll() is None:
            args[0].insert("end", proc.readline())
            args[0].insert("end", "\n")
            args[0].see("end")
        sys.stdout.flush()

        if process.returncode != 0:
            args[0].insert("end", "Error: " + process.communicate()[1].decode("utf-8") +" \n")
            args[0].see("end")
            raise Exception("The subprocess did not terminate correctly.")

        # wait for one process to finish
        # before starting another
        process.wait()



