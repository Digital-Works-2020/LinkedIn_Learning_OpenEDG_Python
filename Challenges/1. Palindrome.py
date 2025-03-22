#Palindrome - Consider Only Letters
input_str = input("Enter a string: ").strip()
let_input_str = ''.join([letter for letter in input_str.lower() if ord(letter) >96 and ord(letter) < 123])
rev_input_str = let_input_str[::-1]

if let_input_str == rev_input_str:
    print("The input string is a palindrome")
