from setuptools import find_namespace_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements file and returns a list of dependencies.
    Removes newline characters, handles blank lines, and removes '-e .' if present.
    """
    requirements = []
    try:
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.strip() for req in requirements if req.strip()]  # Strip and filter empty lines
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)  # Remove '-e .' if it exists
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author="Deva",
    author_email='devraj30103@gmail.com',
    packages=find_namespace_packages(),
    install_requires=get_requirements('requirements.txt')  # Ensure 'requirements.txt' is the correct file name
)
