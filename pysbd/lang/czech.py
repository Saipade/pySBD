# -*- coding: utf-8 -*-
import re
from pysbd.abbreviation_replacer import AbbreviationReplacer
from pysbd.between_punctuation import BetweenPunctuation
from pysbd.lang.common import Common, Standard
from pysbd.lists_item_replacer import ListItemReplacer
from pysbd.utils import Text
from pysbd.processor import Processor
from pysbd.utils import Rule

class Czech(Common, Standard):

    iso_code = 'cz'
    
    # Added explanation/justification case for ':'
    # https://prirucka.ujc.cas.cz/?id=161
    SENTENCE_BOUNDARY_REGEX = r"（(?:[^）])*）(?=\s?[A-Z])|「(?:[^」])*」(?=\s[A-Z])|\((?:[^\)]){2,}\)(?=\s[A-Z])|\'(?:[^\'])*[^,]\'(?=\s[A-Z])|\"(?:[^\"])*[^,]\"(?=\s[A-Z])|\“(?:[^\”])*[^,]\”(?=\s[A-Z])|[。．.！!?？ ]{2,}|\S.*?([。．.！!?？ȸȹ☉☈☇☄]|:(?!\s?\S+[;,]))|[。．.！!?？]"

    SENTENCE_BOUNDARY_REGEX = r'.*?[\.!:\?]|.*?$'
    Punctuations = ['．', '.', '!', '?', ':', ': ']

    class Numbers(Common.Numbers):

        NumberPeriodSpaceRule = Rule(r'(?<=\s[1-9][0-9])\.(?=\s)|(?<=\s[0-9])\.(?=\s)', '∯')

        NegativeNumberPeriodSpaceRule = Rule(r'(?<=\s-[1-9][0-9])\.(?=\s)|(?<=\s-[0-9])\.(?=\s)', '∯')

        All = Common.Numbers.All + [NumberPeriodSpaceRule, NegativeNumberPeriodSpaceRule]

    class AbbreviationReplacer(AbbreviationReplacer):
        SENTENCE_STARTERS = []

        def replace_period_of_abbr(self, txt, abbr):
            abbr_new = abbr.replace(".", "∯") + "∯"
            txt = txt.replace(abbr + ".", abbr_new)
            return txt

    class Abbreviation(Standard.Abbreviation):
        ABBREVIATIONS = ['st', 'p', 'dr', 'mudr', 'judr', 'ing', 'mgr', 'bc', 'drsc', 'doc', 'prof', 'č', 'c', 'no', 'nr', 'arch', 'hovor', 'zast', 'přen', 'neform', 'kniž', 'kniz', 'urážl', 'urazl', 'pej',  
        'vulg', 'abbr', 'příd', 'prid', 'přísl', 'prisl', 'pom. sl', 'sp', 'staž', 'staz', 'zvol', 'ger', 'rozk', 'inf', 'cit', 'm', 'ž', 'z', 'pl', 'zájm', 'zajm', 's', 'm mn', 'ž. mn', 'z. mn', 'ž.mn', 'z.mn', 
        's. mn', 's.mn', 'dok', 'ned', 'předl', 'predl', 'pomn', 'čísl', 'cisl', 'část', 'cast',  'zdrob', '1p', '2p', '3p', '4p', '5p', '6p', '7p', 'předp', 'predp', 'příč. dok', 'pric. dok', 'příč.dok', 
        'pric.dok', 'příč. ned', 'pric. ned', 'příč.ned', 'pric.ned', 'min. dok', 'min. ned', 'form', 'děts', 'dets', 'slang', 's r. o', 's. r. o', 'min', 'max', 'spol', 'a. d', 'o. k', 'a. s. a. p', 'p. n. l', 
        'pol. pr', 'a.s.a.p', 'p.n.l', 'př. n. l', 'př.n.l', 'n.l', 'n. l', 'corp', 'm.o', 'pol.pr', 'pp', 'sl', 'cz', 'cs', 'tz', 'rtg', 'o.c.p', 'o. c. p', 'c.k', 'c. k', 'n.a', 'n. a','a.m', 'a. m', 'p.m', 
        'p. m', 'vz', 'i.b', 'i. b', 'ú.p.v.o', 'u.p.v.o', 'ú. p. v. o', 'u. p. v. o', 'bros', 'rsdr', 'tu', 'ods', 'n.w.a', 'n. w. a', 'nár', 'nar', 'pedg', 'paeddr', 'rndr', 'naprk', 'a.g.p', 'a. g. p', 'pr', 
        'a.v', 'a. v', 'por', 'mvdr', 'nešp', 'nesp', 'u.s', 'u. s', 'u. s. a', 'u.s.a', 'kt', 'vyd', 'e.t', 'e. t', 'al', 'll.m', 'll. m', 'o.f.i', 'o. f. i', 'mr', 'apod', 'súkr', 'sukr', 'stred', 's.e.g', 
        'tvz', 'ind', 'var', 'stor', 'etc', 'atd', 'n.o', 'n. o', 's.a', 's. a', 'např', 'napr', 'a.i.i', 'a. i. i', 'a.k.a', 'a. k. a',  'konkr', 'čsl', 'csl', 'prek', 'gen', 'viď','xx', 'odd', 'ltd', 't.z', 
        't. z', 'o.z', 'o. z', 'obv', 'obr', 'pok', 'tel', 'št', 'š. p', 's. p', 'š.p', 's.p', 'ph.d', 'ph. d', 'm.n.m', 'm. n. m', 'zz', 's. e. g', 'sr', 'roz', 'atď', 'ev', 'v.sp', 't.č', 't. č', 'el', 'os', 
        'co', 'r.o', 'r. o', 'str', 'p.a', 'p. a', 'zdravot', 'cca', 'p.s', 'p. s', 'zák', 'slov', 'arm', 'inc', 'd.c', 'k.o', 'a. r. k', 'd. c', 'soc', 'zs', 'akad', 'sz', 'pozn', 'tr', 'nám', 'kol', 'csc', 
        'ul', 'o.i', 'jr', 'zb', 'sv', 'tj', 'čs', 'tzn', 'príp', 'iv', 'hl', 'pod', 'vi', 'tis', 'rozh', 'mld', 'a.s', 'a. s', 'phd', 'z.z', 'z. z', 'hod', 'písm', 'pism', 's.r.o', 'ml', 'iii', 't.j', 't. j', 
        'ii', 'resp', 'tzv', 'ad',  'aj', 'ap', 'atp', 'atpod', 'bibl', 'hl.n', 'hl. n', 'kar', 'kupř', 'kupr', 'mil', 'mj', 't. r', 't.r', 'zvl', 'k. o', 'v. sp', 'skr', 'phdr', 'adj', 'adm', 'adv', 'arc', 
        'ariz', 'ark', 'art', 'assn', 'asst', 'attys', 'ave', 'btw', 'cal', 'calif', 'capt', 'insp', 'kans', 'ken', 'ky', 'gov', 'hon', 'hosp', 'hr', 'i. e', 'i.e', 'ia', 'id', 'mich', 'minn', 'miss', 'mt', 
        'mtn', 'neb', 'nebr', 'nev', 'ok', 'okla', 'ont', 'ref', 'rep', 'sen', 'surg', 'tenn', 'tex', 'univ', 'vs', 'vt', 'wash', 'wis', 'wisc', 'wy', 'wyo', 'yuk', 'jan', 'feb', 'mar', 'apr', 'aug', 'sept', 
        'oct', 'nov', 'dec', 'led', 'úno', 'uno', 'bře', 'bre', 'dub', 'kvě', 'čvn', 'čvc', 'cvc', 'srp', 'zář', 'zar', 'říj', 'rij', 'lis', 'pro', 'viz']
        PREPOSITIVE_ABBREVIATIONS = ['st', 'p', 'dr', 'mudr', 'judr', 'ing', 'mgr', 'bc', 'drsc', 'doc', 'prof']
        NUMBER_ABBREVIATIONS = ['č', 'c', 'no', 'nr']

    class ListItemReplacer(ListItemReplacer):

        def add_line_break(self):
            # Alphabetical lists are causing a lot of troubles with abbreviations with 
            # multiple periods and spaces.
            # e.g.  "s. r. o.", "a. s.", "hl. n."

            # self.format_alphabetical_lists()
            self.format_roman_numeral_lists()
            self.format_numbered_list_with_periods()
            self.format_numbered_list_with_parens()
            return self.text
    
    class BetweenPunctuation(BetweenPunctuation):


        def sub_punctuation_between_quotes_and_parens(self, txt):
            # Sentence splitting inside parentheses and quotes enabled
            return txt

    class Processor(Processor):

        def __init__(self, text, lang, char_span=False):
            super().__init__(text, lang, char_span)
            
        def process(self):
            if not self.text:
                return self.text
            self.text = self.text.replace('\n', '\r')
            li = self.lang.ListItemReplacer(self.text)  # czech specific
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
            # Rubular: https://rubular.com/r/3ugNL11dQQRF6T
            self.text = re.sub(r'((\s+[VXIvxi]+)|(^[VXIvxi]+))(\.)(?=\s+)', r'\1∯', self.text, re.IGNORECASE)

        def replace_period_in_czech_dates(self):
            MONTHS = ['leden', 'únor', 'březen', 'duben', 'květen', 'červen', 'srpen', 'září', 'říjen', 'listopad', 'prosinec'
                      'ledna', 'února', 'března', 'dubna', 'května', 'června', 'srpna', 'října', 'listopadu', 'prosince']
            for month in MONTHS:
                # Rubular: https://rubular.com/r/dGLZqsbjcdJvCd
                self.text = re.sub(r'(?<=\d)\.(?=\s*{month})'.format(month=month), '∯', self.text)
