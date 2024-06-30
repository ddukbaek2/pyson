#------------------------------------------------------------------------
# 참조 모듈 목록.
#------------------------------------------------------------------------
from setuptools import setup, find_packages


#------------------------------------------------------------------------
# Wheel 패키지 빌드.
#------------------------------------------------------------------------
setup(
	name = "pysonlib",
	version = "v0.0.2",
	author = "ddukbaek2",
	author_email = "ddukbaek2@gmail.com",
	description = "Python Script Object Notation (pysonlib) is a standard text-based format for expressing structured data using Python object syntax.",
	long_description = open(file = "README.md", mode = "r", encoding = "utf-8").read(),
	long_description_content_type = "text/markdown",
	url = "https://github.com/ddukbaek2/pysonlib",
	packages = find_packages(),
	include_package_dat = True,
	package_data = {
		"": [
			"resources/*"
		],
	},
    install_requires = [],
	classifiers = [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires = ">=3.9"
)