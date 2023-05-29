# PATCH DELETE REQUEST LAB WITH FASTAPI

setup
Fork and clone this repo, then navigate into the cloned folder

spawn a virtual environment `pipenv shell`  

install relevant dependencies `pipenv install`  

Here's the directory structure for our application
```

├── alembic
├── lib
│   ├── models
│   │   ├── employee.py
│   ├── test
|   |   |──test_main.py
|   |   |
│   ├── main.py
├── Pipfile
├── Pipfile.lock
|── README.md
```

Similar to the Previous GET Lab you will be working with data concerning Employees The Employee Model has been created and is available in the models directory under the lib folder. Create and run your migrations.

Inside the lib folder you will find a file main.py where you are expected to write your solution.

The Schema for the Employee Model you will be working with is similar to the one from the GET request Lab.
```
id: Integer
last_name -> String 
firs_tname -> String 
email -> String 
age -> Integer
gender -> String
phone_number -> Integer 
salary -> Integer
designation -> String
```
Create a corresponding Pydantic class called EmployeeSchema for the model and use it to annotate your endpoints as per the required return type. 

Add validation to your employee fields as follows.   
`last_name and first_name should include at least 2 characters`   
`email should be valid`  
`Gender should be Male or Female`      
`Age should be greater than 18`   
`Salary should be between 30,000 - 200,000`  

Implement the following endpoints and the required functionality.

`PATCH /employees/partial_update/<id>` Partially Updates an employees details when supplied with the employee id. It should throw an exception when the supplied id doesn't match any employee and should yield the appropriate status code and the message "Employee does not exist"    
`DELETE /employees/delete/<id>` Deletes an employee when supplied with the id.  

To run your server run `uvicorn lib.main:app` or `uvicorn lib.main:app --reload` to enable reloading on file changes

To test your solution run pytest

Resources
POST Requests With FastAPI  
PUT REquest With FastAPi    
Error Handling in FastAPI   

