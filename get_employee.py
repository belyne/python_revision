#dictionary list
employee_list = [{"id": 12345, "Name": "Anne", "Department": "commercial"}, {"id": 23456, "Name": "Jane", "Department": "Human_resouces"}]

#the function to help print the specific dictionary list according to id
def get_employee(id):
    for employee in employee_list:
        if employee["id"] == id:
            return employee

#calling the function with id parameter        
print(get_employee(23456))
print(get_employee(12345))
