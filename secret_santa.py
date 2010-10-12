import random
import sys
import unittest


PAIRS = (
    ('Ben', 'Carolyn', ),
    ('Dan', 'Emilia', ),
    ('Dom', 'Alice', ),
    ('Gordon', 'Lorna', ),
    ('Jamie', 'Liza', ),
    ('John', 'Ro', ),
    ('Stuart', 'Laura', ),
)


def generate_buyers(pairs):
    buyers = []

    for i in xrange(len(pairs[0])):
        random.shuffle(pairs)

        for j in xrange(len(pairs)):
            buys_for = (j + 1) % len(pairs)
            buyers.append((
                pairs[j][i],
                pairs[buys_for][(i + 1) % len(pairs[buys_for])], ))

    return buyers


class TestGenerateBuyers(unittest.TestCase):
    def test_generate_buyers(self):
        import itertools

        pairs = [
            ('A', 'B', ),
            ('C', 'D', ),
            ('E', 'F', ),
            ('G', 'H', ),
        ]
        result = generate_buyers(pairs)

        assert (len(result) == 2 * len(pairs))
        assert sorted([r[0] for r in result]) ==\
            sorted([r[1] for r in result]) == sorted(itertools.chain(*pairs))


def test():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGenerateBuyers)
    unittest.TextTestRunner(verbosity=1).run(suite)


def main():
    print '\n'.join(['%s -> %s' % (f, t)
        for (f, t) in generate_buyers(list(PAIRS))])


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        test()
    else:
        main()
