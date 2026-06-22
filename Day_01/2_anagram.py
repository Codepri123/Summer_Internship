a = input("Enter first string: ")
b = input("Enter second string: ")

if a[::-1] == b[::-1]:
    print("It is a Anagram")
else:
    print("Not Anagram")