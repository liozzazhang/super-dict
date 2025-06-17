.PHONY: build upload upload-local check-local-pypi check-twine check_local_pypi check_twine test release release-local
SHELL=/bin/bash
local_pypi := ${LOCAL_PYPI}
py := python
tests := tests.py

# Check that given variables are set and all have non-empty values, die with an error otherwise.
#
# Params:
#   1. Variable name(s) to test.
#   2. (optional) Error message to print.
check_defined = \
    $(strip $(foreach 1,$1, \
        $(call __check_defined,$1,$(strip $(value 2)))))
__check_defined = \
    $(if $(value $1),, \
      $(error Undefined $1$(if $2, ($2))))

help_msg = 'make <target> local_pypi=<your_local_pypi> \
			or LOCAL_PYPI=<your_local_pypi> make <target> \
			or export LOCAL_PYPI=<your_local_pypi>'

build:
	@python setup.py sdist bdist_wheel

upload-local: check-local-pypi check-twine
	@twine upload dist/*tar.gz -r $(local_pypi)

upload: check-twine
	@twine upload dist/*tar.gz

check-local-pypi:
	@echo "========= Check Local Pypi ========="
	@$(call check_defined, local_pypi, the local_pypi is required! example: ${help_msg})
	@echo "local_pypi set to: ${local_pypi}"
	@echo "========= Pass ========="

check-twine:
	@echo "========= Check twine version ========="
	@twine --version || pip install twine
	@echo "========= Pass ========="

test:
	@$(py) $(tests)

release: build upload

release-local: build upload-local
