import argparse
from this_was_alot_of_work import logo, designed_by
from stories import Story,stories
from random import choice

parser = argparse.ArgumentParser(description='Madlib for Command Line ')
parser.add_argument("--plural_noun",
                    type=str,
                    help="The 'p' flag is for Place")
parser.add_argument("--adverb",
                    type=str,
                    help="The 'n' flag is for Noun")
parser.add_argument("--verb",
                    type=str,
                    help="The 'v' flag is for Verb")
parser.add_argument("--adjective",
                    type=str,
                    help="The 'a' flag is for adjective")
parser.add_argument("--noun",
                    type=str,
                    help="The 'pn' flag is for Plural_noun")

args = parser.parse_args()
p = args.plural_noun
ad = args.adverb
v = args.verb
adj = args.adjective
n = args.noun
# print(p, n, v, a, pn)

logo()
designed_by()
def z():
    selected_story = choice(list(stories))
    print(stories[selected_story].title,'\n')
    ans = {question: input(question+'  ') for question in stories[selected_story].prompts}
    print(stories[selected_story].generate(ans))
    if selected_story in stories:
        del stories[selected_story]
    again = input("Play A again?   ")
    if again.lower() == 'yes':
        z()
    else:
        print('Thanks for playing...')
z()
