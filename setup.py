from setuptools import setup

setup(
	# Needed to silence warnings (and to be a worthwhile package)
	name='flatten_data',
	url='https://github.com/dacog/flatten_data',
	author='Diego Carrasco',
	author_email='diego@diegocarrasco.com',
	# Needed to actually package something
	packages=['flatten_data'],
	# Needed for dependencies
	install_requires=['copy','collections.abc'],
	# *strongly* suggested for sharing
	version='',
	# The license can be anything you like
	license='MIT',
	description='a way to flatten dictionaries and lists',
	# We will also need a readme eventually (there will be a warning)
	# long_description=open('README.md').read(),
)