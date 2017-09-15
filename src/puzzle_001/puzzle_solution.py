for A in range(10):
    for B in range(10):
        for C in range(10):
            for D in range(10):
                for E in range(10):
                    if ((10000 * A + 1000 * B + 100 * C + 10 * D + 1 * E) * 4 ==
                         10000 * E + 1000 * D + 100 * C + 10 * B + 1 * A
                            and len({A, B, C, D, E}) == 5):
                        print('A =', A)
                        print('B =', B)
                        print('C =', C)
                        print('D =', D)
                        print('E =', E)
