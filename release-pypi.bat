@echo off

venv\Scripts\activate

if exist "output" rmdir /s /q "output"
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "pysonlib.egg-info" rmdir /s /q "pysonlib.egg-info"

python setup.py sdist bdist_wheel >NUL 2>&1

rem set TWINE_USERNAME=__token__
rem set TWINE_PASSWORD=
twine upload dist/*
rem set TWINE_USERNAME=
rem set TWINE_PASSWORD=

if exist "output" rmdir /s /q "output"
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "pysonlib.egg-info" rmdir /s /q "pysonlib.egg-info"