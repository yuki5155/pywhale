from setuptools import setup

setup(
    name = 'pywhale',
    version = '1.0.0',
    url = 'https://github.com/yuki5155/pywhale.git',
    license = 'Free',
    author = 'Yuki Asano',
    author_email = 'yukiasano@example.com',
    description = 'Hoge',
    install_requires = ['setuptools'],
    entry_points = {
        'console_scripts': [
            'pywhale = pywhale.core.managers:start_command',
        ]
    }
)