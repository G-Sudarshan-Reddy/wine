from typing import List
from setuptools import find_packages, setup

hypen = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace("\n","") for i in requirements]
        if hypen in requirements:
            requirements.remove(hypen)

    return requirements

# setup(name='mlproject',version=0.0.1,author='Sudarshan',author_email='sudarshangopal10@gmail.com')
setup(name='wine', version=0.1, author='Sudarshan', author_email='sudarshangopal10@gmail.com',
      packages=find_packages(),
      install_requires = get_requirements('requirements.txt'))