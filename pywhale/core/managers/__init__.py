import sys
import subprocess

from .commands.image_list import ImageListClass
from .base import BaseClass
from .commands.setup_python import SetupPythonCLass
from .commands.down_python import DownPythonCLass
from .commands.run import RunPythonClass
# from .commands.start_python_project
# PyShellClass
from .commands.pyshell import PyShellClass

# def run_command(self, command=None):
#     # command.
#     command = command.split(" ")
#     # image_list = self.command.run(["docker","ps"], stdout=subprocess.PIPE, text=True, check=True)
#     result = self.command.run(["docker","ps"], stdout=subprocess.PIPE, text=True, check=True)
   
#     print(result.stdout)

class CommandClass(BaseClass):
    
    def run_command(self):
        if sys.argv[1]=='-h' or sys.argv[1]=='--h':
            self.parser.add_argument('images_list')
            self.parser.add_argument('setup_python')
            self.parser.add_argument('down_python')
            self.parser.add_argument('run')
            self.parser.print_help()
        if sys.argv[1]=='images_list':
            self.parser.add_argument('images_list')
            image = ImageListClass()
            # print("aaa")
            image.run_command()
        if sys.argv[1]=='setup_python':
            self.parser.add_argument('setup_python')
            self.parser.add_argument('--workdir', help='')
            self.parser.parse_args()
            s = SetupPythonCLass()
            s.run_command()
        if sys.argv[1]=='down_python':
            s = DownPythonCLass()
            s.run_command()
        if sys.argv[1]=="start_python_project":
            pass
        if sys.argv[1]=="run":
            self.parser.add_argument('run')
            self.parser.add_argument('--cmd', help='')
            self.parser.parse_args()

            r = RunPythonClass()
            r.run_command()
        if sys.argv[1]=="pyshell":
            self.parser.add_argument('pyshell')
            p = PyShellClass()
            p.run_command()
            

def start_command():
    c = CommandClass()
    c.run_command()