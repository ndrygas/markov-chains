"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()

    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    lst_of_words = []
    

    # your code goes here
    words = text_string.split()

    for i in range(len(words) - 2):
        bigram = (words[i], words[i + 1])
        # lst_of_words.append(bigram)

    # for item in :
        value = words[i+2]
        if bigram not in chains:
            values = [words[i+2]]
            chains[bigram] = values
        elif bigram in chains:
            # add_value = chains[bigram]
            # # add_value.append[words[i+2]]
            # chains[bigram] = add_value.append([words[i+2]])
            chains[bigram].append(value)



        # chains[bigram] = values.append(words[i+2])
        
    print(chains)
    

    return chains


def make_text(chains):
    """Return text from chains."""

    # #tuple of random starter key
    # words = choice(list(chains.keys()))
    # #swaps tuple to main list of strings
    # list_words = list(words)
    
    # while True:
    #     try:
    #         #finds first word for next key
    #         word2 = list_words[-1]
    #         #
    #         next_word = (word2, choice(words))
    #         list_words.append(next_word[0])
            
    #         # words = choice(list(chains.keys()))
    #         # #got a random key (tuple)
    #         # #now need to add first position
    #         # print(words)

    #     except:
    #         break
    # # your code goes here
    # # words = [bigram[i][0], bigram[i][1]]
    
    # return ' '.join(list_words)

    key = choice(list(chains.keys()))
    words = [key[0], key[1]]
    word = choice(chains[key])

    # Keep looping until we reach a value of None
    # (which would mean it was the end of our original text)
    # Note that for long texts (like a full book), this might mean
    # it would run for a very long time.

    while word is not None:
        try:
            key = (key[1], word)
            words.append(word)
            word = choice(chains[key])
        except:
            break

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
