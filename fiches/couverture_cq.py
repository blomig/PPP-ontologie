#!/usr/bin/env python3
"""Table de couverture questions de compétence (spec §6) ↔ fiches (séries 46 et 46 bis).

Usage :
  python3 fiches/couverture_cq.py             affiche la table (contenu de docs/couverture-cq.md)
  python3 fiches/couverture_cq.py --ecrire    réécrit docs/couverture-cq.md
  python3 fiches/couverture_cq.py --verifier  code 1 si docs/couverture-cq.md n'est pas à jour

Sources, sans rien deviner :
- les CQ : lignes « - CQn. … » de la section « ## 6. Questions de compétence » de PPP_Specification.md, dans leur ordre ;
- « dit y répondre » : champ `cq_couvertes` de chaque fiche (lecture de fiches/compte.py ; « CQ4a–e » vaut CQ4a à CQ4e) ;
- « couverte par un champ du patron » : la fiche remplit réellement le champ du patron qui répond à la CQ (CHAMPS ci-dessous) ;
- fiche publique : fiche que le site publie (calcul de fiches/compte.py) ;
- exemplaires : assertions non retirées de fiches/exemplaires.yaml, dont celles relues (calcul de compte.py).
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compte

RACINE = os.path.dirname(compte.FD)
SORTIE = os.path.join(RACINE, 'docs', 'couverture-cq.md')
VIDES = {'', '—', 'à définir', 'à fixer', 'à renseigner', 'none', '[]', '{}'}

def rempli(v):
    """Un champ est rempli s'il porte autre chose qu'une valeur vide ou d'attente."""
    if v is None:
        return False
    if isinstance(v, dict):
        return any(rempli(x) for x in v.values())
    if isinstance(v, list):
        return any(rempli(x) for x in v)
    if isinstance(v, bool):
        return True
    return str(v).strip().lower() not in VIDES

def relation(type_):
    return lambda d: any(r.get('type') == type_ for r in d.get('relations') or [])

def base_declaree(d):
    b = d.get('base_dependance') or {}
    return rempli(b.get('types')) or rempli(b.get('note'))

def champ(nom):
    return lambda d: rempli(d.get(nom))

# CQ → (champs du patron, test, en partie ?)
CHAMPS = {
    'CQ3':   ('arité, porteur', lambda d: champ('arité')(d) and champ('porteur')(d), False),
    # CQ8 : seule la relation confusableWith compte ; contre_exemple est obligatoire dans toute fiche et ne distinguerait rien
    'CQ8':   ('relation confusableWith', relation('confusableWith'), False),
    'CQ16a': ('transfert', champ('transfert'), False),
    'CQ17':  ('nanay, transfert, relations', lambda d: champ('nanay')(d) and champ('transfert')(d) and champ('relations')(d), False),
    # CQ26 : une fiche semi-formelle répond si sa base est déclarée, par des types ou par une note (cas de perceptualContrast)
    'CQ26':  ('strate, base_dependance', lambda d: champ('strate')(d) and (d.get('strate') == 'formel' or base_declaree(d)), False),
    # CQ27 : la clé facteurs_non_perceptuels présente est une réponse, liste vide (« aucun ») comprise
    'CQ27':  ('base_dependance.facteurs_non_perceptuels', lambda d: 'facteurs_non_perceptuels' in (d.get('base_dependance') or {}), False),
    'CQ29':  ('enonces_testables', champ('enonces_testables'), False),
    'CQ31':  ('conditions_critiques', champ('conditions_critiques'), True),
}
MODELE = ['CQ5', 'CQ6', 'CQ7', 'CQ9', 'CQ10', 'CQ11', 'CQ19', 'CQ20', 'CQ21', 'CQ22', 'CQ30']

def cqs_de_la_spec():
    t = open(os.path.join(RACINE, 'PPP_Specification.md'), encoding='utf-8').read()
    a = t.index('\n## 6. Questions de compétence')
    return [(m.group(1), m.group(2).strip()) for m in re.finditer(r'^- (CQ\d+[a-z]?)\. (.*)$', t[a:t.index('\n## 7.', a)], re.M)]

def court(texte, n=90):
    texte = texte.replace('*', '')
    return texte if len(texte) <= n else texte[:n].rsplit(' ', 1)[0] + ' …'

def table():
    fiches, ex = compte.charger()
    relues = compte.assertions_relues(ex)
    pub, prep, nb, couvre = set(), set(), {}, {}
    for i, d in sorted(fiches.items()):
        (pub if compte.palier(d, ex)[0] != 'pas publiable' else prep).add(i)
        tous = compte.exemplaires(d, ex)
        nb[i] = (len(tous), sum(1 for a in tous if a['id'] in relues))
        for c in compte.lire_cq(d.get('cq_couvertes'))[0]:
            couvre.setdefault(c, []).append(i)
    nom = lambda i: '`%s`' % i.replace('ppp:', '')
    liste = lambda L: ', '.join(nom(i) for i in L) or '—'
    def patron(c):
        if c not in CHAMPS:
            return ''
        champs, test, partiel = CHAMPS[c]
        p = [i for i in sorted(fiches) if test(fiches[i])]
        n_pub = [i for i in p if i in pub]
        txt = '%s : %d fiches publiques sur %d, %d en préparation sur %d' % (champs, len(n_pub), len(pub), len(p) - len(n_pub), len(prep))
        return txt + (' (en partie)' if partiel else '')
    cqs = cqs_de_la_spec()
    L = ['# Couverture des questions de compétence par les fiches', '',
         'Une question de compétence est une question à laquelle l’ontologie doit savoir répondre (par exemple : où se situe cet objet sur l’échelle d’une qualité ?). '
         'Ce tableau dit, pour chacune, quelles fiches disent y répondre. Certaines questions portent sur la manière de noter une observation, pas sur une qualité : '
         'aucune fiche ne peut y répondre seule. Les lignes suivent l’ordre de la spécification.', '',
         '*Généré par `python3 fiches/couverture_cq.py --ecrire` ; ne pas corriger à la main. Les questions viennent de la spécification (§6). '
         '« Fiches qui disent y répondre » : la fiche nomme la question dans son champ `cq_couvertes` ; le tableau ne juge pas si c’est fondé. '
         'Une fiche est « publique » quand le site la publie ; les autres sont « en préparation ». '
         '« Couverte par un champ du patron » : pour quelques questions, un champ que toute fiche doit remplir (le patron de fiche, `PPP_FicheType.md`) y répond ; '
         'le tableau compte les fiches où ce champ est réellement rempli.*', '',
         '**%d questions** ; **%d fiches** (%d publiques, %d en préparation).' % (len(cqs), len(fiches), len(pub), len(prep)), '',
         '## Par question', '',
         '| Question | Énoncé (début) | Fiches publiques qui disent y répondre | Fiches en préparation qui disent y répondre | Couverte par un champ du patron |',
         '|---|---|---|---|---|']
    for c, q in cqs:
        f = couvre.get(c, [])
        L.append('| %s | %s | %s | %s | %s |' % (c, court(q), liste([i for i in f if i in pub]), liste([i for i in f if i in prep]), patron(c) or '—'))
    L += ['', '## Exemplaires par fiche publique', '',
          'Un exemplaire place un objet réel (photo publiée) sur l’échelle d’une qualité : il illustre CQ1 et CQ2 pour cette qualité. '
          'Les exemplaires ne nomment pas de question ; le tableau ne leur en attribue pas d’autre. « Relus » : vérifiés par la relecture avant publication.', '',
          '| Fiche publique | Questions nommées | Exemplaires | dont relus |', '|---|---|---|---|']
    for i in sorted(pub):
        L.append('| %s | %s | %d | %d |' % (nom(i), ', '.join(compte.lire_cq(fiches[i].get('cq_couvertes'))[0]), nb[i][0], nb[i][1]))
    sans = [c for c, _ in cqs if not any(i in pub for i in couvre.get(c, []))]
    modele = [c for c in sans if c in MODELE]
    patr = [c for c in sans if c in CHAMPS]
    L += ['', '## Questions qu’aucune fiche publique ne dit couvrir (%d sur %d)' % (len(sans), len(cqs)), '', ', '.join(sans) or '—', '',
          'Cette liste mélange deux sortes de questions :',
          '- des **questions sur la manière de noter une observation** (qui regarde, quoi, dans quel échange, pour quel projet, à partir de quel texte) : %s. '
          'Elles relèvent du modèle des observations (assertions et épisodes, spec §9.3), pas d’une fiche ;' % ', '.join(modele),
          '- des **questions sur les qualités elles-mêmes**, qu’une fiche pourrait déclarer : les autres. Parmi elles, %s ont déjà un champ du patron qui y répond (colonne de droite) ; '
          'le champ `cq_couvertes` des fiches ne les nomme pas encore.' % ', '.join(patr), '']
    return '\n'.join(L)

if __name__ == '__main__':
    t = table()
    if '--ecrire' in sys.argv:
        open(SORTIE, 'w', encoding='utf-8').write(t)
    elif '--verifier' in sys.argv:
        ok = os.path.exists(SORTIE) and open(SORTIE, encoding='utf-8').read() == t
        print('docs/couverture-cq.md : ' + ('à jour.' if ok else 'périmé ; relancer fiches/couverture_cq.py --ecrire.'))
        sys.exit(0 if ok else 1)
    else:
        print(t)
