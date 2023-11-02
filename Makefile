
VERSION := 0.0.1

# Make sure you put the keys in 1password into your ~/.pypirc file
build: 
	python3 -m build

push-test:
	python3 -m twine upload --repository testpypi dist/*

push-prod: 
	python3 -m twine upload dist/*



