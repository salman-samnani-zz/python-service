import time
import random
from pathlib import Path
from SMWinservice import SMWinservice
import add_employee
import os

class PythonCornerExample(SMWinservice):
    _svc_name_ = "PythonCornerExample"
    _svc_display_name_ = "Python Corner's Winservice Example"
    _svc_description_ = "That's a great winservice! :)"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        i = 0
        while self.isrunning:
            #exec(open('add_employee.py').read())
            os.system('python add_employee.py')
            f= open("c:\salman.txt","w+")
            for i in range(10):
                f.write("This is line sas %d\r\n" % (i+1))

if __name__ == '__main__':
    PythonCornerExample.parse_command_line()