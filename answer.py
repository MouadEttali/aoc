def get_number_from_string(string: str)-> int:
    l = 0
    r = len(string) - 1 
    while l != r:
        if not string[l].isdigit():
            l+=1
        elif not string[r].isdigit():
            r-=1
        elif string[l].isdigit() and string[r].isdigit():
            return int(string[l] + string[r])
    return int(string[l] + string[r])


with open('example.txt', 'r') as example:
    content = example.readlines()

numbers = []
for line in content:
    numbers.append(get_number_from_string(line))

print(sum(numbers))