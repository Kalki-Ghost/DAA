hero = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
""" Length of the list"""
print("Length of the string:", len(hero))

""" Add 'black panther' at the end of this list"""
hero.append("Black Panther")
print(hero)
i = len(hero) - 1
while True:
    hero[i] = hero[i - 1]
    i -= 1
    if hero[i] == "hulk":
        break

hero[i] = "Black Panther"
print(hero)
"""Now you don't like thor and hulk because they get angry easily :)So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).Do that with one line of code."""
# hero.remove('thor');hero.remove('hulk');hero.insert(1,"Doctor Strange")
hero[1:3] = ['doctor strange']

print(hero)

"""Sort the hero list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)"""
hero.sort(key=str.lower)
print(hero)


"""All the function which are use to list"""
print(dir(hero))