# List Less Than 10 
# Program that creates a list of the numbers in 
# list a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
# that is less than 10

def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] # original list
    again = True
    print('Original list:', a)
    b = [elem for elem in a if elem < 10] # list comprehension to create new list which has desired values
    print('New list that contains numbers less than 10:', b)
    while again:
        try:
            userNum = int(input("Enter a number: "))
            c = [elem for elem in a if elem < userNum]
            print('List containing numbers less than', userNum,'\n', c)
            again = False
        except ValueError as e:
            print(str(e))

main()