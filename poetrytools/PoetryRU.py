from poetrytools.Poetry import Poetry
from poetrytools.simpletokenizer import tokenize

import re


class PoetryRU(Poetry):
    def __init__(self, path_to_dictionary):
        super(PoetryRU, self).__init__(path_to_dictionary)
        self.language = 'RU'

    def tokenize(self, poem):
        tokens = []
        # Problematic characters to replace before regex
        replacements = {u'-': u' ', u'—': u' '}

        for original, replacement in replacements.items():
            poem = poem.replace(original, replacement)
        replaced = poem
        # TODO: I just switch off accents removal, due to russian ё
        # I think, I should implement something more intelligent
        # replaced = remove_accents(replaced)

        # Keep apostrophes, discard other non-alphanumeric symbols
        cleaned = re.sub(r'[^0-9a-zA-ZА-Яа-яЁё\s\']', '', replaced)

        for line in cleaned.split('\n'):
            tokens.append([word for word in line.strip().split(' ')])
        return tokens

    def __similar_vowels__(self, word):
        return word.replace('ё', 'е')

    def __stunning_consonants__(self, syllables):

        stunning_consonants = {"b": "p", "v": "f", "g": "k", "d": "t", "zh": "sh", "z": "s",
                                "bj": "pj", "vj": "fj", "gj": "kj", "dj": "tj", "zj": "sj"}
        if syllables[-1] in stunning_consonants:
            syllables[-1] = stunning_consonants[syllables[-1]]

        return [syl for syl in syllables]

    def __vowel_reduction__(self, syllables):
        stressed_vowel = -1
        before_stressed_vowel = -1
        for index, syl in enumerate(syllables):
            if "1" in syl:
                stressed_vowel = index
        for index, syl in enumerate(syllables[:stressed_vowel]):
            if syl[0] in "aeiouy":
                before_stressed_vowel = index

        for index, syl in enumerate(syllables):
            if (any(char.isdigit() for char in syl)) and index != stressed_vowel and index != before_stressed_vowel:
                if syl[0] in "ao" and "j" not in syllables[index-1]:
                    syllables[index] = "ъ"
                elif syl[0] in "aoe" and "j" in syllables[index-1]:
                    syllables[index] = "ь"
                elif syl[0] in "aoe" and syllables[index-1] in ("zh","sh","ch","sch","c"):
                    syllables[index] = "ъ"

        return [syl for syl in syllables]

    def __language_specific_syllables__(self, syllables):
        # Work around some limitations of CMU
        equivalents = {"rj": "r", "sj": "s", "nj": "n"}
        eq = [
            ('a0', 'o1'),
            ('e0', 'i0'),
            ('e0', 'a0')
        ]
        if syllables[-1] in equivalents:
            syllables[-1] = equivalents[syllables[-1]]

        return [syl for syl in syllables]
