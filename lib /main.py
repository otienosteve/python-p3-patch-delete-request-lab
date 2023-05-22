from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from employee import session, Employee

app = FastAPI()

class EmployeeSchema(BaseModel):
    id : Optional[int]
    first_name : Optional[str]
    last_name : Optional[str]
    email : Optional[str]
    age : Optional[int]
    gender : Optional[str]
    phone_number : Optional[int]
    salary : Optional[int] 
    designation : Optional[str]
    class Config:
        orm_mode = True


@app.patch('/employees/partial_update/{student_id}', status_code=200)
def partial_update(student_id: int, payload: EmployeeSchema ):
    emp = session.query(Employee).filter_by(id = student_id).first()

    for key, value in payload.dict(exclude_unset=True).items():
        setattr(emp, key,value)
    session.commit()

@app.delete('/employees/delete/{student_id}',status_code=200)
def delete(student_id: int) -> None:
    emp = session.query(Employee).filter_by(id = student_id).first()
    session.delete(emp)
    session.commit()