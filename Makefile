install:
	poetry install

gendiff:
	poetry run gendiff tests/fixtures/file.json tests/fixtures/fille.json

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

quick-reinstall:
	poetry install
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff
test:
	poetry run pytest

git:
	git add .
	git commit -m 'fix'
	git push

.PHONY: gendiff install build publish git