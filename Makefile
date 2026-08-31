.PHONY: run test install build

run:
	py main.py

test:
	py -m unittest discover -s erp -p "test_*.py"

install:
	pip install .
