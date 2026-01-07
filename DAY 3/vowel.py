word = input("Enter a string: ").strip().lower()

if not word.isalpha():
    print("Invalid input")
else:
    first_char = word[0]   


    if (first_char == 'a' or first_char == 'e' or 
        first_char == 'i' or first_char == 'o' or 
        first_char == 'u'):
        print("The string starts with a vowel")
    else:
        print("The string starts with a consonant")