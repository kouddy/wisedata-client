# DataWise

### DataWise is your co-pilot for performing data analysis and visualization in Python.

## Capabilities
* Use SQL to transform Pandas dataframes
* Coming soon: Use English to visualize Pandas dataframes

## Limitations
* May occasionally generate incorrect results

## 🔍 Demo
Try out PandasAI in your browser:

[![Open in Colab](https://camo.githubusercontent.com/84f0493939e0c4de4e6dbe113251b4bfb5353e57134ffd9fcab6b8714514d4d1/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/drive/1onQI_V6NrAnEDY-o6N068xLyvsFojynf?usp=sharing)

## 🔧 Quick install
Install DataWise client first:
```bash
pip install datawise
```

Configure with your account's API key.
Either set it as `DATAWISE_API_KEY` environment variable before using the library:
```bash
export DATAWISE_API_KEY=sk-...
```

Or set `api_key` to its value:
```python
from datawise import DataWise

dw = DataWise(api_key="you_api_key_here")
```

## Use SQL to transform Pandas dataframes
You can use SQLite style SQL query to transform Pandas dataframes. Example:
```sql
SELECT * FROM countries LEFT JOIN country_populations ON countries.country = country_populations.country
```

You need to install `pandas` and `numpy` packages as pre-requisites for SQL query.
```bash
pip install pandas numpy
```

To transform, simply call `sql` function.
```python
from datawise import DataWise
import pandas as pd

countries = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "gdp": [19294482071552, 2891615567872, 2411255037952, 3435817336832, 1745433788416, 1181205135360, 1607402389504, 1490967855104, 4380756541440, 14631844184064],
    "happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12]
})

dw = DataWise(api_key="you_api_key_here")
df = dw.sql("SELECT COUNT(country) FROM countries", {
  "countries": countries
})
print(df)
```

The above code will return the following dataframe:

```
   count
0          10
```

You can also do joins of multiple dataframes:
```python
from datawise import DataWise
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

dw = DataWise(api_key="you_api_key_here")
df = dw.sql("SELECT * FROM countries LEFT JOIN country_populations ON countries.country = country_populations.country", {
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

### Limitations of using SQL to transform Pandas dataframes
* May occasionally generate incorrect results
* Ordering of rows is not strict unless ORDER BY clause is specified
* No support for Window functions: https://www.sqlite.org/windowfunctions.html
* If SQL query contains WHERE clause with `LIKE` operator, incorrect result might be generated

## Use English to visualize Pandas dataframes
Coming soon!

## Printing out translated code
You can ask DataWise to print translated code to console using `code=True` flag.
```python
import logging
import sys

root = logging.getLogger()
root.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
root.addHandler(handler)

...

df = dw.sql("SELECT COUNT(country) FROM countries", {
  "countries": countries
}, code=True)
```

## Error Handling
Errors could happen if we cannot translate the SQL query. Consider the following example:
```python
from datawise import DataWise
import pandas as pd

countries = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "gdp": [19294482071552, 2891615567872, 2411255037952, 3435817336832, 1745433788416, 1181205135360, 1607402389504, 1490967855104, 4380756541440, 14631844184064],
    "happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12]
})

dw = DataWise(api_key="you_api_key_here")
dw.sql("SELECT bad_column FROM bad_table", {
  "countries": countries
})
```

The above code will give following error message:
```
ERROR    root:__init__.py:47 We couldn't translate your query. Here is python code we attempted to generate: 
return_df = bad_table['bad_column']
```

You can modify the SQL query so that it works based on the code we attempted to generate.
You can also take the translated code and use it after modifying it to work.

## 📜 License

DataWise is licensed under the Apache 2.0 License. See the LICENSE file for more details.

## 🤝 Acknowledgements

- This project is leverages [pandas](https://github.com/pandas-dev/pandas) library by independent contributors, but it's in no way affiliated with the pandas project.