# Write a function in Python to parse a string such that it accepts a parameter - an encoded string. This encoded string will contain a first name, last name,
# and an id. You can separate the values in the string by any number of zeros. The id will not contain any zeros. The function should return a Python dictionary
# with the first name, last name, and id values. For example, if the input would be "John000Doe000123". Then the function should return: { "first_name": "John",
# "last_name": "Doe", "id": "123" }

def parseStringToDict(str):
    user_dict = {}
    store = ['first_name', 'last_name', 'id']
    current = 0
    i = 0
    detail = ''
    while len(user_dict.keys()) != 3 and i < len(str):
        if str[i] != '0':
            detail += str[i]
            if i == len(str) - 1:
                user_dict[store[current]] = detail
        else:
            if str[i + 1] != '0':
                user_dict[store[current]] = detail
                detail = ''
                current += 1
        i += 1
    return user_dict


print(
    f"Valid String: {parseStringToDict('John000Doe000123')}")
print(
    f"Valid String: {parseStringToDict('Sarah0000000Smith0000000000006857')}")
print(
    f"Invalid String: {parseStringToDict('Sa000rah0000000Sm00ith000000000000685700')}")
