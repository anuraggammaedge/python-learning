

import csv
# try:
#     with open('tvbhb.csv','r',encoding='utf-8') as tt:
#         csvWords = csv.reader(tt)
#         next(csvWords)
#         print('header skipped!')

#         print('reading......')
#         for row in csvWords:
#             print(f'First Line: {row}')
#             # print(f'Second Line: {row}')
#         print('finished reading!')

# except FileNotFoundError:
#     print('Not found!')
#     print("creating new one.....")

with open('tvbhb.csv','w', newline='',encoding='utf-8') as tt:
    print(csv.writer(tt).writerow(['abc', 'dsa', 'qwwr']))
with open('tvbhb.csv','a', newline='',encoding='utf-8') as tt:
    print(csv.writer(tt).writerows(['abc', 'dsa', 'qwwr']))
