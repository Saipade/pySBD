# -*- coding: utf-8 -*-
from math import ldexp
from pyrsistent import b
from pysbd.abbreviation_replacer import AbbreviationReplacer
from pysbd.lang.common import Common, Standard

class Portuguese(Common, Standard):

    iso_code = 'pt'

    class AbbreviationReplacer(AbbreviationReplacer):
        SENTENCE_STARTERS = []

    class Abbreviation(Standard.Abbreviation):
        ABBREVIATIONS = ['a', 'aa', 'abrev', 'adj', 'adv', 'agl', 'a.c', 'analo', 'aum', 'circun', 'comb', 'col', 'comp', 'comple', 'cond', 'conj', 'conse', 'contr', 'defe', 'der', 
        'det', 'dia', 'dim', 'eufe', 'eur', 'el',  'f', 'a. c', 'a/c ', 'acad', 'a.d', 'a. d', 'adm', 'aeron', 'ag', 'ag.to', 'ag. to', 'ago', 'agr', 'agric', 'al', 'alf', 'álg', 'alm',
        'alt', 'alv', 'a.m', 'a. m', 'anat', 'ap', 'apart', 'arc', 'arcaic', 'arit', 'aritm', 'arq', 'arquit', 'art', 'ass', 'assem ', 'assemb', 'assist', 'assoc', 'astr', 'át', 'atm', 
        'at.te', 'at. te', 'aum', 'aut ', 'auto', 'autom', 'aux', 'av', 'bar', 'b.-art', 'b.-artes', 'b.el ', 'b.eis', 'bibl', 'bibliog', 'bibliot', 'biofís', 'biogr', 'biol', 'bioq', 
        'bioquím', 'bisp', 'bispd', 'b.o', 'bomb', 'bot', 'br', 'bras', 'brasil', 'brig', 'brig.o', 'brit', 'btl', 'bur', 'buroc', 'c', 'c/', 'c/a', 'c.c', 'c/c', 'c.-alm', 'cap', 
        'cap.ão ', 'capt', 'cap', 'caps', 'c.el', 'cia ', 'c.ia', 'ciênc', 'círc', 'cit', 'clim', 'climatol', 'col', 'com', 'comte', 'comp', 'compl', 'cons', 'consel', 'conselh', 
        'const', 'cont', 'contab', 'cos', 'cp', 'créd', 'cron', 'cronol', 'cx', 'd', 'd.c', 'dd', 'dec', 'decr', 'demog', 'demogr', 'dep', 'dep', 'deps', 'des', 'desen', 'desc', 'dez', 
        'dic', 'dipl', 'doc', 'docs', 'dr', 'drs', 'dr.a', 'dra', 'd.ra', 'dr.as', 'e', 'ee', 'e.c', 'e.c.f', 'e.d', 'ed', 'edif', 'educ', 'e.g', 'elem', 'eletr', 'eletrôn', 'eletron', 
        'e.m', 'emb', 'emb.or', 'embr', 'embriol', 'eng', 'enol', 'esc', 'esp', 'equit', 'e.r', 'est', 'est', 'etc', 'ex', 'f', 'fáb', 'fab', 'fac', 'farm', 'fed', 'fed', 'feder', 
        'fenôm', 'fenom', 'fev', 'ff', 'filos', 'fin', 'fisc', 'fl', 'folc', 'folcl', 'for', 'form', 'fot', 'foto', 'r', 'fss', 'fund', 'g', 'g.al', 'g. al', 'gen', 'gar', 'g.de', 
        'g. de', 'gen', 'geneal', 'geo', 'geog', 'geogr', 'ger', 'germ', 'gloss', 'g.m', 'g.-m', 'gov', 'g/p', 'gr', 'gráf', 'graf', 'grav', 'h', 'hebr', 'her', 'herál', 'heral', 'heráld', 
        'herald', 'herd.o', 'herd. o', 'hidr', 'hidrául', 'hidraul', 'hig', 'hip', 'hist', 'humor', 'i', 'igr', 'ib', 'id', 'il', 'imigr', 'impr', 'índ', 'indúst', 'indust', 'inform',
        'jorn', 'jr', 'jud', 'jul', 'jun', 'jur', 'juris', 'jurisp', 'jurispr', 'just.mil', 'just. mil', 'j.z', 'j. z',
        'fam', 'fem', 'forma regre', 'flex', 'Fut', 'g', 'gír', 'ger', 'gern', 'hom', 'homf', 'homg', 'imp', 'impe', 'inde', 'inf', 'infe', 'int', 'Ing', 'irre', 'loc', 'loc. sub', 
        'loc.sub', 'loc. adj', 'loc.adj', 'loc. pron', 'loc.pron', 'loc. verb', 'loc.verb', 'loc. adv', 'loc.adv', 'loc. conj', 'loc.conj', 'loc. prep', 'loc.prep', 'loc. interj', 
        'loc.interj', 'm', 'meto', 'morf', 'n', 'nom', 'nomin', 'neol', 'part', 'parti', 'pass', 'passa', 'pej', 'perf', 'pes', 'pl', 'poss', '', 'pred', 'pref', 'prep', 'pres', 'pret', 
        'pron', 'p. ext', 'p.ext', 'prov', 'rec', 'rad', 'red', 'reg', 'regi', 's', 's. deverbal',  's.deverbal', 'sina', 's. f', 's.f', 's. m', 's.m', 'sing e pl', 'f. pl', 'f.pl', 
        'sf sing e pl', 'sm', 's.m. e f. e s m + f', 'm. pl', 'm.pl', 'S. m. pl', 'S.m.pl', 's.m. sing. e pl', 'semio', 'sigl', 'sin', 'sint', 'socio. ling', 
        'socio.ling', 'subor', 'suf', 'sup', 'supe', 'temp', 'v. acus', 'v.acus', 'v. anôm', 'v. anom',  'v.anôm', 'v.anom', 'v. at', 'v.at', 'v. aux', 'v.aux', 'v. abun', 'v.abun', 
        'v. bit', 'v.bit', 'v. caus', 'v.caus', 'v. depo', 'v.depo', 'v. des', 'v.des', 'v. dim', 'v.dim',  'v. def', 'v.def', 'v. inc', 'v.inc', 'v. ind', 'v.ind', 'v. lig', 'v.lig', 
        'v. pred', 'v.pred', 'v. t', 'v.t', 'v. t. d', 'v.t.d', 'v. t. i', 'v.t.i', 'v. i. Bot', 'v.i. Bot',  'v. i. fam', 'v.i. fam', 'v. i. náut', 'v.i. náut', 'v. i. naut', 'v.i. naut', 
        'v. i. pop', 'v.i. pop', 'v. pron', 'v.pron', 'v. pr', 'v.pr', 'v. t. e v.i', 'v.t. e v.i', 'v. trans', 'v.trans', 'v. reg. múlt',  'v.reg.múlt', 'v. reg', 'v.reg', 'v. irre', 
        'v.irre', 'voc', 'var', 'verb', '2. g. e 2. n', '2.g. e 2.n', 'h', 'cap', 'dic', 'dicc', 'ed', 'fg', 'fig', 'gên', 'gen', 'id', 'vid', 'med', 'rubr', 'univ', 'contrad', 'ltda', 
        'pgto', 'remte', 'testo', 'contdor', 'emmo', 'prq', 'rdv', 'rod', 'exmo', 'exma', 'círc', 'circ', 'caps', 'alq', 'bal', 'cit', 'jan', 'créd', 'cred', 'séc', 'sec', 'arr', 'assem',
        'pess', 'jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

        PREPOSITIVE_ABBREVIATIONS = []
        NUMBER_ABBREVIATIONS = ['cra', 'ext', 'no', 'n', 'nos', 'p', 'pp', 'tel']
