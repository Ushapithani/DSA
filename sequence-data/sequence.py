# sequence_functions.py

def list_operations(lst):
    print("\nList Operations:")
    print("1. Display List")
    print("2. Length")
    print("3. Add Element")
    print("4. Remove Element")
    print("5. Sort List")

    ch = int(input("Enter choice : "))

    if ch == 1:
        print("List :", lst)

    elif ch == 2:
        print("Length :", len(lst))

    elif ch == 3:
        ele = int(input("Enter element to add : "))
        lst.append(ele)
        print("Updated List :", lst)

    elif ch == 4:
        ele = int(input("Enter element to remove : "))
        if ele in lst:
            lst.remove(ele)
            print("Updated List :", lst)
        else:
            print("Element not found")

    elif ch == 5:
        lst.sort()
        print("Sorted List :", lst)


def tuple_operations(tup):
    print("\nTuple Operations:")
    print("1. Display Tuple")
    print("2. Length")
    print("3. First Element")
    print("4. Last Element")

    ch = int(input("Enter choice : "))

    if ch == 1:
        print("Tuple :", tup)

    elif ch == 2:
        print("Length :", len(tup))

    elif ch == 3:
        print("First Element :", tup[0])

    elif ch == 4:
        print("Last Element :", tup[-1])


def set_operations(st):
    print("\nSet Operations:")
    print("1. Display Set")
    print("2. Length")
    print("3. Add Element")
    print("4. Remove Element")

    ch = int(input("Enter choice : "))

    if ch == 1:
        print("Set :", st)

    elif ch == 2:
        print("Length :", len(st))

    elif ch == 3:
        ele = int(input("Enter element to add : "))
        st.add(ele)
        print("Updated Set :", st)

    elif ch == 4:
        ele = int(input("Enter element to remove : "))
        st.discard(ele)
        print("Updated Set :", st)
