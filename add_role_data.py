from typing import List


class Token:
    all_tokens = []

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        cls.all_tokens.append(obj)
        return obj


    def __init__(self, i, token, tagset):
        """
        initialize an instance with id, word replication and text, to which it belongs
        :param token: representation of token itself (word, punctuation etc.)
        :param text: Text object, to which this Token belongs
        """
        
        self.id = int(i)
        self.token = token
        self.tagset = tagset
        self.role = self.add_role_data()


    def __str__(self):
        return  self.token


    def __repr__(self):
        return self.__str__()


    def add_role_data(self) -> str:
        """
            Anya Sheveleva
            ::return argument for each Token, representing it's role in the tripplet:
            ::return options:: obj, subj, pred or None
        """
        
        #для работы нужна только морфологическая разметка от Кости
        
        #ГК
        word_pos = self.tagset.split(',')[0]
        if word_pos == 'Nn' or word_pos == 'Pn' or word_pos == 'Aj':
            word_case = self.tagset.split(',')[2]
            word_number = self.tagset.split(',')[3]
            word_gender = self.tagset.split(',')[4]
        elif word_pos == 'Vb':
            word_number = self.tagset.split(',')[3]
            word_gender = self.tagset.split(',')[4]
            word_pers = self.tagset.split(',')[5]

        obj_noun_cases = ['Gn', 'Dt' , 'Ac', 'Ab', 'Lc']

        #subj_rules
        if (word_pos == 'Nn' or word_pos == 'Pn') and word_case == 'Nm': #существительные и местоимения в И.п.
            role = 'subj'
        #pred_rules
        elif (word_pos == 'Vb' and word_number != '_') or word_pos == 'Pc':
            role = 'pred'
        #obj_rules
        elif word_pos == 'Vb' and word_number == '_' and word_gender == '_' and word_pers == '_': #инфинитив глаголов
            role = 'obj'
        elif ((word_pos == 'Nn' or word_pos == 'Aj' or word_pos == 'Pn') and word_case in obj_noun_cases) or word_pos == 'Pp':
            role = 'obj'
        else:
            role = None

        return role

def load_test_data(file_name):
    tokens = []
    with open(file_name, encoding='utf8') as f:
        lines = f.readlines()
        
        for line in lines:
            args = line.split("\t")
            token = Token(args[0], args[1], args[2])
            tokens.append(token)
            
    return tokens


if __name__ == "__main__":
    """
    you can easily test your functions just by printing the necessary attributes of Token
    """

    tokens = load_test_data('data.txt')
    for token in tokens:
        print(str(token.id) + ' ' + token.token + ': ' + str(token.role))
