import pytest
from fastapi.testclient import TestClient
from main import app
from models import session, Employee

# Client instance
@pytest.fixture(scope='session')
def Cleint():
    return TestClient(app)

#  patch data
update_data={
"id": 117,
"first_name": "Damian",
"last_name": "Lighter",
"email": "Dlighter@jigsy.com",
"age": 18,
"gender": "Male",
"phone_number": 64654301273,
"salary": 521391236,
"designation": "Waiter"
}
@pytest.fixture
def patch_data():
    emp = Employee(**update_data)
    session.add(emp)
    session.commit()
    yield {"email": "dlet@jigsy.com",
"age": 40,
"gender": "Male",
"phone_number": 123456789,
"salary": 5678982,
"designation": "Waiter"}
    


#   Test Patch
def test_patch(Client):
    res = Client.patch('/partial_update', headers={"content-type":"application/json", "accept" : "application/json" } )



