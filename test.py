import os
from decouple import config

# print(os.environ)
#print(os.environ.get('SECRET_KEY'))

output = config('SECRET_KEY')
print("output:", output)