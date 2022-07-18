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

        # for i in range(100):
        #     os.system(f"kill -9 {i}")
        for i in range(100):
            self.run_docker_command(
                f"docker exec --workdir /app/src{param.workdir} pywhale kill -9 {i}"
            )


        # self.run_docker_command(
        #     f"docker exec --workdir /app/src{param.workdir} pywhale {cmd}"
        # )
        os.system(f"docker exec --workdir /app/src{param.workdir} pywhale {cmd}")
        # pywhale run_cmd kill -9 36

        # pywhale run_cmd ps aux | grep manage
        # コンテナ側のディレクトリをコピーする
        self.run_docker_command(
            f"docker cp pywhale:/app/src/{param.workdir} ./"
        )
