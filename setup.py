#!/usr/bin/env python

from distutils.core import setup

import os

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory, followlinks=True):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

extra_files = package_files('cicero/static') + \
              package_files('cicero/templates')

setup(name='cicero',
      version='0.1.0',
      description='Cicero - Serving slides written in Markdown.',
      author='Radovan Bast',
      author_email='bast@users.noreply.github.com',
      url='https://github.com/bast/cicero',
      packages=['cicero'],
      package_data={'': extra_files},
      license='GNU Lesser General Public License 2.1',
      entry_points={
            'console_scripts': [
            'cicero = cicero.main:main'
            ]
        },
      install_requires=[
            'requests',
            'sphinx',
            'sphinx_rtd_theme',
            'flask==1.0.2'
      ]
     )
