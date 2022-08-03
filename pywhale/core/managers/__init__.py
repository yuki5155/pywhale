import sys
from .commands.image_list import ImageListClass
from .base import BaseClass
from .commands.setup_python import SetupPythonCLass
from .commands.down_python import DownPythonCLass
from .commands.run import RunPythonClass
# from .commands.start_python_project
# PyShellClass
from .commands.pyshell import PyShellClass
from .commands.run_cmd import RunCmdClass
from .commands.startmysql import StartMySQLClass
from .commands.create_dockerfile import CreateDockerfileCLass


class CommandClass(BaseClass):
    def run_command(self):
        if sys.argv[1] == '-h' or sys.argv[1] == '--h':
            self.parser.add_argument('images_list')
            self.parser.add_argument('setup_python')
            self.parser.add_argument('down_python')
            self.parser.add_argument('run')
            self.parser.add_argument('run_cmd')
            self.parser.add_argument('pyshell')
            self.parser.add_argument('startmysql')
            self.parser.add_argument('create_dockerfile')
            self.parser.print_help()


        if sys.argv[1] == 'images_list':
            self.parser.add_argument('images_list')
            image = ImageListClass()
            # print("aaa")
            image.run_command()

            
        if sys.argv[1] == 'setup_python':
            self.parser.add_argument(
                'setup_python',
                help="write workdir on dockerfile with /app/src/"
            )
            self.parser.add_argument(
                '--workdir',
                help='for the localdir, not in the container'
            )
            self.parser.add_argument(
                '--dockerfile_dir',
                help='',
                required=True
            )
            self.parser.add_argument('--ports', help='ex: 8000:8000',)
            self.parser.parse_args()
            s = SetupPythonCLass()
            s.run_command()
        if sys.argv[1] == 'down_python':
            s = DownPythonCLass()
            s.run_command()
        if sys.argv[1] == "start_python_project":
            pass
        if sys.argv[1] == "run":
            self.parser.add_argument('run')
            self.parser.add_argument('--cmd', help='')
            self.parser.add_argument('--nocache', help='TRUE or False')
            self.parser.parse_args()

            r = RunPythonClass()
            r.run_command()

        if sys.argv[1] == "install":
            self.parser.add_argument('install')

        if sys.argv[1] == "pyshell":
            self.parser.add_argument('pyshell')
            self.parser.add_argument('--t')
            p = PyShellClass()
            p.run_command()

        if sys.argv[1] == "run_cmd":
            self.parser.add_argument('run_cmd')
            self.parser.add_argument('--cd')
            r = RunCmdClass()
            r.run_command()

        if sys.argv[1] == "startmysql":
            self.parser.add_argument('startmysql')
            # self.parser.add_argument('--cd')
            mysql = StartMySQLClass()
            mysql.run_command()
        
        if sys.argv[1] == "create_dockerfile":
            # self.parser.add_argument('startmysql')
            # self.parser.add_argument('--cd')
            Dockerfile = CreateDockerfileCLass()
            Dockerfile.run_command()


def start_command():
    c = CommandClass()
    c.run_command()
