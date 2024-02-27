from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'dexter_des'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name,'launch'), glob('launch/*')),
        (os.path.join('share', package_name,'world'), glob('world/*')),
        (os.path.join('share', package_name,'urdf'), glob('urdf/*')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ferbin',
    maintainer_email='fjferbin@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'line_follower_node = dexter_des.line_following:main'
        ],
    },
)
