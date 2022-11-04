from pywhale.core.managers.base import BaseClass
import docker


class StartRedis(BaseClass):
    def __init__(self):
        self.is_container_existed: bool = False
        self.container_list = [
            container.name for container in self.client.containers.list()
        ]

    def linux_container_run(self):
        # portとバージョンを指定できるようにする
        self.client.containers.run(
            "redis",
            ports={"6379/tcp": ("0.0.0.0", 6379)},
            environment={},
            detach=True,
            name="pywhaleredis",
            extra_hosts={"host.docker.internal": "host-gateway"},
        )

    def run_command(self):

        if not "pywhaleredis" in self.container_list:
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
                        "redis",
                        ports={"6379/tcp": ("0.0.0.0", 6379)},
                        environment={
                        },
                        detach=True,
                        name="pywhaleredis",
                    )
                except docker.errors.APIError:
                    # まずは消す
                    self.client.containers.prune()
                    self.client.containers.run(
                        "redis",
                        ports={"6379/tcp": ("0.0.0.0", 6379)},
                        environment={
                            
                        },
                        detach=True,
                        name="redis",
                    )
