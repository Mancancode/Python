#Create a manual mapping between the index and value for the items in the list 'names'
names=['John Smith', 'Adam Dom','Tim Cook', 'Sundar Pichai', 'Elon Musk', 'Sebastian Thrun', 'Steve Jobs', 'Bill Gates']
for index, name in zip(index, sorted(names)):
    print(index, name)

    for i in [3, 'A', 3.5]:
        print(type(i))