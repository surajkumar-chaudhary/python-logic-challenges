text = "I love Python"

words = text.split()

rev = ""

for ch in words:
    rev = ch+ " " + rev

print(rev)