import itertools
for i in itertools.permutations(range(10), 5):
    if int(''.join(map(str, i))) * 4 == int(''.join(map(str, reversed(i)))):
        print('A =', i[0])
        print('B =', i[1])
        print('C =', i[2])
        print('D =', i[3])
        print('E =', i[4])
