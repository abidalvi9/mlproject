from setuptools import find_packages, setup
# it will autmatically find packages and setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirments
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        # this will initiate reading of requirement.txt 
        # and read line one by one
        # but whenever we use readline function it will create \n
        # to handle that we need bellow code 
        # requirements[req.replace("\n", " ") for req in requirements]
        requirements[req.strip() for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements        


setup(
name='mlproject',
version='0.0.1'
author="Abhijeet"
author_email="abhidalvi24@gmail.com"
packages=find_packages()
# install_requires=('pandas','numpy','seaborn')
# we are not using above code line because, 
# it is not feasible 
install_requires=get_requirements('requirements.txt')

) 

# we can directly install setup.py or whenever we trying install requirements.txt
# at that time setup.py file also should run
# for that add "-e ." in requiremnet.txt file 

# now at time of triggering def get_requirements()
# -e . y will aslo come