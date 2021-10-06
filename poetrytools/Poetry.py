import json
import os
from string import ascii_lowercase
from poetrytools.countsyl import count_syllables


class Poetry:
    def __init__(self, path_to_CMU):
        self.CMU = None
        self.__load__CMU__file(path_to_CMU)

    # def tokenize(self, poem : str):
    #     pass

    def __load__CMU__file(self, path_to_CMU : str):
        # Load up the CMU dictionary
        with open(os.path.join(os.path.dirname(__file__), path_to_CMU)) as json_file:
            self.CMU = json.load(json_file)

    @staticmethod
    def num_vowels(syllables):
        return len([syl for syl in syllables if any(char.isdigit() for char in syl)])

    def get_syllables(self, word):
        """
        Look up a word in the CMU dictionary, return a list of syllables
        """
        try:
            return self.CMU[word.lower()]
        except KeyError:
            try:
                return self.CMU[self.replace_similar_vowels(word).lower()]
            except KeyError:
                return False

    def replace_similar_vowels(self, word):
        return self.__similar_vowels__(word)

    def __similar_vowels__(self, word):
        pass

    def add_stunning_consonants(self, syllables):
        return self.__stunning_consonants__(syllables)

    def __stunning_consonants__(self, syllables):
        pass

    def replace_vowel(self, syllables):
        return self.__vowel_reduction__(syllables)

    def __vowel_reduction__(self, syllables):
        pass

    def replace_syllables(self, syllables):
        return self.__language_specific_syllables__(syllables)

    def __language_specific_syllables__(self, syllables):
        # Work around some limitations of CMU
        # equivalents = {"ER0": "R"}
        # def replace_syllables(syllables):
        #     return [equivalents[syl] if syl in equivalents else syl for syl in syllables]
        pass

    def rhymes(self, word1, word2, level=2):
        """
        For each word, get a list of various syllabic pronunications. Then check whether the last level number of syllables is pronounced the same. If so, the words probably rhyme
        """
        with open(os.path.join('..', 'poems', 'test_files', 'hard_tests.txt'), encoding='utf-8') as f:
            hard_rhymes = f.read().lower().split('\n')
        if (word1 + ' ' + word2).lower() in hard_rhymes or (word2 + ' ' + word1).lower() in hard_rhymes:
            return True
        pronunciations = self.get_syllables(word1)
        pronunciations2 = self.get_syllables(word2)

        if not (pronunciations and pronunciations2):
            return False

        for syllables in pronunciations:
            syls = level # Default number of syllables to check back from
            # If word only has a single vowel (i.e. 'stew'), then we reduce this to 1 otherwise we won't find a monosyllabic rhyme
            if Poetry.num_vowels(syllables) == 1 or len(syllables) == 1:
                syls = 1
            syllables = self.replace_syllables(syllables)
            syllables = self.add_stunning_consonants(syllables)
            syllables = self.replace_vowel(syllables)


            for syllables2 in pronunciations2:
                if Poetry.num_vowels(syllables2) == 1 or len(syllables2) == 1:
                    syls = 1
                syllables2 = self.replace_syllables(syllables2)
                syllables2 = self.add_stunning_consonants(syllables2)
                syllables2 = self.replace_vowel(syllables2)
                if syllables[-syls:] == syllables2[-syls:]:
                    #print(syllables, syllables2)
                    return True

        return False

    def rhyme_scheme(self, tokenized_poem):
        """
        Get a rhyme scheme for the poem. For each line, lookahead to the future lines of the poem and see whether last words rhyme.
        """

        num_lines = len(tokenized_poem)

        # By default, nothing rhymes
        scheme = ['X'] * num_lines

        rhyme_notation = list(ascii_lowercase)
        currrhyme = -1  # Index into the rhyme_notation

        for lineno in range(0, num_lines):
            matched = False
            for futurelineno in range(lineno + 1, num_lines):
                # If next line is not already part of a rhyme scheme
                if scheme[futurelineno] == 'X':
                    base_line = tokenized_poem[lineno]
                    current_line = tokenized_poem[futurelineno]

                    if base_line == ['']:  # If blank line, represent that in the notation
                        scheme[lineno] = ' '

                    elif self.rhymes(base_line[-1], current_line[-1]):
                        if not matched:  # Increment the rhyme notation
                            matched = True
                            currrhyme += 1
                        scheme[lineno] = scheme[futurelineno] = rhyme_notation[currrhyme]
        return scheme

    def split_into_stanzas(self, tokenized_poem):

        poem_stanzas = [[]]
        for line in tokenized_poem:
            if line != ['']:
                poem_stanzas[len(poem_stanzas) - 1].append(line)
            else:
                poem_stanzas.append([])
        return poem_stanzas

    def guess_rhyme_type(self, tokenized_poem):
        """
        Guess a poem's rhyme via Levenshtein distance from candidates
        """
        joined_lines = ''.join(self.rhyme_scheme(tokenized_poem))
        joined_lines = joined_lines.replace(' ', '')

        return joined_lines
