## Development

```bash
python -m venv venv
source venv/bin/activate
poetry install
poetry run pytest tests/test_sql.py -s
poetry run pytest tests/test_nl.py -s

pip install --upgrade build
rm -rf dist && python -m build

pip install --upgrade twine
twine upload --repository pypi dist/*
```