# affirmation message: "This code is a mad lib generator that allows users to input words to create a fun story."
name = input("Enter a name: ")
pronoun = input("Enter your pronoun: ")
job = input("Enter a job: ")
pronoun2 = input("he/she/they: ")

# print(
#     f"""Once upon a time, there was a person named {name}.
# {pronoun} was the best {job} in the world.
# Every day, {pronoun} would wake up early and go to work with a smile on {pronoun2} face.
# One day, {name} discovered a magical tool that made {pronoun2} job even more exciting.
# From that day on, {name} became known as the legendary {job}, inspiring others to follow their dreams."""
# )
if name == "Benita":
    print("Benita is the best person in the world")
elif name == "Benita" or pronoun == "she":
    print(f"{name} is the best person in the world and she is a great friend")
else:
    print(f"{name} is a wonderful person.")