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
    random.shuffle(pairs)

    for i in xrange(len(pairs)):
        buys_for = i - 1
        if i == 0:
            next = len(pairs)
        print '%s -> %s' % (pairs[i][0], pairs[buys_for][1], )

    random.shuffle(pairs)

    for i in xrange(len(pairs)):
        buys_for = i - 1
        if i == 0:
            next = len(pairs)
        print '%s -> %s' % (pairs[i][1], pairs[buys_for][0], )


if __name__ == '__main__':
    main()
