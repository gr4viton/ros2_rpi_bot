import os
from glob import glob
from setuptools import setup

package_name = 'my_python_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        (os.path.join('share', package_name, 'action'), glob('action/*.action')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gr4viton',
    maintainer_email='lordmutty@gmail.com',
    description='Test python package',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'test = my_python_pkg.my_python_node:main'
        ],
    },
)
