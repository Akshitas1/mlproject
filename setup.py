from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    
    requirements=[]
    with open(file_path) as file_obj:
        HYPHER_E_DOT="-e ."
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPHER_E_DOT in requirements:
            requirements.remove(HYPHER_E_DOT)
            
    return requirements

setup(
    
    name='mlproject',
    version='0.0.1',
    author='Akshita Saxena',
    author_email='akshitasaxena04@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)