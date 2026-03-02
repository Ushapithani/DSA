# main code
import sequence_functions as sf

print("\tSequence Data Types App")

# Initial data
my_list = []
my_tuple = ()
my_set = set()

while True:
    print("\n\nChoices :")
    print("1. Create List")
    print("2. List Operations")
    print("3. Create Tuple")
    print("4. Tuple Operations")
    print("5. Create Set")
    print("6. Set Operations")
    print("7. Exit")

    choice = int(input("Enter choice : "))

    if choice == 1:
        my_list = list(map(int, input("Enter list elements : ").split()))
        print("List created")

    elif choice == 2:
        sf.list_operations(my_list)

    elif choice == 3:
        my_tuple = tuple(map(int, input("Enter tuple elements : ").split()))
        print("Tuple created")

    elif choice == 4:
        sf.tuple_operations(my_tuple)

    elif choice == 5:
        my_set = set(map(int, input("Enter set elements : ").split()))
        print("Set created")

    elif choice == 6:
        sf.set_operations(my_set)

    else:
        print("Ok bye thank you!!!")
        break
