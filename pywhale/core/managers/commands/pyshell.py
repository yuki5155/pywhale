from traceback import print_tb
from pywhale.core.managers.base import BaseClass
import os
# import argparse


class PyShellClass(BaseClass):
    def run_command(self):
        args, unknown = self.parser.parse_known_args()
        print(args, unknown)
        # os.system(f'docker container exec -it pywhale bash')
        # os.system('docker container exec -it pywhale bash')
