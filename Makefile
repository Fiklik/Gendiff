install:
	poetry install

gendiff:
	poetry run gendiff tests/fixtures/file1.yml tests/fixtures/file2.yml

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