String_Key = 'W0wMadeitthisfar'

NewValue = '$(' + '+'.join(map(str, [ord(char) for char in String_Key])) + ')'

chars = [34, 95, 17, 57, 2, 16, 3, 18, 68, 16, 12, 54, 4, 82, 24, 45, 35, 0, 40, 63, 20, 10, 58, 25, 3, 65, 0, 20]

keyAscii = [ord(char) for char in String_Key]

resultArray = [(char ^ keyAscii[i % len(keyAscii)]) for i, char in enumerate(chars)]

# Combine characters of resultArray into a string
resultString = ''.join([chr(value) for value in resultArray])

# Print NewValue, ASCII values of resultArray characters, and the combined string
print("NewValue:", NewValue)
print("ASCII values of resultArray characters:", resultArray)
print("Combined string of resultArray characters:", resultString)
