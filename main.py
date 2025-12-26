import os
from dotenv import dotenv_values

#config = os.environ

config = dotenv_values(".env")

for k,v in config.items():
  print(f"For {k} the value is: {v}.")
