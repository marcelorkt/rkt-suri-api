from time import sleep
from decouple import config
from datetime import datetime

def format_date(date:str) -> str:
  '''
  Format the date string based on the received value
  
  Args:
  date(str): The value received from the API
  
  Return: str
  '''
  try:
    year=date[:4]
    month=date[5:7]
    day=date[8:10]
    hour=date[11:13]
    minute=date[14:16]
    second=date[17:19]
    return f"{day}/{month}/{year} - {hour}:{minute}:{second}"
  except Exception as e:
    return date
    
def verify_lenght(var:str|dict|list) -> bool:
  '''
  Verify if the value received has a valid length
  
  Args:
  var(str|dict|list): The value received from the API
  
  Return: bool
  '''
  if len(var) > 0:
    return True
    
def total_length(var:dict|list) -> range:
  '''
  Return the total length of a list or dictionary
  
  Args:
  var(dict|list): The value received from the API
  
  Return: range
  '''
  return range(len(var))

def see_time() -> str:
  '''
  Return the current time
  
  Args: None
  
  Return: str
  '''
  return datetime.now().time().strftime('%H:%M:%S')

def wait() -> None:
  '''
  Execute a sleep of 1 minute
  
  Args: None
  
  Return: None
  '''
  print(f'{see_time()} - Aguarde 1 minuto')
  sleep(60)

def verify_none(val:str) -> str:
  '''
  Verify if the value is None
  
  Args:
  val (str): Value to be verified
  
  Return: str
  '''
  if val is None:
    return 'None'
  else:
    return val
  
def val_space(val:str) -> str:
  '''
  Set a space after the value
  
  Args:
  val (str): Value to be verified
  
  Return: str
  '''
  return val+', '