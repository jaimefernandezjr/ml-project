from setuptools import find_packages, setup
from typing import List

# 2
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:   # read each line in requirements.txt
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:   # if setup.py is run and not run through requirements.txt, we should not execute '-e .'
            requirements.remove(HYPEN_E_DOT)

    return requirements

# 1
setup(
    name='mlproject',
    version='0.0.1',
    author='Jaime',
    author_email='jjrfernandeztech@gmail.com',
    package=find_packages(),   #  automatically discover and include all the Python packages (directories containing __init__.py files) in your project.
    install_requires=get_requirements('requirements.txt')
)

