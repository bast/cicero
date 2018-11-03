from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.rst')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, 'cicero', 'version.py')) as f:
    exec(f.read(), version)

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory, followlinks=True):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

extra_files = package_files('cicero/static') + \
              package_files('cicero/templates')

setup(
    name='cicero',
    version=version['__version__'],
    description='Cicero - Serving presentation slides written in Markdown.',
    long_description=long_description,
    author='Radovan Bast',
    author_email='bast@users.noreply.github.com',
    url='https://github.com/bast/cicero',
    license='GNU Affero General Public License v3',
    packages=['cicero'],
    package_data={'': extra_files},
    entry_points={'console_scripts': ['cicero = cicero.main:main']},
    install_requires=[
        'requests==2.20.0',
        'flask==1.0.2'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.6'
    ],
)
