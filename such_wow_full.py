""" 
Other considerations
- To add a new word we would only need to add a new if statement like the others
- We could use a dict where the key is the number to divide by and the value is the word to print
  that way it'd easier to extend because we would just add a new entry to the dict
"""
def such_wow_full(max):
    for n in range(1, max):
        final = ''

        if n % 3 == 0:
            final += 'Such'

        if n % 5 == 0:
            final += 'Wow'

        print(final or n)


if __name__ == "__main__":
    such_wow_full(101)
