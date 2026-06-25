# =========================
# Codesaga Day 44
# String Methods
# =========================

# -------------------------
# upper()
# -------------------------

name = "nainu"

print(name.upper())

# -------------------------
# lower()
# -------------------------

city = "PATNA"

print(city.lower())

# -------------------------
# replace()
# -------------------------

animal = "cat"

print(animal.replace("c", "b"))

# -------------------------
# Replace One Character
# With Multiple Characters
# -------------------------

text = "cat"

print(text.replace("a", "ABCDE"))

# -------------------------
# Original String Remains Safe
# -------------------------

word = "hello"

new_word = word.upper()

print("Original:", word)
print("New:", new_word)

# -------------------------
# Case Sensitivity
# -------------------------

language = "Python"

print(language.replace("P", "X"))
print(language.replace("p", "X"))

# -------------------------
# Data Cleaning Example
# -------------------------

city1 = "PATNA"
city2 = "Patna"
city3 = "patna"

print(city1.lower())
print(city2.lower())
print(city3.lower())

# -------------------------
# Search System Example
# -------------------------

user_input = "RAHUL"

search_name = user_input.lower()

print(search_name)

# -------------------------
# Username Standardization
# -------------------------

username = "DragonKing"

username_search = username.lower()

print(username_search)

# -------------------------
# Original + Search Version
# -------------------------

original_name = "Rahul Kr"

search_name = original_name.lower()

print("Original:", original_name)
print("Search:", search_name)

