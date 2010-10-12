import random


PAIRS = (
    ('Ben', 'Carolyn', ),
    ('Dan', 'Emilia', ),
    ('Dom', 'Alice', ),
    ('Gordon', 'Lorna', ),
    ('Jamie', 'Liza', ),
    ('John', 'Ro', ),
    ('Stuart', 'Laura', ),
)


def main():
    pairs = list(PAIRS)

    for i in xrange(len(pairs[0])):
        random.shuffle(pairs)

        for j in xrange(len(pairs)):
            buys_for = (j + 1) % len(pairs)
            print '%s -> %s' % (pairs[j][i], pairs[buys_for][(i + 1) % len(pairs[buys_for])], )


if __name__ == '__main__':
    main()
