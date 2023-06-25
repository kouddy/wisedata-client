from datawise import DataWise
import logging
import pandas as pd
import sys

from datawise.exceptions import TranslationError

root = logging.getLogger()
root.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
root.addHandler(handler)

def test_simple():
  countries = pd.DataFrame({
      "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
      "gdp": [19294482071552, 2891615567872, 2411255037952, 3435817336832, 1745433788416, 1181205135360, 1607402389504, 1490967855104, 4380756541440, 14631844184064],
      "happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12]
  })

  dw = DataWise()
  df = dw.transform("Give me all countries.", {
    "countries": countries
  })
  print(df)

  df = dw.transform("Give me number of countries.", {
    "countries": countries
  }, code=True)
  print(df)

def test_multiple_tables():
  countries = pd.DataFrame({
      "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
      "gdp": [19294482071552, 2891615567872, 2411255037952, 3435817336832, 1745433788416, 1181205135360, 1607402389504, 1490967855104, 4380756541440, 14631844184064],
      "happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12]
  })

  country_populations = pd.DataFrame({
      "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
      "population": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  })

  dw = DataWise()
  df = dw.sql("Give me all data with countries and country_populations combined", {
    "countries": countries,
    "country_populations": country_populations
  }, code=True)
  print(df)

def test_exception():
  countries = pd.DataFrame({
      "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
      "gdp": [19294482071552, 2891615567872, 2411255037952, 3435817336832, 1745433788416, 1181205135360, 1607402389504, 1490967855104, 4380756541440, 14631844184064],
      "happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12]
  })
    
  dw = DataWise()
  try:
    dw.transform("Give me list of values for this_is_error", {
      "countries": countries
    })
  except TranslationError:
    pass
