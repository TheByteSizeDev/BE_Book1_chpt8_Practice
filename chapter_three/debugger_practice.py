import random

my_random = list()
for i in range(10):
    my_randoms.append(random.randrange(1,6,1))


num_list= range(1, 10)

for number in num_list:
    contains = False

    for ranNum in my_randoms:

        if ranNum == number:

            containers = True

    print(
        f"my_randoms list {f'does contain {number}' if contains else f'does not contain {number}'}"
    )