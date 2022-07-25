from pywhale.core.managers.base import BaseClass
import pickle
import os
from pywhale.core.managers.paramaters import ParamClass


class SetupPythonCLass(BaseClass):
    def run_command(self):

        # dockerの場所を取得する
        docker_file = self.parser.parse_args().dockerfile_dir
        ports = self.parser.parse_args().ports
        if docker_file is None:
            docker_file = os.getcwd() + "./"

        if ports is not None:

            self.run_docker_command(
                f"docker image build -t pywhale {docker_file}"
            )
            self.run_docker_command(
                f"docker run --name pywhale -itd -p {ports} pywhale /bin/sh"
            )

        else:
            self.run_docker_command(
                f"docker image build -t pywhale {docker_file}"
            )
            self.run_docker_command(
                "docker run --name pywhale -itd pywhale /bin/sh"
            )

        param = ParamClass()
        # print(self.parser.parse_args().workdir)
        if self.parser.parse_args().workdir is None:
            try:
                os.makedirs("./script")
                param.workdir = "/script"
                self.run_docker_command(
                    "docker exec --workdir /app/src/ pywhale mkdir script"
                )
            except FileExistsError:
                param.workdir = "/script"
                self.run_docker_command(
                    "docker exec --workdir /app/src/ pywhale mkdir script"
                )
        
        else:
            try:
                os.makedirs(self.parser.parse_args().workdir)
                param.workdir = f"/{self.parser.parse_args().workdir}"
            except FileExistsError:
                param.workdir = f"/{self.parser.parse_args().workdir}"
        
        # 実行をするスクリプトのファイル

        with open(f"{os.getcwd()}/projectparams.pkl", "wb") as file:
            pickle.dump(param, file)
