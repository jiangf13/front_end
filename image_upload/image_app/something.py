import requests

def tmp(a):
    files = {'file': open(a, 'rb')}
    r = requests.post('http://127.0.0.1:5000/infer', files=files)
    print(r.text)