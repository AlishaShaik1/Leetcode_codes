class WordDictionary:

    def __init__(self):
        self.a={}

    def addWord(self,word:str)->None:
        x=self.a

        for y in word:
            if y not in x:
                x[y]={}

            x=x[y]

        x['#']=True

    def search(self,word:str)->bool:
        def dfs(x,y):
            if y==len(word):
                return '#' in x

            if word[y]=='.':
                for z in x:
                    if z!='#' and dfs(x[z],y+1):
                        return True

                return False

            if word[y] not in x:
                return False

            return dfs(x[word[y]],y+1)

        return dfs(self.a,0)