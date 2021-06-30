#Write a Python program to create a list of random integers and randomly select multiple items from the said list.
# Use random.sample()
import random

my_list = []
for i in range(random.randint(1, 50)):
    my_list.append(i)

print(my_list)
print(random.sample(my_list, 5))

# import random
# print("Set a random seed and get a random number between 0 and 1:")
# random.seed(0)
# new_random_value = random.random()
# print(new_random_value)
# random.seed(1)
# new_random_value = random.random()
# print(new_random_value)
# random.seed(2)
# new_random_value = random.random()
# print(new_random_value)
