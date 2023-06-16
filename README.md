# data-kit-client

python -m venv venv
source venv/bin/activate
poetry install
poetry run pytest tests -s


pip install --upgrade build
python -m build

pytest tests/

pip install --upgrade twine
twine upload --repository pypitest dist/*