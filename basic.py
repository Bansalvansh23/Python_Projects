
### TYPE CONVERSION
# old_age = int(input("Enter your age: "))
# new_age = old_age + 2
# print(new_age)
# old_age = input("Enter your age: ")
# new_age = old_age + "2"
# print(new_age)


### VARIOUS METHODS TO USE IN STRING
## METHOD TO SHIFT EVERY WORD IN UPPER CASE
name = input("Enter any name for various string operations: ")
print(name.upper())

## METHOD TO SHIFT TO LOWER CASE
print(name.lower())

## METHOD TO FIND INDEX OF STRING IN THE STRING ENTERED
print(name.find('s'))

## METHOD TO REPLACE THE WHOLE STRING WITH OTHER STRING
print(name.replace(name,"Bansal Ji"))

## TO FIND THE EXITANCE OF PARTICUALR STRING IN THE ENTERED STRING
print('Z'in name)

## ARITHMETIC OPERATORS
print(5 ** 2) ## to find power it is used


## DICTIONARY IN PYTHON
marks = {"DSA":98, "JAVA":99, "Cloud":97}

## FORMAT TO PRINT IN THIS
print(marks["DSA"])

## IF WANT TO INSERT NEW VALUE IN IT
marks["PYTHON"] = 99

print(marks)

## FUNCTION DEFINITION IN PYTHON
def print_sum(first,second=20):
    print(first+second)
    
print_sum(10)