TEST_CMD = python3 -m doctest
CHECKSTYLE_CMD = python3 -m flake8

all: compile test checkstyle clean

compile:
	@echo "Nothing to compile for Python"

test:
	$(TEST_CMD) *.py

checkstyle:
	$(CHECKSTYLE_CMD) *.py

clean:
	rm -f *.pyc
	rm -rf __pycache__
