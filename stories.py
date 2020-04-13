

class Story:
    """Madlibs story.

    To  make a story, pass a code, a title, a list of prompts,
    and the text of the template.

        >>> s = Story(
        ...     "simple",
        ...     "A Simple Tale",
        ...     ["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, code, title, words, text):
        """Create story with words and template text."""

        self.code = code
        self.title = title
        self.prompts = words
        self.template = text


    def generate(self, d):
        """Substitute answers into text template and print."""

        print(eval(f'f"""{self.template}"""'))


# Here's a story to get you started


story1 = Story(
    "history",
    "A History Tale",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """


          Once upon a time in a long-ago {d.place}, there lived a
        large {d.adjective} {d.noun}. It loved to {d.verb} {d.plural_noun}.
       

    """
)

story2 = Story(
    "date",
    "How to Date the Coolest Guy/Girl in School",
    [
        "plural_noun",
        "adverb",
        "verb",
        "article_of_clothing",
        "body part",
        "adjective3",
        "noun",
        "another_body_part",
        "plural_noun",
        "another_body_part2",
        "noun2",
        "verb_ending_in_ing",
        "adjective",
        "adjective2",
        "verb2"
    ],
    """ 
    
          It's simple. Turn the {d.plural_noun}. Make him/her want {d.adverb} 
        to date you. Make sure you're always dressed to {d.adjective}. Each and 
        every day, wear a/an {d.article_of_clothing} that you know shows off 
        your {d.noun2} to advantage and make your {d.verb} look like a million {d.noun}.
        
        Even if the two of you make meaningful contact, don't admit it. No hugs or 
        {d.verb_ending_in_ing}. Just shake his/her {d.another_body_part} firmly. And 
        remember, when he/she asks you out, even though a chill may run down your 
        {d.another_body_part2} and you can't stop your {d.verb2} from {d.adjective}, 
        just play it {d.adjective2}. Take a long pause before answering in a very 
        {d.adjective3} voice. I'll have to {d.plural_noun} it over.  


    """
)

story3 = Story(
    "pirate",
    "Talk Like a Pirate",
     [
        "noun",
        "adjective",
        "verb",
        "adverb",
        "noun2",
        "adjective2",
        "plural_noun",
        "part_of_the_body",
        "noun3",
        "noun4",
        "part_of_the_body2"
    ],
    """
    
          Ye can always pretend to be a bloodthirsty {d.noun},
        threatening everyone by waving yer sword in the air, 
        but until ye learn to {d.adjective}, like a pirate, 
        ye'll never be {d.adjective2}, accepted as an authentic {d.verb}.

        So here's what ye do: Cleverly work into yer daily conversations,
        pirate phrases such as "Ahoy there, {d.adverb}", "Avast, ye {d.noun2}", 
        and "Shiver me {d.adjective2}". Remember to drop all yer gs when ye say 
        such words as sailin', spittin', and fightin'. This will give ye a/an 
        {d.plural_noun}, start to being recognized as a swashbucklin'. Once ye 
        have the lingo down pat, it helps to wear a three-cornered {d.noun3},
        on yer head, stash a/an {d.part_of_the_body}, in yer pants, and keep 
        a/an {d.part_of_the_body2}, perched atop yer{d.noun4}. 
        
        Aye, now ye be a real pirate!
        
        
        """
)

# Make dict of {code:story, code:story, ...}
stories = {s.code: s for s in [story1, story2, story3]}