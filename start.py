import argparse
from logo import logo, designed_by
from stories import Story,stories
from random import choice
from types import SimpleNamespace


# Parser to grab command line input when game is initiated.
# Any values set here will supercede any other input values
# given later. Use flag plus value like: --noun "box".
# choices are:
#   --plural_noun
#   --adverb
#   --verb
#   --adjective
#   --noun
parser = argparse.ArgumentParser(description='Madlib for Command Line. Any given value arguments will supercede later promted values.')
parser.add_argument("--plural_noun",
                    type=str,
                    help="A plural noun indicates that there is more than one of that noun (while a singular noun indicates that there is just one of the noun). Most plural forms are created by simply adding an -s or –es to the end of the singular word. For example, there's one dog (singular), but three dogs (plural).\n")
parser.add_argument("--adverb",
                    type=str,
                    help="Adverb- word or phrase that modifies or qualifies an adjective, verb, or other adverb or a word group, expressing a relation of place, time, circumstance, manner, cause, degree, etc. (e.g., gently, quite, then, there\n ")
parser.add_argument("--verb",
                    type=str,
                    help="A verb is a word or a combination of words that indicates action or a state of being or condition. A verb is the part of a sentence that tells us what the subject performs. Verbs are the hearts of English sentences. Examples: Jacob walks in the morning.\n")
parser.add_argument("--adjective",
                    type=str,
                    help="Adjective examples include small, large, square, round, poor, wealthy, slow and. Age adjectives denote specific ages in numbers, as well as general ages. Examples are old, young, new, five-year-old, and. Color adjectives are exactly what they sound like – they're adjectives that indicate color.\n")
parser.add_argument("--noun",
                    type=str,
                    help="Noun word used to describe an action, state, or occurrence, and forming the main part of the predicate of a sentence, such as hear, become, happen\n")

# convert parser.parse_args() SimpleNamespace to dictionary.
# Remove keys with value of None. 
args = { k: v for k, v in vars(parser.parse_args()).items() if v!=None }


def playMadlibs():
    '''Fuction to play games of madlibs.'''
    # base case
    if len(list(stories)) == 0: return
    # choose story and print title
    selected_story = choice(list(stories))
    print(stories[selected_story].title,'\n')
    # get user input. store in dict { word_descriptor: word }
    ans = {question: input(question+'  ') for question in stories[selected_story].prompts}
    # overwrite any interactive input given values with command line given values
    ans = {**ans, **args}
    # make accesable by dot notation
    d = SimpleNamespace(**ans)
    # print story with word substitutions
    stories[selected_story].generate(d)
    # remove story from rotation:
    del stories[selected_story]
    # ending choice
    again = input("Type 'yes' to play again   ").lower()
    if again == 'yes' or again=='y':
        playMadlibs()
    else:
        print('Thanks for playing...')

# show logo, show designed by, play game
logo()
designed_by()
playMadlibs()