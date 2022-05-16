# Write a program to mine a log file and find out whether it contains ‘python’.

with open('pr06.txt','r') as f:
    data = f.read()

if 'python' in data:
    print("Yes, File contains 'python' word")