from pywhale.core.managers.base import BaseClass
import pickle
import os

class RunPythonClass(BaseClass):
    def run_command(self):
        #parameterを読み込む
        dir = os.getcwd()
        with open(dir + "/projectparams.pkl", "rb") as p:
            param = pickle.load(p)
        
        # print(param.workdir)
        # ディレクトリ元を丸ごとコピーしてコンテナ内に入れる

        # print(f"docker cp .{param.workdir} pywhale:/app/src")
        # docker内のworkdir内にコピーする
        self.run_docker_command(
            f"docker cp .{param.workdir} pywhale:/app/src"
        )
        # 指定されたコマンドを実行
        self.run_docker_command(
            f"docker exec --workdir /app/src/sample pywhale python aaa.py"
        )
