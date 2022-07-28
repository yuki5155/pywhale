from traceback import print_tb
from pywhale.core.managers.base import BaseClass
import os
# import argparse


class PyShellClass(BaseClass):
    def run_command(self):
        args, unknown = self.parser.parse_known_args()
        print(args, unknown)
        if args.t == None:
            container_list = [container.name for container in self.client.containers.list()]
            # print(a)
            print("select a container you desire to get into")
            for c, i in enumerate(container_list):
                print(f"[{c}]:{i}")
            container_number = input()
            container_number = int(container_number)
            print(container_list[container_number])
            os.system(f'docker container exec -it {container_list[container_number]} bash')
        # os.system('docker container exec -it pywhale bash')
