class DataKitError(Exception):
  def __init__(self, msg):
    self.msg = msg
    super().__init__(f"Error: {self.msg}")

class DataKitInternalError(DataKitError):
  """
  Raised when an internal error occurs
  """

class AuthorizationError(DataKitError):
  def __init__(self):
    super().__init__(f"Invalid authorization token.")