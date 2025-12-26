import os
from dotenv import dotenv_values

#config = os.environ

config = dotenv_values(".env")

print(config['EMAIL'])
print(config)