text = "abc123xyz45"

digit_count = 0

for ch in text:
        if ch.isdigit():
        # if ch in '0123456789':
            digit_count += 1

print(digit_count)