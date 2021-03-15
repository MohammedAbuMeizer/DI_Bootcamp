import string

class Text():

    def __init__(self,text):
        self.text = text
    
    def frequrncy(self,word=""):
        wordlist = []
        wordlist = self.text.split()
        result = wordlist.count(word)
        if result > 1:
            return result
        else:
            return None
        

    def most_common_word(self):
        wordfreq = []
        wordlist = self.text.split()
        maxf = 0
        for w in wordlist:
            fre = self.frequrncy(w)
            wordfreq.append(fre)
          
        maxf = max(wordfreq)
        max_index = wordfreq.index(maxf)
        return (wordlist[max_index])

    def unique_words(self):
        fil = self.text 
        fil = fil.lower()
        words = fil.split()
        words = [word.strip('.,!;()[]') for word in words]
        words = [word.replace("'s", '') for word in words]
        unique = []
        for word in words:
            if word not in unique:
                unique.append(word)

        return (unique)

    @classmethod
    def from_file(cls,fil):
        return (cls,fil)


class TextModification(Text):

    def punctuation(self):
        punctuations = '''!()-[]{}\;:'",<>./?@#$%^&*_~'''

        my_str =self.text
        no_punct = ""
        for char in my_str:
            if char not in punctuations:
                no_punct = no_punct + char

        print(no_punct)


    def stop_words(self):
        stop = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
        my_str = self.text.split()
        no_stop = ""
        for word in my_str:
            if word not in stop:
                no_stop = no_stop + word + " "

        print(no_stop)

    def special(self):
        punctuations = '''!()-[]{}\;:'"+=-*,<>./?@#$%^&*_~'''

        my_str =self.text
        no_punct = ""
        for char in my_str:
            if char not in punctuations:
                no_punct = no_punct + char

        print(no_punct)




with open("my_text.txt","r") as fil:
    f = fil.read()

tx = Text(f)
print(tx.unique_words())
print(tx.frequrncy("was"))