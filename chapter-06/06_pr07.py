# Write a program to find out whether a given post is talking about “Harry” or not.

story = '''harry,this is a story about one youtuber who is teaching python programmig languange in youtube through his youtube channel freely and his name is piyush and teach best python languange '''

if(story.find('harry') > -1):
    print("Yeah,The Given Post is talking about 'harry' ")
else :
    print("No,The Given Post is not talking about 'harry' ")