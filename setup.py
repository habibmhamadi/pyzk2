# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    description = fh.read()

setup(
    name='pyzk2',
    version='0.2',
    url='https://github.com/habibmhamed/pyzk2',
    author='Habib Mhamadi',
    author_email='habibmhamadi@gmail.com',
    description='Forked version of fananimi/pyzk with latest changes.',
    license='LICENSE.txt',
    packages=find_packages(),
    keywords=[
        'zk',
        'pyzk',
        'pyzk2',
        'zksoftware',
        'attendance machine',
        'fingerprint',
        'biometrics',
        'security'
    ],
    zip_safe=False,
    long_description=description,
    long_description_content_type="text/markdown",
    python_requires='>=3.6',
)