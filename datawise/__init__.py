import logging
import json
import os
import requests

from dotenv import load_dotenv
from .exceptions import AuthorizationError, DataWiseInternalError
from requests.exceptions import RequestException
from retry import retry


class DataWise:
  def __init__(
    self, 
    api_base="https://datawise.vercel.app/api",
    api_key=None
  ):
    load_dotenv()
    self.api_base = api_base if api_base else os.getenv("DATAWISE_API_BASE")
    self.api_key = api_key if api_key else os.getenv("DATAWISE_API_KEY")
    
  @retry(exceptions=(RequestException, DataWiseInternalError), tries=3, delay=2)
  def sql(self, query, dataframes, error=None, code=False, num_retries=0):
    if not (type(dataframes) is dict): raise Exception("dataframes needs to be a dictionary with key being dataframe name and value being the dataframe.")
    if num_retries > 3: raise Exception("We couldn't translate your query. :(")

    data = {
      "dataframe": "\n".join([f"{idx+1}. Dataframe named {key} with columns {value.columns.tolist()}" for idx, (key, value) in enumerate(dataframes.items())]),
      "sql": query,
      "error": error
    }

    response = requests.post(
      self.api_base + "/sql2pandas", 
      data=json.dumps(data), 
      headers={
        "Authorization": "Bearer " + self.api_key,
        "content-type": "application/json"
      }
    )

    if (response.status_code == 400): raise AuthorizationError()
    if (response.status_code >= 500): raise DataWiseInternalError()

    python_code = response.json()
    
    import pandas as pd
    globals = { "pd": pd }
    locals = dataframes.copy()
    try:
      exec(python_code, globals, locals)
      if isinstance(locals["return_df"], pd.DataFrame):
        return_df=locals["return_df"].reset_index(drop=True)
        if code: logging.info(f"Given query: \n{query} \nOutput code: \n{python_code}\n")
      else:
        num_retries += 1
        data["error"] = "Is not a pandas dataframe. Please return dataframe."
        return_df = self.sql(query, dataframes, error=data["error"], code=code, num_retries=num_retries)
    except Exception as e:
      num_retries += 1
      data["error"] = f"Threw exception: `{e}`"
      return_df = self.sql(query, dataframes, error=data["error"], code=code, num_retries=num_retries)
    
    return return_df