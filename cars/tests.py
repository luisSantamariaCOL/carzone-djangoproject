from django.test import TestCase
from datetime import datetime

# Create your tests here.
year_choice = []
for r in range(2000, (datetime.now().year+1)):
    year_choice.append((r,r))

print(year_choice)