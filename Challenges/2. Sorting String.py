input_str = input("Enter a string: ").strip()
list_input = input_str.split(" ")

sorted_list_input = sorted(list_input, key = str.lower)
print(' '.join(sorted_list_input))
