@echo off

rem unittest 패키지를 활용한 유닛테스트.

rem .venv\Scripts\activate

pip install -r requirements.txt

python -m unittest discover -s tests