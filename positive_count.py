import PyPDF2
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(s):
    for i in s:
        if i in punctuation_chars:
            s=s.replace(i,"")
    return s   
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
def get_pos(st):
    ct=0
    st=st.lower()
    y=st.split()
    for j in range(len(y)):
        y[j]=strip_punctuation(y[j])
        
    for i in positive_words:
        if i in y:
            ct+=st.count(i)
    return ct  

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def get_neg(s):
    ct=0
    s=s.lower()
    y=s.split()
    for j in range(len(y)):
        y[j]=strip_punctuation(y[j])
        
    for i in negative_words:
        if i in y:
            ct+=s.count(i)
    return ct

pdffileobj=open("sample.pdf","rb")
pdfreader=PyPDF2.PdfFileReader(pdffileobj)
num_pages=pdfreader.numPages
n=0
p=0
for i in range(num_pages):
    pageobj=pdfreader.getPage(i)
    text=pageobj.extractText()
    n+=get_neg(text)
    p+=get_pos(text)


for i,j in pdfreader.documentInfo.items():
    print(i[1:],j)
print(str(round((1-(n/(n+p)))*100,2))+"%"+" Positive")
print(str(round((1-(p/(n+p)))*100,2))+"%"+" Negative")

