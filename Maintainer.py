import os
import sys
import platform

class Maintainer(object):
    def __init__(self):
        self.system = platform.uname().system
        self.version = platform.uname().version
        self.arch = platform.uname().machine
        self.pyversion = sys.version.split("(")[0]
        self.feedbacks = ["Scanning for updates...", "Downloading updates...", "Installing updates..."]
        self.cleaner = {"Windows": "cls", 
                         "Linux": "clear", 
                         "Darwin": "clear"}
    
    @property
    def system_info(self):
        return str("     [ System Information ]\n"
                  f"Operating System:\t{self.system}\n"
                  f"System Version:\t\t{self.version}\n"
                  f"Architecture:\t\t{self.arch}\n"
                  f"Python Version:\t\t{self.pyversion}")
    
    def __str__(self):
        return str(self.system)


class WindowsMaintain(Maintainer):
    def __init__(self, *args, **kwargs):
        super(WindowsMaintain, self).__init__(*args, **kwargs)
    
    def updater(self):
        commands = ["UsoClient StartScan", "UsoClient StartDownload", "UsoClient StartInstall"]
        for feed, command in enumerate(commands):
            print(f"{self.feedbacks[feed]}\n")
            os.system(command)
        

class DebianMaintain(Maintainer):
    def __init__(self, *args, **kwargs):
        super(DebianMaintain, self).__init__(*args, **kwargs)
    
    def updater(self):
        commands = ["sudo apt update -y", "sudo apt upgrade -y", "sudo apt dist-upgrade -y"]
        for feed, command in enumerate(commands):
            print(f"{self.feedbacks[feed]}\n")
            os.system(command)


if __name__ == "__main__":
    operating_systems = {"Windows": WindowsMaintain(), 
                         "Linux": DebianMaintain(), 
                         "Darwin": "None"}
    ops = platform.uname().system
    os.system(Maintainer().cleaner[ops])
    if ops in operating_systems.keys():
        print(operating_systems[ops].system_info)
    else:
        print(f"Unsupported Operating System: {ops}")

