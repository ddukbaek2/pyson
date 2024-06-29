#------------------------------------------------------------------------
# 참조 모듈 목록.
#------------------------------------------------------------------------
from setuptools import setup, find_packages


#------------------------------------------------------------------------
# 설치.
#------------------------------------------------------------------------
setup(
	name = "pyson",
	version = "0.0.1",
	author = "ddukbaek2",
	author_email = "ddukbaek2@gmail.com",
	description = "Python Script Object Notation (pyson) is a standard text-based format for expressing structured data using Python object syntax.",
	long_description = open("README.md").read(),
	long_description_content_type = "text/markdown",
	url = "https://github.com/ddukbaek2/pyson",
	packages = find_packages(),
	classifiers = [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires = ">=3.9",
)