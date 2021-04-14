from flask import json
from requests import post


print(post("http://localhost:5000/api/works",
           json={"name": "lab",
                 "about": "About"}
           ).json())
