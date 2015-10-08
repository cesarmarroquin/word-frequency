
start = '"'
end = '"'
s = ' "hello" world'

print(s[s.find(start)+len(start):s.rfind(end)])





"""
print([[word_count,normalized_file.count(word_count)] for word_count in set(normalized_file)])
combined = [item for sublist in normalized_file for item in sublist]
print(combined)



for i in range(0, 7): #len(normalized_file)):

    normalized_file[i] = re.sub( r'[^A-Za-z]', ' ', normalized_file[i])
    normalized_file[i] = re.findall(r'\S+', normalized_file[i])



    if normalized_file[i] == " ":
        normalized_file[i] = ""
    else:
        #normalized_file[i] += normalized_file[i-1]
        word_list[i] = [word for line in normalized_file[i] for word in line.split()]
        print(normalized_file[i])

    #str(re.sub( r'[^A-Za-z]', '', normalized_file[i]))

print(word_list)
print(normalized_file)













from collections import Counter
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
print(Counter(z))
print(z)



l = ["a","b","b"]
print(l)
print([[x,l.count(x)] for x in set(l)])
print(l)





animals = ["cat", "dog", "mouse", "dog", "dog", "cat", "frog", "hippo"]
num_animals = len(animals)
counter = 1

print(animals)
print("total number of ",num_animals)

for i in range(0, len(animals)):

    if animals[i] == animals[i-1]:
        counter += 1
        print(counter)


x = ['a', ['b'], ['c'], ['d'], 'e', 'f', 'g']
x[0] = [' '.join(x[0:-1])]
print(x)




# def normalize():
#     normalized_string = ''.join(map(str, file))#converts the list into a string
#     normalized_string = re.sub( r'[^A-Za-z]', ' ', str(normalized_string).lower())#removes commas extra chars etc
#     normalized_string = re.sub( '\s+', ' ', normalized_string ).strip()#strips off extra ' ' chars
#     normalized_string = normalized_string.split(" ")#converts back to list
#     return normalized_string
"""
