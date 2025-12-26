import os
from dotenv import dotenv_values

#config = os.environ

config = dotenv_values(".env")

#print(config.keys())
#print(config.values())
#print(config.items())

#listing all key values
for k,v in config.items():
  print(f"For {k} the value is: {v}")
