#  NO 1
def confirm_length(word):

    # Complete the condition statement using a string operation. 
    # if ___ 
    #     # Complete the return statement using a string operation.
    #     return ___ 
    # else:
    #     return 0
    return len(word)

print(confirm_length("a")) # Should print 1
print(confirm_length("This is a long string")) # Should print 21
print(confirm_length("Monday")) # Should print 6
print(confirm_length("")) # Should print 0


# NO 2
def string_words(string):
    # Complete the return statement using both a string operation and 
    # a string method in a single line.
    return len(string.split(" "))

print(string_words("Hello, World")) # Should print 2
print(string_words("Python is awesome")) # Should print 3
print(string_words("Keep going")) # Should print 2
print(string_words("Have a nice day")) # Should print 4

# NO 3
def sort_distance(distances):
    # ___ # Sort the list
    # ___ # Reverse the order of the list
    return sorted(distances)[::-1]


print(sort_distance([2,4,0,15,8,9]))
# Should print [15, 9, 8, 4, 2, 0]

# NO 4
def increments(start, end):
    return [ x+2 for x in range(start, end+1) ] # Create the required list comprehension.

print(increments(2, 3)) # Should print [4, 5]
print(increments(1, 5)) # Should print [3, 4, 5, 6, 7]
print(increments(0, 10)) # Should print [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# NO 5
def car_listing(car_prices):
  result = ""
  # Complete the for loop to iterate through the key and value items 
  # in the dictionary.
  dict_len = len(car_prices)
  for k, v in car_prices.items() :
    result += f"A {k} costs {v} dollars" # Use a string method to format the required string. 
    dict_len -= 1
    if dict_len > 0:
      result += "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# Should print:
# A Kia Soul costs 19000 dollars
# A Lamborghini Diablo costs 55000 dollars
# A Ford Fiesta costs 13000 dollars
# A Toyota Prius costs 24000 dollars

# no 6
def combine_guests(guests1, guests2):
  guests2.update(guests1) # Use a dictionary method to combine the dictionaries.
  return guests2

Ricks_guests = { "Adam":2, "Camila":3, "David":1, "Jamal":3, "Charley":2, "Titus":1, "Raj":4}
Tessas_guests = { "David":4, "Noemi":1, "Raj":2, "Adam":1, "Sakira":3, "Chidi":5}

print(combine_guests(Ricks_guests, Tessas_guests))
# Should print:
# {'David': 1, 'Noemi': 1, 'Raj': 4, 'Adam': 2, 'Sakira': 3, 'Chidi': 5, 'Camila': 3, 'Jamal': 3, 'Charley': 2, 'Titus': 1}


# NO 7
def count_numbers(text):
  # Initialize a new dictionary.
  dictionary = {} 
  # Complete the for loop to iterate through each "text" character.
  for x in text:
    # Complete the if-statement using a string method to check if the
    # character is a number.
    if x.isnumeric():
      # Complete the if-statement using a logical operator to check if 
      # the number is not already in the dictionary.
      if x not in dictionary:
           # Use a dictionary operation to add the number as a key
           # and set the initial count value to zero.
          dictionary[x] = 1
          continue 
      # Use a dictionary operation to increment the number count value 
      # for the existing key.
      dictionary[x] += 1
  return dictionary

print(count_numbers("1001000111101"))
# Should be {'1': 7, '0': 6}

print(count_numbers("Math is fun! 2+2=4"))
# Should be {'2': 2, '4': 1}

print(count_numbers("This is a sentence."))
# Should be {}

print(count_numbers("55 North Center Drive"))
# Should be {'5': 2}

# NEW - 1
def alpha_length(string):
    # character = ""
    count_alpha = 0
    # Complete the for loop sequence to iterate over "string".
    for x in string: 
        # Complete the if-statement using a string method. 
        if x.isalpha():
            count_alpha += 1  
    return count_alpha
 
print(alpha_length("This has 1 number in it")) # Should print 17
print(alpha_length("Thisisallletters")) # Should print 16
print(alpha_length("This one has punctuation!")) # Should print 21


# no 2
def alphabetize_lists(list1, list2):


  # new_list = ___ # Initialize a new list.
  # ___ # Combine the lists.
  # ___ # Sort the combined lists.
  # new_list = ___ # Assign the combined lists to the "new_list".
  return sorted(list1 + list2) 


Aniyahs_list = ["Jacomo", "Emma", "Uli", "Nia", "Imani"]
Imanis_list = ["Loik", "Gabriel", "Ahmed", "Soraya"]


print(alphabetize_lists(Aniyahs_list, Imanis_list))
# Should print: ['Ahmed', 'Emma', 'Gabriel', 'Imani', 'Jacomo', 'Loik', 'Nia', 'Soraya', 'Uli']
