from setuptools import find_packages, setup #This will automatically find all the packages in the ML application
from typing import List

HYPEN_E = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this funtion will return the list of requirements
    '''
    # requirements = []
    # with open(file_path) as f:
    #     requirements = f.readlines()
    #     requirements = [req.replace('\n','')for req in requirements]
    requirements = open(file_path , 'r').read().splitlines()

    if HYPEN_E in requirements:
        requirements.remove(HYPEN_E) # This will remove the -e . text from the requirements.txt file and run  the code smoothly
    
    return requirements



setup(
    name = 'MLProject',
    version='0.0.1', # Update when I make next version 
    author = 'zahid',
    author_email='zahidshuvobd@gmail.com',
    packages=find_packages(), # It will find packages
    install_requires=get_requirements('requirements.txt'),
    
)