from setuptools import find_packages, setup

package_name = 'follow_me_v1_0'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pi4bjazzy',
    maintainer_email='lhddw02@gmail.com',
    description='follow-me-ros',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'receiver = follow_me_v1_0.sub_func:main',
            'uwbserial = follow_me_v1_0.serial_sub_func:main',
        ],
    },
)
