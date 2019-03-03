from setuptools import setup

setup(
	# Needed to silence warnings (and to be a worthwhile package)
	name='foursquare_api_tools',
	url='https://github.com/dacog/foursquare_api_tools',
	author='Diego Carrasco',
	author_email='diego@diegocarrasco.com',
	# Needed to actually package something
	packages=['foursquare_api_tools'],
	# Needed for dependencies
	install_requires=['pandas','foursquare'],
	# *strongly* suggested for sharing
	version='0.2',
	# The license can be anything you like
	license='MIT',
	description='some functions to interact with foursquare using \'foursquare\' package',
	# We will also need a readme eventually (there will be a warning)
	# long_description=open('README.md').read(),
)