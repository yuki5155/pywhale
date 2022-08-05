from pywhale.core.managers.base import BaseClass
import requests

class StartDockerCLass(BaseClass):
    def run_command(self):
        
        # dockerの場所を取得する
        args, unknown = self.parser.parse_known_args()
        # if docker_file is None:
        #     docker_file = os.getcwd() + "./"
        print(args, unknown)