REQUIREMENTS	:= requirements.txt

PIP_USER_FLAGS	:= --user
PIP_FLAGS		:=

install-reqs-user:
	pip install -r $(REQUIREMENTS) $(PIP_USER_FLAGS)

install-reqs:
	pip install -r $(REQUIREMENTS) $(PIP_FLAGS)