import argparse
import subprocess

class BaseClass:
    parser = argparse.ArgumentParser(
        description='Process some integers.', 
        formatter_class=argparse.RawTextHelpFormatter
    )
    command = subprocess
    def run_docker_command(self, cmd=None):
        cmd = cmd.split(" ")
        image_list = subprocess.run(cmd, stdout=subprocess.PIPE, text=True, check=True)
        print(image_list.stdout)