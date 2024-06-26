from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'merge_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='haocheng',
    maintainer_email='s3789513@student.rmit.edu.au',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            f'marker_checker = {package_name}.MarkerChecker:main',
            f'exploration_manager = {package_name}.ExplorationManager:main',
            f'path_tracker = {package_name}.PathTracker:main',
            f'back_to_init = {package_name}.BackToInit:main'
        ],
    },
)
