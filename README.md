# Employee Data
Employee data management application with employee and department information

## Server running details

####Database setup

Run below to commands to setup database. Here this application db is using sqlite3

    python manage.py makemigrations
    python manage.py migration
 
Load initial database data for both department and employee

    python manage.py loaddata utils/initial_data/department_data.sjon
    python manage.py loaddata utils/initial_data/employee_data.json

Finally start server

    python manage.py runserver <0.0.0.0:port|localhost:port|nil>

## Database details
Employee database

    emp_id -> Charfield(ex: EI101)
    emp_name -> Charfield(ex: emp1)
    emp_age -> Integerfield(ex: 34)
    emp_salary -> Integerfield(ex: 34000)
    emp_dept -> ForeignKey(Department table)
    
Department database

    dept_id -> CharField(ex: D114)
    dept_name -> CharField(ex: hr)
    

## API details

###Employee APIs:

Get all employee details
    
    URL     : /api/data/employee
    Method  : GET
    Resonse : [
                {
                    "id": 4
                    "emp_id": "EI102",
                    "emp_name": "emp4",
                    "emp_age": 34,
                    "emp_salary": 35000,
                    "emp_dept": {
                        "id": 4,
                        "dept_id": "D114",
                        "dept_name": "development"
                    }
                }
              ]

Get an employee details
    
    URL     : /api/data/employee/EI102
    Method  : GET
    Resonse : [
                {
                    "id": 4
                    "emp_id": "EI102",
                    "emp_name": "emp4",
                    "emp_age": 34,
                    "emp_salary": 35000,
                    "emp_dept": {
                        "id": 4,
                        "dept_id": "D114",
                        "dept_name": "development"
                    }
                }
              ]
             
Add a new employee
    
    URL     : /api/data/employee/add
    Method  : POST
    Request : {
                "emp_id": "EI104",
                "emp_name": "emp6",
                "emp_age": 34,
                "emp_dept": "development",
                "emp_salary": 35000
              }
    Resonse : [
                {
                    "id": 4
                    "emp_id": "EI102",
                    "emp_name": "emp4",
                    "emp_age": 34,
                    "emp_salary": 35000,
                    "emp_dept": {
                        "id": 4,
                        "dept_id": "D114",
                        "dept_name": "development"
                    }
                }
              ]
    
Update an employee details

    URL     : /api/data/employee/update
    Method  : PUT
    Request : {
                "emp_id": "EI104",
                "emp_name": "emp3",
                "emp_age": 37,
                "emp_dept": "hr",
                "emp_salary": 43000
              }
    Resonse : [
                {
                    "id": 6 
                    "emp_id": "EI104",
                    "emp_name": "emp3",
                    "emp_age": 37,
                    "emp_salary": 43000,
                    "emp_dept": {
                        "id": 3,
                        "dept_id": "D113",
                        "dept_name": "hr"
                    }
                }
              ]
 
Delete an employee details
    
    URL     : /api/data/employee/delete/EI103
    Method  : DELETE
    Response: "Done"
 
Search employee details
    
    Search by department
    
        URL     : /api/data/employee/search
        Method  : POST
        Request : {
                	"search_by": "department",
	                "search_key": "development"
                  }
        Response: [
                    {
                        "id": 10
                        "emp_id": "EI102",
                        "emp_name": "emp4",
                        "emp_age": 34,
                        "emp_salary": 35000,
                        "emp_dept": {
                            "id": 4,
                            "dept_id": "D114",
                            "dept_name": "development"
                        }
                    }
                  ]
        
    Search by salary
        
        URL     : /api/data/employee/search
        Method  : POST
        Request : {
                	"search_by": "salary",
	                "low_bound": "40000",
	                "high_bound": "55000"
                  }        
        Response: [
                    {
                        "id": 13
                        "emp_id": "EI101",
                        "emp_name": "emp1",
                        "emp_age": 30,
                        "emp_salary": 50000,
                        "emp_dept": {
                            "id": 1,
                            "dept_id": "D111",
                            "dept_name": "sales"
                        }
                    }
                  ]
 
### Department APIs:
 
Get all departments
    
    URL     : /api/data/department
    Method  : GET
    Repsonse:[
                {
                    "id": 1,
                    "dept_id": "D111",
                    "dept_name": "sales"
                },
                {
                    "id": 2,
                    "dept_id": "D112",
                    "dept_name": "finance"
                }
              ]
 

Get a department details


    URL     : /api/data/department/D111
    Method  : GET
    Repsonse:[
                {
                    "id": 1,
                    "dept_id": "D111",
                    "dept_name": "sales"
                }
              ]

Add a department details
    
    URL     : /api/data/department/add
    Method  : POST
    Request : {
                "dept_id": "D111",
                "dept_name": "sales"
              }
    Response: [
                {
                    "id": 1,
                    "dept_id": "D111",
                    "dept_name": "sales"
                }
              ]
           
Delete a department details

   
    URL     : /api/data/department/delete/D113
    Method  : DELETE
    Response: "Done"