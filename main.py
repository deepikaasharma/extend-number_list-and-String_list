"""In the code block below complete the following:

    In a variable called number_list create a list that contains the values zero through 9 (inclusive)
    In a variable called string_list create a list that contains the words 'This' 'is' 'a' 'test'
    Extend number_list so it also contains the values 100 through 109 (inclusive)
    Extend string_list so it also contains the words 'of' 'how' 'to' 'use' 'the' 'extend' 'method'

"""

number_list = list(range(0,10))
string_list = ['This', 'is', 'a', 'test']
number_list2 = list(range(100, 110))
number_list.extend(number_list2)
string_list2 = ['of', 'how', 'to', 'use', 'the', 'extend', 'method']
string_list.extend(string_list2)

print(number_list)
print(string_list)