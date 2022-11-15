import urllib
import requests
r = requests.get('https://opend.data.go.th/get-ckan/datastore_search?resource_id=3cea9bc0-df36-4b36-b46a-7bbc206b36dd&limit=5&q=title:jones')
print(r)
print(dir(r))

""" I want to make a bar graph"""