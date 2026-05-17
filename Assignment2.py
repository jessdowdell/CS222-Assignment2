import math

#Constants
HOTDOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8

#User input
num_people = int(input("Enter the number of people attending the cookout: "))
hotdogs_per_person = int(input("Enter the number of hotdogs each person will get: "))

#Total hot dogs needed
total_hotdogs = (num_people * hotdogs_per_person)

#Calculate packages needed
hotdogs_packages = math.ceil(total_hotdogs / HOTDOGS_PER_PACKAGE )
buns_packages = math.ceil(total_hotdogs / BUNS_PER_PACKAGE)

#Calculate leftovers
hotdogs_leftover = ((hotdogs_packages * HOTDOGS_PER_PACKAGE) - total_hotdogs)
buns_leftover = ((buns_packages * BUNS_PER_PACKAGE) - total_hotdogs)

# Display Results
print("\nCookout Requirements:")
print("Minimum hot dog packages needed: ", hotdogs_packages)
print("Minimum hot dog bun packages needed: ", buns_packages)
print("Hot dogs left over: ", hotdogs_leftover)
print("Hot dog buns left over: ", buns_leftover)

