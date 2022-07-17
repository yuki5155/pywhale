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
    packages=[
        "pywhale",
        'pywhale.templates.python_temps'
    ],
    package_dir={
        "pywhale.core:":"pywhale/core",
        'pywhale.templates.python_temps': 'pywhale/templates',
        #"pywhale": 'pywhale'
    },
    package_data={
        "pywhale": ['./*'],
        'pywhale.templates.python_temps': ['python_temps/*']
    },
    entry_points = {
        'console_scripts': [
            'pywhale = pywhale.core.managers:start_command',
        ]
    }
)