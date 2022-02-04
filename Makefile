make install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

make lint: 
	pylint --disable=R,C,W1203,W0702 app.py

make format:
	echo formating 

make test:
	echo testing

make all:
	install lint format test
