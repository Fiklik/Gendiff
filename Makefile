install:
	poetry install

gendiff:
	poetry run gendiff file1.json file2.json

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3.11 -m pip install --user dist/*.whl

quick-reinstall:
	poetry install
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl --break-system-packages

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

.PHONY: gendiff