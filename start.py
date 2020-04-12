import argparse
from this_was_alot_of_work import logo, designed_by
from stories import Story,stories
from random import choice

parser = argparse.ArgumentParser(description='Madlib for Command Line ')
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
    again = input("Type 'yes' to play again   ")
    if again.lower() == 'yes':
        z()
    else:
        print('Thanks for playing...')
z()
