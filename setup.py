#!/usr/bin/env python

from distutils.core import setup

setup(name='cicero',
      version='0.1.0',
      description='Cicero - Serving slides written in Markdown.',
      author='Radovan Bast',
      author_email='bast@users.noreply.github.com',
      url='https://github.com/bast/cicero',
      packages=['cicero'],
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
            'flask>=0.10.1,<0.10.2'
      ]
     )
