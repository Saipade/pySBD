import re
from pysbd.abbreviation_replacer import AbbreviationReplacer
from pysbd.lang.common import Common, Standard
from pysbd.lists_item_replacer import ListItemReplacer
from pysbd.utils import Text

class Czech(Common, Standard):

    iso_code = 'cz'

    class ListItemReplacer(ListItemReplacer):

        def add_line_break(self):
            # Same as slovak one

            self.format_roman_numeral_lists()
            self.format_numbered_list_with_periods()
            self.format_numbered_list_with_parens()
            return self.text

    class AbbreviationReplacer(AbbreviationReplacer):
        SENTENCE_STARTERS = []

        def replace_period_of_abbr(self, txt, abbr):
            # Same as slovak one

            abbr_new = abbr.replace(".", "∯") + "∯"
            txt = txt.replace(abbr + ".", abbr_new)
            return txt

    class Abbreviation(Standard.Abbreviation):
        ABBREVIATIONS = ['st', 'p', 'dr', 'mudr', 'judr', 'ing', 'mgr', 'bc', 'drsc', 'doc', 'prof', 'č', 'no', 'nr', 'arch', 'hovor', 'zast', 'přen', 'neform', 'kniž', 'urážl', 'pej', 'vulg', 'abbr', 'příd', 'přísl', 'pom. sl', 'sp', 'staž', 'zvol', 'ger', 'rozk', 'inf', 'cit', 'm', 'ž', 'pl', 'zájm', 's', 'm mn', 'ž. mn', 's. mn', 'dok', 'ned', 'předl', 'pomn', 'čísl', 'část', 'zdrob', '1p', '2p', '3p', '4p', '5p', '6p', '7p', 'předp', 'příč. dok', 'příč. ned', 'min. dok', 'min. ned', 'form', 'děts', 'slang', 's r. o', 's. r. o', 'min', 'max', 'spol', 'a. d', 'o. k', 'a. s. a. p', 'p. n. l', 'pol. pr', 'a.s.a.p', 'p.n.l', 'př. n. l', 'př.n.l', 'n.l', 'n. l' 'corp', 'm.o', 'pol.pr', 'pp', 'sl', 'cz', 'cs', 'tz', 'rtg', 'o.c.p', 'o. c. p', 'c.k', 'c. k', 'n.a', 'n. a','a.m', 'a. m', 'p.m', 'p. m', 'vz', 'i.b', 'i. b', 'ú.p.v.o', 'ú. p. v. o', 'bros', 'rsdr', 'tu', 'ods', 'n.w.a', 'n. w. a', 'nár', 'pedg', 'paeddr', 'rndr', 'naprk', 'a.g.p', 'a. g. p', 'pr', 'a.v', 'a. v', 'por', 'mvdr', 'nešp', 'u.s', 'u. s', 'kt', 'vyd', 'e.t', 'e. t', 'al', 'll.m', 'll. m', 'o.f.i', 'o. f. i', 'mr', 'apod', 'súkr', 'stred', 's.e.g', 's. e. g', 'sr', 'tvz', 'ind', 'var', 'etc', 'atd', 'n.o', 'n. o', 's.a', 's. a', 'např', 'a.i.i', 'a. i. i', 'a.k.a', 'a. k. a', 'konkr', 'čsl', 'prek', 'gen', 'viď', 'k. o', 'v. sp', 'skr', 'phdr', 'xx', 'š.p', 'odd', 'ltd', 't.z', 't. z', 'o.z', 'o. z', 'obv', 'obr', 'pok', 'tel', 'št', 'š. p', 'ph.d', 'ph. d', 'm.n.m', 'm. n. m', 'zz', 'roz', 'atď.', 'ev', 'v.sp', 't.č', 't. č', 'el', 'os', 'co', 'r.o', 'r. o', 'str', 'p.a', 'p. a', 'zdravot', 'cca', 'p.s', 'p. s', 'zák', 'slov', 'arm', 'inc', 'd.c', 'k.o', 'a. r. k', 'd. c', 'soc', 'zs', 'akad', 'sz', 'pozn', 'tr', 'nám', 'kol', 'csc', 'ul', 'o.i', 'jr', 'zb', 'sv', 'tj', 'čs', 'tzn', 'príp', 'iv', 'hl', 'pod', 'vi', 'tis', 'stor', 'rozh', 'mld', 'atď', 'a.s', 'a. s', 'phd', 'z.z', 'z. z', 'hod', 'vs', 'písm', 's.r.o', 'ml', 'iii', 't.j', 't. j','ii', 'napr', 'resp', 'tzv', 'ad', 'aj', 'ap', 'atp', 'atpod', 'bibl','hl.n', 'hl. n', 'kar', 'kupr', 'kupř', 'mil', 'mj', 't. r', 't.r', 'zvl']
        PREPOSITIVE_ABBREVIATIONS = ['st', 'p', 'dr', 'mudr', 'judr', 'ing', 'mgr', 'bc', 'drsc', 'doc', 'prof']
        NUMBER_ABBREVIATIONS = ['č', 'no', 'nr']

    class AbbreviationReplacer(AbbreviationReplacer):

        def __init__(self, text, lang, char_span=False):
            super().__init__(text, lang, char_span)

        def process(self):
            if not self.text:
                return self.text
            self.text = self.text.replace('\n', '\r')

            # Here we use language specific ListItemReplacer:
            li = self.lang.ListItemReplacer(self.text)
            self.text = li.add_line_break()

            self.replace_abbreviations()
            self.replace_numbers()
            self.replace_continuous_punctuation()
            self.replace_periods_before_numeric_references()
            self.text = Text(self.text).apply(
                self.lang.Abbreviation.WithMultiplePeriodsAndEmailRule,
                self.lang.GeoLocationRule, self.lang.FileFormatRule)
            postprocessed_sents = self.split_into_segments()
            return postprocessed_sents

        def replace_numbers(self):
            self.text = Text(self.text).apply(*self.lang.Numbers.All)
            self.replace_period_in_czech_dates()
            self.replace_period_in_ordinal_numerals()
            self.replace_period_in_roman_numerals()
            return self.text

        def replace_period_in_ordinal_numerals(self):
            # Rubular: https://rubular.com/r/0HkmvzMGTqgWs6
            self.text = re.sub(r'(?<=\d)\.(?=\s*[a-z]+)', '∯', self.text)

        def replace_period_in_roman_numerals(self):
            # Rubular: https://rubular.com/r/XlzTIi7aBRThSl
            self.text = re.sub(r'((\s+[VXI]+)|(^[VXI]+))(\.)(?=\s+)', r'\1∯', self.text, re.IGNORECASE)

        def replace_period_in_czech_dates(self):
            MONTHS = ['leden', 'únor', 'březen', 'duben', 'květen', 'červen', 'srpen', 'září', 'říjen', 'listopad', 'prosinec'
                      'ledna', 'února', 'března', 'dubna', 'května', 'června', 'srpna', 'října', 'listopadu', 'prosince']
            for month in MONTHS:
                # Rubular: https://rubular.com/r/dGLZqsbjcdJvCd
                self.text = re.sub(r'(?<=\d)\.(?=\s*{month})'.format(month=month), '∯', self.text)
