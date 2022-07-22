import argparse
import subprocess
import docker


class BaseClass:
    parser = argparse.ArgumentParser(
        description='Process some integers.',
        formatter_class=argparse.RawTextHelpFormatter
    )
    command = subprocess
    client = docker.from_env()

    def run_docker_command(self, cmd=None):
        cmd = cmd.split(" ")
        image_list = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            text=True,
            check=True
        )
        print(image_list.stdout)
