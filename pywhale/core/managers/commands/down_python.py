from pywhale.core.managers.base import BaseClass
import pywhale.templates as pytemps

class DownPythonCLass(BaseClass):
    def run_command(self):
        self.run_docker_command(
            f"docker container stop pywhale"
        )

        self.run_docker_command(
            f"docker container rm pywhale"
        )

        # docker container stop pywhale
        # docker container rm pywhale

        # dockerの場所を取得する
        # print(pytemps.temp_python)
        # self.run_docker_command(
        #     f"docker image build -t pywhale {pytemps.temp_python}"
        # )
        # self.run_docker_command(
        #     f"docker run --name pywhale -itd pywhale /bin/sh"
        # )

        # parameterファイルを作成

        # docker run --name pywhale -itd pywhale /bin/sh
        
        # docker image build -t pywhale .
        # self.run_docker_command("docker image ls")