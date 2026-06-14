import requests
import ssl
import urllib3
import socket

text = requests.get("https://w3schools.com/python/demopage.htm")
print(text.text)