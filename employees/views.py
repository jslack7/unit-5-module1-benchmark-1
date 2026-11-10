from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest  # pyright: ignore[reportMissingModuleSource]

# Create your views here.
  # 1.) Get ID from query parameters
    # 2.) Enumerate through employees array
    # 3.) Select employee dict that has the proper ID
    # 4.) Return the entire dict as a JSON response
    # If the ID does not exist, return a 404 response

# Find an employee using their ID
def filter_by_id(request):

    # Get the ID entered in the URL
    employee_id = request.GET.get("id")

    # Go through each employee in the list
    for employee in employees:

        # Check if the employee's ID matches the requested ID
        # Convert the ID to a string because URL values are strings
        if str(employee["id"]) == employee_id:

            # Return the matching employee as JSON
            return JsonResponse(employee)
    # Return a 404 if no employee has that ID
    return HttpResponseNotFound("Employee not found")

# Find an employee using their first name
def filter_by_first_name(request):
    
    # Get the first name entered in the URL
    first_name = request.GET.get("first_name")

    # Go through each employee in the list
    for employee in employees:

        # Check if the employee's first name matches
        if employee["first_name"] == first_name:

            #Return the first matching employee as JSON
            return JsonResponse(employee)
    #Return a 404 if no matching employee is found
    return HttpResponseNotFound("Employee not found")

# Find employees who earn more than a given salary
def filter_by_greater_than_salary(request):
    # Same thing as above, but using a conditional to return
    # a list of employee dicts that have greater than a certain salary
    
    # Get the salary entered in the URL
    salary_value = request.GET.get("salary")

    # Make sure a salary was provided and is a valid number
    try:
        salary = float(salary_value)
    except (TypeError, ValueError):
        return HttpResponseBadRequest("Please enter a valid salary")

    # Create an empty list to store matching employees
    matches = []

    # Go through each employee in the list
    for employee in employees:

        # Check if the employee earns more than the given salary
        if employee["salary"] > salary:

            # Add the employee to our matches list
            matches.append(employee)

    # Return all matching employees as a JSON list
    # safe=False allows Django to return a list
    return JsonResponse(matches, safe=False)




# Fake employee data to use for this exercise
employees = [
    {'id': 1, 'first_name': 'Liam', 'last_name': 'Garcia', 'email': 'liam.garcia@examplecorp.com', 'department': 'Engineering', 'title': 'QA Analyst', 'salary': 68800.0, 'hire_date': '2019-06-30', 'location': 'Seattle, WA', 'is_active': True},
    {'id': 2, 'first_name': 'Chloe', 'last_name': 'Jackson', 'email': 'chloe.jackson@examplecorp.com', 'department': 'Engineering', 'title': 'Engineering Manager', 'salary': 136200.0, 'hire_date': '2023-06-19', 'location': 'Jackson, MS', 'is_active': True},
    {'id': 3, 'first_name': 'Ethan', 'last_name': 'White', 'email': 'ethan.white@examplecorp.com', 'department': 'Engineering', 'title': 'Engineering Manager', 'salary': 161900.0, 'hire_date': '2018-06-17', 'location': 'Seattle, WA', 'is_active': True},
    {'id': 4, 'first_name': 'Sofia', 'last_name': 'Thomas', 'email': 'sofia.thomas@examplecorp.com', 'department': 'Finance', 'title': 'Financial Analyst', 'salary': 81700.0, 'hire_date': '2014-02-23', 'location': 'Austin, TX', 'is_active': True},
    {'id': 5, 'first_name': 'Carlos', 'last_name': 'Okafor', 'email': 'carlos.okafor@examplecorp.com', 'department': 'Sales', 'title': 'Sales Representative', 'salary': 50900.0, 'hire_date': '2021-07-20', 'location': 'Denver, CO', 'is_active': False},
    {'id': 6, 'first_name': 'Zara', 'last_name': 'Wilson', 'email': 'zara.wilson@examplecorp.com', 'department': 'Finance', 'title': 'Financial Analyst', 'salary': 81200.0, 'hire_date': '2014-12-22', 'location': 'Atlanta, GA', 'is_active': True},
    {'id': 7, 'first_name': 'Ava', 'last_name': 'Chen', 'email': 'ava.chen@examplecorp.com', 'department': 'Engineering', 'title': 'Engineering Manager', 'salary': 166100.0, 'hire_date': '2020-07-29', 'location': 'Atlanta, GA', 'is_active': True},
    {'id': 8, 'first_name': 'Emma', 'last_name': 'Singh', 'email': 'emma.singh@examplecorp.com', 'department': 'Sales', 'title': 'Sales Manager', 'salary': 95700.0, 'hire_date': '2015-07-24', 'location': 'Austin, TX', 'is_active': True},
    {'id': 9, 'first_name': 'Robert', 'last_name': 'Martinez', 'email': 'robert.martinez@examplecorp.com', 'department': 'Engineering', 'title': 'DevOps Engineer', 'salary': 116500.0, 'hire_date': '2020-03-27', 'location': 'Remote', 'is_active': True},
    {'id': 10, 'first_name': 'Emma', 'last_name': 'Wilson', 'email': 'emma.wilson@examplecorp.com', 'department': 'Sales', 'title': 'Sales Manager', 'salary': 112900.0, 'hire_date': '2019-12-28', 'location': 'Seattle, WA', 'is_active': True},
    {'id': 11, 'first_name': 'Grace', 'last_name': 'Harris', 'email': 'grace.harris@examplecorp.com', 'department': 'Sales', 'title': 'Sales Manager', 'salary': 98800.0, 'hire_date': '2019-06-29', 'location': 'Denver, CO', 'is_active': True},
    {'id': 12, 'first_name': 'Ava', 'last_name': 'Harris', 'email': 'ava.harris@examplecorp.com', 'department': 'Customer Support', 'title': 'Support Specialist', 'salary': 50000.0, 'hire_date': '2021-04-10', 'location': 'Remote', 'is_active': False},
    {'id': 13, 'first_name': 'Ryan', 'last_name': 'Johnson', 'email': 'ryan.johnson@examplecorp.com', 'department': 'Marketing', 'title': 'Content Strategist', 'salary': 58700.0, 'hire_date': '2020-01-03', 'location': 'Atlanta, GA', 'is_active': True},
    {'id': 14, 'first_name': 'Carlos', 'last_name': 'Kim', 'email': 'carlos.kim@examplecorp.com', 'department': 'Customer Support', 'title': 'Support Team Lead', 'salary': 67300.0, 'hire_date': '2022-11-16', 'location': 'Seattle, WA', 'is_active': True},
    {'id': 15, 'first_name': 'Daniel', 'last_name': 'Patel', 'email': 'daniel.patel@examplecorp.com', 'department': 'Sales', 'title': 'Sales Manager', 'salary': 114100.0, 'hire_date': '2019-11-23', 'location': 'Denver, CO', 'is_active': True},
    {'id': 16, 'first_name': 'Kwame', 'last_name': 'Wilson', 'email': 'kwame.wilson@examplecorp.com', 'department': 'Sales', 'title': 'Sales Representative', 'salary': 56300.0, 'hire_date': '2025-06-06', 'location': 'Remote', 'is_active': False},
    {'id': 17, 'first_name': 'Aisha', 'last_name': 'Patel', 'email': 'aisha.patel@examplecorp.com', 'department': 'Customer Support', 'title': 'Support Specialist', 'salary': 47200.0, 'hire_date': '2023-06-21', 'location': 'Denver, CO', 'is_active': True},
    {'id': 18, 'first_name': 'Luis', 'last_name': 'Moore', 'email': 'luis.moore@examplecorp.com', 'department': 'Marketing', 'title': 'Marketing Manager', 'salary': 104900.0, 'hire_date': '2014-04-05', 'location': 'Jackson, MS', 'is_active': True},
    {'id': 19, 'first_name': 'Fatima', 'last_name': 'Young', 'email': 'fatima.young@examplecorp.com', 'department': 'Marketing', 'title': 'Marketing Manager', 'salary': 90900.0, 'hire_date': '2021-08-18', 'location': 'Denver, CO', 'is_active': True},
    {'id': 20, 'first_name': 'James', 'last_name': 'Walker', 'email': 'james.walker@examplecorp.com', 'department': 'Customer Support', 'title': 'Support Team Lead', 'salary': 65400.0, 'hire_date': '2025-03-24', 'location': 'Atlanta, GA', 'is_active': True},
    {'id': 21, 'first_name': 'Zara', 'last_name': 'Harris', 'email': 'zara.harris@examplecorp.com', 'department': 'Marketing', 'title': 'Marketing Manager', 'salary': 103100.0, 'hire_date': '2025-05-21', 'location': 'Austin, TX', 'is_active': True},
    {'id': 22, 'first_name': 'Priya', 'last_name': 'Jackson', 'email': 'priya.jackson@examplecorp.com', 'department': 'Finance', 'title': 'Accountant', 'salary': 66400.0, 'hire_date': '2021-04-09', 'location': 'Jackson, MS', 'is_active': True},
    {'id': 23, 'first_name': 'Tyler', 'last_name': 'Davis', 'email': 'tyler.davis@examplecorp.com', 'department': 'Sales', 'title': 'Sales Representative', 'salary': 61600.0, 'hire_date': '2019-05-28', 'location': 'Jackson, MS', 'is_active': False},
    {'id': 24, 'first_name': 'Hannah', 'last_name': 'Nguyen', 'email': 'hannah.nguyen@examplecorp.com', 'department': 'Finance', 'title': 'Accountant', 'salary': 69200.0, 'hire_date': '2016-11-17', 'location': 'Atlanta, GA', 'is_active': True},
    {'id': 25, 'first_name': 'Olivia', 'last_name': 'Kim', 'email': 'olivia.kim@examplecorp.com', 'department': 'Finance', 'title': 'Controller', 'salary': 134800.0, 'hire_date': '2018-07-06', 'location': 'Denver, CO', 'is_active': True},
    {'id': 26, 'first_name': 'Liam', 'last_name': 'Wilson', 'email': 'liam.wilson@examplecorp.com', 'department': 'Human Resources', 'title': 'HR Manager', 'salary': 88400.0, 'hire_date': '2024-02-16', 'location': 'Austin, TX', 'is_active': False},
    {'id': 27, 'first_name': 'James', 'last_name': 'Singh', 'email': 'james.singh@examplecorp.com', 'department': 'Finance', 'title': 'Accountant', 'salary': 58600.0, 'hire_date': '2018-12-10', 'location': 'Seattle, WA', 'is_active': True},
    {'id': 28, 'first_name': 'Sofia', 'last_name': 'Nguyen', 'email': 'sofia.nguyen@examplecorp.com', 'department': 'Engineering', 'title': 'QA Analyst', 'salary': 74100.0, 'hire_date': '2015-08-04', 'location': 'Chicago, IL', 'is_active': True},
    {'id': 29, 'first_name': 'David', 'last_name': 'Jackson', 'email': 'david.jackson@examplecorp.com', 'department': 'Sales', 'title': 'Sales Manager', 'salary': 100900.0, 'hire_date': '2024-08-08', 'location': 'Denver, CO', 'is_active': True},
    {'id': 30, 'first_name': 'David', 'last_name': 'Garcia', 'email': 'david.garcia@examplecorp.com', 'department': 'Engineering', 'title': 'DevOps Engineer', 'salary': 115700.0, 'hire_date': '2021-12-12', 'location': 'Denver, CO', 'is_active': True},
    {'id': 31, 'first_name': 'Maria', 'last_name': 'Clark', 'email': 'maria.clark@examplecorp.com', 'department': 'Customer Support', 'title': 'Support Specialist', 'salary': 45000.0, 'hire_date': '2015-05-12', 'location': 'Chicago, IL', 'is_active': True},
    {'id': 32, 'first_name': 'Aisha', 'last_name': 'Martinez', 'email': 'aisha.martinez@examplecorp.com', 'department': 'Sales', 'title': 'Sales Representative', 'salary': 51400.0, 'hire_date': '2024-01-24', 'location': 'Austin, TX', 'is_active': True},
    {'id': 33, 'first_name': 'Luis', 'last_name': 'Jackson', 'email': 'luis.jackson@examplecorp.com', 'department': 'Engineering', 'title': 'Software Engineer', 'salary': 108500.0, 'hire_date': '2014-05-01', 'location': 'Remote', 'is_active': True},
    {'id': 34, 'first_name': 'Priya', 'last_name': 'Anderson', 'email': 'priya.anderson@examplecorp.com', 'department': 'Human Resources', 'title': 'Recruiter', 'salary': 69200.0, 'hire_date': '2018-10-18', 'location': 'Jackson, MS', 'is_active': True},
    {'id': 35, 'first_name': 'James', 'last_name': 'Chen', 'email': 'james.chen@examplecorp.com', 'department': 'Marketing', 'title': 'Content Strategist', 'salary': 64400.0, 'hire_date': '2020-05-25', 'location': 'Seattle, WA', 'is_active': True},
    {'id': 36, 'first_name': 'Fatima', 'last_name': 'Clark', 'email': 'fatima.clark@examplecorp.com', 'department': 'Customer Support', 'title': 'Support Team Lead', 'salary': 56800.0, 'hire_date': '2017-06-22', 'location': 'Austin, TX', 'is_active': True},
    {'id': 37, 'first_name': 'Noah', 'last_name': 'Walker', 'email': 'noah.walker@examplecorp.com', 'department': 'Finance', 'title': 'Accountant', 'salary': 59400.0, 'hire_date': '2021-01-13', 'location': 'Atlanta, GA', 'is_active': True},
    {'id': 38, 'first_name': 'Ava', 'last_name': 'Moore', 'email': 'ava.moore@examplecorp.com', 'department': 'Sales', 'title': 'Sales Representative', 'salary': 50600.0, 'hire_date': '2025-05-23', 'location': 'Austin, TX', 'is_active': False},
    {'id': 39, 'first_name': 'Robert', 'last_name': 'Clark', 'email': 'robert.clark@examplecorp.com', 'department': 'Sales', 'title': 'Account Executive', 'salary': 88600.0, 'hire_date': '2016-09-09', 'location': 'Atlanta, GA', 'is_active': True},
    {'id': 40, 'first_name': 'Grace', 'last_name': 'Johnson', 'email': 'grace.johnson@examplecorp.com', 'department': 'Finance', 'title': 'Accountant', 'salary': 69200.0, 'hire_date': '2023-05-28', 'location': 'Atlanta, GA', 'is_active': True},
    {'id': 41, 'first_name': 'Ava', 'last_name': 'Okafor', 'email': 'ava.okafor@examplecorp.com', 'department': 'Sales', 'title': 'Sales Manager', 'salary': 100800.0, 'hire_date': '2021-01-17', 'location': 'Denver, CO', 'is_active': True},
    {'id': 42, 'first_name': 'Liam', 'last_name': 'Davis', 'email': 'liam.davis@examplecorp.com', 'department': 'Human Resources', 'title': 'Recruiter', 'salary': 55900.0, 'hire_date': '2015-08-18', 'location': 'Atlanta, GA', 'is_active': True},
    {'id': 43, 'first_name': 'Aisha', 'last_name': 'Nguyen', 'email': 'aisha.nguyen@examplecorp.com', 'department': 'Finance', 'title': 'Accountant', 'salary': 62800.0, 'hire_date': '2025-05-07', 'location': 'Chicago, IL', 'is_active': True},
    {'id': 44, 'first_name': 'Tyler', 'last_name': 'Martinez', 'email': 'tyler.martinez@examplecorp.com', 'department': 'Marketing', 'title': 'Content Strategist', 'salary': 64600.0, 'hire_date': '2017-07-16', 'location': 'Atlanta, GA', 'is_active': True},
    {'id': 45, 'first_name': 'Ethan', 'last_name': 'Smith', 'email': 'ethan.smith@examplecorp.com', 'department': 'Customer Support', 'title': 'Support Team Lead', 'salary': 68100.0, 'hire_date': '2016-04-28', 'location': 'Austin, TX', 'is_active': True},
    {'id': 46, 'first_name': 'Tyler', 'last_name': 'Garcia', 'email': 'tyler.garcia@examplecorp.com', 'department': 'Customer Support', 'title': 'Support Specialist', 'salary': 43700.0, 'hire_date': '2020-02-10', 'location': 'Austin, TX', 'is_active': True},
    {'id': 47, 'first_name': 'David', 'last_name': 'Clark', 'email': 'david.clark@examplecorp.com', 'department': 'Customer Support', 'title': 'Support Team Lead', 'salary': 61300.0, 'hire_date': '2025-05-03', 'location': 'Remote', 'is_active': False},
    {'id': 48, 'first_name': 'Liam', 'last_name': 'Anderson', 'email': 'liam.anderson@examplecorp.com', 'department': 'Marketing', 'title': 'Marketing Coordinator', 'salary': 51100.0, 'hire_date': '2014-01-30', 'location': 'Austin, TX', 'is_active': True},
    {'id': 49, 'first_name': 'Daniel', 'last_name': 'Brown', 'email': 'daniel.brown@examplecorp.com', 'department': 'Customer Support', 'title': 'Support Team Lead', 'salary': 62400.0, 'hire_date': '2023-08-05', 'location': 'Jackson, MS', 'is_active': False},
    {'id': 50, 'first_name': 'Tyler', 'last_name': 'Lewis', 'email': 'tyler.lewis@examplecorp.com', 'department': 'Sales', 'title': 'Sales Manager', 'salary': 116400.0, 'hire_date': '2014-10-23', 'location': 'Atlanta, GA', 'is_active': True},
    {'id': 51, 'first_name': 'Olivia', 'last_name': 'Patel', 'email': 'olivia.patel@examplecorp.com', 'department': 'Engineering', 'title': 'QA Analyst', 'salary': 81000.0, 'hire_date': '2022-03-07', 'location': 'Remote', 'is_active': True},
    {'id': 52, 'first_name': 'Maria', 'last_name': 'Wilson', 'email': 'maria.wilson@examplecorp.com', 'department': 'Sales', 'title': 'Sales Manager', 'salary': 112000.0, 'hire_date': '2019-08-07', 'location': 'Chicago, IL', 'is_active': True},
    {'id': 53, 'first_name': 'Tyler', 'last_name': 'Anderson', 'email': 'tyler.anderson@examplecorp.com', 'department': 'Finance', 'title': 'Controller', 'salary': 141400.0, 'hire_date': '2017-06-20', 'location': 'Austin, TX', 'is_active': True},
    {'id': 54, 'first_name': 'Isabella', 'last_name': 'Brown', 'email': 'isabella.brown@examplecorp.com', 'department': 'Human Resources', 'title': 'HR Generalist', 'salary': 62900.0, 'hire_date': '2018-01-09', 'location': 'Chicago, IL', 'is_active': True},
    {'id': 55, 'first_name': 'Olivia', 'last_name': 'Clark', 'email': 'olivia.clark@examplecorp.com', 'department': 'Customer Support', 'title': 'Support Specialist', 'salary': 42300.0, 'hire_date': '2019-12-26', 'location': 'Seattle, WA', 'is_active': True},
    {'id': 56, 'first_name': 'Zara', 'last_name': 'Johnson', 'email': 'zara.johnson@examplecorp.com', 'department': 'Human Resources', 'title': 'HR Generalist', 'salary': 64000.0, 'hire_date': '2018-06-23', 'location': 'Denver, CO', 'is_active': True},
    {'id': 57, 'first_name': 'Ryan', 'last_name': 'Martinez', 'email': 'ryan.martinez@examplecorp.com', 'department': 'Sales', 'title': 'Sales Representative', 'salary': 55000.0, 'hire_date': '2018-05-02', 'location': 'Chicago, IL', 'is_active': True},
    {'id': 58, 'first_name': 'Omar', 'last_name': 'Okafor', 'email': 'omar.okafor@examplecorp.com', 'department': 'Marketing', 'title': 'Marketing Manager', 'salary': 98000.0, 'hire_date': '2025-06-05', 'location': 'Remote', 'is_active': True},
    {'id': 59, 'first_name': 'James', 'last_name': 'Garcia', 'email': 'james.garcia@examplecorp.com', 'department': 'Marketing', 'title': 'Marketing Coordinator', 'salary': 47300.0, 'hire_date': '2019-12-15', 'location': 'Atlanta, GA', 'is_active': True},
    {'id': 60, 'first_name': 'Chloe', 'last_name': 'Lopez', 'email': 'chloe.lopez@examplecorp.com', 'department': 'Human Resources', 'title': 'HR Manager', 'salary': 88200.0, 'hire_date': '2025-06-21', 'location': 'Atlanta, GA', 'is_active': True},
    {'id': 61, 'first_name': 'Maria', 'last_name': 'Lewis', 'email': 'maria.lewis@examplecorp.com', 'department': 'Human Resources', 'title': 'HR Generalist', 'salary': 65600.0, 'hire_date': '2025-08-30', 'location': 'Atlanta, GA', 'is_active': True},
    {'id': 62, 'first_name': 'Chloe', 'last_name': 'Walker', 'email': 'chloe.walker@examplecorp.com', 'department': 'Customer Support', 'title': 'Support Specialist', 'salary': 45400.0, 'hire_date': '2022-03-03', 'location': 'Seattle, WA', 'is_active': True},
    {'id': 63, 'first_name': 'Grace', 'last_name': 'Lopez', 'email': 'grace.lopez@examplecorp.com', 'department': 'Customer Support', 'title': 'Support Specialist', 'salary': 46200.0, 'hire_date': '2020-09-26', 'location': 'Seattle, WA', 'is_active': True},
    {'id': 64, 'first_name': 'Kwame', 'last_name': 'Lewis', 'email': 'kwame.lewis@examplecorp.com', 'department': 'Marketing', 'title': 'Marketing Manager', 'salary': 92900.0, 'hire_date': '2016-11-08', 'location': 'Seattle, WA', 'is_active': True},
    {'id': 65, 'first_name': 'Yuki', 'last_name': 'Walker', 'email': 'yuki.walker@examplecorp.com', 'department': 'Sales', 'title': 'Sales Manager', 'salary': 105200.0, 'hire_date': '2020-10-01', 'location': 'Remote', 'is_active': False},
    {'id': 66, 'first_name': 'Mei', 'last_name': 'Kim', 'email': 'mei.kim@examplecorp.com', 'department': 'Human Resources', 'title': 'HR Manager', 'salary': 96500.0, 'hire_date': '2021-03-24', 'location': 'Denver, CO', 'is_active': True},
    {'id': 67, 'first_name': 'Ethan', 'last_name': 'Hernandez', 'email': 'ethan.hernandez@examplecorp.com', 'department': 'Customer Support', 'title': 'Support Specialist', 'salary': 43700.0, 'hire_date': '2015-11-26', 'location': 'Seattle, WA', 'is_active': True},
    {'id': 68, 'first_name': 'Carlos', 'last_name': 'Nguyen', 'email': 'carlos.nguyen@examplecorp.com', 'department': 'Sales', 'title': 'Sales Manager', 'salary': 100400.0, 'hire_date': '2020-12-17', 'location': 'Austin, TX', 'is_active': True},
    {'id': 69, 'first_name': 'Maria', 'last_name': 'Martinez', 'email': 'maria.martinez@examplecorp.com', 'department': 'Human Resources', 'title': 'HR Manager', 'salary': 96300.0, 'hire_date': '2015-08-20', 'location': 'Seattle, WA', 'is_active': True},
    {'id': 70, 'first_name': 'Marcus', 'last_name': 'Lewis', 'email': 'marcus.lewis@examplecorp.com', 'department': 'Human Resources', 'title': 'Recruiter', 'salary': 59600.0, 'hire_date': '2022-12-18', 'location': 'Seattle, WA', 'is_active': True},
    {'id': 71, 'first_name': 'Tyler', 'last_name': 'Young', 'email': 'tyler.young@examplecorp.com', 'department': 'Engineering', 'title': 'DevOps Engineer', 'salary': 108600.0, 'hire_date': '2018-11-28', 'location': 'Seattle, WA', 'is_active': True},
    {'id': 72, 'first_name': 'Maria', 'last_name': 'Jackson', 'email': 'maria.jackson@examplecorp.com', 'department': 'Sales', 'title': 'Sales Representative', 'salary': 51300.0, 'hire_date': '2024-03-28', 'location': 'Denver, CO', 'is_active': True},
    {'id': 73, 'first_name': 'Fatima', 'last_name': 'White', 'email': 'fatima.white@examplecorp.com', 'department': 'Marketing', 'title': 'Content Strategist', 'salary': 64400.0, 'hire_date': '2025-04-28', 'location': 'Atlanta, GA', 'is_active': True},
    {'id': 74, 'first_name': 'Priya', 'last_name': 'Walker', 'email': 'priya.walker@examplecorp.com', 'department': 'Human Resources', 'title': 'Recruiter', 'salary': 67500.0, 'hire_date': '2019-10-25', 'location': 'Remote', 'is_active': True},
    {'id': 75, 'first_name': 'Omar', 'last_name': 'Young', 'email': 'omar.young@examplecorp.com', 'department': 'Finance', 'title': 'Financial Analyst', 'salary': 72600.0, 'hire_date': '2019-05-14', 'location': 'Jackson, MS', 'is_active': True},
    {'id': 76, 'first_name': 'Sofia', 'last_name': 'Okafor', 'email': 'sofia.okafor@examplecorp.com', 'department': 'Marketing', 'title': 'Content Strategist', 'salary': 59800.0, 'hire_date': '2015-10-23', 'location': 'Austin, TX', 'is_active': True},
    {'id': 77, 'first_name': 'Michael', 'last_name': 'Lewis', 'email': 'michael.lewis@examplecorp.com', 'department': 'Sales', 'title': 'Sales Representative', 'salary': 55100.0, 'hire_date': '2023-04-22', 'location': 'Atlanta, GA', 'is_active': True},
    {'id': 78, 'first_name': 'Maria', 'last_name': 'Kim', 'email': 'maria.kim@examplecorp.com', 'department': 'Human Resources', 'title': 'Recruiter', 'salary': 69100.0, 'hire_date': '2014-06-10', 'location': 'Remote', 'is_active': True},
    {'id': 79, 'first_name': 'Hannah', 'last_name': 'Smith', 'email': 'hannah.smith@examplecorp.com', 'department': 'Marketing', 'title': 'Content Strategist', 'salary': 71300.0, 'hire_date': '2022-09-30', 'location': 'Remote', 'is_active': True},
    {'id': 80, 'first_name': 'Hannah', 'last_name': 'Martinez', 'email': 'hannah.martinez@examplecorp.com', 'department': 'Marketing', 'title': 'Content Strategist', 'salary': 58100.0, 'hire_date': '2024-11-22', 'location': 'Chicago, IL', 'is_active': True},
    {'id': 81, 'first_name': 'Isabella', 'last_name': 'Chen', 'email': 'isabella.chen@examplecorp.com', 'department': 'Customer Support', 'title': 'Support Specialist', 'salary': 50800.0, 'hire_date': '2024-06-25', 'location': 'Atlanta, GA', 'is_active': True},
    {'id': 82, 'first_name': 'Noah', 'last_name': 'Singh', 'email': 'noah.singh@examplecorp.com', 'department': 'Customer Support', 'title': 'Support Specialist', 'salary': 47700.0, 'hire_date': '2015-11-19', 'location': 'Austin, TX', 'is_active': True},
    {'id': 83, 'first_name': 'Priya', 'last_name': 'Johnson', 'email': 'priya.johnson@examplecorp.com', 'department': 'Marketing', 'title': 'Content Strategist', 'salary': 61000.0, 'hire_date': '2021-05-05', 'location': 'Chicago, IL', 'is_active': True},
    {'id': 84, 'first_name': 'Tyler', 'last_name': 'Chen', 'email': 'tyler.chen@examplecorp.com', 'department': 'Marketing', 'title': 'Content Strategist', 'salary': 71000.0, 'hire_date': '2019-08-29', 'location': 'Denver, CO', 'is_active': False},
    {'id': 85, 'first_name': 'Fatima', 'last_name': 'Johnson', 'email': 'fatima.johnson@examplecorp.com', 'department': 'Marketing', 'title': 'Marketing Coordinator', 'salary': 57000.0, 'hire_date': '2015-07-17', 'location': 'Seattle, WA', 'is_active': False},
    {'id': 86, 'first_name': 'James', 'last_name': 'Martinez', 'email': 'james.martinez@examplecorp.com', 'department': 'Sales', 'title': 'Sales Representative', 'salary': 52800.0, 'hire_date': '2017-06-02', 'location': 'Denver, CO', 'is_active': True},
    {'id': 87, 'first_name': 'Noah', 'last_name': 'Kim', 'email': 'noah.kim@examplecorp.com', 'department': 'Human Resources', 'title': 'HR Manager', 'salary': 103700.0, 'hire_date': '2019-10-01', 'location': 'Austin, TX', 'is_active': True},
    {'id': 88, 'first_name': 'Chloe', 'last_name': 'Lewis', 'email': 'chloe.lewis@examplecorp.com', 'department': 'Engineering', 'title': 'Senior Software Engineer', 'salary': 120500.0, 'hire_date': '2020-12-23', 'location': 'Jackson, MS', 'is_active': True},
    {'id': 89, 'first_name': 'Noah', 'last_name': 'Clark', 'email': 'noah.clark@examplecorp.com', 'department': 'Human Resources', 'title': 'Recruiter', 'salary': 57000.0, 'hire_date': '2018-06-13', 'location': 'Seattle, WA', 'is_active': True},
    {'id': 90, 'first_name': 'Sofia', 'last_name': 'Garcia', 'email': 'sofia.garcia@examplecorp.com', 'department': 'Customer Support', 'title': 'Support Team Lead', 'salary': 65900.0, 'hire_date': '2016-09-18', 'location': 'Atlanta, GA', 'is_active': True},
    {'id': 91, 'first_name': 'Emma', 'last_name': 'Jackson', 'email': 'emma.jackson@examplecorp.com', 'department': 'Human Resources', 'title': 'HR Manager', 'salary': 87100.0, 'hire_date': '2022-04-24', 'location': 'Seattle, WA', 'is_active': True},
    {'id': 92, 'first_name': 'Zara', 'last_name': 'Anderson', 'email': 'zara.anderson@examplecorp.com', 'department': 'Human Resources', 'title': 'HR Generalist', 'salary': 66100.0, 'hire_date': '2023-09-22', 'location': 'Seattle, WA', 'is_active': True},
    {'id': 93, 'first_name': 'Luis', 'last_name': 'Lewis', 'email': 'luis.lewis@examplecorp.com', 'department': 'Sales', 'title': 'Account Executive', 'salary': 84500.0, 'hire_date': '2017-12-13', 'location': 'Seattle, WA', 'is_active': True},
    {'id': 94, 'first_name': 'Isabella', 'last_name': 'Jackson', 'email': 'isabella.jackson@examplecorp.com', 'department': 'Human Resources', 'title': 'Recruiter', 'salary': 68600.0, 'hire_date': '2023-10-09', 'location': 'Atlanta, GA', 'is_active': True},
    {'id': 95, 'first_name': 'Zara', 'last_name': 'Martinez', 'email': 'zara.martinez@examplecorp.com', 'department': 'Engineering', 'title': 'QA Analyst', 'salary': 69200.0, 'hire_date': '2024-02-10', 'location': 'Denver, CO', 'is_active': True},
    {'id': 96, 'first_name': 'Yuki', 'last_name': 'Chen', 'email': 'yuki.chen@examplecorp.com', 'department': 'Marketing', 'title': 'Marketing Coordinator', 'salary': 57900.0, 'hire_date': '2025-02-01', 'location': 'Austin, TX', 'is_active': True},
    {'id': 97, 'first_name': 'Emma', 'last_name': 'Okafor', 'email': 'emma.okafor@examplecorp.com', 'department': 'Marketing', 'title': 'Content Strategist', 'salary': 66500.0, 'hire_date': '2020-03-13', 'location': 'Atlanta, GA', 'is_active': True},
    {'id': 98, 'first_name': 'Chloe', 'last_name': 'Anderson', 'email': 'chloe.anderson@examplecorp.com', 'department': 'Human Resources', 'title': 'HR Manager', 'salary': 101900.0, 'hire_date': '2019-05-23', 'location': 'Seattle, WA', 'is_active': True},
    {'id': 99, 'first_name': 'Luis', 'last_name': 'Smith', 'email': 'luis.smith@examplecorp.com', 'department': 'Engineering', 'title': 'QA Analyst', 'salary': 72100.0, 'hire_date': '2018-12-21', 'location': 'Austin, TX', 'is_active': True},
    {'id': 100, 'first_name': 'Noah', 'last_name': 'Wilson', 'email': 'noah.wilson@examplecorp.com', 'department': 'Human Resources', 'title': 'HR Manager', 'salary': 95600.0, 'hire_date': '2021-09-17', 'location': 'Seattle, WA', 'is_active': True},
]