import setuptools

setuptools.setup(
	name='syntax-scraper',
	version='1.0.0',
	author='Mustafa Said Ağca',
	long_description_content_type='text/markdown',
	url='https://github.com/msagca/syntax_scraper',
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
	],
	packages=['ieee'],
	include_package_data=True,
	install_requires=['antlr4-python3-runtime', 'pdfplumber'],
	entry_points={'console_scripts': ['scrape-ieee=ieee.__main__:main']},
)
