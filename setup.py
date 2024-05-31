from setuptools import find_packages, setup
from typing import List

# Function to parse the Requirements.txt file
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name='ML-PREDICTIONS',
    version='0.0.1',
    author='simrannavya',
    author_email='dhruv.bhambani@position2.com',
    packages=find_packages(),
    install_requires=get_requirements('Requirements.txt')  # Pass path to Requirements.txt here
)

    