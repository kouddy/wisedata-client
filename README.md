# DataWise

## 🔧 Quick install

```bash
pip install datawise
```

## 💻 Usage
This library needs to be configured with your account's API key.
Either set it as `DATAWISE_API_KEY` environment variable before using the library:
```bash
export DATAWISE_API_KEY=sk-...
```

Or set `api_key` to its value:
```python
import datawise as dw

datawise = dw.DataWise(api_key="you_api_key_here")
df = datawise.sql(...)
```

## SQL Query
You can use SQL query to transform Pandas dataframes.

You need to install `pandas` and `numpy` packages as pre-requisites.
```bash
pip install pandas numpy
```

To transform, simply call `sql` function.
```python
import datawise as dw
import pandas as pd

countries = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "gdp": [19294482071552, 2891615567872, 2411255037952, 3435817336832, 1745433788416, 1181205135360, 1607402389504, 1490967855104, 4380756541440, 14631844184064],
    "happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12]
})

datawise = dw.DataWise(api_key="you_api_key_here")
df = datawise.sql("SELECT COUNT(country) AS NumCountry FROM countries", {
  "countries": countries
}, code=True) # "code=True" will print out the code in addition to transforming dataframe.
print(df)
```

The above code will return the following dataframe:

```
   NumCountry
0          10
```

You can also do joins of multiple dataframes:
```python
import datawise as dw
import pandas as pd

countries = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "gdp": [19294482071552, 2891615567872, 2411255037952, 3435817336832, 1745433788416, 1181205135360, 1607402389504, 1490967855104, 4380756541440, 14631844184064],
    "happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12]
})

country_populations = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "population": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
})

datawise = dw.DataWise(api_key="you_api_key_here")
df = datawise.sql("SELECT * FROM countries LEFT JOIN country_populations ON countries.country = country_populations.country", {
  "countries": countries,
  "country_populations": country_populations
})
print(df)
```
The above code will return the following dataframe:

```
          country             gdp  happiness_index  population
0   United States  19294482071552             6.94           1
1  United Kingdom   2891615567872             7.16           2
2          France   2411255037952             6.66           3
3         Germany   3435817336832             7.07           4
4           Italy   1745433788416             6.38           5
5           Spain   1181205135360             6.40           6
6          Canada   1607402389504             7.23           7
7       Australia   1490967855104             7.22           8
8           Japan   4380756541440             5.87           9
9           China  14631844184064             5.12          10
```

## Error Handling
Errors could happen if we cannot translate the SQL query. Consider the following example:
```python
import datawise as dw
import pandas as pd

countries = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "gdp": [19294482071552, 2891615567872, 2411255037952, 3435817336832, 1745433788416, 1181205135360, 1607402389504, 1490967855104, 4380756541440, 14631844184064],
    "happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12]
})

datawise = dw.DataWise(api_key="you_api_key_here")
datawise.sql("SELECT bad_column FROM bad_table", {
  "countries": countries
})
```

The above code will give following error message:
```
ERROR    root:__init__.py:47 We couldn't translate your query. Here is python code we attempted to generate: 
return_df = bad_table['bad_column']
```

You should modify the SQL query so that it works based on the code we attempted to generate.

## Development

```bash
python -m venv venv
source venv/bin/activate
poetry install
poetry run pytest tests/tests.py -s

pip install --upgrade build
rm -rf dist && python -m build

pip install --upgrade twine
twine upload --repository pypi dist/*
```

## 📜 License

DataWise is licensed under the Apache 2.0 License. See the LICENSE file for more details.

## Acknowledgements

- This project is leverages [pandas](https://github.com/pandas-dev/pandas) library by independent contributors, but it's in no way affiliated with the pandas project.