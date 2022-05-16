# Repeat program 4 for a list of such words to be censored

words = ['donkey' , 'kaddu' , 'mote'] 

with open('pr05.txt' , 'r') as f:
    content = f.read()

for word in words:
    content = content.replace(word, '&&&&')

with open('pr05.txt','w') as w:
    w.write(content)