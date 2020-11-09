print("Char: ")
char = input()

print("Text: ")
txt = input()

count = 0
# not recommended/harder version:
''' for i in range(len(txt)):
    if txt[i] == char:
        count = count + 1 '''

# recommended/easier version:
count = txt.count(char)

print(count)
