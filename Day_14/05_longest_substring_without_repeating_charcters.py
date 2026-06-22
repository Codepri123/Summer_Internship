s = "abcabcbb"

longest = 0
substring = ""

for char in s:
    while char in substring:
        substring = substring[1:]

    substring += char
    longest = max(longest, len(substring))

print(longest)