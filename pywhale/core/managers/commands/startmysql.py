from pywhale.core.managers.base import BaseClass

class StartMySQLClass(BaseClass):
    def run_command(self):
        # self.client.build("mysql")
        # MySQLのコンテナがあるのかを確認する
        print("aaaa")
        print(self.client.containers.list())