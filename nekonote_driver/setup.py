from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['follow_joint_trajectory_action'],
    package_dir={'': 'src'}
)

setup(**d)
