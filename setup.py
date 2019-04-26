#!/usr/bin/env python3
import os
from pathlib import Path
from setuptools import setup, find_packages
from dota2picker.version import VERSION

PACKAGE_DIR = Path(os.path.join(os.path.dirname(__file__), 'dota2picker'))

if __name__ == '__main__':
    setup(
        name='dota2picker',
        version=VERSION,
        packages=find_packages(),
        include_package_data=True,
        install_requires=['setuptools', 'setuptools-git', 'Pillow'],
        license='gpl-3.0',
        url='https://github.com/ellysh/dota2-counter-picker',
        author='Ilya Shpigor',
        author_email='petrsum@gmail.com',
        description='Various tools for counter picking heros in dota2',
        download_url = 'https://github.com/ellysh/dota2-counter-picker/archive/master.zip',
        keywords=['dota2', 'counter-pick'],
        entry_points={
            'console_scripts': [
                'd2-checker=dota2picker.checker:main',
                'd2-csv2pkl=dota2picker.csv2pkl:eluac',
                'd2-editor=dota2picker.editor:main',
                'd2-pk2csv=dota2picker.pkl2csv:main',
                'd2-picker=dota2picker.picker:main',
                'd2-team-picker=dota2picker.team_picker:main',
            ],
        },
        classifiers=[
            'Development Status :: 3 - Alpha',

            'Intended Audience :: End Users/Desktop',
            'Topic :: Games/Entertainment :: Real Time Strategy',

            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
          ],

    )
