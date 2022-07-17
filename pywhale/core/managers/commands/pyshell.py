from pywhale.core.managers.base import BaseClass
import subprocess
import os
import pty
import select
import sys

pty, tty = pty.openpty()


class PyShellClass(BaseClass):
    def run_command(self):
        #parameterを読み込む
        
        # self.run_docker_command(
        #     f"docker container exec -it pywhale bash"
        # )
        # p = subprocess.Popen((["docker", "container","exec", "-it", "pywhale", "bash",]), stdin=tty, stdout=tty, stderr=tty)
        # # 指定されたコマンドを実行
        # while p.poll() is None:
        #     # Watch two files, STDIN of your Python process and the pseudo terminal
        #     r, _, _ = select.select([sys.stdin, pty], [], [])
        #     if sys.stdin in r:
        #         input_from_your_terminal = os.read(sys.stdin.fileno(), 10240)
        #         os.write(pty, input_from_your_terminal)
        #     elif pty in r:
        #         output_from_docker = os.read(pty, 10240)
        #         os.write(sys.stdout.fileno(), output_from_docker)
        os.system('docker container exec -it pywhale bash')