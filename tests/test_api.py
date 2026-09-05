import uuid

import pytest
from utils.API_util import APIClient
#hi
@pytest.fixture(scope="module")
def API_util():
    return APIClient()

def test_get_api(API_util):
    response=API_util.get("public/v2/users")
    assert response.status_code==200
    assert len(response.json())>0
    data=response.json()
    print(data)

def test_post_api(API_util,load_test_data):
    data=load_test_data["newuser"]
    unique_name=f"{uuid.uuid4().hex[:4]}@ABC"
    data["name"]=unique_name
    unique_email=f"{uuid.uuid4().hex[:6]}@mail.com"
    data["email"]=unique_email
    response=API_util.post("public/v2/users",data)
    assert response.status_code==201
    dat=response.json()
    print(dat)

def test_put_api(API_util, load_test_data, load_put_data):
    # Step 1: Create user with POST
    data = load_test_data["newuser"]
    data["name"] = f"{uuid.uuid4().hex[:4]}@ABC"
    data["email"] = f"{uuid.uuid4().hex[:6]}@mail.com"

    response_post = API_util.post("public/v2/users", data)
    assert response_post.status_code == 201, f"POST failed: {response_post.text}"
    user_id = response_post.json()["id"]
    data_post=response_post.json()
    print(data_post)

    # Step 2: Update user with PUT
    putdata = load_put_data["update_user"]
    putdata["name"] = f"{uuid.uuid4().hex[:4]}@ABC"
    putdata["email"] = f"{uuid.uuid4().hex[:6]}@mail.com"

    response_put = API_util.put(f"public/v2/users/{user_id}", putdata)
    assert response_put.status_code == 200, f"PUT failed: {response_put.text}"

    dataput = response_put.json()
    print(dataput)

def test_delete_api(API_util,load_delete_data):
    response=API_util.get("public/v2/users")
    getdata=response.json()[0]
    print(getdata)
    delete_id=getdata["id"]
    print(delete_id)

    delete_data=load_delete_data["delete_user"]
    delete_data["name"]=f"{uuid.uuid4().hex[:4]}@ABC"
    delete_data["email"]=f"{uuid.uuid4().hex[:6]}@mail.com"
    delete_reponse=API_util.delete(f"public/v2/users/{delete_id}",delete_data)
    assert delete_reponse.status_code==204, f"DELETE Failed:{delete_reponse.text}"
  

