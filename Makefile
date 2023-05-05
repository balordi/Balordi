REQUIREMENTS	:= requirements.txt

PIP_USER_FLAGS	:= --user
PIP_FLAGS		:= -e

SRC				:= src
PACKAGE_NAME	:= bandiere
ENTRY_POINT		:= __init__.py

FLASK_CMD		:= run

APP_PATH		:= $(addsuffix /$(addsuffix /$(ENTRY_POINT), $(PACKAGE_NAME)), $(SRC))

install-reqs-user:
	pip install -r $(REQUIREMENTS) $(PIP_FLAGS) $(PIP_USER_FLAGS)

install-reqs:
	pip install -r $(REQUIREMENTS) $(PIP_FLAGS)

install:
	pip install $(PIP_FLAGS) .

install-user:
	pip install $(PIP_FLAGS) . $(PIP_USER_FLAGS)

run:
	python -m flask --app $(APP_PATH) $(FLASK_CMD)