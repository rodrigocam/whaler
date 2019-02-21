import os
import re
from setuptools import setup, find_packages

init = open(os.path.join('src', 'whaler', '__init__.py')).read()
version = re.search(r"__version__ = '(\d+\.\d+.\d+)'", init).group(1)

setup(
    name='whaler',
    version=version,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    setup_requires='setuptools >= 30.3',
    entry_points={
        'console_scripts': ['whaler=whaler.cli:main'],
    }
)
