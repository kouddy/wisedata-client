import datawise as dw
import logging
import pandas as pd
import sys

from datawise.exceptions import AuthorizationError, TranslationError

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

  datawise = dw.DataWise()
  df = datawise.sql("SELECT * FROM countries", {
    "countries": countries
  })
  print(df)

  df = datawise.sql("SELECT COUNT(country) AS NumCountry FROM countries", {
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

  datawise = dw.DataWise()
  df = datawise.sql("SELECT * FROM countries LEFT JOIN country_populations ON countries.country = country_populations.country", {
    "countries": countries,
    "country_populations": country_populations
  }, code=True)
  print(df)

def test_error():
  countries = pd.DataFrame({
      "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
      "gdp": [19294482071552, 2891615567872, 2411255037952, 3435817336832, 1745433788416, 1181205135360, 1607402389504, 1490967855104, 4380756541440, 14631844184064],
      "happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12]
  })
  
  datawise = dw.DataWise(api_key="sk-wrong-key")

  try:
    datawise.sql("SELECT * FROM countries", {
      "countries": countries
    }, code=True)
  except AuthorizationError as e:
    print(e)

def test_exception():
  countries = pd.DataFrame({
      "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
      "gdp": [19294482071552, 2891615567872, 2411255037952, 3435817336832, 1745433788416, 1181205135360, 1607402389504, 1490967855104, 4380756541440, 14631844184064],
      "happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12]
  })
    
  datawise = dw.DataWise()
  try:
    datawise.sql("SELECT bad_column FROM bad_table", {
      "countries": countries
    })
  except TranslationError:
    pass
