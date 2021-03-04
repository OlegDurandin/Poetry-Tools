import os
import unittest
from poetrytools.PoetryRU import PoetryRU

class TestENPoems(unittest.TestCase):
    def setUp(self):
        self.poetryRUS = PoetryRU('cmudict/ru_cmudict.json')
        self.number = 0

    def open_poem(self, poem):
        with open(os.path.join('..','poems', 'ru', poem), encoding='utf-8') as f:
            return self.poetryRUS.tokenize(f.read())

    def open_test(self, test):
        with open(os.path.join('..', 'poems', 'test_files', test), encoding='utf-8') as f:
            return self.poetryRUS.tokenize(f.read())

    def test_easy_rhyme(self):
        easy_test = self.open_test('easy_tests.txt')
        for pair in easy_test:
            print(pair[0], pair[1])
            self.assertTrue(self.poetryRUS.rhymes(pair[0], pair[1]))

    def test_medium_rhyme(self):
        medium_test = self.open_test('tests_with_phonetic_processes.txt')
        for pair in medium_test:
            print(pair[0], pair[1])
            self.assertTrue(self.poetryRUS.rhymes(pair[0], pair[1]))

    def test_hard_rhyme(self):
        hard_test = self.open_test('hard_tests.txt')
        for pair in hard_test:
            print(pair[0], pair[1])
            self.assertTrue(self.poetryRUS.rhymes(pair[0], pair[1]))



    '''def test_rhyme_1(self):
        self.assertTrue(self.poetryRUS.rhymes('счастье', 'красным'))

    def test_rhyme_2(self):
        self.assertTrue(self.poetryRUS.rhymes('забаррикадируйся', 'вируса'))'''

    def test_poem_1(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('rhyme_aa.txt'))
        for stanza in stanzas:
            rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanza)
            for line in stanza:
                print(' '.join(line))
            print(rhyme_scheme_string, '\n')
            self.assertTrue(rhyme_scheme_string == 'aa')

    def test_poem_2(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('rhyme_aaaa.txt'))
        for stanza in stanzas:
            rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanza)
            for line in stanza:
                print(' '.join(line))
            print(rhyme_scheme_string, '\n')
            self.assertTrue(rhyme_scheme_string == 'aaaa')

    def test_poem_3(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('rhyme_aaabaaabbbabbcdcdb.txt'))
        for stanza in stanzas:
            rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanza)
            for line in stanza:
                print(' '.join(line))
            print(rhyme_scheme_string, '\n')
            self.assertTrue(rhyme_scheme_string == 'aaabaaabbbabbcdcdb')

    def test_poem_4(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('rhyme_aabb.txt'))
        for stanza in stanzas:
            rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanza)
            for line in stanza:
                print(' '.join(line))
            print(rhyme_scheme_string, '\n')
            self.assertTrue(rhyme_scheme_string == 'aabb')

    def test_poem_5(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('rhyme_aabbcc.txt'))
        for stanza in stanzas:
            rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanza)
            for line in stanza:
                print(' '.join(line))
            print(rhyme_scheme_string, '\n')
            self.assertTrue(rhyme_scheme_string == 'aabbcc')

    def test_poem_6(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('rhyme_aabbccaa.txt'))
        for stanza in stanzas:
            rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanza)
            for line in stanza:
                print(' '.join(line))
            print(rhyme_scheme_string, '\n')
            self.assertTrue(rhyme_scheme_string == 'aabbccaa')

    def test_poem_7(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('rhyme_aabbccdd.txt'))
        for stanza in stanzas:
            rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanza)
            for line in stanza:
                print(' '.join(line))
            print(rhyme_scheme_string, '\n')
            self.assertTrue(rhyme_scheme_string == 'aabbccdd')

    def test_poem_8(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('rhyme_aabcbc.txt'))
        for stanza in stanzas:
            rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanza)
            for line in stanza:
                print(' '.join(line))
            print(rhyme_scheme_string, '\n')
            self.assertTrue(rhyme_scheme_string == 'aabcbc')

    def test_poem_9(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('rhyme_aax.txt'))
        for stanza in stanzas:
            rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanza)
            for line in stanza:
                print(' '.join(line))
            print(rhyme_scheme_string, '\n')
            self.assertTrue(rhyme_scheme_string == 'aaX')

    def test_poem_10(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('rhyme_aaxa.txt'))
        for stanza in stanzas:
            rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanza)
            for line in stanza:
                print(' '.join(line))
            print(rhyme_scheme_string, '\n')
            self.assertTrue(rhyme_scheme_string == 'aaXa')

    def test_poem_11(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('rhyme_aaxb.txt'))
        for stanza in stanzas:
            rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanza)
            for line in stanza:
                print(' '.join(line))
            print(rhyme_scheme_string, '\n')
            self.assertTrue(rhyme_scheme_string == 'aaXX')

    def test_poem_12(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('rhyme_ab.txt'))
        for stanza in stanzas:
            rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanza)
            for line in stanza:
                print(' '.join(line))
            print(rhyme_scheme_string, '\n')
            self.assertTrue(rhyme_scheme_string == 'XX')

    def test_poem_14(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('rhyme_abab.txt'))
        for stanza in stanzas:
            rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanza)
            for line in stanza:
                print(' '.join(line))
            print(rhyme_scheme_string, '\n')
            self.assertTrue(rhyme_scheme_string == 'abab')

    def test_poem_15(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('rhyme_ababcdcd.txt'))
        for stanza in stanzas:
            rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanza)
            for line in stanza:
                print(' '.join(line))
            print(rhyme_scheme_string, '\n')
            self.assertTrue(rhyme_scheme_string == 'ababcdcd')

    '''def test_poem_16(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('rhyme_ababcdcdefef.txt'))
        for stanza in stanzas:
            rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanza)
            for line in stanza:
                print(' '.join(line))
            print(rhyme_scheme_string, '\n')
            self.assertTrue(rhyme_scheme_string == 'ababcdcdefef')'''

    def test_poem_17(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('rhyme_abaxb.txt'))
        for stanza in stanzas:
            rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanza)
            for line in stanza:
                print(' '.join(line))
            print(rhyme_scheme_string, '\n')
            self.assertTrue(rhyme_scheme_string == 'abaXb')

    def test_poem_18(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('rhyme_abba.txt'))
        for stanza in stanzas:
            rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanza)
            for line in stanza:
                print(' '.join(line))
            print(rhyme_scheme_string, '\n')
            self.assertTrue(rhyme_scheme_string == 'abba')

    def test_poem_19(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('rhyme_abbaa.txt'))
        for stanza in stanzas:
            rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanza)
            for line in stanza:
                print(' '.join(line))
            print(rhyme_scheme_string, '\n')
            self.assertTrue(rhyme_scheme_string == 'abbaa')

    def test_poem_20(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('rhyme_abbab.txt'))
        for stanza in stanzas:
            rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanza)
            for line in stanza:
                print(' '.join(line))
            print(rhyme_scheme_string, '\n')
            self.assertTrue(rhyme_scheme_string == 'abbab')

    '''def test_poem_21(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('rhyme_abbabcbcddefef.txt'))
        for stanza in stanzas:
            rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanza)
            for line in stanza:
                print(' '.join(line))
            print(rhyme_scheme_string, '\n')
            self.assertTrue(rhyme_scheme_string == 'abbabcbcddefef')'''

    def test_poem_22(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('rhyme_axa.txt'))
        for stanza in stanzas:
            rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanza)
            for line in stanza:
                print(' '.join(line))
            print(rhyme_scheme_string, '\n')
            self.assertTrue(rhyme_scheme_string == 'aXa')

    def test_poem_23(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('rhyme_xaa.txt'))
        for stanza in stanzas:
            rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanza)
            for line in stanza:
                print(' '.join(line))
            print(rhyme_scheme_string, '\n')
            self.assertTrue(rhyme_scheme_string == 'Xaa')

    def test_poem_24(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('rhyme_xabab.txt'))
        for stanza in stanzas:
            rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanza)
            for line in stanza:
                print(' '.join(line))
            print(rhyme_scheme_string, '\n')
            self.assertTrue(rhyme_scheme_string == 'Xabab')

    def test_poem_25(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('rhyme_xaxbab.txt'))
        for stanza in stanzas:
            rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanza)
            for line in stanza:
                print(' '.join(line))
            print(rhyme_scheme_string, '\n')
            self.assertTrue(rhyme_scheme_string == 'XaXbab')

    def test_poem_26(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('rhyme_axaa.txt'))
        for stanza in stanzas:
            rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanza)
            for line in stanza:
                print(' '.join(line))
            print(rhyme_scheme_string, '\n')
            self.assertTrue(rhyme_scheme_string == 'aXaa')

    def test_poem_27(self):
        stanzas = self.poetryRUS.split_into_stanzas(self.open_poem('problems.txt'))
        rhyme_scheme_string, rhyme = self.poetryRUS.guess_rhyme_type(stanzas[0][:4])
        for line in stanzas[0]:
            print(' '.join(line))
        print(rhyme_scheme_string, '\n')
        self.assertTrue(rhyme_scheme_string == 'aaaa')


if __name__ == '__main__':
    unittest.main()
