from pywhale.core.managers.base import BaseClass
import pywhale.templates as pytemps
import pickle
import os
from pywhale.core.managers.paramaters import ParamClass

class SetupPythonCLass(BaseClass):
    def run_command(self):

        # dockerの場所を取得する
        # print(pytemps.temp_python)
        docker_file = self.parser.parse_args().dockerfile_dir
        if docker_file==None:
            docker_file = os.getcwd()
        self.run_docker_command(
            f"docker image build -t pywhale {docker_file}"
        )
        self.run_docker_command(
            f"docker run --name pywhale -itd pywhale /bin/sh"
        )

        param = ParamClass()
        # print(self.parser.parse_args().workdir)
        if self.parser.parse_args().workdir == None:
            try:
                os.makedirs("./script")
                param.workdir = f"/script"
            except FileExistsError:
                param.workdir = f"/script"
        
        else:
            try:
                os.makedirs(self.parser.parse_args().workdir)
                param.workdir = f"/{self.parser.parse_args().workdir}"
            except FileExistsError:
                param.workdir = f"/{self.parser.parse_args().workdir}"
        

        # print(os.getcwd())
        # try:
        #     os.makedirs("projectparams")
        # except FileExistsError:
        #     pass

        # 実行をするスクリプトのファイル

        with open(f"{os.getcwd()}/projectparams.pkl", "wb") as file:
            pickle.dump(param, file)

        # parameterファイルを作成

        # docker run --name pywhale -itd pywhale /bin/sh
        
        # docker image build -t pywhale .
        # self.run_docker_command("docker image ls")