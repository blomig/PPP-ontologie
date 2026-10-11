# Gouvernance publique de PPP

*Document de PPP, spec v2.8 (§13). Rédigé le 2026-10-11, mis à jour en série 9 (dépôt public, formulaires de tickets GitHub). Fait foi avec le §13 de la spécification ; en cas d'écart, la spécification l'emporte. Ce qui n'est pas décidé est marqué « position de travail, à trancher ».*

## 1. Qui décide

| Point | Règle | Statut |
|---|---|---|
| Équipe | deux membres, nommés au §13 de la spécification (noms publics) | décidé (2026-10-11) |
| Éditeur du projet | un des deux membres, nommé au §13 ; arbitrage final | décidé (2026-10-11) |
| Mode de décision | consensus sur le dépôt public, arbitrage final de l'éditeur du projet | décidé (Q10) |
| Instruction | l'équipe est fermée pour l'instant et instruit seule les suggestions et les contestations | décidé (2026-10-11) |
| Délai | tickets reçus et jugés recevables ou non dans la semaine (sept jours à compter de la réception) ; un ticket recevable reste ouvert jusqu'à l'épreuve qui le traite | décidé (2026-10-11 ; formulation corrigée en série 9) |
| Ticket qui demande une épreuve | réponse motivée dans la semaine, qui dit ce qui est ouvert (anomalie, épreuve) ; le ticket reste `recevable` jusqu'à l'issue de l'épreuve. Raisons : une épreuve reproduite ne se fait pas en sept jours ; le visiteur doit savoir sans attendre ce qui est ouvert | position de travail, à trancher |
| Conflit d'intérêts | l'équipe ne tranche pas seule une contestation qui la vise : l'issue épistémique repose sur une épreuve reproduite par des observateurs indépendants (§9.7 N) et le motif est publié avec le ticket. Raisons : une équipe fermée de deux membres serait juge et partie ; l'épreuve reproduite est déjà le critère du programme ; le ticket public rend la décision contrôlable. Qui fait la revue extérieure : à trancher | position de travail, à trancher |
| Rejoindre l'équipe | fermée (décidé) ; pas de procédure d'entrée tant que personne ne la demande ; on contribue par les tickets. Raisons : une procédure sans candidat serait du texte sans usage ; les tickets ouvrent déjà chaque geste à tous | position de travail, à trancher |
| Dépôt et site | dépôt public neuf `PPP-ontologie`, adresse retenue https://github.com/blomig/PPP-ontologie ; site publié par GitHub Pages, adresse retenue https://blomig.github.io/PPP-ontologie (404 sans connexion le 2026-10-11 à 14 h 58, heure de Paris : dépôt non visible à cette date, ce qui ne prouve pas son absence) | décidé (2026-10-11, séries 9 et 10) |
| Adresse de dépôt des tickets | formulaires de tickets GitHub du dépôt public (https://github.com/blomig/PPP-ontologie/issues), un par type ; compte GitHub requis | décidé (2026-10-11, séries 9 et 10) |
| Conversion ticket GitHub → fichier `tickets/` | à la main par l'équipe au jugement de recevabilité ; numéro du fichier = numéro du ticket GitHub (2.1). Raisons : aucun outil à maintenir ; conversion au moment de la lecture | position de travail, à trancher |
| Identifiant pérenne | archive Zenodo du dépôt public, un DOI par *release* GitHub (Zenodo lit `CITATION.cff`). Raisons : procédure documentée et gratuite ; un DOI par version colle à X6 ; demande un dépôt public | position de travail, à trancher |
| Publication du journal des épreuves sur le site | public dans le dépôt (`epreuves/`, un fichier par épreuve) et affiché sur le site : une page du journal, et un renvoi depuis chaque fiche vers ses épreuves (X8) | décidé (2026-10-11, série 10) |
| Licences | contenu CC BY 4.0, code MIT ; pas d'accord de contribution | décidé (Q11) |

**Rôles de travail.** Conception de l'ontologie ; relecture explicative (une fiche s'explique-t-elle à un non-spécialiste, les sources citées sont-elles exactes) ; tests sur objets publics ; design du site ; coordination. Ce sont des fonctions. Les contenus publiés nomment la fonction (« relu en relecture explicative », « décision de l'éditeur du projet »), jamais un prénom ni un nom d'agent. Les noms de l'équipe ne paraissent que sur la page « Qui sommes-nous ? », au §13 de la spécification et dans la citation ; Aucun autre document du dépôt, interne ou publié, ne nomme une personne ni un agent (v2.8) ; `fiches/compte.py --noms` le vérifie sur tout le dépôt (liste blanche : citation, licences, §13 ; exceptions comptées : rapports de crash test, guide de structure, `maquette/`).

## 2. Les tickets

### 2.1 Circuit

Décidé (v2.8) : dépôt public neuf, site publié par GitHub Pages, tickets par les **formulaires de tickets GitHub** (*issue forms*) du dépôt public, un formulaire par type (`.github/ISSUE_TEMPLATE/<nn>-<type>.yml`) ; ouvrir un ticket demande un **compte GitHub**. Modèles : `docs/depot-public/ISSUE_TEMPLATE/`. Sources : GitHub Docs, « Syntax for issue forms », « Syntax for GitHub's form schema », « Configuring issue templates for your repository » (https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms , …/syntax-for-githubs-form-schema , …/configuring-issue-templates-for-your-repository ; consultés le 2026-10-11) : formulaires YAML dans `.github/ISSUE_TEMPLATE`, clés obligatoires `name`, `description`, `body` ; fonction en « public preview », susceptible de changer ; les validations `required` ne s'appliquent que dans un dépôt public ; `config.yml` avec `blank_issues_enabled: false` réserve le ticket vierge aux personnes qui ont un droit d'écriture.

1. Un visiteur ouvre un ticket GitHub par le formulaire du geste (le site renvoie vers ce formulaire, depuis chaque fiche et le pied de page). Le formulaire pose le label du type ; l'équipe ajoute le label `reçu`.
2. *Position de travail, à trancher* (circuit le plus simple) : dans la semaine, l'équipe juge la recevabilité et **convertit à la main** le ticket en fichier `tickets/<nnnn>-<type>.md`, où `<nnnn>` est le numéro du ticket GitHub sur quatre chiffres (unique, jamais réattribué par GitHub) ; `source: github`, `github_issue: <numéro>`. Raisons : aucun outil à écrire ni à maintenir ; la conversion se fait au moment où l'équipe lit déjà le ticket ; le fichier garde la trace si GitHub change. Une conversion automatique (workflow GitHub Actions) est possible plus tard, si le volume le demande.
3. Ticket recevable : fichier en `recevable`, réponse sur le ticket GitHub avec le lien du fichier. Ticket non recevable : fichier en `traité` / `rejeté` avec le motif « contenu minimal manquant : … », et ticket GitHub fermé avec le même motif. L'état `reçu` n'existe que sur GitHub (label), le temps du jugement.
4. L'équipe instruit et décide : `traité`, avec l'issue `accepté` ou `rejeté` et un motif. Une décision qui change la spécification ou une fiche est consignée au changelog ; une épreuve qu'elle demande va au journal des épreuves (section 3).
5. Aucun ticket n'est fermé sans réponse. Un ticket hors sujet est rejeté avec le motif « hors périmètre » et, si possible, un renvoi.

Seul un ticket **recevable** a un effet affiché (un exemplaire ou une fiche peut passer `contesté`, §13) ; un ticket simplement reçu n'a aucun effet.

### 2.2 États

| `etat` | Sens | Champs remplis |
|---|---|---|
| `reçu` | le ticket GitHub est ouvert (label `reçu`) ; le fichier n'existe pas encore (2.1) | `recu_le` (date du ticket GitHub) |
| `recevable` | le contenu minimal du type est présent | `recevable_le` |
| `traité` | l'équipe a décidé | `traite_le`, `issue` (`accepté` ou `rejeté`), `motif` |

### 2.3 Nom et emplacement

- Dossier : `tickets/` à la racine du dépôt (file d'attente unique).
- Nom : `tickets/<nnnn>-<type>.md`, par exemple `tickets/0007-contestation.md`. Le numéro a quatre chiffres, il est unique et jamais réattribué ; c'est le numéro du ticket GitHub (position de travail, 2.1). Le fichier ne change pas de nom quand l'état change (liens stables).
- Le fichier ne contient aucune adresse électronique (le dépôt est public) : un pseudonyme au plus, champ `auteur`, facultatif.

### 2.4 Types et contenu minimal (recevabilité)

Neuf types pour huit gestes (correspondance : spec §13 ; série 12 : « Signaler un problème de formulation » devient deux gestes, comme dans le texte public). **Les quatre premiers du tableau** (`suggestion-type`, `label-charge`, `correction`, `objet-suggere`) **sont ouverts à tous, sans compétence technique** ; les cinq autres demandent le minimum reproductible ou une fiche complète (retenu, série 13 : les formulaires sont prêts ; l'éditeur du projet peut le changer).

| `type` | Geste (§13) | Contenu minimal pour être recevable |
|---|---|---|
| `suggestion-type` | Suggérer un type | un label ; une phrase ; deux exemples (images ou descriptions) ; le type existant le plus proche ; **l'aspect perceptible décrit** ; **pourquoi aucun type existant ne le couvre** ; une formulation **factuelle**, sans jugement de valeur (X13, v2.7). Une suggestion qui redécoupe un aspect couvert est requalifiée en demande de spécialisation ou de révision du type existant (champ `requalifie_en`) |
| `label-charge` | Signaler un mot qui juge ou une mauvaise traduction | le label, la traduction ou la phrase visés (fiche, clé, langue) ; le problème : valence (le mot évalue au lieu de décrire), ambiguïté, homonymie, erreur de traduction ; une proposition, facultative |
| `correction` | Signaler une erreur (erreur de fait) | la fiche ou la page, le champ ou l'`id` visé (par ex. l'`id` d'une référence) ; l'erreur (référence fautive, statut de vérification surévalué, crédit d'image, coquille, lien mort) ; la source qui la montre, si elle existe |
| `objet-suggere` | Suggérer un objet (public) pour les épreuves | nom ; créateur (ou « inconnu ») ; date ou période, ou « inconnue » (« je ne sais pas » dans le formulaire), **admise seulement si la variante identifie l'objet** à elle seule (sinon le ticket n'est pas recevable ; série 11) ; **variante** précise, obligatoire et jamais « inconnue » (libellé public « Quelle version exactement ? » : version, exemplaire, état, édition, ce qui identifie exactement l'objet vu) ; **lien source public** (obligatoire) ; images : lien seulement par défaut, reproduite seulement si licence réellement libre, vérifiée, avec crédit complet (Q15 : `usage`, `lien_externe`) ; conditions de perception de l'observation : régime complet du §9.7 H (`presentation`, `lumiere`, `distance`, `angle`, `duree`, `unknown` si inconnue). Un objet qui n'est pas public n'est pas recevable |
| `contestation` | Contester une assertion ou un énoncé | `cible` : l'identifiant de l'assertion (`ppp-a:…`) ou de l'énoncé (`E1`–`E6` d'une fiche, ou énoncé propre) ; pour un exemplaire : la région proposée à la place ; pour un énoncé : ce que la fiche prédit et ce qui est observé ; le **minimum reproductible** du §13 (objets décrits, régime de perception au vocabulaire du §9.7 H, observateurs, versions, région ou prédiction citée) |
| `assertion-exemplaire` | Ajouter une assertion sur un objet du registre | l'objet (`app:…`, déjà au registre) ; le type ; la région proposée ; les conditions de perception ; une note factuelle ; `doute` si l'on hésite. Contester une assertion existante : type `contestation` |
| `anomalie` | Signaler une anomalie | types visés ; objets ou situations décrits de façon reproductible ; ce que la fiche prédit, ce qui est observé ; minimum reproductible |
| `refutation` | Publier une réfutation | énoncé visé ; protocole et seuil fixés avant l'épreuve (avec la date) ; matériel publiable ou décrit ; résultats bruts |
| `proposition-type` | Proposer un type | fiche de type complète (`PPP_FicheType.md`), avec au moins un énoncé testable et le test de neutralité |

### 2.5 Format du fichier

En-tête YAML entre deux lignes `---`, puis corps Markdown libre (texte du visiteur, puis réponse de l'équipe sous un titre `## Réponse`). Champs communs :

```yaml
id: ticket-0001            # = le numéro du fichier
type: suggestion-type      # suggestion-type | contestation | label-charge | correction | objet-suggere | assertion-exemplaire | anomalie | refutation | proposition-type
etat: reçu                 # reçu | recevable | traité
issue: null                # accepté | rejeté (seulement si etat = traité)
motif: null                # obligatoire si etat = traité
recu_le: "2026-10-12"
recevable_le: null
traite_le: null
source: github             # github (formulaire de ticket du dépôt public) ; valeur `site` réservée à un éventuel formulaire hors GitHub
github_issue: 1            # numéro du ticket GitHub = numéro du fichier (position de travail, à trancher)
auteur: null               # pseudonyme, facultatif ; jamais d'adresse électronique
langue: fr
cible: []                  # ids visés : ppp:<type>, ppp:<type>/<clé> (région), ppp:<type>#E<n> (énoncé n de la fiche), ppp-a:… (assertion), app:… (objet)
version_spec: "2.8"
version_fiche: null        # version de l'ontologie au moment de l'assertion visée (ontologyVersion), si une assertion est visée
liens: []                  # autres tickets, épreuves (epreuves/<nnnn>-…), commits
```

Les exemples ci-dessous sont **fictifs** : ils montrent la forme, pas des tickets reçus (relus en série 12 : version 2.8, vocabulaire des formulaires, image d'un objet suggéré).

**`tickets/0001-suggestion-type.md`**

```markdown
---
id: ticket-0001
type: suggestion-type
etat: recevable
issue: null
motif: null
recu_le: "2026-10-12"
recevable_le: "2026-10-13"
traite_le: null
source: github
github_issue: 1
auteur: null
langue: fr
cible: [ppp:texture]
version_spec: "2.8"
version_fiche: null
liens: []
label: "souplesse au toucher"
phrase: "Combien une surface cède sous la pression des doigts."
exemples:
  - "une éponge et une planche de bois, pressées du bout des doigts"
  - "un coussin de mousse et un coussin de plumes"
type_le_plus_proche: ppp:texture
aspect_decrit: "la déformation d'une surface sous la pression, perçue au toucher"
non_couvert_parce_que: "ppp:texture porte sur le relief de la surface, pas sur ce qu'elle cède sous la main ; aucun type ne porte sur la déformation"
requalifie_en: null        # specialisation | revision (si l'aspect est déjà couvert)
---

Texte du visiteur.

## Réponse

(Réponse de l'équipe, avec la date.)
```

**`tickets/0002-contestation.md`** (contestation d'un exemplaire)

```markdown
---
id: ticket-0002
type: contestation
etat: traité
issue: rejeté
motif: "Le ticket est recevable, mais une seconde observation indépendante classe la dalle dans la même région que l'assertion ; l'assertion est maintenue (détail dans la réponse)."
recu_le: "2026-10-12"
recevable_le: "2026-10-12"
traite_le: "2026-10-18"
source: github
github_issue: 2
auteur: "observatrice-12"
langue: fr
cible: [ppp-a:pilote-0102]
version_spec: "2.8"
version_fiche: "…"
liens: [epreuves/0001-texture.md]
region_proposee: ppp:texture/medium
objets: "la dalle polie de l'assertion, vue sur la page Commons citée, image en grand"
regime: {presentation: screen, lumiere: unknown, distance: room, angle: frontal, duree: exam}   # régime complet (§9.7 H), `unknown` si inconnu
observateurs: {nombre: 1, pseudonymes: ["observatrice-12"]}
versions: {fiche: "…", page: "site du 2026-10-12", materiel: "image Commons, révision vue le 2026-10-12"}
---
```

**`tickets/0003-contestation.md`** (contestation d'un énoncé) : mêmes champs, avec `cible: [ppp:perceptualDensity#E1]`, et à la place de `region_proposee` : `prediction_de_la_fiche` et `observe`.

**`tickets/0004-label-charge.md`**

```markdown
---
id: ticket-0004
type: label-charge
etat: reçu
issue: null
motif: null
recu_le: "2026-10-12"
recevable_le: null
traite_le: null
source: github
github_issue: 4
auteur: null
langue: en
cible: [ppp:scaleContrast/strong]
version_spec: "2.8"
version_fiche: null
liens: []
element_vise: "label anglais propre de la région (labels_regions_propres)"
texte_vise: "vastly different sizes"
probleme: valence            # valence | ambiguite | homonymie | traduction | autre (options du formulaire 02 : « valence (le mot évalue) », « ambiguïté », « homonymie », « erreur de traduction », « autre »)
proposition: null
---
```

**`tickets/0005-correction.md`**

```markdown
---
id: ticket-0005
type: correction
etat: traité
issue: accepté
motif: "Le DOI cité ne correspond pas à l'article ; corrigé, statut de vérification et date mis à jour (§9.7 P), changelog."
recu_le: "2026-10-12"
recevable_le: "2026-10-12"
traite_le: "2026-10-14"
source: github
github_issue: 5
auteur: null
langue: fr
cible: [ppp:texture]
version_spec: "2.8"
version_fiche: null
liens: []
champ_vise: "references.<id>.citation"
erreur: "DOI erroné"
source_de_la_correction: "page de l'éditeur de l'article"
---
```

**`tickets/0006-objet-suggere.md`**

```markdown
---
id: ticket-0006
type: objet-suggere
etat: recevable
issue: null
motif: null
recu_le: "2026-10-12"
recevable_le: "2026-10-13"
traite_le: null
source: github
github_issue: 6
auteur: null
langue: fr
cible: []
version_spec: "2.8"
version_fiche: null
liens: []
objet:
  nom: "« … » (titre de l'œuvre ou nom de l'objet)"
  createur: "inconnu"                 # ou le nom
  date: "vers 1920"                   # date ou période ; ou "inconnue", admise seulement si `variante` identifie l'objet
  variante: "exemplaire du musée X, n° d'inventaire …, état actuel (restauré en …)"   # « Quelle version exactement ? »
  lien_source_public: "https://…"     # obligatoire : page publique de l'objet
  institution: "…"                    # facultatif
images:
  - url: "https://…"                   # un lien, jamais un fichier
    libre_selon_le_visiteur: "je ne sais pas"   # « Savez-vous si elle est libre ? » : oui | je ne sais pas | non (indication, pas une vérification)
    credit:                            # rempli par l'équipe à l'instruction, après sa propre vérification de la licence (Q15)
      auteur: "…"
      licence: "…"
      source: "…"
      date_verification: "2026-10-13"
      mention_requise: "…"
      usage: lien_seulement            # défaut ; image_reproduite seulement si licence réellement libre, vérifiée
      lien_externe: "https://…"
      motif_usage: "…"
conditions_de_perception:              # codes du §9.7 H, écrits d'après les libellés du formulaire (tableau ci-dessous)
  presentation: inSitu                 # « Sur place »
  distance: room                       # « plusieurs mètres », « dans une pièce »
  lumiere: unknown                     # « Je ne sais pas », ou question sans réponse
  angle: varied
  duree: exam                          # régime complet (§9.7 H) : les cinq facettes
remarques: "trois rangées d'arches, les plus petites en haut ; pierre claire"   # facultatif : « Ce que vous remarquez », sans jugement
types_envisages: []                    # rempli par l'équipe à l'instruction (le formulaire ne demande pas de type)
---

Pourquoi cet objet est utile pour une épreuve (texte du visiteur).

## Réponse

(Après instruction : « objet ajouté au registre sous `app:…` (commit …) », ou rejet motivé.)
```

**Du ticket au registre.** Le registre des objets est `fiches/exemplaires.yaml` (gabarit : `PPP_FicheExemplaire.md`). Un ticket n'y écrit jamais : après instruction, l'équipe ajoute l'**objet seul** (id `app:…`, description, créateur, date, variante, lien, crédit), et le commit cite le ticket. Les assertions par type (région, épisode avec ses conditions de perception, `doute`, note) viennent ensuite, de l'équipe ou d'un ticket `assertion-exemplaire` ou `contestation`. **Objets internes** : le dépôt public n'a que le statut public ; un objet interne n'est jamais publié et n'existe pas côté public ; les objets internes vivent hors du dépôt public, et aucun ticket public ne les nomme.

**Formulaire « Suggérer un objet » : libellés et codes** (série 12). Le formulaire n'affiche aucun code : ses libellés sont ceux du texte public (`docs/public/formulaire-objet.md`). À la conversion du ticket en fichier, l'équipe écrit le code de la facette (§9.7 H) d'après le tableau ci-dessous. Une question sans réponse, ou « Je ne sais pas » / « Je ne sais plus », s'écrit `unknown` ; le régime reste complet (cinq facettes). « Quand ? » sans réponse ou « je ne sais pas » s'écrit `date: "inconnue"`, recevable seulement si `variante` (« Quelle version exactement ? ») identifie l'objet. Le formulaire ne demande pas la version de la spécification : la conversion note `version_spec` en cours à la réception.

| Question (champ) | Libellé affiché | Code |
|---|---|---|
| Comment l'avez-vous vu ? (`presentation`) | Sur place · En main · Posé sur une table · Au mur ou en vitrine · À l'écran, en photo · Sur une image imprimée · En le parcourant de l'intérieur, une pièce, un bâtiment · Je ne sais plus | `inSitu` · `inHand` · `tableTop` · `wallOrShowcase` · `screen` · `printedImage` · `walkThrough` · `unknown` |
| À quelle distance ? (`distance`) | Assez près pour le toucher · À moins d'un mètre · Dans la même pièce, à quelques mètres · De loin, à plus de 5 mètres · Je ne sais pas | `contact` · `near` · `room` · `far` · `unknown` |
| Quelle lumière ? (`lumiere`) | Douce et égale · Venant d'un côté, soleil ou lampe · Rasante : elle fait ressortir les reliefs · À contre-jour : la lumière vient de derrière l'objet · Je ne sais pas | `diffuse` · `directional` · `raking` · `backlit` · `unknown` |
| Sous quel angle ? (`angle`) | De face · De biais · Presque à ras de la surface · En tournant autour, ou en le tournant dans les mains · Je ne sais pas | `frontal` · `oblique` · `grazing` · `varied` · `unknown` |
| Combien de temps ? (`duree`) | Un coup d'œil, quelques secondes · Environ une minute · Longtemps, plus de cinq minutes · Je ne sais pas | `glance` · `exam` · `prolonged` · `unknown` |

Les autres champs se reportent tels quels : `nom`, `createur` (« je ne sais pas » → `inconnu`), `date`, `variante`, `lien` (→ `lien_source_public`), `images` et « Savez-vous si elle est libre ? » (indication du visiteur ; l'équipe vérifie la licence elle-même), `remarques`, `pseudonyme` (→ `auteur`).

**`tickets/0007-assertion-exemplaire.md`** : champs communs, plus `objet: app:…`, `type_vise: ppp:…`, `region_proposee: ppp:…/<clé>`, `conditions_de_perception` (comme ci-dessus), `note`, `doute: non`.

Les types `anomalie`, `refutation` et `proposition-type` prennent les mêmes champs communs, plus les champs de leur contenu minimal (tableau 2.4) : `predit`, `observe` et le minimum reproductible pour une anomalie ; `protocole`, `seuil`, `seuil_fixe_le`, `materiel`, `resultats` pour une réfutation (avec un lien vers le journal des épreuves) ; `fiche` (chemin du fichier proposé) pour une proposition de type.

## 3. Le journal des épreuves

**Pourquoi le garder.** Le changelog dit ce qui a changé et pourquoi ; `tickets/` dit ce qui a été signalé et ce qu'on en a fait. Ni l'un ni l'autre ne garde une épreuve elle-même : protocole et seuil fixés avant, objets, observateurs, versions, résultats bruts, conséquence. Sans ce registre, on ne peut pas vérifier qu'un seuil a été fixé avant l'épreuve (§9.7 M, condition 2), ni reproduire une épreuve (§9.7 N). Le terme est donc gardé et défini (spec §13, v2.7).

**Où.** Un fichier par épreuve dans `epreuves/` à la racine du dépôt : `epreuves/<nnnn>-<type-visé>.md` (par exemple `epreuves/0001-texture.md`). Le numéro est unique, jamais réattribué. Le dossier contient aussi `README.md` (le format) et `0000-modele.md` (modèle, qui n'est pas une épreuve) ; modèles du futur dépôt : `docs/depot-public/epreuves/`.

**Affichage** (décidé, série 10). Le journal est affiché sur le site : une **page du journal** liste les épreuves (numéro, nature, types et énoncés visés, seuil et date de fixation, conséquence, lien vers le fichier), et **chaque fiche renvoie à ses épreuves**. Le statut affiché (X8) se vérifie ainsi depuis la fiche comme depuis le journal.

**Règle d'écriture.** La partie « avant » (protocole, seuil, date de fixation, objets, versions) est écrite et commitée **avant** l'épreuve ; on n'y touche plus ensuite. La partie « après » (résultats bruts, conséquence) s'ajoute à la suite. Une épreuve sans seuil fixé avant est notée `exploratoire` : elle informe, elle ne compte pas pour le statut. Les premiers tests sur objets publics (`docs/crash-test-0*.md`) sont de cette sorte.

```yaml
id: epreuve-0001
nature: programme          # programme | exploratoire
types: [ppp:texture]
enonces: [E1]
protocole: "…"
seuil: "…"
seuil_fixe_le: "2026-10-20"   # date du commit de la partie « avant »
objets: [ppp-a:pilote-0102]   # objets publics (Q12)
observateurs: {nombre: 3, pseudonymes: [], independants_de_l_equipe: oui}
versions: {fiche: "…", page: "…", materiel: "…"}
resultats: null               # ajoutés après l'épreuve (données brutes ou lien)
consequence: null             # corroboré | anomalie ouverte | réfutation reproduite (§9.7 N) | aucune (exploratoire)
tickets: [ticket-0002]
```

## 4. Bonnes pratiques des ontologies ouvertes : ce que PPP reprend

Sources lues le 2026-10-11 sur les pages officielles (références complètes : `bibliographie-par-type.md#groupe-gouvernance`).

### OBO Foundry (principes)

Ce que disent les pages lues :
- **P1 Ouverte** : l'ontologie doit être utilisable par tous, sous deux seules contraintes : reconnaître son origine, et ne pas la redistribuer modifiée sous le même nom ou avec les mêmes identifiants.
- **P4 Versionnement** : des procédures documentées ; chaque version est marquée, conservée et publiée ; le contenu d'une version publiée ne change pas.
- **P11 Lieu d'autorité** : une personne est responsable des échanges avec la communauté et veille à ce que chaque retour soit traité.
- **P16 Maintenance** : l'ontologie doit répondre aux demandes de la communauté ; si un point reste controversé, le mainteneur peut l'écarter, ou choisir un point de vue et noter la controverse dans une note d'éditeur.
- **P19 Stabilité des termes** : la définition d'un terme désigne toujours les mêmes choses ; si un changement de définition change ce qu'elle désigne, on crée un terme nouveau avec un nouvel identifiant, et l'ancien peut être rendu obsolète (« should possibly be deprecated »), avec des indications de remplacement.
- **P20 Réactivité** : un dispositif public de suivi des demandes est obligatoire ; on vise une réponse sous 2 à 5 jours ouvrés ; des consignes de contribution sont recommandées ; on ne ferme pas un ticket sans répondre.

| PPP reprend | PPP ne reprend pas (pour l'instant) |
|---|---|
| ouverture avec attribution (CC BY 4.0) ; | identifiants pérennes de type PURL, format OWL publié, réutilisation de la Relations Ontology : PPP n'a ni adresse pérenne ni export OWL à ce jour (§9.8) ; rien n'est inventé ; |
| une personne responsable : l'éditeur du projet ; | la pluralité documentée d'utilisateurs (P9) et le développement collaboratif ouvert (P10) : l'équipe est fermée pour l'instant ; |
| version marquée, changelog, version citée (X6) ; | le délai de 2 à 5 jours ouvrés : PPP s'engage sur une semaine, délai qu'une équipe de deux personnes peut tenir ; |
| stabilité des identifiants et dépréciation avec renvoi (A11), qui disent la même chose que P19 ; | |
| file publique de tickets, modèles de ticket, aucun ticket fermé sans motif ; | |
| controverse notée plutôt que cachée (le statut `contesté`, le champ `doute`). | |

### schema.org (« How we work »)

Ce que dit la page lue :
- les améliorations sont discutées dans le groupe communautaire du W3C, en pratique dans les tickets GitHub du projet ; la meilleure façon de proposer un changement est d'ouvrir un ticket GitHub ;
- les changements sortent par versions nommées, décrites sur la page des versions ; une version de travail (staging) suit le dépôt ;
- une zone « pending » montre des propositions de vocabulaire pas encore acceptées, à utiliser avec prudence ;
- une version candidate est revue par un petit groupe de pilotage, puis publiée si aucune objection n'est levée sous 10 jours ouvrés ; aucune version n'a été publiée sans l'accord unanime de ce groupe ;
- un terme n'est presque jamais supprimé sans être marqué remplacé par un autre (`supersededBy`) ;
- schema.org ne définit aucune propriété obligatoire.

| PPP reprend | PPP ne reprend pas |
|---|---|
| tickets dans le dépôt comme canal principal ; | le groupe de pilotage et la revue de 10 jours : l'équipe a deux membres, l'éditeur du projet arbitre ; |
| versions nommées avec leur journal (changelog) ; | l'absence de champ obligatoire : une fiche PPP a des champs requis, parce qu'un type doit être testable (A1–A12, §9.6) ; |
| propositions visibles mais marquées : un type est `candidat`, et une fiche non publiable est listée « en préparation », sans page (X17) ; tout le dépôt est sous licence, fiches non publiques comprises ; | |
| remplacement plutôt que suppression (A11, dépréciation avec renvoi). | |

### SKOS (W3C)

Ce que disent les documents lus :
- la **SKOS Reference** est une Recommandation du W3C (18 août 2009), produite par le groupe de travail Semantic Web Deployment ; les commentaires vont à une liste publique, et des errata sont publiés à part ;
- le **SKOS Primer** (Note du W3C, 18 août 2009) dit à quoi servent les notes : `skos:historyNote` décrit les changements importants du sens ou de la forme d'un concept, pour les utilisateurs ; `skos:changeNote` documente les changements fins, pour l'administration et la maintenance ; `skos:editorialNote` sert au travail éditorial (choses à faire, mises en garde).

| PPP reprend | PPP ne reprend pas |
|---|---|
| la distinction entre deux historiques : ce que le lecteur doit savoir (changelog public, label ou définition changés : à exporter en `skos:historyNote`) et le suivi fin du travail (champs `a_reconfirmer`, `avant` / `apres` / `raison` des fiches : `skos:changeNote`) ; | le processus formel du W3C (groupe de travail, Recommandation) : PPP n'est pas une norme ; |
| des corrections publiées à part et datées (changelog, tickets `correction`). | l'export SKOS lui-même : prévu par la spec, pas encore fait. |

## 5. Points à trancher (récapitulatif)

Réglé en série 9 (décisions de l'éditeur du projet) : dépôt public neuf, site par GitHub Pages, tickets par formulaires GitHub (compte requis), équipe fermée, délai d'une semaine. Réglé en série 10 : journal des épreuves affiché sur le site, adresses du dépôt public et du site retenues (compte GitHub `blomig`). Reste à trancher (positions de travail ci-dessus, avec leurs raisons) :

1. Conversion des tickets GitHub en fichiers `tickets/` : à la main au jugement de recevabilité, numéro = numéro GitHub (2.1) ; workflow plus tard ou non.
2. Conflit d'intérêts : qui fait la revue extérieure d'une contestation qui vise l'équipe.
3. Rejoindre l'équipe : procédure, le jour où quelqu'un la demande.
4. ~~Journal des épreuves : renvoi depuis chaque fiche ou page à part~~ : réglé en série 10 (page du journal sur le site, et renvoi depuis chaque fiche).
5. Champs `createur`, `date`, `variante` des objets du registre (proposés dans `PPP_FicheExemplaire.md`) : à ajouter à `exemplaires.yaml` (passe à faire, et lecture par la maquette).
6. Délai quand le traitement demande une épreuve : réponse motivée dans la semaine, issue après l'épreuve (position de travail).
7. Identifiant pérenne : archive Zenodo, un DOI par *release* (position) ; DOI à renseigner après la première archive. L'adresse du site est réglée en série 10 (https://blomig.github.io/PPP-ontologie, adresse retenue).
8. ~~Adresse du dépôt public~~ : réglé en série 10 (https://github.com/blomig/PPP-ontologie, adresse retenue ; reportée dans la citation, `CITATION.cff`, `README.md`). Compte GitHub : `blomig`.
