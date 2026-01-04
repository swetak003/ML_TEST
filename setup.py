## JAI GANEHSHAY NAMAH
### basic information of the package:TRacking info, licence date, author name, maintaner name, version name

from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    the function will return the list of requirements
    '''
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]
    
    return requirements

setup(
    name="ML Project",
    version="0.0.0.1",
    author="Sweta Kumari",
    author_email="swetakumari071188@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')###it will read the package from the requirememts from txt & install the same
)