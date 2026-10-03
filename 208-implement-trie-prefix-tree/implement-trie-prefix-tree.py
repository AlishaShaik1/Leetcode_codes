class Trie:

    def __init__(self):
        self.a={}

    def insert(self,word:str)->None:
        x=self.a

        for y in word:
            if y not in x:
                x[y]={}

            x=x[y]

        x['#']=True

    def search(self,word:str)->bool:
        x=self.a

        for y in word:
            if y not in x:
                return False

            x=x[y]

        return '#' in x

    def startsWith(self,prefix:str)->bool:
        x=self.a

        for y in prefix:
            if y not in x:
                return False

            x=x[y]

        return True