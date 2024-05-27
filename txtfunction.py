#create stock price txt file 

data = """6-Mar    310
7-Mar    340
8-Mar    380
9-Mar    302
10-Mar   297
11-Marc  323"""

with open('stockprices.txt', 'w') as file:
    file.write(data)