# Fiche de type PPP

Patron unique pour une entrée du **cœur**. Une fiche d’objet (carte d’identité) est autre chose : elle *instancie* ces types par des assertions (spec §9.3).

Choisir **un** patron : P1 Entity–Quality–Value | P2 Relator | P3 Situation.
Les champs marqués — ne s’appliquent pas à tous les patrons.

*v2 (2026-10-08) — ajustement minimal pour la spec 2.0* :
- champs `strate`, `base_dependance`, `enonces_testables`, `remplace_par` ajoutés ;
- sortes alignées sur les patrons ; statut `déprécié` ajouté ;
- les méta-propriétés OntoClean qualifient le type de qualité.

*v2.2 (2026-10-10)* : `dimension_comparee` fixée par un contraste spécialisé, libre pour le général (spec §9.7 B) ; `ce_qui_est_saillant` réservé hors V1 (spec §9.9) ; `facettes` = familles de lecture (spec §9.7 L, X9) ; plus de mode d’assemblage (spec §9.7 A). Aucun nouveau champ.

*v2.8 (2026-10-12, série 34, décisions de l’éditeur du projet)* : champ optionnel `labels_alternatifs_en` (T38 : labels alternatifs anglais, affichés et cherchables sur le site anglais ; pendant de `labels_alternatifs`, en français) ; `conditions_critiques` : `distance` et `angle` déclarables par un type à deux sens quand ils sont critiques à la vue (spec §9.7 H, règle 3, exception ; règle 4 : « sans objet » n’est pas « inconnu »).

*v2.6 (2026-10-11, série 7)* : champ optionnel `labels_regions_propres` d’un contraste spécialisé (spec §9.7 B, T34) ; renvoi de `etat_de_l_art` au format `docs/bibliographie-par-type.md#groupe-…` et appel des références par `[[id]]` (spec §9.7 P) ; usage des images (`usage`, `lien_externe`, spec X16, Q15).

*v2.5 (2026-10-10, série 6)* : « condition de perception » nom canonique, « condition d’observation » en alternatif (spec §9.7 H, C1) ; crédit des images des objets d’exemplaires (`credit`, spec X16, Q15), patron ci-dessous ; « régime de perception » pour une combinaison de facettes.

*v2.4 (2026-10-10, exigence de l’éditeur du projet sur les sources ; spec §9.7 P, X15)* : champs `references_statut`, `references` et `etat_de_l_art` ; dans `alignements_externes`, `reference_id` renvoie à une entrée de `references`. Tout emprunt à un travail existant (classification, ontologie, théorie, étude) est cité ; une source non vérifiée est marquée comme telle, jamais présentée comme vérifiée. Règles de validation : chaque entrée a un statut ; une entrée autre que « non vérifiée » a un DOI ou une URL de vérification ; une fiche promue au cœur a au moins une référence autre que « non vérifiée », ou `references_statut` « aucune source trouvée », daté. L’exemple de la densité reçoit ses références.

*v2.3 (2026-10-10, crash tests ; position de travail, révisable par l’éditeur du projet)* : champ optionnel `conditions_critiques` (facettes de la condition de perception dont la région dépend fortement, spec §9.7 H, A5) ; pour `tendsToProduce`, champs `depuis` (région source) et `sous_conditions` (spec §9.2, 7), relation ouverte à tout type P1 ou P2. Le bloc de l’exemple redevient du YAML valide (X5) : `définition` et `contre_exemple` en scalaires repliés (`>-`), texte inchangé. Contenu de l’exemple inchangé (`fiches/perceptualDensity.yaml` fait foi ; `conditions_critiques` y sera décidé en partie 2).

*v2.2.3 (2026-10-10)* : champ optionnel `alignements_externes` (spec §9.7 O) ; exemple de la densité : `separableFrom` `ppp:saturation` (l’intensité passe en `attente`, spec §9.9).

*v2.2.2 (2026-10-10)* : labels FR des régions de la densité « clairsemé / dense / très dense » (décision de l’éditeur du projet, T17) ; exemple réaligné sur la seconde relecture explicative.

*2026-10-10, après la relecture explicative* : exemple de la densité réaligné sur `fiches/perceptualDensity.yaml`, qui fait foi. Aucun champ du patron modifié.

*v2.1.8 (2026-10-08)* : OntoClean en lecture conceptuelle (champ `unite` ajouté) ; `axiomes` à double libellé, conceptuel puis règle de validation (spec §9.8, A5).

*v2.1 (2026-10-08) — tests de design (spec §9.7)* :
- `regions` structurées (clé, rang, sens croissant, repère, exemplaires) ;
- `exemplaires` (ids d’assertions), `statut_epistemique`, `introduit_en` / `modifie_en`, `label_court`, `grandeur_physique_homonyme`, `mode_de_presentation`, `facettes`, `dimension_comparee` (P2 paramétré) ;
- `remplace_par` multivalué ; `voisins_a_ne_pas_confondre` devient la relation `confusableWith` ;
- le bloc `application` sort du fichier (X7) ;
- exemple *densité* refait.

Le bloc doit être du YAML valide (spec §12, X5). Ids : convention X1 (`ppp:` + lowerCamelCase anglais sur le label complet). Tout id cité doit être défini, par une fiche ou par le registre de la spec, Annexe A (A12).

---

## Patron vide

```
id:                 "ppp:"
label_fr:
label_en:
label_court:        # le mot qu’on dit à voix haute, même sens (« densité »)
labels_alternatifs: # jargon d’atelier, marqué comme tel
labels_alternatifs_en: # optionnel (v2.8, T38) : labels alternatifs anglais (anciens labels anglais, termes du métier en anglais)
patron:             P1 | P2 | P3
sorte:              qualité (P1) | relateur (P2) | régime d’épisode (P3)
sous_sorte:         gestalt (qualité d’une configuration, P1 seulement) | —
strate:             formel | semi-formel | —   # deux strates seulement ; — pour P3, l’attentionnel n’est pas une strate (spec §0.3, A9)
base_dependance:    # semi-formel : seule source de dependsOn, vers chaque type listé (formel ou semi-formel) ; ≥ 1 formel, directement ou transitivement
  types:            []
  facteurs_non_perceptuels: []   # [{facteur, lien_perceptible: id d’un type perceptuel de la base}] ; sortes libres (Q2)
facettes:           []   # optionnel, multivalué : familles de lecture des dérivés (clés du registre des familles, spec §9.7 L, X9) ; un type peut être dans plusieurs

définition:         (une phrase, sans jugement ; passe le test de neutralité, spec §0.4)
question_attentionnelle:
contre_exemple:
grandeur_physique_homonyme:   # grandeur mesurée portant le même nom, à ne pas confondre (spec §9.7, J)
modalites:          # sens par lesquels le type est décrit et éprouvé : vision | toucher | audition | odorat (série 43) ; chaque assertion en déclare une, l’épisode l’ensemble (spec §9.3, §9.7 H) ; ≠ conditions de perception ; identité intermodale : Q13
mode_de_presentation:  image | séquence | échantillon | protocole   # minimum pour montrer les régions
conditions_critiques: []   # optionnel (v2.3) : facettes du régime de perception dont la région dépend fortement, parmi presentation | lumiere | distance | angle | duree | geste | temperature_objet | production | bruit_de_fond | exposition | air (`production` et `bruit_de_fond` pour un type de l’ouïe seule, `exposition` et `air` pour un type de l’odorat seul : spec §9.7 H, règles 9 et 10, série 43, à relire ; `geste` et `temperature_objet` pour un type au toucher seul : spec §9.7 H, règles 3 et 8 ; `distance` et `angle` restent déclarables par un type à deux sens s’ils sont critiques à la vue : règle 3, exception, série 34) ; une facette critique `unknown` dans l’épisode impose « non tranché » (spec §9.7 H, A5)

porteur:            # P1 : exactement 1. P2 : arité ≥ 2, rôles nommés. P3 : l’épisode.
arité:              # P2
dimension_comparee: # P2 contraste : un spécialisé (ex. ppp:lightnessContrast) fixe ici l’id d’un type P1 ; le général (ppp:perceptualContrast) la laisse vide, chaque assertion déclare alors ppp:comparedDimension (spec §9.7 B)
# ce_qui_est_saillant : réservé hors V1 (spec §9.9), ne pas remplir
condition_NA:       # quand la carte d’identité coche « non applicable » (sans décision de calendrier)

espace_valeurs:
  echelle:          nominale | ordinale | intervalle | ratio   # nominale : régions = catégories
  sens_croissant:   # ordinale : du rang 1 vers le rang n, ce qui augmente
  voisinages:       # nominale : voisinages déclarés, sinon aucune adjacence
  numerique:        non | oui (unité / jauge)
  regions:
    - cle:          # anglais, lowerCamelCase, passe le test de neutralité, jamais réemployée
      label_fr:
      label_en:
      rang:         # ordinale seulement (1 = pôle bas)
      repere:       # une phrase pour se repérer
      exemplaires:  []   # ids d’assertions (≥ 1 par région, ≥ 2 régimes au total)
labels_regions_propres:   # optionnel (v2.6, spec §9.7 B, T34) : P2 spécialisé dont la dimension comparée n’a pas de bout d’échelle ; affichage seulement, les régions restent celles du général
  - cle:            # clé d’une région du général (même clé, même rang)
    label_fr:       # label propre affiché sur la fiche du spécialisé (passe A2 et A10)
    label_en:
    region_generale:  # id de la région du général, ex. ppp:perceptualContrast/weak ; le site peut l’afficher à côté

identite:           # en quoi ce n’est PAS le voisin le plus proche

relations:          # dependsOn n’y figure pas (voir base_dependance) ; symétriques écrites une seule fois
  - type:           integralWith | separableFrom | confusableWith | tendsToProduce
    cible:          "ppp:"   # jamais un id en attente (A12)
    depuis:         # tendsToProduce seulement : clé de la région source de ce type
    sous_conditions: []   # tendsToProduce seulement : facettes et valeurs du régime (ex. lumiere: raking) ; un énoncé testable de structure l’accompagne
    note:
alignements_externes:  # optionnel (spec §9.7 O) : dimension d'une classification publiée rapprochée de ce type
  - relation:       skos:closeMatch | skos:relatedMatch   # jamais skos:exactMatch pour une mesure calculée
    cible:          (nom de la dimension dans la source)
    reference:      (référence vérifiée, DOI ou URL)
    reference_id:   (id d'une entrée de references ci-dessous ; la référence complète et son statut y figurent)
    note:           (nature de la source — mesure, système, catégorie ; ce qu'on en reprend)

references_statut:  renseignées | à renseigner | aucune source trouvée (recherche faite le AAAA-MM-JJ, bases consultées)   # spec §9.7 P
references:         # tout travail existant sur lequel la fiche s'appuie (classification, ontologie, théorie, étude) ; [] si aucune
  - id:             (clé courte, ex. tamura1978)
    citation:       (auteurs, année, titre, support, pages)
    doi_ou_url:     (DOI sous forme https://doi.org/…, ou URL de la notice ou de la page vérifiée)
    role:           fonde | alimente | discute | contraste
    statut_verification: vérifiée sur la source | vérifiée sur résumé ou source secondaire | non vérifiée
    verifie_le:     (AAAA-MM-JJ)
    verifie_sur:    (ce qui a été vu — texte, résumé, métadonnées Crossref, notice de bibliothèque, page de l'éditeur)
    reprend:        (ce que PPP en reprend, en langage courant)
    ne_reprend_pas: (ce que PPP n'en reprend pas)
    note_verification:  # optionnel — affirmation de la fiche que la source vue ne permet pas de confirmer
# Appel dans le texte (v2.6, spec §9.7 P, point 4 bis) : dans etat_de_l_art et les note…, écrire [[id]] juste après la mention en clair
# (« Durgin (1995) [[durgin1995]] ») ; l'id doit exister dans references de la fiche.
etat_de_l_art:      (2 à 5 phrases en langage courant ; références appelées par [[id]] ; finit par le lien docs/bibliographie-par-type.md#groupe-<groupe>)
etat_de_l_art_renvoi: docs/bibliographie-par-type.md#groupe-   # v2.6 : ancre stable du groupe (groupe-texture, groupe-couleur, groupe-forme, groupe-organisation, groupe-matiere, groupe-joint, groupe-etagement, groupe-contrastes)

ontoClean:          # LECTURE CONCEPTUELLE : méta-propriétés du type, dont les instances sont des
                    # qualités (ou relateurs) particulières ; pas de la propriété de l’objet « avoir telle région ».
                    # Dans le modèle machine, ces instances n’existent pas (spec §9.8).
  rigidite:         +R | ~R | -R
  identite_propre:  +I | -I
  unite:            +U | ~U | -U | —   # — : non encore évaluée
  dependance:       +D | -D

axiomes:            # ce qui est toujours vrai du type, avec double libellé (spec §9.8)
  - conceptuel:     # énoncé en langue contrainte, éventuellement sur des instances
    validation:     # traduction en règle sur les assertions (ppp:about, ppp:inRegion, ppp:role…)

nanay:              y prêter attention fait une différence ? (oui, et comment ; formulation neutre)
transfert:          objet conçu | tableau | cuisine/high-tech | échec → application

enonces_testables:  # spec §0.2 : au moins un pour un type du cœur
  - id:             E1 | E2 | E3 | E4 | E5 | E6
    nature:         existence (E1, E4, E5, E6) | structure (E2, E3 ; défaut pour un énoncé propre)   # spec §9.7 F
    enonce:
    statut_epistemique: non éprouvé | corroboré | contesté | réfuté
    epreuve:        # référence publique : versions de la fiche, de la page publiée et du matériel montré

cq_couvertes:       # numéros
statut:             candidat | cœur | application | attente | rejeté | déprécié   # promotion / rétrogradation : spec §9.7 M
statut_epistemique: non éprouvé | corroboré | contesté | réfuté   # dérivé (spec §9.7, F)
introduit_en:       # version
modifie_en:         # [{version, motif, decision}]
remplace_par:       # si déprécié : [{cible: id de type ou de région, motif, decision}]
```

Opérations (`op:`), partitions C-K et lexique d’atelier ne figurent **pas** dans ce fichier. Ils vivent dans des fichiers `app:` / `op:` qui référencent l’id (spec §9.7, K).

## Champs de travail (hors patron, non publiés comme contenu)

Noms de clés fixés en v2.8 (renommés en série 9 ; anciens noms : `valide_par_le_professeur`, `a_valider_par_le_professeur`) :

```
relecture_explicative:        # ce que la relecture explicative a relu
  date: AAAA-MM-JJ
  champs: []                  # champs relus et corrigés en langage courant
  a_reconfirmer: []           # {champ, avant, apres, raison} : phrase relue puis corrigée, à re-confirmer
a_relire: []                  # noms de champs seulement, préremplis par l'équipe, à relire en relecture explicative
remarque: []                  # facultatif : résumés libres des modifications (série 14) ; jamais compté comme un champ
manques: []
bloque_par: []
```

Une nouvelle fiche porte en `a_relire` tous ses champs en langage courant et ses références (`fiches/compte.py` la compte « en attente de la relecture explicative »).

---

## Exemple rempli — Densité perceptive (P1)

*Réaligné le 2026-10-10 sur `fiches/perceptualDensity.yaml`, qui fait foi (définition, question et contre-exemple relus en relecture explicative). Les champs de travail de la fiche (`relecture_explicative`, `manques`…) ne sont pas repris ici. Labels de région « clairsemé / dense / très dense » : décision de l’éditeur du projet, spec 2.2.2 (`fiches/QUESTIONS-A-TRANCHER.md`, T17).*

```
id:                 ppp:perceptualDensity
label_fr:           densité perceptive
label_en:           perceptual density
label_court:        densité
labels_alternatifs: []
patron:             P1
sorte:              qualité
sous_sorte:         —
strate:             semi-formel
base_dependance:
  types:            [ppp:contour, ppp:distribution]   # contour formel ; distribution P1 gestalt semi-formelle, de base ppp:contour
  facteurs_non_perceptuels: []
facettes:           [organisation]

définition: >-
                    Quantité d’éléments ou de détails distincts qu’on perçoit dans un objet ou une zone,
                    rapportée à sa taille : d’aucun élément distinct à des éléments qui couvrent presque tout le fond.
question_attentionnelle: Pour sa taille, l’objet ou la zone contient-il peu ou beaucoup d’éléments distincts ?
contre_exemple: >-
                    Une seule tache rouge très saturée sur un mur blanc attire le regard, mais elle ne fait qu’un
                    élément : le mur compte très peu d’éléments pour sa taille, et ce qui frappe tient à la saturation
                    et au contraste. Un enduit finement granuleux ne montre pas d’éléments distincts : sa texture est
                    fine, mais il ne compte pas pour autant beaucoup d’éléments.
grandeur_physique_homonyme: masse volumique (densité au sens physique), aucune région ne s’en déduit.
modalites:          [vision]   # ajouter `toucher` à `modalites` quand la fiche est décrite et éprouvée au toucher ; second type seulement si l’accord ne passe pas d’un sens à l’autre (Q13)
mode_de_presentation: image

porteur:            un objet d’attention, ou une partie / une zone
arité:              1
condition_NA:       porteur sans étendue perceptible (point, instant isolé).
                    Une surface uniforme est APPLICABLE, en région `uniform`.

espace_valeurs:
  echelle:          ordinale
  sens_croissant:   de `uniform` (rang 1) vers `veryDense` (rang 5), le nombre d’éléments distincts perçus augmente
  numerique:        non   # un rang de nuancier est un attribut d’application, pas une région
  regions:
    - cle: uniform
      label_fr: uniforme
      label_en: uniform
      rang: 1
      repere: aucun élément distinct, variation imperceptible (un mur enduit, un aplat)
      exemplaires: []
    - cle: sparse
      label_fr: clairsemé   # ex-« aéré » (2.2.2, T17)
      label_en: sparse
      rang: 2
      repere: quelques éléments isolés sur un fond qui domine (une page de titre)
      exemplaires: [ppp-a:pilote-0203]   # fiches/exemplaires.yaml
    - cle: moderate
      label_fr: moyen
      label_en: moderate
      rang: 3
      repere: éléments et fond à parts comparables (une page de texte courant)
      exemplaires: []
    - cle: dense
      label_fr: dense       # ex-« chargé » (2.2.2, T17)
      label_en: dense
      rang: 4
      repere: les éléments dominent le fond (un parement de briques à motifs)
      exemplaires: [ppp-a:pilote-0202]   # fiches/exemplaires.yaml
    - cle: veryDense
      label_fr: très dense  # ex-« très chargé » (2.2.2, T17)
      label_en: very dense
      rang: 5
      repere: le fond n’est presque plus perceptible (une mosaïque serrée)
      exemplaires: []

identite:           Quantité d’éléments perçus, pas force d’une couleur (saturation), pas taille des reliefs d’une surface (texture).

relations:
  - type: separableFrom
    cible: ppp:saturation
    note: une zone peut être très saturée et clairsemée (une seule tache saturée sur fond uniforme)
  - type: confusableWith
    cible: ppp:texture
    note: une texture fine peut faire paraître une surface dense ; la texture, c’est la taille des reliefs d’une surface,
          la densité compte des éléments distincts
  - type: confusableWith
    cible: ppp:negativeSpace
    note: l’espace négatif dit si les espaces entre les éléments se lisent comme des formes ;
          une zone peu dense peut en avoir peu ou beaucoup

references_statut:  renseignées
references:
  - id:             durgin1995
    citation:       "Durgin, F. H. (1995). Texture density adaptation and the perceived numerosity and distribution of texture. Journal of Experimental Psychology: Human Perception and Performance, 21(1), 149–169."
    doi_ou_url:     https://doi.org/10.1037/0096-1523.21.1.149
    role:           alimente
    statut_verification: vérifiée sur résumé ou source secondaire
    verifie_le:     "2026-10-10"
    verifie_sur:    métadonnées Crossref et résumé (OpenAlex)
    reprend:        la densité perçue comme dimension distincte du nombre d'éléments et de leur répartition
    ne_reprend_pas: les mesures d'adaptation et les champs de points
etat_de_l_art:      >-
  Durgin (1995) [[durgin1995]] étudie la densité de texture perçue, distinguée de la numérosité et de la répartition des éléments,
  et montre qu'elle s'adapte. La densité au sens physique (masse volumique) est un homonyme. Aucune source trouvée
  ne fixe des régions perçues de densité. Détail : docs/bibliographie-par-type.md#groupe-organisation.
etat_de_l_art_renvoi: docs/bibliographie-par-type.md#groupe-organisation

ontoClean:          # lecture conceptuelle, sur le type ppp:perceptualDensity (instances : densités particulières)
  rigidite:         +R   # toute densité particulière est nécessairement une densité
  identite_propre:  +I   # même porteur + même type (au même instant) ⇒ même densité particulière
                         # machine : même ppp:about + même type + même épisode ⇒ une seule région (CQ20)
  unite:            —    # non encore évaluée (pilote)
  dependance:       +D   # une densité particulière dépend existentiellement de son porteur
                         # machine : toute assertion de ce type a un ppp:about
  # « Être très dense » est une propriété de l’OBJET (il peut changer de région) :
  # ce n’est pas un type PPP mais une région (ppp:perceptualDensity/veryDense) attribuée par une assertion.

axiomes:
  - conceptuel:     Toute qualité particulière de ce type inhère à exactement un porteur.
    validation:     Toute assertion de type ppp:perceptualDensity a exactement un ppp:about.
  - conceptuel:     Les 5 régions sont deux à deux disjointes et totalement ordonnées par rang.
    validation:     Les 5 ppp:Region de l’échelle du type ont des ppp:rank distincts, de 1 à 5 ; une assertion a au plus un ppp:inRegion.
  - conceptuel:     Une région de cet espace n’est pas un sous-type du type.
    validation:     Aucune ppp:Region n’est sujet ou objet de ppp:specializes.

nanay:              Oui — passer de « je regarde la forme » à « je vois combien c’est dense ou clairsemé »
                    modifie la description de l’expérience (place du fond, parcours du regard).
transfert:          objet conçu oui | tableau oui (composition) | cuisine oui (décor vs lisse) |
                    high-tech oui (face clairsemée vs face très dense en informations)

enonces_testables:
  - id: E1
    nature: existence
    enonce: sur 6 à 10 objets publics, accord inter-observateurs à une région près, au-dessus du seuil fixé avant l’épreuve
    statut_epistemique: non éprouvé
    epreuve: null
  - id: E2
    nature: structure
    enonce: on peut faire varier la densité en tenant la saturation constante (une tache saturée sur fond uniforme vs un semis serré de taches de même saturation)
    statut_epistemique: non éprouvé
    epreuve: null
  - id: E4
    nature: existence
    enonce: l’accord ne baisse pas entre observateurs qui aiment et n’aiment pas les objets très denses
    statut_epistemique: non éprouvé
    epreuve: null

cq_couvertes:       CQ1, CQ2, CQ4a–e, CQ12a–e, CQ14, CQ16a, CQ23, CQ24
statut:             candidat
statut_epistemique: non éprouvé
introduit_en:       "2.1"
modifie_en:         ["2.2.2", "2.2.3"]
remplace_par:       []
```

### Ce que la fiche change par rapport à v0.2

v0.2 disait : *« Quantité d’information perceptive par unité de surface ou de temps »* + exemples + relations `Distribution, Niveaux d’échelle, Vide actif`.

Ici on a en plus :
- **ce n’est pas la saturation** (l’intensité, en `attente` depuis la v2.2.3, n’est plus citée) ;
- **échelle ordinale à cinq régions**, avec clé, rang, sens croissant et repère, dont un pôle bas `uniform` montrable ;
- **N/A** réservé à l’absence d’étendue ;
- **séparable de la saturation** ;
- **l’espace négatif n’est pas la région « clairsemé »** ;
- **le type de qualité est rigide (+R)**, l’objet changeant seulement de région ;
- **une base qui passe A9** ;
- **aucune corrélation affichée comme intégralité** (le lien avec les niveaux d’échelle est retiré jusqu’à une épreuve).

C’est ça, la liste rendue utile.

---

## Objet d’exemplaire et crédit de l’image (`fiches/exemplaires.yaml` ; v2.5, spec X16, Q15)

Les exemplaires d’une fiche sont des ids d’assertions ; l’objet et son image sont décrits une fois dans `fiches/exemplaires.yaml`. Une assertion que son auteur juge discutable porte `doute: oui` (v2.6, spec §9.7 G, T35 ; champ éditorial, hors ontologie) ; la raison va dans `note`, qui ne commence plus par « contestable » (tout exemplaire est contestable au sens du §13). Chaque objet ou image porte un `credit`, relevé sur la page de l’image (API Wikimedia Commons, API du musée…) ; une valeur inconnue s’écrit « à renseigner ». **Règle d’usage (v2.6, décision de l’éditeur du projet, Q15 ; spec X16)** : une image réellement libre (Commons sous licence CC, domaine public avéré, Met Open Access) est reproduite avec son crédit complet (`usage: image_reproduite`) ; toute autre image (domaine public « selon le pays », provenance non avérée, licence incertaine) n’est pas copiée : la fiche cite l’objet et pointe vers la page où l’image est en ligne (`usage: lien_seulement`, `lien_externe`) ; `motif_usage` dit pourquoi.

```yaml
objets:
  - id: app:…                 # id d’application, opaque
    description: ""           # ce que l’on voit, d’après la page source
    page_objet: null          # page de l’institution, si vérifiée
    image: ""                 # URL de la page de l’image
    licence_affichee: ""      # licence lue sur la page
    auteur_image: ""
    regime: ""                # sorte d’objet (tableau, objet conçu, matériau exposé…)
    parties: []               # parties nommées (#…) visées par les assertions
    droits: ""                # v2.6 : une ligne propre à l’objet : licence, auteur, usage (ex. « CC BY-SA 2.0, Jim Barton, image reproduite » ; « PD-Art, statut selon le pays, lien seulement ») ; la règle Q15 est dans la spec (X16), pas répétée ici
    credit:                   # v2.5 (X16) : ce que le site affiche dans « Droits et crédits »
      auteur: ""              # auteur de l’image (et de l’œuvre si distinct), tel que la page le donne
      licence: ""             # ex. CC BY-SA 4.0, CC0 1.0, domaine public (selon la page)
      source: ""              # ex. Wikimedia Commons, « Own work » ; geograph.org.uk ; musée
      url: ""                 # page de l’image
      url_telechargement: ""  # facultatif (série 20) : adresse du fichier original (Commons : upload.wikimedia.org), lue par l’API
      fichier: ""             # facultatif (série 20) : nom de fichier de l’image reproduite (identifiant de l’objet sans « app: », .jpg), sans chemin (série 23)
      date_verification: ""   # AAAA-MM-JJ
      mention_requise: ""     # mention exigée par la licence (CC BY-SA : titre, auteur, lien, licence et lien vers la licence, modifications) ; « aucune » pour CC0 ou domaine public
      usage: image_reproduite # v2.6 (Q15) : image_reproduite | lien_seulement
      lien_externe: ""        # lien seulement : page où l’image est en ligne (aucune copie) ; absent si image_reproduite
      motif_usage: ""         # pourquoi ce classement (licence lue, statut avéré ou non, provenance)
```

## Variantes de champs selon le patron

| Champ | P1 Qualité | P2 Relateur | P3 Épisode |
|---|---|---|---|
| porteur | 1 objet / partie / zone | 2+ relata, rôles | l’épisode (observateurs, cible, régime de perception) |
| espace | souvent ordinal | souvent ordinal (contraste) | — en V1 (types de régime réservés, spec §9.9) |
| paramètre | — | `dimension_comparee` : fixée par un spécialisé, libre pour le général (contraste) | — |
| condition_NA | pas de porteur étendu | moins de deux termes distincts (ex. une seule zone homogène) | pas d’observation |
| tendsToProduce | rare | possible, depuis une région | — |
| pertinence | attribuée *dans* un épisode (A6) | idem | l’épisode *porte* la pertinence |

Ne pas remplir les champs P2 sur une fiche P1 « pour faire complet ».

---

## Mini-jeu de reclassement (stock)

Pour chaque nom de v0.2, une seule case. Les noms v0.2 n’ont pas d’id : le résultat est une **table de correspondance** (nom v0.2 → id ou région v2), pas une dépréciation (spec §9.5).

| Verdict | Quand |
|---|---|
| **Type P1** | inhère à un porteur, espace de valeurs |
| **Type P2** | relie ≥ 2 termes (contraste et ses spécialisations, interpénétration) |
| **Type P3** | caractérise un épisode d’attention ; en V1, verdict **Attente** (types attentionnels réservés, spec §9.9) |
| **Gestalt** | organisation d’ensemble d’une configuration : P1 seulement (A7). Si c’est une relation entre parties, c’est un relateur P2, pas une gestalt |
| **Région** | pôle ou étiquette (« symétrie / asymétrie », « focalisée / distribuée » sont des pôles, pas des types) — A2. Les noms de modes d’assemblage (juxtaposition, entrelacement) ne sont ni types ni régions : on décrit le joint par ses qualités (spec §9.7 A) |
| **Condition de perception** (alt. condition d’observation) | paramètre d’épisode, pas qualité d’objet (ex. « luminosité ambiante » v0.2) |
| **Facette** | vue (eidétique / chromatique) — pas une classe |
| **Consigne** | « il faut des centres forts » — hors cœur |
| **Doublon** | même identité qu’un type déjà là |
| **Attente** | pertinent, pas encore d’espace / d’identité stables |
| **Rejet** | jugement, émotion, marque, non ancré perceptuellement, échec au test de neutralité sans redéfinition possible |

---

*Document de travail — à utiliser pour les quatre pilotes, puis pour le reclassement v0.2.*
