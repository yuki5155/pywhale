from pywhale.core.managers.base import BaseClass
import docker



class StartMySQLClass(BaseClass):

    def linux_container_run(self):
        
        self.client.containers.run(
            'mysql', 
                    ports={
                        '3306/tcp': ('0.0.0.0', 3306)
                    },
                    environment = {
                        "MYSQL_ROOT_PASSWORD": "sample",
                        "MYSQL_USER": "sample",
                        "MYSQL_PASSWORD": "sample"
                    },
                    detach=True,
                    name="pywhalemysql",
                    extra_hosts={
                        "host.docker.internal": "host-gateway"
                    }

                )
    def run_command(self):
        # MySQLのコンテナがあるのかを確認する
       
        a = [container.name for container in self.client.containers.list()]
        
        if not "pywhalemysql" in a:
            if self.operating_system == "Linux":
                try:
                    self.linux_container_run()
                except docker.errors.APIError:
                    # まずは消す
                    self.client.containers.prune()
                    self.linux_container_run()
            else:
                try:
                    self.client.containers.run(
                        'mysql', 
                        ports={
                            '3306/tcp': ('0.0.0.0', 3306)
                        },
                        environment = {
                            "MYSQL_ROOT_PASSWORD": "sample",
                            "MYSQL_USER": "sample",
                            "MYSQL_PASSWORD": "sample"
                        },
                        detach=True,
                        name="pywhalemysql"
                    )
                except docker.errors.APIError:
                    # まずは消す
                    self.client.containers.prune()
                    self.client.containers.run(
                        'mysql', 
                        ports={
                            '3306/tcp': ('0.0.0.0', 3306)
                        },
                        environment = {
                            "MYSQL_ROOT_PASSWORD": "sample",
                            "MYSQL_USER": "sample",
                            "MYSQL_PASSWORD": "sample"
                        },
                        detach=True,
                        name="pywhalemysql"
                    )



