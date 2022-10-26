from distutils.command.install import install
from pkg_resources import Requirement
from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    requirement_list:List[str] = []
    return requirement_list
    

setup(
    name = "sensor",
    version = "0.0.1",
    author = "Developer Ashish",
    author_email = "therobomarket@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)




# python3 setup.py install 