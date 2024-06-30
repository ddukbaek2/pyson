@echo off
rem wheel 빌드 후 PyPi에 배포 (토큰 입력 필요).

rem .venv\Scripts\activate

pip install -r requirements.txt

if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "pysonlib.egg-info" rmdir /s /q "pysonlib.egg-info"

python build.py sdist bdist_wheel >NUL 2>&1

rem set TWINE_USERNAME=__token__
rem set TWINE_PASSWORD=
twine upload dist/*
rem set TWINE_USERNAME=
rem set TWINE_PASSWORD=

if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "pysonlib.egg-info" rmdir /s /q "pysonlib.egg-info"