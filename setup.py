from setuptools import find_packages, setup 
from typing import List

def get_requirements() -> List[str]:
    '''
    This function will return lot of requirements
    '''
    requirement_1st:List[str] = []

    try:
        with open ('requirements.txt', 'r') as file:
            ## Read line from the file
            lines = file.readlines()
        
            ## Process each file
            for line in lines:
                requirement = line.strip()
            
            ## Ignore empty lines.
            if requirement and requirement != '-e .':
                requirement_1st.append(requirement)

    except FileNotFoundError:
        print('requirements.txt file not found')
    
    return requirement_1st

print(get_requirements())

## Settingup Metadata 
setup(
    name="NetworkSecurity",
    version="0.0.2",
    author="Olumide Oba",
    author_email="olumide2obanla@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
) 