from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    """This function reads a requirements file and returns a list of requirements.""" 
    requirements=[]




    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements=[req.replace('\n', '') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlprojects',
    version='0.1.0',
    author='Raushan Raja',
    author_email='Raushanraja181933@gmail.com',
    packages=find_packages(),
    install_requires=['numpy','pandas','scikit-learn','matplotlib','seaborn'],
    extras_require={
        'all': get_requirements('requirements.txt')
    },
)