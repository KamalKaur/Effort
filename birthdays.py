'''Function with parameter.'''

def happyBirthday(person):
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear " + person + ".")
    print("Happy Birthday to you!")

happyBirthday('Emily')
happyBirthday('Andre')

def main():
    userName = input("Enter the Birthday person's name: ")
    happyBirthday(userName)

main()
