# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in svouchers/__init__.py
from svouchers import __version__ as version

setup(
	name='svouchers',
	version=version,
	description='Request and payment voucher app',
	author='SILAP Company Limited',
	author_email='info@silap.net',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
