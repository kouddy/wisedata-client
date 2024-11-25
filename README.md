# WiseData

### AI Assistant for Python Data Analytics
| Capabilities                                      | Limitations                                     |
|---------------------------------------------------|-------------------------------------------------|
| Use SQL to transform Pandas dataframes            | May occasionally generate incorrect results     |
| Use English to transform Pandas dataframes        | May generate incorrect results due to ambiguity |
| Use English to visualize Pandas dataframes        | May generate incorrect results due to ambiguity |

[Sign Up Here](https://wisedata.app/)

## 🔍 Demo
Try out WiseData in your browser:

[![Open in Colab](https://camo.githubusercontent.com/84f0493939e0c4de4e6dbe113251b4bfb5353e57134ffd9fcab6b8714514d4d1/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/drive/1onQI_V6NrAnEDY-o6N068xLyvsFojynf?usp=sharing)

## 🔧 Quick install
Install WiseData client first:
```bash
pip install wisedata
```

Configure with your account's API key.
Either set it as `WISEDATA_API_KEY` environment variable before using the library:
```bash
export WISEDATA_API_KEY=sk-...
```

Or set `api_key` to its value:
```python
from wisedata import WiseData

wd = WiseData(api_key="you_api_key_here")
```

## Use SQL to transform Pandas dataframes
You need to install `pandas` and `numpy` packages as pre-requisites for SQL query.
```bash
pip install pandas numpy
```

To transform, simply call `sql` function. You can use SQLite style SQL query to transform Pandas dataframes.
```python
from wisedata import WiseData
import pandas as pd

countries = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "gdp": [19294482071552, 2891615567872, 2411255037952, 3435817336832, 1745433788416, 1181205135360, 1607402389504, 1490967855104, 4380756541440, 14631844184064],
    "happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12]
})

wd = WiseData(api_key="you_api_key_here")
df = wd.sql("SELECT COUNT(country) FROM countries", {
  "countries": countries
})
print(df)
```

The above code will return following dataframe:

```
        count
0          10
```

You can also do joins of multiple dataframes:
```python
from wisedata import WiseData
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

wd = WiseData(api_key="you_api_key_here")
df = wd.sql("SELECT * FROM countries LEFT JOIN country_populations ON countries.country = country_populations.country", {
  "countries": countries,
  "country_populations": country_populations
})
print(df)
```
The above code will return following dataframe:

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

## Use English to transform Pandas dataframes
Using English to transform is nice for simple transformations. Sometimes transforming data using SQL can be complex whereas easy for English.

To transform, simply call `transform` function.
```python
from wisedata import WiseData
import pandas as pd

countries = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "gdp": [19294482071552, 2891615567872, 2411255037952, 3435817336832, 1745433788416, 1181205135360, 1607402389504, 1490967855104, 4380756541440, 14631844184064],
    "happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12]
})

wd = WiseData(api_key="you_api_key_here")
df = wd.transform("give me gdp data pivotted by country", {
  "countries": countries
})
print(df)
```

The above code will return the following dataframe:

```
gdp             1181205135360   1490967855104   1607402389504   1745433788416   2411255037952   2891615567872   3435817336832   4380756541440   14631844184064  19294482071552
country                                                                                                                                                                       
Australia                  NaN            7.22             NaN             NaN             NaN             NaN             NaN             NaN             NaN             NaN
Canada                     NaN             NaN            7.23             NaN             NaN             NaN             NaN             NaN             NaN             NaN
China                      NaN             NaN             NaN             NaN             NaN             NaN             NaN             NaN            5.12             NaN
France                     NaN             NaN             NaN             NaN            6.66             NaN             NaN             NaN             NaN             NaN
Germany                    NaN             NaN             NaN             NaN             NaN             NaN            7.07             NaN             NaN             NaN
Italy                      NaN             NaN             NaN            6.38             NaN             NaN             NaN             NaN             NaN             NaN
Japan                      NaN             NaN             NaN             NaN             NaN             NaN             NaN            5.87             NaN             NaN
Spain                      6.4             NaN             NaN             NaN             NaN             NaN             NaN             NaN             NaN             NaN
United Kingdom             NaN             NaN             NaN             NaN             NaN            7.16             NaN             NaN             NaN             NaN
United States              NaN             NaN             NaN             NaN             NaN             NaN             NaN             NaN             NaN            6.94
``` 

### Limitations of using English to transform Pandas dataframes
* May generate incorrect results due to ambiguity

## Use English to visualize Pandas dataframes
You can write English to describe how you want to visualize your dataframe.

You need to install `matplotlib` and `seaborn` packages as pre-requisites for SQL query.
```bash
pip install matplotlib seaborn
```

To visualize, simply call `viz` function.
```python
from wisedata import WiseData
import seaborn as sns

wd = WiseData(api_key="you_api_key_here")
tips = sns.load_dataset("tips")
wd.viz("Show me relationship between total bill and tip. Each day should have different colour. Title is: Total Bill vs Tip", { "tips": tips })
```

## Printing out translated code
You can ask WiseData to print translated code to console using `code=True` flag.
```python
import logging
import sys

root = logging.getLogger()
root.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
root.addHandler(handler)

...

df = wd.sql("SELECT COUNT(country) FROM countries", {
  "countries": countries
}, code=True)
```

## Error Handling
Errors could happen if we cannot translate the SQL query. Consider the following example:
```python
from wisedata import WiseData
import pandas as pd

countries = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "gdp": [19294482071552, 2891615567872, 2411255037952, 3435817336832, 1745433788416, 1181205135360, 1607402389504, 1490967855104, 4380756541440, 14631844184064],
    "happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12]
})

wd = WiseData(api_key="you_api_key_here")
wd.sql("SELECT bad_column FROM bad_table", {
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

WiseData is licensed under the Apache 2.0 License. See the LICENSE file for more details.

## 🤝 Acknowledgements

- This project is leverages [pandas](https://github.com/pandas-dev/pandas) library by independent contributors, but it's in no way affiliated with the pandas project.