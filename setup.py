from setuptools import setup
from valgrind_parser._version import _version

import os
with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r') as f:
    long_description = f.read()

setup(name='valgrind_parser',
      version=_version,
      description='The valgrind logs parser. Creates the html report from txt logs.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/siddheshsathe/Valgrind-Log-Parser',
      author='Siddhesh Sathe',
      author_email='siddheshsathe@rediffmail.com',
      licence='GNU General Public License v3.0',
      packages=['valgrind_parser'],
      install_requires=['json2table'],
      zip_safe=False
)
