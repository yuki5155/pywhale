from pywhale.core.managers.base import BaseClass
import pywhale.templates as pytemps

class SetupPythonCLass(BaseClass):
    def run_command(self):

        # dockerの場所を取得する
        print(pytemps.temp_dir)

        pass

        # self.run_docker_command("docker image ls")