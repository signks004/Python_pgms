def divisible(input_list):
    divisible_by_3 = [num for num in input_list if num % 3 == 0]
    not_divisible_by_3 = [num for num in input_list if num % 3 != 0]
    return divisible_by_3, not_divisible_by_3

def square(input_list):
    even_squares = [num ** 2 for num in input_list if num % 2 == 0]
    return even_squares

def sum_digits(num):
    return sum(int(digit) for digit in str(num))

def sum_even(input_list):
    even_digit_sums = [sum_digits(num) for num in input_list if num % 2 == 0]
    return even_digit_sums

def duplicates(input_list):
    no_duplicates = list(set(input_list))
    return no_duplicates

def birthDate(employee_name):
    if employee_name in employee_details:
        return employee_details[employee_name]
    else:
        return "This employee is not in the given dictionary."

# Example employee details dictionary
employee_details = {
    'Virat Kohli': '5 November 1988',
    'Umesh Yadav': '25 October 1987',
    'Manish Pandey': '10 September 1989',
    'Rohit Sharma': '30 April 1987',
    'Ravindra Jadeja': '6 December 1988',
    'Hardik Pandya': '11 October 1993'
}

while True:
    print("Options:")
    print("1. Perform operations on a list of numbers")
    print("2. Get birthdate of an employee")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        input_string = input("Enter a list of numbers: ")
        input_list = [int(num) for num in input_string.split()]
        
        divisible_by_3, not_divisible_by_3 = divisible(input_list)
        even_squares = square(input_list)
        even_digit_sums = sum_even(input_list)
        no_duplicates = duplicates(input_list)
        
        print("List after the given operations")
        print("__________________________________")
        print("Numbers divisible by 3:", divisible_by_3)
        print("__________________________________")
        print("Numbers NOT divisible by 3:", not_divisible_by_3)
        print("__________________________________")
        print("Square of even numbers:", even_squares)
        print("__________________________________")
        print("Sum of digits of even numbers:", even_digit_sums)
        print("__________________________________")
        print("List with duplicates removed:", no_duplicates)
        print("__________________________________")
        
    elif choice == '2':
        employee_name = input("Enter employee's full name: ")
        print("__________________________________")
        birthdate = birthDate(employee_name)
        print("Birthdate:", birthdate)
        
    elif choice == '3':
        print("Exiting the program.")
        break
        
    else:
        print("Invalid choice. Please enter a valid option.")
