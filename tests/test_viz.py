from datawise import DataWise
from datawise.exceptions import BadRequestError

import logging
import pandas as pd
import sys

root = logging.getLogger()
root.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
root.addHandler(handler)

countries = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "gdp": [19294482071552, 2891615567872, 2411255037952, 3435817336832, 1745433788416, 1181205135360, 1607402389504, 1490967855104, 4380756541440, 14631844184064],
    "happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12]
})

def test_bar_chart():
  dw = DataWise()
  dw.viz("Show me bar chart with country's gdp sorted by gdp descending.", { "countries": countries }, code=True)

def test_scatter_plot():
  dw = DataWise()
  dw.viz("Show me relationship between gdp and happiness_index. Include title", { "countries": countries }, code=True)

def test_exception():
  dw = DataWise()
  try:
    dw.viz("Error", { "countries": countries }, code=True)
  except BadRequestError as e:
    if ("Number of words need to be larger than 5 and less than or equal to 20." in e.msg):
      pass

  dw = DataWise()
  try:
    dw.viz("This is long message. This is long message. This is long message. This is long message. This is long message. This is long message. This is long message.", { "countries": countries }, code=True)
  except BadRequestError as e:
    if ("Number of words need to be larger than 5 and less than or equal to 20." in e.msg):
      pass

