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
        url='https://github.com/ellysh/dota2-counter-picker',
        author='Ilya Shpigor',
        author_email='petrsum@gmail.com',
        description='Various tools for counter picking heros in dota2',
        keywords=['dota2', 'counter-pick'],
        entry_points={
            'console_scripts': [
                'dota2picker-checker=dota2picker.checker:main',
                'dota2picker-csv2pkl=dota2picker.csv2pkl:eluac',
                'dota2picker-editor-job=dota2picker.editor:main',
                'dota2picker-pk2csv=dota2picker.pkl2csv:main',
                'dota2picker-picker=dota2picker.picker:main',
                'dota2picker-team-picker=dota2picker.team_picker:main',
            ],
        },
    )
