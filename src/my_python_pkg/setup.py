import os
from glob import glob
from setuptools import setup
from io import open

import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

package_name = 'my_python_pkg'

# automatically captured required modules for install_requires in requirements file and as well as configure dependency lin
with open(os.path.join(HERE, 'pip-reqs.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [
    x.strip() for x in all_reqs if ('git+' not in x) and (not x.startswith('#')) and (not x.startswith('-'))
]
install_requires.append("setuptools")

dependency_links = [x.strip().replace('git+', '') for x in all_reqs if 'git+' not in x]


setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        (os.path.join('share', package_name, 'action'), glob('action/*.action')),
    ],
    # install_requires=['setuptools'],
    install_requires=install_requires,
    zip_safe=True,
    maintainer='gr4viton',
    maintainer_email='lordmutty@gmail.com',
    description='Test python package',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'test = my_python_pkg.my_python_node:main',
            'led = my_python_pkg.led_service_server:main',
            'but = my_python_pkg.button_service_client:main',
            'mot = my_python_pkg.motor_service_server:main',
        ],
    },
)
