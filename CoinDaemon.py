#!/usr/bin/python

from Constants import Constants as cnt

class CoinDaemon:
    coinName = ""

    coinPort = 00000

    COMMAND = ""

    coinDaemon = None
    coinDaemonStop = None

    def __init__(self, a_str, b_int, c_str):
        self.coinName = a_str
        self.coinPort = b_int
        self.COMMAND = cnt.SCRIPT_DIR + "bin/" + self.coinName + " -daemon "

    def start_daemon(self):
        """Responsible for starting the coin daemon process"""

        import subprocess, shlex, os

        os.system(self.COMMAND)
        #~ self.coinDaemon = subprocess.Popen(self.COMMAND.split())
        #~ proc.wait()
        #~ subprocess.call(self.COMMAND.split(), shell=True)


    def stop_daemon(self):
        """Responsible for stopping the coin daemon process"""

        import subprocess, time, os, signal

        self.COMMAND = "/usr/bin/pkill -9 " + self.coinName
        os.system(self.COMMAND)




    def is_running(self):
        import re, subprocess

        s = subprocess.Popen(["ps", "axw"],stdout=subprocess.PIPE)

        for x in s.stdout:
            if re.search(self.coinName, x):
                ding = True
                break
            else:
                ding = False

        return ding
