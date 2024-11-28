Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Create an empty list
... my_list = []
... 
... # Append the elements 10, 20, 30, 40
... my_list.append(10)
... my_list.append(20)
... my_list.append(30)
... my_list.append(40)
... 
... # Insert the value 15 at the second position
... my_list.insert(1, 15)  # Index starts at 0, so 1 is the second position
... 
... # Extend the list with another list [50, 60, 70]
... my_list.extend([50, 60, 70])
... 
... # Remove the last element from the list
... my_list.pop()
... 
... # Sort the list in ascending order
... my_list.sort()
... 
... # Find and print the index of the value 30
... index_of_30 = my_list.index(30)
... print("The index of 30 in my_list is:", index_of_30)
... 
... # Print the final list for verification
... print("Final my_list:", my_list)
