from pywhale.core.managers.base import BaseClass

class StartMySQLClass(BaseClass):
    def run_command(self):
        # self.client.build("mysql")
        # MySQLのコンテナがあるのかを確認する
       
        a = [container.name for container in self.client.containers.list()]
        print(a)
        if not "pywhalemysql" in a:
            self.client.run('alpine', ports={'3306/tcp': ('0.0.0.1', 3306)})

