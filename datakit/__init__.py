import json
import os
import requests

from dotenv import load_dotenv
from .exceptions import AuthorizationError, DataKitInternalError
from requests.exceptions import RequestException
from retry import retry


class DataKit:
  def __init__(
    self, 
    api_base="https://data-kit-z9aq.vercel.app/api",
    api_key=None
  ):
    load_dotenv()
    self.api_base = os.getenv("DATAKIT_API_BASE", api_base)
    self.api_key = os.getenv("DATAKIT_API_KEY", api_key)
    print(self.api_key)
    
  @retry(exceptions=(RequestException, DataKitInternalError), tries=3, delay=2)
  def sql(self, query, dataframes):
    if not (type(dataframes) is dict): raise Exception("dataframes needs to be a dictionary with key being dataframe name and value being the dataframe.")

    data = {
      "dataframe": "\n".join([f"{idx+1}. Dataframe named {key} with columns {value.columns.tolist()}" for idx, (key, value) in enumerate(dataframes.items())]),
      "sql": query
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
    if (response.status_code >= 500): raise DataKitInternalError()
    
    # TODO: execute the dataframes.
    return response