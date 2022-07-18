from pywhale.core.managers.base import BaseClass
import pickle
import os

class RunCmdClass(BaseClass):
    def run_command(self):
        args, unknown = self.parser.parse_known_args()

        # print(args)
        # print(unknown)
        dir = os.getcwd()
        with open(dir + "/projectparams.pkl", "rb") as p:
            param = pickle.load(p)
        cmd = " ".join(unknown)

        # ローカルのディレクトリをコンテナ内にコピーする
        self.run_docker_command(
            f"docker cp .{param.workdir} pywhale:/app/src"
        )


        # self.run_docker_command(
        #     f"docker exec --workdir /app/src{param.workdir} pywhale {cmd}"
        # )
        os.system(f"docker exec --workdir /app/src{param.workdir} pywhale {cmd}")

        # コンテナ側のディレクトリをコピーする
        self.run_docker_command(
            f"docker cp pywhale:/app/src/{param.workdir} ./"
        )
