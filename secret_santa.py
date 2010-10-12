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

    for i in xrange(len(pairs) - 1):
        print '%s -> %s' % (pairs[i][0], pairs[i + 1][1], )

    random.shuffle(pairs)

    for i in xrange(len(pairs) - 1):
        print '%s -> %s' % (pairs[i][1], pairs[i + 1][0], )


if __name__ == '__main__':
    main()
