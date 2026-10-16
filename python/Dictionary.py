# student = {"name": "Rahul", "age": 20, "course": "Python"}

# print(student.get("name"))          # Rahul
# print(student.get("marks"))         # None (no error!)
# print(student.get("marks", 0))      # 0 (default value)



# Python Dictionary — 5 Real-World Practice Tasks

# 1. Student Record
# Create a dictionary containing a student's name, age, course, college, and marks. Display each key and value separately.


# Student_Record={"name":"Sakham","age":23,"course":"Computer_Science","college":"Softflew","Marks":56}
# for key, value in Student_Record.items():
#     print(key, "→", value)





# 2. Product Inventory
# Create a dictionary containing product names and their quantities. Perform the following:

# Add a new product

# Update the quantity of an existing product

# Remove a product

# Display all products and quantities


# Product_name={"Laptop": 10, "Mobile": 20, "Tablet": 15}
# Product_name["earphone"]=50
# print(Product_name)

# Product_name["Laptop"]=20
# print(Product_name)

# removed_product=Product_name.pop("Mobile")
# print(removed_product)


# for key, value in Product_name.items():
#     print(key, "→", value)



# 3. Employee Salary
# Create a dictionary containing employee names and salaries. Write a program to:

# Add a new employee

# Update an employee's salary

# Delete an employee

# Display all employees and salaries

# employee={"emp1":"Naman",
#           "Salary":50000,
#           "emp2":"Aakash",
#           "Salary":45000,
#           "emp3":"Sandeep",
#           "Salary":60000,
#           "emp4":"Sudheer",
#           "Salary":100000}


# employee["emp5"]="Rohit"
# employee["Salary"]=70000

# employee["emp2"]=60000

# del employee["emp2"]

# for key, value in employee.items():
#     print(key, "→", value)




# 4. Shopping Cart
# Create a dictionary containing product names and prices. Calculate the total price of all products and display the product with its price.


# Products={"Laptop": 50000, "Mobile": 20000, "Tablet": 15000}
# total=0
# for key, value in Products.items():
#     print(key, "→", value)
#     total+=value
# print("Total price:", total)





# 5. Contact Book
# Create a dictionary containing names and phone numbers. Allow the user to:

# Add a contact

# Search for a contact

# Update a phone number

# Delete a contact

# Display all contacts


# details={"Naman": 1234567890, "Aakash": 9876543210, "Sandeep": 4567891230}
# details["Sumit"]=7894561230
# print(details)


# details["Naman"]=1111111111


# del details["Aakash"]


# print("Naman" in details)


# for key, value in details.items():
#     print(key, "→", value)



# Word frequcncy counter

# sentence="the cat set on the mat the cat set on the mat the cat "
# word=sentence.split()
# count={}
# for i in word:
#     if i in count:
#         count[i]+=1
#     else:
#         count[i]=1
# print(count)



# contact={}
# while True:
#     print("1. Add new Contact")
#     print("2. Search contact")
#     print("3. Update Contact")
#     print("4. Delete Contact")
#     print("5. Exit")
#     ch=int(input("Enter your choice : "))
#     if ch in [1,2,3,4]:
#         name=input("Enter name : ")
#         names=contact.keys()
#         if ch==1:
#             phone=input("Enter Phone Number : ")
#             contact[name]=phone
#             print(f"{name} Added in your contact book")
#         elif ch==2:
#             if name in names:
#                 print(f"{name} : {contact[name]}")
#             else:
#                 print("Contact Not found")
#         elif ch==3:
#             if name in names:
#                 phone=input("Enter updated Phone Number : ")
#                 contact[name]=phone
#                 print(f"{name}'s Phone number updated")
#             else:
#                 print("Contact Not found")
#         elif ch==4:
#             if name in names:
#                 del contact[name]
#                 print(f"{name} deleted from your contact book")
#             else:
#                 print("Contact Not found")
#     elif ch==5:
#         print("Exitting.....")
#         break



### 10 Real-World Python Dictionary Programming Questions

# Level: Beginner to Intermediate

# Topics: Dictionary creation, accessing, updating, adding, deleting, looping, and nested dictionaries.

# ### 1\. Student Record Management

# Create a dictionary to store student details, including name, roll number, course, and marks.

# * Display all student details.

# * Update the student's marks.

# * Add a new field for attendance percentage.

# * Display the updated record.


detail={
    34:
    {
        "name":"Ravi",
        "marks":78,
        "course":"MCA"

    }

}

while True:
    print("1. Add new student data")
    print("2. Display All records")
    print("3. Update the student marks")
    print("4. Add a new fields attendance percentage ")
    print("5. Display the updated record")
    print("6. Exit")
    ch=int(input("Enter choice :"))
    if ch in [1,2,3,4]:
        if ch==1:
            roll=int(input("Enter Roll NUmber : "))
            marks=float(input("Enter marks : "))
            name=input("Enter Student name : ")
            course=input("Enter course :")
            detail[roll]={"name":name,"marks":marks,"course":course}
            print(f"{roll} Added succefully ")
        elif ch==2:
            for i,j in detail.items():
                print(f"Roll Number : {i}\n Name : {j["name"]}\n Marks : {j["marks"]}\n Course : {j["course"]}")
        elif ch==3:
            roll=int(input("Enter Roll number : "))
            marks=float(input("Enter updated marks : "))
            detail[roll]["marks"]=marks
            print("Student Marks updated!!! ")
        elif ch==4:
            roll=input("Enter Roll number : ")
            attendance=float(input("Enter Attendance percentage : "))
            detail[roll]["attendance"]=attendance
            print("Attendance percentage added!!! ")
        elif ch==5:
            for i,j in detail.items():
                print(f"Roll Number : {i}\n Name : {j["name"]}\n Marks : {j["marks"]}\n Course : {j["course"]}\n Attendance : {j.get("attendance","Not Available")}")
                
        

            
    elif ch==6:
        print("Exiting.......")
        break







# ### 2\. Mobile Contact Book

# Create a contact book using a dictionary where names are keys and phone numbers are values.

# * Add a new contact.

# * Search for a contact by name.

# * Update an existing phone number.

# * Delete a contact.

# * Display all contacts.






# ### 3\. Shopping Cart System

# Create a shopping cart dictionary where product names are keys and their prices are values.

# * Add products to the cart.

# * Update product prices.

# * Remove a product.

# * Calculate the total shopping cost.

# * Display the final cart.

# ### 4\. Employee Salary Management

# Create a dictionary containing employee names and their monthly salaries.

# * Add 5 employees.

# * Increase the salary of employees earning less than ₹25,000 by 10%.

# * Find the highest salary.

# * Display all employees and their updated salaries.

# ### 5\. Inventory Management System

# Create a dictionary to store product names and their available stock quantities.

# * Add new products.

# * Update stock after a sale.

# * Add stock after a new delivery.

# * Display products with stock below 10.

# * Display the complete inventory.

# ### 6\. Restaurant Menu and Billing

# Create a dictionary containing food items and their prices.

# * Display the restaurant menu.

# * Ask the customer to select food items.

# * Take the quantity of each item.

# * Calculate the total bill.

# * Display the final bill with item names, quantities, and prices.

# ### 7\. Online Voting System

# Create a dictionary to store candidate names and their vote counts.

# * Add 3 candidates with an initial vote count of zero.

# * Ask users to vote for a candidate.

# * Increase the selected candidate's vote count.

# * Display the total votes received by each candidate.

# * Display the candidate with the highest number of votes. Handle ties.

# ### 8\. Expense Tracker

# Create a dictionary to store daily expenses, where the date is the key and the expense amount is the value.

# * Add expenses for 7 days.

# * Update an expense for a particular day.

# * Calculate total expenses.

# * Find the day with the highest expense.

# * Display days when expenses exceeded ₹500.

# ### 9\. Library Book Management

# Create a dictionary where book IDs are keys and book details are stored as nested dictionaries.

# Each book should contain:

# * Book name

# * Author

# * Availability status

# Perform the following operations:

# * Add a new book.

# * Search for a book by ID.

# * Issue a book by changing its availability.

# * Return a book.

# * Display all available books.

# ### 10\. Online Course Enrollment System

# Create a nested dictionary to manage students and their enrolled courses.

# Example structure:

# Perform the following operations:

# * Add a new student.

# * Enroll a student in a new course.

# * Remove a course from a student's list.

# * Search for students enrolled in Python.

# * Display all students and their courses.







