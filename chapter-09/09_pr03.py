# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13- year old boy.

for i in range(1,21):
    for j in range(1,11):
        with open(f"tables/mul{i}.txt",'a') as f:
            # f.write('')
            f.write(f"{i} * {j} = {i*j}\n")