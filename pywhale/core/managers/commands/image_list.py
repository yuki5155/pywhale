from pywhale.core.managers.base import BaseClass


class ImageListClass(BaseClass):
    def run_command(self):
        self.run_docker_command("docker image ls")
