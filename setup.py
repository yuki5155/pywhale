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
    packages=['./pywhale/templates/python_temps'],
    package_dir={'./pywhale/templates/python_temps': 'pywhale/templates'},
    package_data={'./pywhale/templates/python_temps': ['python_temps/*']},
    entry_points = {
        'console_scripts': [
            'pywhale = pywhale.core.managers:start_command',
        ]
    }
)