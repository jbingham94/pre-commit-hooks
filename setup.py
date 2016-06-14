from setuptools import find_packages
from setuptools import setup

setup(
    name='pre_commit_hooks',
    description='Pre-commit hooks for mark43.',
    url='https://github.com/mark43/mark43/pre-commit-hooks',
    version='1.0',

    author='Jasper Bingham',
    author_email='jasper.bingham@mark43.com',

    platforms='linux',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages('.', exclude=('tests*', 'testing*')),
    install_requires=[
        # quickfix to prevent pep8 conflicts
        'flake8!=2.5.3',
        'argparse',
        'autopep8>=1.1',
        'pyyaml',
        'simplejson',
        'six',
    ],
    entry_points={
        'console_scripts': [
            'trailing-whitespace-fixer = pre_commit_hooks.trailing_whitespace_fixer:fix_trailing_whitespace',
        ],
    },
)