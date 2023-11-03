1. Simple if statement

Python
number = 10

if number > 0:
  print("The number is positive.")
else:
  print("The number is negative.")
=======================================
Output:
The number is positive.
=======================================
2. if-else if statement

Python
number = 0

if number > 0:
  print("The number is positive.")
elif number < 0:
  print("The number is negative.")
else:
  print("The number is zero.")
=======================================
Output:
The number is zero.
=======================================

3. Set membership

Python
my_set = {"a", "b", "c"}

if "a" in my_set:
  print("The element 'a' is in the set.")
else:
  print("The element 'a' is not in the set.")
=======================================
Output:
The element 'a' is in the set.
=======================================
4. Set intersection

Python
my_set1 = {"a", "b", "c"}
my_set2 = {"d", "e", "f"}

my_intersection = my_set1.intersection(my_set2)

if my_intersection:
  print("The sets have at least one element in common.")
else:
  print("The sets have no elements in common.")

Output:
=======================================
The sets have no elements in common.
=======================================
5. Set difference

Python
my_set1 = {"a", "b", "c"}
my_set2 = {"d", "e", "f"}

my_difference = my_set1.difference(my_set2)

if my_difference:
  print("The sets have at least one element that is not present in the other set.")
else:
  print("The sets have no elements that are not present in the other set.")

Output:
=======================================
The sets have at least one element that is not present in the other set.
=======================================

6. Set union

Python
my_set1 = {"a", "b", "c"}
my_set2 = {"d", "e", "f"}

my_union = my_set1.union(my_set2)

if my_union:
  print("The sets have at least one element in common.")
else:
  print("The sets have no elements in common.")

Output:
=======================================
The sets have at least one element in common.
=======================================

7. Check if a set is empty

Python
my_set = {"a", "b", "c"}

if my_set:
  print("The set is not empty.")
else:
  print("The set is empty.")

Output:
=======================================
The set is not empty.
=======================================

8. Remove an element from a set

Python
my_set = {"a", "b", "c"}

my_set.remove("b")

if "b" in my_set:
  print("The element 'b' is in the set.")
else:
  print("The element 'b' is not in the set.")

Output:
=======================================
The element 'b' is not in the set.
=======================================

9. Add an element to a set

Python
my_set = {"a", "b", "c"}

my_set.add("d")

if "d" in my_set:
  print("The element 'd' is in the set.")
else:
  print("The element 'd' is not in the set.")

Output:
=======================================
The element 'd' is in the set.
=======================================

10. Check if a set is a subset of another set

Python
my_set1 = {"a", "b", "c"}
my_set2 = {"a", "b"}

if my_set2.issubset(my_set1):
  print("The set 'my_set2' is a subset of the set 'my_set1'.")
else:
  print("The set 'my_set2' is not a subset of the set 'my_set1'.")
  
Output:
=======================================
The set 'my_set2' is a subset of the set 'my_set1'.
=======================================
