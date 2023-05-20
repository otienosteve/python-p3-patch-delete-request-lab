import pytest
from fastapi.testclient import TestClient
from main import app
from models.employee import session, Employee

# Client instance
@pytest.fixture(scope='session')
def Client():
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
# path setup teardown 
@pytest.fixture()
def patch_data():
    emp = Employee(**dict(update_data))
    session.add(emp)
    session.commit()
    yield {"email": "dlet@jigsy.com",
"age": 40,
"gender": "Male",
"phone_number": 123456789,
"salary": 5678982,
"designation": "Janitor"}
    emp = session.query(Employee).filter_by(id=117).first()
    session.delete(emp)
    session.commit()
    


#   Test Patch
def test_patch(Client, patch_data):
    res = Client.patch('/employees/partial_update/{117}', headers={"content-type":"application/json", "accept" : "application/json"}, json=patch_data )
    emp = session.query(Employee).filter_by(id=117).first()
    assert emp.email == 'dlet@jigsy.com', 'Unexpected Email'
    assert emp.age == 'age', 'Unexpected age '
    assert emp.gender == 'Male', 'Unexpected Gender'
    assert emp.phone_number ==  123456789, 'Unexpected Phone Number'
    assert emp.designation == 'Janitor', 'Unexpected Designation'




