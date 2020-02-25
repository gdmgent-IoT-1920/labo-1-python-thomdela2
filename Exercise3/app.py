from random import randint

random_number = randint(1000, 10000)
print(random_number)

guessed_number = int(input("\nGeef een viercijferig nummer in:\n"))

try_count = 1

def return_matches(a,b):
       return list(set(a) & set(b))

while guessed_number != random_number:
    random_array = [int(x) for x in str(random_number)]
    guessed_array = [int(y) for y in str(guessed_number)]

    chickens = len([i for i, j in zip(random_array, guessed_array) if i == j])
    eggs = len(return_matches(random_array,guessed_array)) - chickens

    if eggs < 0:
        eggs = 0
    
    print("\nU heeft " + str(chickens) + " kippen!")
    print("U heeft " + str(eggs) + " eieren!")

    guessed_number = int(input(" "))
    try_count += 1

print("\nProficiat! U heeft er " + str(pogingen) + " pogingen over gedaan.\n")