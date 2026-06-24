text = "madam"

rev = ""

for ch in text:
    rev = ch + rev

if text == rev:
    print("It's palindrome")
else:
    print("Not palindrome")

# number = 1214
# original_number = 121
# rev = 0
# temp = 0
# while number>0:
#     rev = number%10
#     temp = temp * 10 + rev
#     number = number//10

# if temp == original_number:
#     print("Palindrome")
# else:
#     print("Not palindrome")