users = ["Kristine", "Tiffany", "Jordan"]

print(users)

users.insert(0, "Anthony")

print(users)

users.append("Ian")

print(users)

tags = ['python', 'development', 'tutorials', 'code']

number_of_tags = len(tags)
last_item = tags[-1]
index_of_last_item = tags.index(last_item)

print(number_of_tags)
print(last_item)
print(index_of_last_item)

tags2 = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
  'computer science'
]

tag_range = tags2[1:-1:2]
tag_range = tags2[::-1]

print(tag_range)

tags2.sort(reverse=True)

print(tags2)


sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1
  
]

sale_price_list = len(sale_prices) 
sale_prices.sort() 
  
if sale_price_list % 2 == 0: 
    median1 = sale_prices[sale_price_list//2] 
    median2 = sale_prices[sale_price_list//2 - 1] 
    median = (median1 + median2)/2
else: 
    median = sale_prices[sale_price_list//2] 
print(median) 




my_string = ["this", "is", "something", "to", "congigate"]

print("".join(my_string))

def hello (stringy):
    new_string = "".join(stringy)

    return new_string

print(hello(my_string))







from functools import reduce


sum_these_please = [1,2,3]

heres_your_sum = sum(sum_these_please)

print(heres_your_sum)

reduce(lambda x, y: (x + y) / 2, sum_these_please)

#summr = sum(my_string[0:len(my_string)])
#print(summr)

def sortString(str): 
    return ''.join(sorted(str)) 
      
 
str = "HiThere"
print(sortString(str)) 

itemsyay = "green-red-black-white"

items=[n for n in itemsyay.split('-')]
items.sort()
print('-'.join(items))