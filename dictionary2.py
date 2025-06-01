dict ={}

while True:
    print("\n Mini Dictionary App")
    print("\n 1. Add/Update a word")
    print("\n 2. Retrieve a word")
    print("\n 3. Delete")
    print("\n 4. View All")
    print ("\n 5. Exit")

choice = input("choose an option")

if choice == "1":
    word= input("Enter the word").strip()
    defination= input("Enter the description").strip()
    dict[word]= defination
    print ("Word '{}' has been added successfully".format(word))

if choice == "2":
    word= input("Enter a word to be retrieved").strip
