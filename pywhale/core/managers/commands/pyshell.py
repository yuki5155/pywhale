from pywhale.core.managers.base import BaseClass
import os
import pty

pty, tty = pty.openpty()


class PyShellClass(BaseClass):
    def run_command(self):

        os.system('docker container exec -it pywhale bash')
