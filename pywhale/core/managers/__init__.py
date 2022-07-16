import sys
import subprocess
from .commands.image_list import ImageListClass
from .base import BaseClass
from .commands.setup_python import SetupPythonCLass
from .commands.down_python import DownPythonCLass
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
            self.parser.print_help()
        if sys.argv[1]=='images_list':
            self.parser.add_argument('images_list')
            image = ImageListClass()
            # print("aaa")
            image.run_command()
        if sys.argv[1]=='setup_python':
            s = SetupPythonCLass()
            s.run_command()
        if sys.argv[1]=='down_python':
            s = DownPythonCLass()
            s.run_command()
        if sys.argv[1]=="":
            pass

def start_command():
    c = CommandClass()
    c.run_command()