my_set = {1,2,3,4,5,6,7,1}
my_set_1 = {2,4,5,9.11,12,6,7,8,}
print(my_set)
print('Union =',my_set|my_set_1)
print('Intersection=',my_set & my_set_1)
print('Difference=',my_set_1 - my_set)

names=['John Smith', 'Adam Dom','Tim Cook', 'Sundar Pichai', 'Elon Musk', 'Sebastian Thrun', 'Steve Jobs', 'Bill Gates']
for name in names:
    print(name)



def print_names(li):
    for name in li:
        if name[1]=='Thrun':
            print(name)