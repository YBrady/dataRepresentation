# Testing to see does the convert work - it does
colnames = ["id", "name", "age"]
result = (1, "mary", 21)
item = {} # blank dictionary object

for i, colName in enumerate(colnames):
    #value = result[i]
    #item[colName] = value
    item[colName] = result[i]
print(item)
