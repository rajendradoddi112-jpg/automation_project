import requests
import os
import json
import uuid


class APIClient:
    base_url="https://gorest.co.in"
    base_post_url="https://gorest.co.in"
    put_url="https://gorest.co.in"

    def __init__(self):
        self.json_header={
            "contest_type":"application/json",
            "Authorization":"Bearer 83b769428f6a51a13cbdb4efb789b61956e0b465f77cf2da5b2564d360a97c9c"
            }
    def get(self,endpoint):
        url=f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        response=requests.get(url,headers=self.json_header)
        return response
    
    def post(self,endpoint,data):
        url=f"{self.base_post_url.rstrip('/')}/{endpoint.lstrip('/')}"
        response=requests.post(url,headers=self.json_header,json=data)
        return response
    
    def put(self,endpoint,data):
        url=f"{self.put_url.rstrip('/')}/{endpoint.lstrip('/')}"
        response=requests.put(url,headers=self.json_header,json=data)
        return response

    def delete(self,endpoint,data):
        url=f"{self.put_url.rstrip('/')}/{endpoint.lstrip('/')}"
        response=requests.delete(url,headers=self.json_header,json=data)
        return response  
