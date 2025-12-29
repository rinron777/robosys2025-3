from setuptools import find_packages, setup

package_name = 'robosysros2_pkg'

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
    maintainer='tiba07',
    maintainer_email='github4273senyou564@gmail.com',
    description='TODO: Package description',
    license='BSD-3-Clause',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
             'cpu_usage_publisher = robosysros2_pkg.cpu_usage_publisher:main',
             'cpu_usage_listener  = robosysros2_pkg.cpu_usage_listener:main',
        ],
    },
)
