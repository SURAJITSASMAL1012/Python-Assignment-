#list comprehension to generate list of forst 50 positive integers
#anonymous function for check and then filter into result list
result = list(filter(lambda x: (x % 5 == 0), [i for i in range(1,51)]))
print(result)
