from setuptools import setup
import setuptools
setup(
    name = 'pywhale',
    version = '1.0.0',
    url = 'https://github.com/yuki5155/pywhale.git',
    license = 'Free',
    author = 'Yuki Asano',
    author_email = 'yukiasano@example.com',
    description = 'Hoge',
    install_requires = ['setuptools'],
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': [
            'pywhale = pywhale.core.managers:start_command',
        ]
    }
)