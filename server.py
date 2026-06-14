import requests
import ssl
import urllib3
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 6767

client.connect(("", port))




