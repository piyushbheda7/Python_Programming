try:
    with open('1.txt' , 'r') as f:
        f.read()
    with open('2.txt' , 'r') as f:
        f.read()
    with open('3.txt' , 'r') as f:
        f.read()
except Exception as e:
    print(f"The File is Not present. Reason: {e}")

print("Thanks for using this program")