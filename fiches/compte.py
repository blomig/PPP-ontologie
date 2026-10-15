#!/usr/bin/env python3
"""Comptes du lot de fiches, calculés depuis les fichiers (série 7, point d de la coordination).

Usage :
  python3 fiches/compte.py            affiche les comptes (bloc à recopier dans fiches/README.md)
  python3 fiches/compte.py --ecrire   réécrit le bloc entre les marqueurs (refuse si un marqueur manque ou est mal placé)
  python3 fiches/compte.py --verifier vérifie que le bloc entre <!-- compte:debut --> et <!-- compte:fin -->
                                      de fiches/README.md est identique au calcul, et que les appels [[id]]
                                      sont complets (spec §9.7 P, point 4 bis), et qu'aucun prénom ni nom d'agent
                                      ne figure hors des fichiers autorisés (spec §13, v2.8), et que le rôle
                                      de chaque référence est dans la liste fermée ROLES_REFERENCES
                                      (PPP_FicheType.md, spec §9.7 P ; série 15) ; code 1 sinon
  python3 fiches/compte.py --noms     seulement le contrôle des noms (tout le dépôt sauf .git, local/ ; liste
                                      blanche NOMS_AUTORISES, §13 de la spec ; exceptions comptées, non signalées :
                                      docs/crash-test-0*.md, docs/guide-structure-ontologie.md, maquette/ ;
                                      noms lus dans PPP_NOMS, .noms-prives ou maquette/noms-prives.txt, absents de ce fichier)
  python3 fiches/compte.py --paliers  palier T35 de chaque fiche, avec ses raisons

Règles de lecture (celles de fiches/README.md, « Avancement ») :
- état de travail : « bloquée » si bloque_par n'est pas vide ; sinon « en attente de la relecture explicative » si
  a_relire ou a_reconfirmer n'est pas vide ; sinon « exemple concret manquant » si un manque
  le dit ; sinon « explicabilité validée par la relecture explicative » ;
- « minimale » (origine C6) : introduit_en = 2.5 ;
- références : une fiche « a des références » si sa liste references n'est pas vide ; une référence distincte
  est comptée par son DOI ou son URL (à défaut, par sa citation) ;
- exemplaires : assertions non retirées de exemplaires.yaml (withdrawn ≠ oui), toutes modalités ; pour T35, seules
  comptent les assertions relues en relecture explicative (relecture_explicative.assertions, rien en attente) ; une
  assertion que son auteur a marquée comme discutable (`doute: oui`) ne compte pas pour le palier 1 (tout
  exemplaire reste contestable au sens du §13 : ce n'est pas ce que dit `doute`) ;
- palier de première publication (spec X17 ; T35, tranché le 2026-10-11, QUESTIONS-A-TRANCHER.md).
Le script lit fiches/*.yaml (et, pour les noms, les fichiers texte du dépôt) ; il n'écrit rien.
"""
import glob, os, sys
import yaml

FD = os.path.dirname(os.path.abspath(__file__))
SKIP = {'familles.yaml', 'exemplaires.yaml'}

def charger():
    fiches = {}
    for f in sorted(glob.glob(os.path.join(FD, '*.yaml'))):
        if os.path.basename(f) in SKIP:
            continue
        d = yaml.safe_load(open(f, encoding='utf-8'))
        fiches[d['id']] = d
    ex = yaml.safe_load(open(os.path.join(FD, 'exemplaires.yaml'), encoding='utf-8'))
    return fiches, ex

def en_attente(d):
    v = d.get('relecture_explicative') or {}
    return bool(d.get('a_relire')) or bool(v.get('a_reconfirmer'))

def etat(d):
    """État de travail (fiches/README.md, « Avancement ») ; « en attente de la relecture explicative » passe avant les états validés."""
    if d.get('bloque_par'):
        return 'bloquée'
    if en_attente(d):
        return 'en attente de la relecture explicative'
    if 'exemple concret' in ' '.join(d.get('manques') or []):
        return 'exemple concret manquant'
    return 'explicabilité validée'

def assertions_relues(ex):
    """Assertions relues (relecture explicative) et sans rien en attente dans exemplaires.yaml (T35, condition c)."""
    v = ex.get('relecture_explicative') or {}
    relues = set(v.get('assertions') or [])
    attente = set()
    for e in (v.get('a_relire') or []) + (v.get('a_valider') or []) + (v.get('a_reconfirmer') or []) + (ex.get('a_relire') or []):   # a_valider : ancien nom (avant la série 12)
        if isinstance(e, dict) and e.get('assertion'):
            attente.add(e['assertion'])
        elif isinstance(e, str):
            attente.update(x for x in relues if x in e)
    return relues - attente

def discutable(a):
    """Exemplaire marqué comme discutable par son auteur (champ `doute: oui` de exemplaires.yaml, v2.6, T35)."""
    return str(a.get('doute', 'non')).lower() in ('oui', 'true')

def exemplaires(d, ex, relues_seulement=False, sans_discutables=False):
    """Assertions non retirées du type ; options : seulement relues en relecture explicative, sans celles marquées `doute: oui`."""
    rel = assertions_relues(ex)
    out = []
    for a in ex['assertions']:
        if str(a.get('withdrawn', 'non')) == 'oui' or a['assertedType'] != d['id']:
            continue
        if relues_seulement and a['id'] not in rel:
            continue
        if sans_discutables and discutable(a):
            continue
        out.append(a)
    return out

def regions_illustrees(d, ex, **kw):
    cles = [r['cle'] for r in (d.get('espace_valeurs') or {}).get('regions') or []]
    vues = {a['inRegion'].split('/')[-1] for a in exemplaires(d, ex, **kw)}
    return [c for c in cles if c in vues], cles

def ecart_montre(d, ill):
    """Deux régions illustrées non voisines : rangs séparés d'au moins une région (échelle ordinale),
    ou deux régions non déclarées voisines (échelle nominale)."""
    ev = d.get('espace_valeurs') or {}
    if ev.get('echelle') == 'nominale':
        vois = {frozenset(p) for p in ev.get('voisinages') or []}
        return any(frozenset((x, y)) not in vois for i, x in enumerate(ill) for y in ill[i + 1:])
    rang = {r['cle']: r.get('rang') for r in ev.get('regions') or []}
    rs = [rang[c] for c in ill if rang.get(c) is not None]
    return len(rs) >= 2 and max(rs) - min(rs) >= 2

def objet_de(a):
    about = a['about']
    part = about if isinstance(about, str) else about[0]['relatum']
    return part.split('#')[0]

def palier(d, ex):
    """X17 (T35, tranché) : 'publiable', 'publiable avec exemplaires incomplets' ou 'pas publiable',
    les raisons, et la mention à afficher s'il y a lieu."""
    raisons = []
    regs = (d.get('espace_valeurs') or {}).get('regions') or []
    for k in ('définition', 'question_attentionnelle', 'contre_exemple'):
        if not d.get(k):
            raisons.append(k + ' manquant')
    if not regs or not all(r.get('repere') for r in regs):
        raisons.append('repères manquants')
    ids_e = {e.get('id') for e in d.get('enonces_testables') or []}
    if d['id'] != 'ppp:perceptualContrast' and not {'E1', 'E4'} <= ids_e:
        raisons.append('énoncés E1 ou E4 non déclarés')
    if d.get('bloque_par'):
        raisons.append('bloquée (' + ', '.join(map(str, d['bloque_par'])) + ')')
    if en_attente(d):
        raisons.append('champs à valider ou à re-confirmer par la relecture explicative')
    rs = str(d.get('references_statut') or '')
    if not (d.get('references') or rs.lower().startswith('aucune source trouvée')) or rs == 'à renseigner':
        raisons.append('références à renseigner')
    if any(r.get('statut_verification') == 'non vérifiée' for r in d.get('references') or []):
        raisons.append('référence non vérifiée')
    # (f) exemplaires : seuls comptent les exemplaires relus en relecture explicative (c)
    ill2, cles = regions_illustrees(d, ex, relues_seulement=True)
    if not ill2:
        n_tous = len(exemplaires(d, ex))
        raisons.append('aucun exemplaire relu' if n_tous else 'aucun exemplaire')
    if raisons:
        return 'pas publiable', raisons, None
    # palier 1 : exemplaires relus que leur auteur n'a pas marqués comme discutables, dans deux régions non voisines ; une image reproduite, sinon mention
    forts = exemplaires(d, ex, relues_seulement=True, sans_discutables=True)
    ill1 = [c for c in cles if c in {a['inRegion'].split('/')[-1] for a in forts}]
    if ecart_montre(d, ill1):
        objets = {o['id']: o for o in ex['objets']}
        repro = any((objets.get(objet_de(a), {}).get('credit') or {}).get('usage') == 'image_reproduite' for a in forts)
        return 'publiable', [], (None if repro else 'exemplaires en lien seulement')
    f = lambda L: ', '.join(L) or 'aucune'
    pourquoi = ['écart non montré au palier 1 : régions illustrées par des exemplaires relus : %s ; dont non marquées discutables (`doute`) : %s (sur %d régions)' % (f(ill2), f(ill1), len(cles))]
    return 'publiable avec exemplaires incomplets', pourquoi, None

# --- appels [[id]] (spec §9.7 P, point 4 bis) ---------------------------------------
import re
ALIAS = {'NCS Colour AB': ['NCS'], 'Office québécois de la langue française': ['OQLF'], 'Académie française': ['Académie française'],
         'ISO 2813:2014': ['ISO 2813'], 'ASTM D523-14': ['ASTM D523'], 'ASTM D1003-21': ['ASTM D1003'],
         'CIE S 017:2020': ["vocabulaire international de l'éclairage", 'CIELAB'], 'CIE': ['CIE']}

def _noms(c):
    for k, v in ALIAS.items():
        if c.startswith(k):
            return v
    m = re.match(r"\s*([^,(]+?)\s*[,(.]", c)
    return [m.group(1).strip() if m else c.split()[0]]

def _annee(c):
    y = re.search(r"\((\d{4})", c) or re.search(r"(1[89]\d\d|20\d\d)", c)
    return y.group(1) if y else None

# Liste fermée des rôles de référence (PPP_FicheType.md, champ `role` ; spec §9.7 P ; série 15).
ROLES_REFERENCES = ('fonde', 'alimente', 'discute', 'contraste')

def roles_hors_liste(d):
    """Références de la fiche dont le rôle n'est pas dans ROLES_REFERENCES : liste de (id de la référence, rôle)."""
    return [(r.get('id', '?'), r.get('role')) for r in (d.get('references') or []) if r.get('role') not in ROLES_REFERENCES]

def appels_manquants(d):
    """Toute mention nominative d'une référence dans etat_de_l_art et les note… a son appel [[id]] après sa première mention."""
    refs = d.get('references') or []
    out, noms = [], {}
    for r in refs:
        for n in _noms(r['citation']):
            noms.setdefault(n, []).append(r['id'])
    for k, t in d.items():
        if not isinstance(t, str) or not (k == 'etat_de_l_art' or k.startswith('note')):
            continue
        for r in refs:
            for n in _noms(r['citation']):
                ambigu, y = len(noms[n]) > 1, _annee(r['citation'])
                if ambigu and not y:
                    continue
                pat = re.escape(n) + r"\b" + ((r"[^()\[]{0,90}?" + y) if ambigu else '')
                def coauteur(x):
                    w = re.search(r"([A-ZÀ-Ý][\wÀ-ÿ'’-]+)(?:,? [\wÀ-ÿ'’-]+)*\s+(?:et|&)\s+(?:de\s+)?$", t[max(0, x.start() - 60):x.start()])
                    return bool(w) and any(o['id'] != r['id'] and w.group(1) in o['citation'] and n in o['citation'] for o in refs)
                m = next((x for x in re.finditer(pat, t) if not coauteur(x)), None)
                if not m:
                    continue
                j = t.find('[[%s]]' % r['id'], m.start())
                if j < 0 or j - m.end() > 160:
                    out.append((k, r['id'], t[m.start():m.end() + 30]))
                for x in re.findall(r'\[\[([^\]]*)\]\]', t):
                    if x not in [z['id'] for z in refs]:
                        out.append((k, x, 'id inconnu'))
                break
    return sorted(set(out))

def bloc():
    fiches, ex = charger()
    n = len(fiches)
    etats = {}
    for i, d in fiches.items():
        etats.setdefault(etat(d), []).append(i)
    minimales = sorted(i for i, d in fiches.items() if str(d.get('introduit_en')) == '2.5')
    avec_refs = sorted(i for i, d in fiches.items() if d.get('references'))
    sans_refs = sorted(set(fiches) - set(avec_refs))
    distinctes, statuts = {}, {}
    for d in fiches.values():
        for r in d.get('references') or []:
            k = (r.get('doi_ou_url') or r['citation']).strip().lower()
            distinctes.setdefault(k, r.get('statut_verification'))
    for s in distinctes.values():
        statuts[s] = statuts.get(s, 0) + 1
    attente = sorted(i for i, d in fiches.items() if en_attente(d))
    sans_ex = sorted(i for i, d in fiches.items() if not regions_illustrees(d, ex)[0])
    paliers = {}
    for i, d in fiches.items():
        paliers.setdefault(palier(d, ex)[0], []).append(i)
    c = lambda L: ', '.join('`%s`' % x.replace('ppp:', '') for x in sorted(L)) or '—'
    pl = lambda k, sg, plu: '%d %s' % (k, sg if k == 1 else plu)   # accord : « 1 bloquée », « 1 fiche » (série 48 bis)
    lignes = [
        '<!-- compte:debut (calculé par fiches/compte.py ; ne pas corriger à la main) -->',
        '- **%d fiches de type actives** ; **%d sans point bloquant** (`bloque_par` vide) : %d à explicabilité validée par la relecture explicative (%s), %d au langage courant validé avec exemple concret manquant (%s), %d en attente de la relecture explicative (champs à valider ou à re-confirmer : %s) ; **%s** par un point T ou C (%s) ; dont **%d minimales** (2.5, C6) : %s.'
        % (n, n - len(etats.get('bloquée', [])), len(etats.get('explicabilité validée', [])), c(etats.get('explicabilité validée', [])),
           len(etats.get('exemple concret manquant', [])), c(etats.get('exemple concret manquant', [])),
           len(etats.get('en attente de la relecture explicative', [])), c(etats.get('en attente de la relecture explicative', [])),
           pl(len(etats.get('bloquée', [])), 'bloquée', 'bloquées'), c(etats.get('bloquée', [])), len(minimales), c(minimales)),
        '- **Références** : %d fiches sur %d en ont (%d références distinctes, comptées par DOI ou URL : %s) ; sans référence : %s.'
        % (len(avec_refs), n, len(distinctes), ', '.join('%d %s' % (v, k) for k, v in sorted(statuts.items())), c(sans_refs)),
        '- **Relecture explicative en attente** (`a_relire` ou `a_reconfirmer` non vides), bloquées comprises : %s (%s).' % (pl(len(attente), 'fiche', 'fiches'), c(attente)),
        '- **Sans aucun exemplaire** : %s (%s).' % (pl(len(sans_ex), 'fiche', 'fiches'), c(sans_ex)),
        '- **Fiches publiques (X17, paliers 1 et 2)** : %d fiches publiques (%s) ; publiable : %s ; publiable avec exemplaires incomplets : %s ; pas publiable : %d fiches (détail : `python3 fiches/compte.py --paliers`).'
        % (len(publiques(paliers)), c(publiques(paliers)), c(paliers.get('publiable', [])), c(paliers.get('publiable avec exemplaires incomplets', [])), len(paliers.get('pas publiable', []))),
        ligne_familles(fiches),
        '<!-- compte:fin -->',
    ]
    return '\n'.join(lignes), fiches, ex

def ligne_familles(fiches):
    """Familles de lecture (fiches/familles.yaml, série 12) : types par famille, types sans famille, introductions en attente de relecture."""
    fam = yaml.safe_load(open(os.path.join(FD, 'familles.yaml'), encoding='utf-8'))['familles']
    ranges = [t for f in fam for t in f.get('types') or []]
    sans = sorted(set(fiches) - set(ranges))
    attente = [f['cle'] for f in fam if f.get('a_relire') or f.get('a_valider') or (f.get('relecture_explicative') or {}).get('a_reconfirmer')]
    return '- **Familles de lecture** : %d (%s) ; types sans famille : %s ; introduction en attente de la relecture explicative : %s.' % (
        len(fam), ', '.join('`%s` %d %s' % (f['cle'], len(f.get('types') or []), 'type' if len(f.get('types') or []) <= 1 else 'types') for f in fam),
        ', '.join('`%s`' % x.replace('ppp:', '') for x in sans) or '—', ', '.join('`%s`' % x for x in attente) or '—')

# Fiches publiques (série 10, décision de l'éditeur du projet relayée par la coordination) : les fiches des paliers 1 et 2
# de X17. Le calcul reste fait depuis les fiches ; la liste attendue sert seulement de contrôle : --verifier signale un écart
# (fiche en plus ou en moins) sans corriger le calcul.
# Série 19 : `perceivedSize` revient dans la liste (quatrième cran relu ; sortie en série 17, a_relire non vide, X17).
# Série 21 : `hue` sortie de la liste le temps de reconfirmer son seul exemplaire, ppp-a:pilote-0601 (note et source réécrites
# après le changement d'image du Carré rouge) ; série 22 : 0601 reconfirmée, `hue` revient.
# Série 44 quater : publication libérale (X17, décision de l'éditeur du projet du 2026-10-14) ; neuf fiches du groupe A entrent
# (exemplaires validés par la relecture) ; série 44 quinquies : jointSpacing entre (1603 et 1604 relues) ; textureContrast reste hors de la liste.
# Lot 3 bis : les douze fiches des lots 1 à 3 entrent (assertions des lots 1, 2 et 3 validées par la relecture).
FICHES_PUBLIQUES_ATTENDUES = {'hue', 'lightness', 'lightnessContrast', 'perceivedSize', 'perceptualDensity', 'texture',
                              'textureDirectionality', 'distribution', 'hueContrast', 'hueCount', 'hueRange', 'jointLevelOffset',
                              'jointSpacing', 'perceptualContrast', 'saturation', 'scaleContrast', 'surfaceGloss',
                              'contour', 'lightnessRange', 'saturationRange', 'symmetry', 'translucency', 'curvature',
                              'outlineIndentation', 'negativeSpace', 'localIrregularity', 'partNesting', 'subsurfaceDepth', 'perceivedDepth'}

def publiques(paliers):
    return sorted(paliers.get('publiable', []) + paliers.get('publiable avec exemplaires incomplets', []))

# Noms (spec §13, v2.7 ; étendu en v2.8, série 9) : le dépôt sera public ; aucun prénom ni nom d'agent, ni dans les
# sources publiées ni dans les documents internes. Les noms publics de l'équipe ne paraissent que dans les fichiers
# autorisés ci-dessous (citation, licences, §13 de la spec) et sur la page « Qui sommes-nous ? » (maquette).
import re
# La liste des noms cherchés n'est pas dans ce fichier (publié) : elle est lue dans la variable d'environnement PPP_NOMS
# (motifs séparés par « | »), dans un fichier `.noms-prives` à la racine (un motif par ligne ; ignoré par Git) et, dans le
# dépôt de travail, dans maquette/noms-prives.txt (sections [personnes] et [agents] ; jamais publié). Sans aucune source,
# le contrôle des noms n'est pas exécuté (il est fait avant chaque publication par l'équipe).
def _motifs():
    racine = os.path.normpath(os.path.join(FD, '..'))
    m = os.environ.get('PPP_NOMS', '').split('|')
    f = os.path.join(racine, '.noms-prives')
    if os.path.exists(f):
        m += [l.strip() for l in open(f, encoding='utf-8') if l.strip() and not l.startswith('#')]
    f = os.path.join(racine, 'maquette', 'noms-prives.txt')
    if os.path.exists(f):
        sec = None
        for l in open(f, encoding='utf-8').read().split('\n'):
            if not l.strip() or l.lstrip().startswith('#'): continue
            if re.match(r'^\[\w+\]$', l.strip()): sec = l.strip()[1:-1]; continue
            if sec in ('personnes', 'agents'): m.append(l.strip())
    m = sorted({x.strip() for x in m if x.strip()}, key=len, reverse=True)
    return re.compile(r'(?<![A-Za-zÀ-ÿ])(' + '|'.join(re.escape(x) for x in m) + r')(?![A-Za-zÀ-ÿ])', re.I) if m else None   # « _ », « - », « . », chiffres : séparateurs
NOMS = _motifs()
RACINE = os.path.normpath(os.path.join(FD, '..'))
# Fichiers où les noms publics sont autorisés (liste blanche).
NOMS_AUTORISES = {'CITATION.cff', 'LICENSE', 'LICENSE-CONTENT.md', 'CONTRIBUTORS.md', 'docs/comment-citer.md'}   # compte.py n'en fait plus partie : il ne contient aucun nom
NOMS_SECTION_AUTORISEE = {'PPP_Specification.md': '## 13.',            # autorisés dans cette section seulement
                          'docs/public/README-accueil.md': '## Citer'}    # forme de citation du README public
# Exceptions, non corrigées (documents historiques et domaine de la maquette) : comptées, pas signalées.
NOMS_EXCEPTIONS = (re.compile(r'^docs/crash-test-0\d[^/]*\.md$'), re.compile(r'^docs/guide-structure-ontologie\.md$'),
                   re.compile(r'^maquette/'))
NOMS_EXT = re.compile(r'(\.(md|ya?ml|cff|txt|py|html|json)|^LICENSE[^/]*)$')
NOMS_IGNORES = {'.git', 'local', '__pycache__', 'node_modules'}

def _fichiers_texte():
    for d, sous, fs in os.walk(RACINE):
        sous[:] = [s for s in sous if s not in NOMS_IGNORES]
        for f in fs:
            rel = os.path.relpath(os.path.join(d, f), RACINE).replace(os.sep, '/')
            if f.startswith('._') or not NOMS_EXT.search(f):
                continue
            yield rel

def _section(lignes, titre):
    """Indices (début, fin) de la section de niveau 2 qui commence par `titre`."""
    deb = next((i for i, l in enumerate(lignes) if l.startswith(titre)), None)
    if deb is None:
        return (0, 0)
    fin = next((i for i in range(deb + 1, len(lignes)) if lignes[i].startswith('## ')), len(lignes))
    return (deb, fin)

def noms_publics(avec_exceptions=False):
    """Liste (fichier, ligne, nom) des noms trouvés hors des fichiers et sections autorisés ;
    avec avec_exceptions, renvoie aussi le compte par fichier d'exception."""
    out, exc = [], {}
    if NOMS is None:   # aucune liste de noms disponible (dépôt public sans PPP_NOMS ni .noms-prives) : contrôle non exécuté
        return (out, exc) if avec_exceptions else out
    for rel in sorted(_fichiers_texte()):
        if rel in NOMS_AUTORISES:
            continue
        try:
            lignes = open(os.path.join(RACINE, rel), encoding='utf-8').read().split('\n')
        except (UnicodeDecodeError, OSError):
            continue
        if any(e.search(rel) for e in NOMS_EXCEPTIONS):
            n = sum(len(NOMS.findall(l)) for l in lignes)
            if n:
                exc[rel] = n
            continue
        deb, fin = _section(lignes, NOMS_SECTION_AUTORISEE[rel]) if rel in NOMS_SECTION_AUTORISEE else (0, 0)
        for n, l in enumerate(lignes, 1):
            if deb <= n - 1 < fin:
                continue
            for m in NOMS.finditer(l):
                out.append((rel, n, m.group(1)))
    return (out, exc) if avec_exceptions else out


# --- questions de compétence (spec §6 ; série 46 bis) -------------------------------------------
def cq_de_la_spec():
    """Ids des CQ, lus dans les lignes « - CQn. » de la section 6 de la spec."""
    t = open(os.path.join(os.path.dirname(FD), 'PPP_Specification.md'), encoding='utf-8').read()
    a = t.index('\n## 6. Questions de compétence')
    return set(re.findall(r'^- (CQ\d+[a-z]?)\. ', t[a:t.index('\n## 7.', a)], re.M))

def lire_cq(valeur):
    """CQ nommées par un champ cq_couvertes (« CQ4a–e » vaut CQ4a à CQ4e), et les morceaux qui n'en nomment aucune."""
    ids, reste = [], []
    for m in re.split(r'\s*,\s*', str(valeur or '').strip()):
        r = re.fullmatch(r'CQ(\d+)([a-z])?(?:[–-]([a-z]))?', m)
        if not r:
            if m:
                reste.append(m)
            continue
        n, x, y = r.groups()
        ids += ['CQ%s%s' % (n, chr(c)) for c in range(ord(x), ord(y) + 1)] if x and y else ['CQ%s%s' % (n, x or '')]
    return ids, reste

def cq_fautives(d, connues):
    """Morceaux de cq_couvertes qui ne nomment pas une CQ existante (valeur vide comprise), et CQ en double (série 46 ter)."""
    ids, reste = lire_cq(d.get('cq_couvertes'))
    fautes = reste + [c for c in ids if c not in connues] + ['%s en double' % c for c in sorted({c for c in ids if ids.count(c) > 1})]
    return fautes or ([] if ids else ['(aucune CQ nommée)'])

MARQ_DEBUT, MARQ_FIN = '<!-- compte:debut', '<!-- compte:fin -->'

def decouper_readme(r):
    """Repère le bloc généré par marqueurs en début de ligne (série 48 ter).
    Rend (bloc, fautes) : fautes signale un marqueur absent, en double ou hors début de ligne, et un titre « ## » en double."""
    lignes = r.split('\n')
    fautes = []
    for m in (MARQ_DEBUT, MARQ_FIN):
        n = [k for k, l in enumerate(lignes) if l.startswith(m)]
        if len(n) != 1:
            fautes.append('marqueur %s présent %d fois en début de ligne (1 attendu)' % (m, len(n)))
        for k, l in enumerate(lignes):
            if m in l and not l.startswith(m):
                fautes.append('marqueur %s hors début de ligne, l.%d' % (m, k + 1))
    titres = [l.strip() for l in lignes if l.startswith('## ')]
    for t in sorted({t for t in titres if titres.count(t) > 1}):
        fautes.append('titre « %s » présent %d fois' % (t, titres.count(t)))
    d = [k for k, l in enumerate(lignes) if l.startswith(MARQ_DEBUT)]
    f = [k for k, l in enumerate(lignes) if l.startswith(MARQ_FIN)]
    if len(d) == 1 and len(f) == 1 and d[0] < f[0]:
        return '\n'.join(lignes[d[0]:f[0] + 1]), fautes
    if len(d) == 1 and len(f) == 1:
        fautes.append('marqueur de fin avant le marqueur de début')
    return '', fautes

def ecrire_readme(texte):
    """Remplace le bloc entre les marqueurs ; refuse d'écrire si le README ou le calcul est anormal."""
    p = os.path.join(FD, 'README.md')
    r = open(p, encoding='utf-8').read()
    actuel, fautes = decouper_readme(r)
    if fautes or not actuel or not texte.startswith(MARQ_DEBUT) or not texte.rstrip().endswith(MARQ_FIN):
        print('fiches/README.md : réécriture refusée (%s)' % ('; '.join(fautes) or 'bloc calculé vide ou sans marqueurs'))
        sys.exit(1)
    open(p, 'w', encoding='utf-8').write(r.replace(actuel, texte.rstrip('\n'), 1))
    print('fiches/README.md : bloc de comptes réécrit.')

if __name__ == '__main__':
    texte, fiches, ex = bloc()
    if '--verifier' in sys.argv:
        r = open(os.path.join(FD, 'README.md'), encoding='utf-8').read()
        actuel, fautes = decouper_readme(r)
        ok = not fautes
        for f in fautes:
            print('fiches/README.md : %s' % f)
        if actuel != texte:
            print('fiches/README.md : bloc de comptes périmé ; relancer fiches/compte.py et recopier le bloc.')
            ok = False
        for i, d in sorted(fiches.items()):
            for k, rid, m in appels_manquants(d):
                print('appel [[%s]] manquant ou fautif : %s, %s : « %s »' % (rid, i, k, m))
                ok = False
        for i, d in sorted(fiches.items()):
            for rid, role in roles_hors_liste(d):
                print('rôle de référence hors liste : %s, référence %s : « %s » (rôles admis : %s ; PPP_FicheType.md, spec §9.7 P)'
                      % (i, rid, role, ', '.join(ROLES_REFERENCES)))
                ok = False
        connues = cq_de_la_spec()
        for i, d in sorted(fiches.items()):
            f = cq_fautives(d, connues)
            if f:
                print('cq_couvertes fautif : %s : « %s » ne nomme pas une CQ de la spec §6 (%s)' % (i, d.get('cq_couvertes'), ', '.join(f)))
                ok = False
        calc = set()
        for i, d in fiches.items():
            if palier(d, ex)[0] != 'pas publiable':
                calc.add(i.replace('ppp:', ''))
        if calc != FICHES_PUBLIQUES_ATTENDUES:
            print('fiches publiques : écart avec la liste attendue (%d attendues) : en plus %s ; en moins %s'
                  % (len(FICHES_PUBLIQUES_ATTENDUES), sorted(calc - FICHES_PUBLIQUES_ATTENDUES) or '—', sorted(FICHES_PUBLIQUES_ATTENDUES - calc) or '—'))
            ok = False
        for f, n, nom in noms_publics():
            print('nom hors des fichiers autorisés : %s:%d : %s' % (f, n, nom))
            ok = False
        if not ok:
            sys.exit(1)
        print('fiches/README.md : comptes à jour ; appels [[id]] complets ; cq_couvertes valides ; rôles de références dans la liste fermée ; %d fiches publiques, comme attendu ; aucun nom hors des fichiers autorisés.' % len(FICHES_PUBLIQUES_ATTENDUES))
    elif '--ecrire' in sys.argv:
        ecrire_readme(texte)
    elif '--noms' in sys.argv:
        r, exc = noms_publics(avec_exceptions=True)
        for f, n, nom in r:
            print('%s:%d : %s' % (f, n, nom))
        for f, n in sorted(exc.items()):
            print('exception (non corrigée) : %s : %d' % (f, n))
        print('noms hors des fichiers autorisés : %d (fichiers autorisés : %s ; spec : §13 seulement)'
              % (len(r), ', '.join(sorted(NOMS_AUTORISES))))
        sys.exit(1 if r else 0)
    elif '--paliers' in sys.argv:
        for i, d in sorted(fiches.items()):
            p, r, mention = palier(d, ex)
            print('%-28s %-40s %s' % (i, p, ' ; '.join(r + (['mention : « %s »' % mention] if mention else []))))
    else:
        print(texte)
