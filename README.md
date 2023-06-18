# data-kit-client

python -m venv venv
source venv/bin/activate
poetry install
poetry run pytest tests/tests.py -s


pip install --upgrade build
rm -rf dist && python -m build

pip install --upgrade twine
twine upload --repository pypi dist/*