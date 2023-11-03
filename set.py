1. Find the maximum element in a set

Python
def max_element(set1):
  """Finds the maximum element in a set.

  Args:
    set1: A set of elements.

  Returns:
    The maximum element in the set.
  """

  max_element = None
  for element in set1:
    if max_element is None or element > max_element:
      max_element = element
  return max_element


# Example usage:

set1 = {1, 2, 3, 4, 5}
max_element = max_element(set1)
print(max_element)

Output:

5
2. Find the minimum element in a set

Python
def min_element(set1):
  """Finds the minimum element in a set.

  Args:
    set1: A set of elements.

  Returns:
    The minimum element in the set.
  """

  min_element = None
  for element in set1:
    if min_element is None or element < min_element:
      min_element = element
  return min_element


# Example usage:

set1 = {1, 2, 3, 4, 5}
min_element = min_element(set1)
print(min_element)

Output:

1
3. Check if a set is empty

Python
def is_empty(set1):
  """Checks if a set is empty.

  Args:
    set1: A set of elements.

  Returns:
    True if the set is empty, False otherwise.
  """

  return len(set1) == 0


# Example usage:

set1 = {}
is_empty = is_empty(set1)
print(is_empty)

Output:

True
4. Check if an element is present in a set

Python
def is_present(set1, element):
  """Checks if an element is present in a set.

  Args:
    set1: A set of elements.
    element: The element to check for.

  Returns:
    True if the element is present in the set, False otherwise.
  """

  return element in set1


# Example usage:

set1 = {1, 2, 3, 4, 5}
element = 3
is_present = is_present(set1, element)
print(is_present)

Output:

True
5. Remove an element from a set

Python
def remove_element(set1, element):
  """Removes an element from a set.

  Args:
    set1: A set of elements.
    element: The element to remove.

  Returns:
    None.
  """

  set1.remove(element)


# Example usage:

set1 = {1, 2, 3, 4, 5}
element = 3
remove_element(set1, element)
print(set1)

Output:

{1, 2, 4, 5}
6. Add an element to a set

Python
def add_element(set1, element):
  """Adds an element to a set.

  Args:
    set1: A set of elements.
    element: The element to add.

  Returns:
    None.
  """

  set1.add(element)


# Example usage:

set1 = {1, 2, 4, 5}
element = 3
add_element(set1, element)
print(set1)

Output:

{1, 2, 3, 4, 5}
7. Find the union of two sets

Python
def union(set1, set2):
  """Finds the union of two sets.

  Args:
    set1: A set of elements.
    set2: A set of elements.

  Returns:
    A new set containing all of the elements of both sets.
  """

  return set1.union(set2)


# Example usage:

set1 = {1, 2, 3, 4, 5}

