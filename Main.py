import os
import platform

class Maintainer(object):
    def __init__(self):
        self.system = platform.uname().system
        self.version = platform.uname().version
        self.arch = platform.uname().machine
        self.feedbacks = ["Scanning for updates...", "Downloading updates...", "Installing updates..."]
    
    @property
    def system_info(self):
        return str("     [ System Information ]\n"
                  f"Operating System:\t{self.system}\n"
                  f"System Version:\t\t{self.version}\n"
                  f"Architecture:\t\t{self.arch}")


class WindowsMaintain(Maintainer):
    def __init__(self, *args, **kwargs):
        super(WindowsMaintain, self).__init__(*args, **kwargs)
    
    def updater(self):
        commands = ["UsoClient StartScan", "UsoClient StartDownload", "UsoClient StartInstall"]
        for feed, command in enumerate(commands):
            print(f"{self.feedbacks[feed]}\n")
            os.system(command)
        



WindowsMaintain().updater()