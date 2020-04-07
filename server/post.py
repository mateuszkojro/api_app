#!/bin/python
#simple POST request sending  JSON
import requests
res = requests.post('http://localhost:5000/echo', json={"not mine":"koniec"})
if res.ok:
    print (res.json())