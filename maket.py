from typing import List


class Token:
    new_id = 0
    regexp_for_name = ""  # Lena, here's for you
    all_tokens = []

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        cls.all_tokens.append(obj)
        return obj

    def __init__(self, token):
        """
        initialize an instance with id, word replication and text, to which it belongs
        :param token: representation of token itself (word, punctuation etc.)
        :param text: Text object, to which this Token belongs
        """
        self.id = Token.new_id
        self.token = token
        Token.new_id += 1
        self.initialize_additional_parameters()

    def initialize_additional_parameters(self):
        """
        initializes additional parameters for a Token
        :return:
        """
        self.tagset = self.add_morphology_data()
        self.lemma = self.add_lemma_data()
        self.syntagm = self.add_syntagmatic_data()
        self.heads = self.add_heads_data()
        self.sentim = self.add_sentim_data()
        self.stem = self.add_stemming_data()
        self.role = self.add_role_data()
        self.named_entity = self.add_named_entities()
        self.refers_to = self.add_reference_data()

    def __str__(self):
        return self.token

    def __repr__(self):
        return self.__str__()

    def add_morphology_data(self) -> str:
        """
        Kostya Sipunin

        ::return tagset for a Token instance, that describes Token's morphology
        you can access all Tokens with the help of Token.all_words -> List[Token]

        """
        return 'here'

    def add_lemma_data(self) -> str:
        """
        Kostya Sipunin

        ::return lemma for a Token instance
        you can access all Tokens with the help of Token.all_words -> List[Token]

        """
        return 'example'

    def add_syntagmatic_data(self) -> int:
        """
        Nastya Golovina

        ::return syntagm for each Token, that indicates its belonging to a specific syntagm
        you can access all Tokens with the help of .all_words -> List[Token]

        Example::
            >>> word = Token.all_words[0]
            >>> print(word.token, word.tagset)
            >>> Председатель Nn,An,Nm,Sg,Ms,_,_
        """
        return 1

    def add_heads_data(self) -> int: 
        """
        Natasha Vedeneeva

        ::return ID of main token.
        Example::

            "Председатель комиссии" -
            "комиссии" будет иметь head = 1, потому что он "Председатель" - главное слово

        NB! you can access all Tokens of the text with the help of Token.all_words: List[Token]
        Example::
            >>> word = Token.all_words[0]
            >>> print(word.token, word.tagset)
            >>> Председатель Nn,An,Nm,Sg,Ms,_,_
        """
        return 1

    def add_sentim_data(self) -> int:
        """
        Bentse

        ::return sentim for each Token, representing it's naive tone. Can be 1, -1 or 0
        """
        return 1

    def add_stemming_data(self) -> str:
        """
        Bentse

        ::return stem for each Token, representing it's unchangable form. Комиссии -> Комисси
        """
        return "stem"

    def add_role_data(self) -> str:
        """
        Anya Sheveleva
        ::return argument for each Token, representing it's role in the tripplet:
        ::return options:: obj, subj, pred or None
        """
        return "obj"

    def add_named_entities(self):
        """
        Lena

        :return is_named_entity for each Token. If you need to store regexp, you might use class attributes
        example on line 5

        P.S. Do we really need IDs for these things? Maybe just let it be boolean (True, False)?
        """
        return

    def add_reference_data(self) -> int:
        """
        Katya Gvozdeva

        add .refers_to for each Token, taking into account anaphores. It has to be the id of Token, to which this
        specific Token is an anaphore.
                        0       1       2   3   4       5
        Example: Председатель пошел гулять. Он любит кошек.
        Token(id=3, token="он").refers_to = 0, потому что ID Председатель = 0.

        """
        return 1

    def correct_sentim_data(self):
        """
        Katya Kurganskaya

        correct sentim (self.sentim) data according to your task
        """

    def correct_role_data(self):
        """
        Vadmin Gudkov

        depending on passive constructions and morphological .tagset correct the roles of Tokens
        """
        return


class Triplet:

    def __init__(self, subj: List[Token], obj: List[Token], sentiment_feature: List[Token]):
        self.subj = subj
        self.obj = obj
        self.sentiment_feature = sentiment_feature
        self.sentiment_mark = self.get_sentiment_mark()

    @classmethod
    def build_from_tokens(cls, tokens: List[Token]):
        """
        Katya Zamirajlova

        somehow build tripplets out of tokens and return list of tripplets

        :param tokens: list of Tokens
        :return: list of Triplets with all meta information needed
        """
        return []

    def get_sentiment_mark(self) -> int:
        """
        Katya Zamirajlova

        assess sentiment mark -5 to 5, for example, for the whole triplet

        :return: int result mark
        """


def tokenize_text(text):
    """
    Stas Kurganskyy

    :param text: input text from file
    :return: list of Tokens, ready for further processing
    """

    return [Token(word) for word in text.split()]


def write_triplets_to_file(triplets: List[Triplet], path: str):
    """
    SOMEONE
    writes triplets to table, i might suggest xlwt library

    :param triplets:
    :param path:
    :return:
    """


if __name__ == "__main__":
    """
    you can easily test your functions just by printing the necessary attributes of Token
    """

    with open("test.txt", encoding='utf8') as f:
        raw_text = f.read()

    tokens = tokenize_text(raw_text)

    triplets = Triplet.build_from_tokens(tokens)
    write_triplets_to_file(triplets, "file.txt")

    for token in tokens[:10]:
        print(token.tagset)  # print the attribute you're working at here
