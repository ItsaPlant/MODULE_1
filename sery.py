sery = {
    'ser1': ['roquefort', 1, 12.50 ],
    'ser2': ['stilton', 2,  15.56 ],
    'ser4': ['brie', 3, 32.45 ],
    'ser5': ['gouda', 4, 32.45 ],
    'ser6': ['edam', 5, 87.90 ],
    'ser7': ['parmezan', 6, 24.64 ],
    'ser8': ['mozzarella', 7, 24.94 ],
    'ser9': ['czechosłowacki', 8, 255.26 ]
}


for i, ser in enumerate(sery):
    print(f'{i} {sery[ser][1]}kg {sery[ser][0]}_y/a/u/i/ego for {sery[ser][2]}PLN')

print('\n')
for i in range(10):
    if i%2 == True:
        print((' *')*10)
    else:
        print(('* ')*10)

for i in range(10):
    print(('*')*(i-(i%2)))

print('\n')
for i in reversed(range(10)):
    print('*'*i)