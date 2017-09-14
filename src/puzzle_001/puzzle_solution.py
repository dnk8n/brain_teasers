unique_ints = [i for i in range(10)]
for A in unique_ints:
    for B in unique_ints:
        for C in unique_ints:
            for D in unique_ints:
                for E in unique_ints:
                    if ((10000 * A + 1000 * B + 100 * C + 10 * D + 1 * E) * 4 ==
                         10000 * E + 1000 * D + 100 * C + 10 * B + 1 * A
                            and len({A, B, C, D, E}) == 5):
                        print('A =', A)
                        print('B =', B)
                        print('C =', C)
                        print('D =', D)
                        print('E =', E)

