import pytest
import requests
import json
#below are header to submit payload for post requests
header={
    "accept":"text/plain",
    "Content-Type":"application/json"
}

head={
    "Content-Type":"application/json",
    "Authorization":"Bearer 83b769428f6a51a13cbdb4efb789b61956e0b465f77cf2da5b2564d360a97c9c"
}

param={
    "page":1,
    "per_page":3
}
#url of the API
BASE_URL="https://automationexercise.com/api/productsList"

#fixtures --to collect the data from API response and share the data to methods
@pytest.fixture(scope="module")
def products_data():
    response=requests.get(BASE_URL)
    assert response.status_code==200
    data=response.json()
    assert "products" in data
    return data["products"]

#test status code and data
def test_status_code(products_data):
    assert len(products_data)>0
    print(products_data[:2])

#validate the data
def test_validation(products_data):
    product=products_data[0]
    for k,v in product.items():
        print(k,":",v)

#test status code 
def test_status_code1():
    response=requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities")
    assert response.status_code==200

#test get request
def test_get_request():
    response=requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/1")
    data=response.json()
    for k,v in data.items():
        print(k,":",v)

#test post request
def test_post_request():
    with open("data/request_payload.json") as d:
        payload=json.load(d)
    response=requests.post("https://fakerestapi.azurewebsites.net/api/v1/Authors",headers=header,json=payload)
    assert response.status_code==200
    data=response.json()
    x=data["id"]
    if x==33:
        print("record created")
    else:
        print("record not created")

#test put request
def test_put_request():
    with open("data/put_payload.json") as p:
        payload=json.load(p)
    response=requests.put("https://fakerestapi.azurewebsites.net/api/v1/Activities/1",headers=header,json=payload)
    assert response.status_code==200
    data=response.json()
    for k,v in data.items():
        print(k,":",v)

# test authorizations related post request
def test_authrelated_post():
    with open("data/Auth_post_payload.json") as ap:
        payload=json.load(ap)
        authresponsepost=requests.post("https://gorest.co.in/public/v2/users",headers=head,json=payload)
        assert authresponsepost.status_code==201
        data=authresponsepost.json()
        # for k,v in data.items():
        #     print(k,":",v)

        getauthresponsepost=requests.get("https://gorest.co.in/public/v2/users"+"/"+str(authresponsepost.json()["id"]),headers=head)
        data=getauthresponsepost.json()
        # for k,v in data.items():
        #     print(k,":",v)

        assert authresponsepost.json()==getauthresponsepost.json()

#Filter the response using parameters

def test_get_request_with_params():
    responsewithparams=requests.get("https://gorest.co.in/public/v2/users",params=param)
    assert responsewithparams.status_code==200
    print(responsewithparams.json())
    
