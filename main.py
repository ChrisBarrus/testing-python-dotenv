import os
from dotenv import dotenv_values

#config = os.environ

config = dotenv_values(".env")

#listing all key values
for k,v in config:
  print(f"For {k} the value is: {v}")
