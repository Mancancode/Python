names=['John Smith', 'Adam Dom','Tim Cook', 'Sundar Pichai', 'Elon Musk', 'Sebastian Thrun', 'Steve Jobs', 'Bill Gates']
for name in names:
    print(name)

len(names)
print(len(names))

names.index('Elon Musk')
#print(name)

names.append("Achonwa Chris")
#print(names)

indexes = range(len(names))
#print(indexes)

#print(list(indexes))

#Lists can store different types of variables like strings and integers
#Example of list with values of different data types

for i in [3,'A',3.5]:
    print(type(i))

    #Dictionary
    # Create a manual mapping between the index and value for the items in the list 'names'
    for index, name in zip(indexes, sorted(names)):
        print(index, name)
