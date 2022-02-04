make install:
	pip install --upgrade pip &&
		pip install -r requirements.txt

make lint: 
	echo linting 

make format:
	echo formating 

make test:
	echo testing

make all:
	install lint format test
