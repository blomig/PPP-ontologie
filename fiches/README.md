# `fiches/` — fiches de types PPP (lot pilote)

**État** : lot du 2026-10-11, sur la spec v2.8 : **37 fiches de type actives** (les 19 du lot pilote, sept candidats issus des crash tests, spec 2.3, quatre fiches minimales de 2.5, C6, `elementaryShapeCount`, crash test 03, créée en 2.8, et six fiches Son et Odorat en préparation, série 50) et une fiche réservée hors V1 (`reserve/perceptualIntensity.yaml`, statut `attente`). Statut éditorial de tous les types : `candidat`. Statut épistémique : `non éprouvé`. **Rien n'est validé au sens de la spec** : la structure est proposée par l’équipe. La relecture explicative a relu les champs en langage courant des fiches et des exemplaires (`relecture_explicative`) ; ce qui reste à relire est dans `a_relire` et `a_reconfirmer` de chaque fiche (série 9 : relus et levés pour neuf fiches ; reste `elementaryShapeCount`, nouvelle). Comptes calculés depuis les fiches par `fiches/compte.py` (`python3 fiches/compte.py --verifier` dit si ce bloc est périmé) :

<!-- compte:debut (calculé par fiches/compte.py ; ne pas corriger à la main) -->
- **47 fiches de type actives** ; **46 sans point bloquant** (`bloque_par` vide) : 26 à explicabilité validée par la relecture explicative (`contour`, `curvature`, `distribution`, `hue`, `hueContrast`, `hueCount`, `hueRange`, `jointLevelOffset`, `jointSpacing`, `lightness`, `lightnessContrast`, `lightnessRange`, `localIrregularity`, `negativeSpace`, `outlineIndentation`, `partNesting`, `perceivedDepth`, `perceivedSize`, `perceptualDensity`, `saturation`, `saturationRange`, `subsurfaceDepth`, `symmetry`, `texture`, `textureDirectionality`, `translucency`), 3 au langage courant validé avec exemple concret manquant (`perceptualContrast`, `scaleContrast`, `surfaceGloss`), 17 en attente de la relecture explicative (champs à valider ou à re-confirmer : `astringency`, `bitterness`, `flavourBalance`, `flavourComplexity`, `flavourIntensity`, `hardnessInMouth`, `hardnessToTouch`, `odourCharacter`, `odourIntensity`, `oralPungency`, `oralThickness`, `pitchClarity`, `soundAttack`, `soundDecay`, `soundSharpness`, `tastePersistence`, `textureContrast`) ; **1 bloquée** par un point T ou C (`elementaryShapeCount`) ; dont **4 minimales** (2.5, C6) : `hueCount`, `lightnessRange`, `outlineIndentation`, `saturationRange`.
- **Références** : 47 fiches sur 47 en ont (204 références distinctes, comptées par DOI ou URL : 23 vérifiée sur la source, 181 vérifiée sur résumé ou source secondaire) ; sans référence : —.
- **Relecture explicative en attente** (`a_relire` ou `a_reconfirmer` non vides), bloquées comprises : 18 fiches (`astringency`, `bitterness`, `elementaryShapeCount`, `flavourBalance`, `flavourComplexity`, `flavourIntensity`, `hardnessInMouth`, `hardnessToTouch`, `odourCharacter`, `odourIntensity`, `oralPungency`, `oralThickness`, `pitchClarity`, `soundAttack`, `soundDecay`, `soundSharpness`, `tastePersistence`, `textureContrast`).
- **Sans aucun exemplaire** : 17 fiches (`astringency`, `bitterness`, `elementaryShapeCount`, `flavourBalance`, `flavourComplexity`, `flavourIntensity`, `hardnessInMouth`, `hardnessToTouch`, `odourCharacter`, `odourIntensity`, `oralPungency`, `oralThickness`, `pitchClarity`, `soundAttack`, `soundDecay`, `soundSharpness`, `tastePersistence`).
- **Fiches publiques (X17, paliers 1 et 2)** : 29 fiches publiques (`contour`, `curvature`, `distribution`, `hue`, `hueContrast`, `hueCount`, `hueRange`, `jointLevelOffset`, `jointSpacing`, `lightness`, `lightnessContrast`, `lightnessRange`, `localIrregularity`, `negativeSpace`, `outlineIndentation`, `partNesting`, `perceivedDepth`, `perceivedSize`, `perceptualContrast`, `perceptualDensity`, `saturation`, `saturationRange`, `scaleContrast`, `subsurfaceDepth`, `surfaceGloss`, `symmetry`, `texture`, `textureDirectionality`, `translucency`) ; publiable : `contour`, `curvature`, `distribution`, `hue`, `hueContrast`, `hueCount`, `hueRange`, `jointSpacing`, `lightness`, `lightnessContrast`, `lightnessRange`, `localIrregularity`, `negativeSpace`, `outlineIndentation`, `partNesting`, `perceivedDepth`, `perceptualContrast`, `saturation`, `saturationRange`, `scaleContrast`, `subsurfaceDepth`, `surfaceGloss`, `symmetry`, `translucency` ; publiable avec exemplaires incomplets : `jointLevelOffset`, `perceivedSize`, `perceptualDensity`, `texture`, `textureDirectionality` ; pas publiable : 18 fiches (détail : `python3 fiches/compte.py --paliers`).
- **Familles de lecture** : 8 (`forme` 11 types, `couleur` 9 types, `matiere` 7 types, `organisation` 10 types, `toucher` 8 types, `son` 4 types, `odorat` 2 types, `gout` 9 types) ; types sans famille : — ; introduction en attente de la relecture explicative : `gout`.
<!-- compte:fin -->

**Aucune fiche n’est « rédigée » au sens de T12** (X12 : un exemplaire par région, sur deux régimes de perception ; calcul et manques plus bas). Les points ouverts sont dans `QUESTIONS-A-TRANCHER.md` (T1–T38) et `docs/questions-crash-tests.md` (C1–C25). Aucun accord n'est déclaré.

## Contenu

| Fichier | Rôle |
|---|---|
| `<id sans préfixe>.yaml` | une fiche de type active par fichier, au format de `PPP_FicheType.md` (spec §12, X5) ; YAML pur |
| `reserve/` | fiches de types passés en `attente` (spec §9.9), gardées pour trace, hors liste active et non tenues à jour |
| `familles.yaml` | registre des familles de lecture (spec §9.7 L, X9) : clé, labels, introduction, appartenance |
| `exemplaires.yaml` | objets publics, épisode et assertions proposés comme exemplaires (spec §9.3, §9.7 G) |
| `compte.py` | calcule les comptes du README (états, références, exemplaires, paliers de T35) depuis les fiches ; `--verifier` contrôle le bloc du README, `--paliers` détaille T35 |
| `QUESTIONS-A-TRANCHER.md` | décisions demandées à l’éditeur du projet (T1–T38), avec position de travail ; ce qui est tranché dans le cadre de la spec y est marqué |

**Champs de travail** (hors patron, à retirer une fois la fiche validée) :
- `a_relire` : champs préremplis, à vérifier en relecture explicative (clé nommée `a_valider_par_la_relecture` jusqu’à la série 8) ;
- `relecture_explicative` (clé nommée `valide_par_la_relecture` jusqu’à la série 8) : relecture explicative, avec `date` (AAAA-MM-JJ) et `champs` (liste des champs relus et corrigés en langage courant). Ces champs ne sont plus réécrits par l’équipe ; une relecture n'est ni une épreuve ni un changement de statut éditorial ;
- `manques` : ce qui manque à la fiche ;
- `source_de_la_fiche` : d'où vient la fiche ;
- `statut_note` ;
- `note_joint` ;
- `dimension_comparee_regle` ;
- `meme_echelle_que` ;
- `avertissement_label` (contour, T18), `note_categories` (teinte, T6), `note_reference` (taille perçue, T8), `note_dimension` (contraste d'échelle, T8) ;
- `note_conditions` (v2.3.1) : pourquoi ces facettes sont critiques, et ce qui ne l'est que pour une modalité (T22) ;
- `note_echelle` (éventail des teintes, T31), `note_porteur` (courbure, T30), `note_base` (emboîtement, T25) (v2.3.2) ;
- `bloque_par` (v2.3.1) : points T ou C ouverts qui empêchent de finir la fiche ; vide si rien ne bloque ;
- `a_reconfirmer` (dans `relecture_explicative` d'une fiche ou de `exemplaires.yaml` ; `champ`, `avant`, `apres`, `raison`) : phrase validée puis corrigée au minimum par l’équipe, à re-confirmer par la relecture explicative.

Ils préfigurent le calcul « rédigée / minimale » (T12).

**Champs du patron ajoutés en 2.4** (spec §0.1 point 7, §9.7 P, X15 ; exigence de l’éditeur du projet sur les sources) : `references_statut`, `references` (citation, DOI ou URL, rôle, statut de vérification, date, ce qui a été vu, ce que PPP en reprend et n'en reprend pas) et `etat_de_l_art` (renvoi à `docs/bibliographie-par-type.md`). Les 30 fiches les ont ; le compte des références est dans le bloc calculé en tête (`fiches/compte.py`) ; `perceptualContrast` et `scaleContrast` ont des sources depuis la série 7 (résumés lus). En 2.6, le texte appelle chaque référence par `[[id]]` (spec §9.7 P, point 4 bis) et le renvoi au groupe est dans `etat_de_l_art_renvoi` (`docs/bibliographie-par-type.md#groupe-…`). Dans `alignements_externes`, `reference_id` renvoie à l'entrée `tamura1978`. Point ouvert : T32 (affichage des sources) ; T33 (attribution OQLF de l'avertissement de la brillance) est corrigé et re-confirmé par la relecture explicative.

**Champ du patron ajouté en 2.3** : `conditions_critiques` (spec §9.7 H, A5) : facettes du régime de perception dont la région dépend fortement ; une facette critique `unknown` impose « non tranché ». Rempli en 2.3.1 là où il a un sens ; absent de `distribution`, `negativeSpace`, `scaleContrast` et `perceptualContrast` (aucune facette ne s'y impose ; pour le contraste général, ce sont celles de la dimension comparée).

**Champ du patron ajouté en 2.2.3** : `alignements_externes` (spec §9.7 O) : rapprochement avec une classification publiée (`skos:closeMatch` ou `skos:relatedMatch`, référence vérifiée). Utilisé dans `texture`, `textureDirectionality`, `localIrregularity`, `lightnessContrast` (Tamura, Mori et Yamawaki 1978, T1).

## Avancement

États (2.3.2, reformulés en série 6, partie 7) : **explicabilité validée par la relecture explicative** = tous les champs du patron remplis, langage courant validé par la relecture explicative (elle juge que la fiche s’explique à un lecteur), `bloque_par` vide ; des champs ajoutés depuis peuvent rester dans `a_relire`, et des points T non bloquants rester ouverts (colonne de droite). Ce n’est **pas** l’état « rédigée » de X12 (T12) : voir « Fiche rédigée ou minimale » ci-dessous. **langage courant validé ; exemple concret manquant** = comme la précédente (champs remplis, langage courant validé, `bloque_par` vide), mais la relecture explicative juge que la fiche ne s’explique pas sans un exemple concret, qui reste à trouver (`manques`). **en attente de la relecture explicative** (série 7, calculé par `fiches/compte.py`) = `bloque_par` vide, mais des champs attendent sa validation ou sa re-confirmation (`a_relire` ou `a_reconfirmer` non vides) ; cet état passe avant les deux précédents : une fiche dont des phrases changées attendent la relecture explicative n’a plus son explicabilité validée. **bloquée (T… / C…)** = langage courant validé, structure remplie aussi loin que possible, un point ouvert empêche de la finir. **minimale** = l’une des quatre fiches créées en 2.5 comme « fiches minimales » à partir des crash tests 01 et 02 (C6) : langage courant, état de l’art et références validés par la relecture explicative (série 6) ; champs du patron remplis (vérifié : rien n’y manque par rapport aux autres fiches) ; aucun exemplaire ; et chacune était bloquée par un point C ou T à sa création (`lightnessRange` : C7 ; `saturationRange` : C7, C25 ; `hueCount` : T6, C22, levés en 2.6 ; `outlineIndentation` : C19, T14). Par les champs, rien ne les distingue d’une autre fiche sans exemplaire : « minimale » dit ici leur origine (C6), pas un manque de plus ; ce n’est pas la « fiche minimale » de X12 (toutes les fiches le sont aujourd’hui, voir plus bas). Plus aucune fiche n'est « préremplie ».

| Type | Patron / strate | Familles | État | Conditions critiques | Exemplaires | Ce qui manque |
|---|---|---|---|---|---|---|
| `ppp:texture` | P1 / formel | matière | **explicabilité validée par la relecture explicative** (pilote) | distance | `smooth` ×2, `medium` ×2 (0105 passe de `coarse` à `medium` en 2.5, T24) | `fine`, `coarse` ; exemplaires tactiles ; T2 (« grain » : label alternatif, T1, 2.5) |
| `ppp:perceptualDensity` | P1 / semi-formel | organisation | **explicabilité validée par la relecture explicative** (pilote) | distance | `sparse` ×1, `dense` ×1 | `uniform`, `moderate`, `veryDense` |
| `ppp:perceptualContrast` | P2 / semi-formel | organisation | **langage courant validé ; exemple concret manquant** (série 6) ; labels « faible / modéré / évident / maximal » (T3, 2.5) ; question et `nanay` re-confirmées par la relecture explicative (série 6) ; sources trouvées en 2.6 (Peli 1990, Haun et Peli 2013 ; état de l’art re-confirmé en série 9) ; labels EN des régions (série 29, validés en série 31) | (celles de la dimension comparée) | — (0301 retirée, T24) | toutes les régions |
| `ppp:lightnessContrast` | P2 / semi-formel | couleur, organisation | **explicabilité validée par la relecture explicative** (pilote) ; labels T3 (2.5) ; question re-confirmée par la relecture explicative (série 6) | presentation | `weak` ×2, `strong` ×1 | `moderate`, `marked` |
| `ppp:hueContrast` | P2 / semi-formel | couleur | **explicabilité validée par la relecture explicative** ; labels T3 (2.5) ; question et contre-exemple re-confirmés par la relecture explicative (série 6) ; `note_cercle` et repères recalculés sur le cercle à six teintes (T6, 2.6), re-confirmés (série 9) ; labels EN des régions (série 29, validés en série 31) | presentation | — | exemplaires |
| `ppp:textureContrast` | P2 / semi-formel | matière | **explicabilité validée par la relecture explicative** ; labels T3 (2.5) ; question re-confirmée par la relecture explicative (série 6) ; labels EN des régions (série 29, validés en série 31) | distance | — | exemplaires |
| `ppp:scaleContrast` | P2 / semi-formel | forme | **langage courant validé ; exemple concret manquant** (série 6) ; labels propres « tailles voisines / nettement différentes / très différentes / sans commune mesure » (T34, 2.6, validés en série 9) ; sources trouvées en 2.6 (Girgus et al. 1972, de Fockert et al. 2007, Mruczek et al. 2017 ; état de l’art re-confirmé, série 9) ; labels EN des régions générales (série 29, validés en série 31) | — | — | exemplaires |
| `ppp:contour` (« netteté du bord ») | P1 / formel | forme | **bloquée (T7)** | distance | — | exemplaires ; label EN |
| `ppp:perceivedSize` | P1 / formel | forme | **explicabilité validée par la relecture explicative** (quatrième cran `fingertipSized` « plus petit que le bout du doigt », séries 17 et 18, T8 ; relu en série 19) | presentation, distance | `beyondBody` ×1 (2.3.1) | `fingertipSized`, `handSized`, `bodySized` |
| `ppp:symmetry` | P1 gestalt / semi-formel | forme, organisation | **bloquée (T9)** | angle | — | exemplaires |
| `ppp:jointSpacing` | P1 / semi-formel | forme, organisation | **explicabilité validée par la relecture explicative** | distance | — | exemplaires |
| `ppp:jointLevelOffset` | P1 / semi-formel | forme, organisation | **explicabilité validée par la relecture explicative** ; série 29 : `conditions_critiques` et `note_conditions` revus (T22), validés en série 31 | — (`angle` en note, à la vue seulement : T22, série 29) | — | exemplaires |
| `ppp:distribution` | P1 gestalt / semi-formel | organisation | **explicabilité validée par la relecture explicative** ; `scattered` « aléatoire » (T21, 2.5) ; question et `nanay` re-confirmées par la relecture explicative (série 6) | — | — | exemplaires |
| `ppp:lightness` | P1 / formel | couleur | **explicabilité validée par la relecture explicative** | presentation | `veryDark` ×1 (2.3.1) | autres régions |
| `ppp:hue` | P1 / formel | couleur | **explicabilité validée par la relecture explicative** ; T6 tranché par l’éditeur du projet (2.6 : six teintes, brun = orange, rose = rouge, gris non applicable) ; `note_categories` re-confirmée (série 9) | presentation | `red` ×1 (2.3.1) | autres catégories ; exemplaires de brun et de rose |
| `ppp:saturation` | P1 / formel | couleur | **explicabilité validée par la relecture explicative** | presentation | — | exemplaires |
| `ppp:localIrregularity` | P1 / semi-formel | matière | **bloquée (T11)** | distance | — | exemplaires |
| `ppp:negativeSpace` | P1 gestalt / semi-formel | organisation | **bloquée (T11)** | — | — | exemplaires |
| `ppp:textureDirectionality` | P1 / semi-formel | matière | **explicabilité validée par la relecture explicative** ; limitée aux reliefs (T26) | distance | `oriented` ×1 (2.3.1), `nonOriented` ×1 (2.3.2, remplace 0502 retirée, T24) | `partlyOriented` ; *line-likeness* (T1) |
| `ppp:translucency` (« transparence », 2.6) | P1 / formel | matière | **bloquée (C4)** ; label canonique « transparence » (T28, décision de l’éditeur du projet, 2.6), « vue à travers » en alternatif ; avertissement et `note_conditions` re-confirmés (série 9) | lumiere, presentation | — | exemplaires |
| `ppp:surfaceGloss` | P1 / formel | matière | **langage courant validé ; exemple concret manquant** (série 6) ; labels « mat / satiné / brillant / miroir » (T29, 2.5) ; avertissement corrigé (T33) et re-confirmé par la relecture explicative ; `identite` et `note_conditions` re-confirmés (« transparence », T28 ; série 9) | lumiere, angle | — | exemplaires |
| `ppp:curvature` | P1 / formel | forme | **bloquée (T30)** ; jugement local ; série 29 : `conditions_critiques` et `bloque_par` revus (T22), validés en série 31 ; série 34 : `angle` et `distance` de nouveau critiques (T22, option (b)), validés en série 35 ; plus rien à relire | angle, distance | — | exemplaires |
| `ppp:partNesting` | P1 gestalt / semi-formel | organisation, forme | **bloquée (T14, C4, T25)** ; base `ppp:contour` (2.3.2) | distance | — | exemplaires |
| `ppp:hueRange` | P1 gestalt / semi-formel | couleur | **explicabilité validée par la relecture explicative** ; T6 tranché (2.6) ; `note_echelle` (2.3.2, complétée en 2.6) et `etat_de_l_art` re-confirmés (série 9) | presentation, distance | — | exemplaires |
| `ppp:perceivedDepth` (« étagement en plans », 2.3.2) | P1 / formel (à vérifier) | forme, organisation | **bloquée (C4, T25)** ; label EN *layering into planes* (série 29, validé en série 31) | presentation, distance, angle | — | exemplaires ; strate ; label |
| `ppp:subsurfaceDepth` | P1 / semi-formel | matière | **bloquée (C4 point 4)** ; matière opaque = « en surface » (2.3.2) ; contre-exemple, `identite`, `note_conditions` re-confirmés (série 9) ; label EN *depth within the material* (série 29, validé en série 31) | lumiere, angle | — | exemplaires |
| `ppp:lightnessRange` (2.5) | P1 gestalt / semi-formel | couleur | **minimale** (C6) ; bloquée (C7) | presentation, lumiere, distance | — | exemplaires ; C7 |
| `ppp:saturationRange` (2.5) | P1 gestalt / semi-formel | couleur | **minimale** (C6) ; bloquée (C7, C25) | presentation, lumiere | — | exemplaires ; C7, C25 |
| `ppp:hueCount` (2.5) | P1 gestalt / semi-formel | couleur | **minimale** (C6) ; aucun blocage (T6 tranché, C22 levé, 2.6) ; `note_categories` validée (série 9) ; label EN *number of hues* (série 29, validé en série 31) | presentation, distance | — | exemplaires |
| `ppp:outlineIndentation` (2.5) | P1 gestalt / semi-formel | forme | **minimale** (C6) ; bloquée (C19, T14) | angle, distance | — | exemplaires ; base (tracé sans type) |
| `ppp:elementaryShapeCount` (2.8) | P1 gestalt / semi-formel | forme | **bloquée (T37, questions 1, 4, 5, 6)** ; candidat créé en série 9 (crash test 03) ; formes répétées et percements comptent (T37) ; champs validés par la relecture explicative (séries 15 à 17) (E3 validé en série 16 ; base à revoir, T37, question 6 : la compléter ou n’en déclarer aucune) | distance, angle, presentation | — | exemplaires ; répertoire des formes simples ; seuils et tolérance de l’épreuve |

## Fiche rédigée ou minimale (calcul de X12, T12)

**Aucune fiche n’est encore « rédigée » au sens de T12.** X12 calcule l’état sur les champs : une fiche est rédigée si elle a une définition, une question attentionnelle, un contre-exemple, des régions avec repères, **au moins un exemplaire par région** sur au moins deux régimes de perception (E5), et des énoncés E1 et E4 déclarés ; sinon elle est minimale (et s’affichera grisée). Calcul du 2026-10-10 (série 6, partie 7), sur les assertions non retirées de `exemplaires.yaml` : toutes les fiches ont définition, question, contre-exemple et repères ; **aucune n’a un exemplaire dans chaque région** ; et tous les exemplaires sont des photos vues à l’écran (neuf épisodes, présentation `screen`) : aucune fiche n’a d’exemplaires sur deux régimes de perception. Toutes les fiches sont donc minimales au sens du calcul, y compris celles dont l’explicabilité est validée.

| Type | Régions avec exemplaire | Régions sans exemplaire | Autre manque |
|---|---|---|---|
| `ppp:contour` | 0 / 3 | `sharp`, `gradual`, `blurred` | — |
| `ppp:curvature` | 0 / 3 | `straight`, `slightlyCurved`, `stronglyCurved` | — |
| `ppp:distribution` | 0 / 3 | `clustered`, `scattered`, `regular` | — |
| `ppp:elementaryShapeCount` | 0 / 4 | `oneShape`, `fewShapes`, `manyShapes`, `beyondCount` | — |
| `ppp:hue` | 1 / 6 | `orange`, `yellow`, `green`, `blue`, `purple` | — |
| `ppp:hueContrast` | 0 / 4 | `weak`, `moderate`, `marked`, `strong` | — |
| `ppp:hueCount` | 0 / 3 | `oneHue`, `twoOrThreeHues`, `fourOrMoreHues` | — |
| `ppp:hueRange` | 0 / 3 | `singleHue`, `neighbouringHues`, `distantHues` | — |
| `ppp:jointLevelOffset` | 0 / 3 | `flush`, `slight`, `marked` | — |
| `ppp:jointSpacing` | 0 / 3 | `closed`, `narrow`, `wide` | — |
| `ppp:lightness` | 1 / 5 | `dark`, `mid`, `light`, `veryLight` | — |
| `ppp:lightnessContrast` | 2 / 4 | `moderate`, `marked` | — |
| `ppp:lightnessRange` | 0 / 3 | `singleLightness`, `closeLightnesses`, `distantLightnesses` | — |
| `ppp:localIrregularity` | 0 / 3 | `none`, `slight`, `marked` | — |
| `ppp:negativeSpace` | 0 / 3 | `none`, `slight`, `marked` | — |
| `ppp:outlineIndentation` | 0 / 3 | `unindented`, `indented`, `deeplyIndented` | — |
| `ppp:partNesting` | 0 / 3 | `oneLevel`, `twoLevels`, `threeOrMoreLevels` | — |
| `ppp:perceivedDepth` | 0 / 3 | `flat`, `fewPlanes`, `manyPlanes` | — |
| `ppp:perceivedSize` | 1 / 4 | `fingertipSized`, `handSized`, `bodySized` | — |
| `ppp:perceptualContrast` | 0 / 4 | `weak`, `moderate`, `marked`, `strong` | E1, E4 non déclarés (épreuve propre à chaque spécialisé, §9.7 B) |
| `ppp:perceptualDensity` | 2 / 5 | `uniform`, `moderate`, `veryDense` | — |
| `ppp:saturation` | 0 / 4 | `neutral`, `low`, `medium`, `high` | — |
| `ppp:saturationRange` | 0 / 3 | `singleSaturation`, `closeSaturations`, `distantSaturations` | — |
| `ppp:scaleContrast` | 0 / 4 | `weak`, `moderate`, `marked`, `strong` | — |
| `ppp:subsurfaceDepth` | 0 / 3 | `atSurface`, `slightlyInside`, `farInside` | — |
| `ppp:surfaceGloss` | 0 / 4 | `matte`, `satin`, `lustrous`, `mirror` | — |
| `ppp:symmetry` | 0 / 3 | `asymmetric`, `nearSymmetric`, `symmetric` | — |
| `ppp:texture` | 2 / 4 | `fine`, `coarse` | — |
| `ppp:textureContrast` | 0 / 4 | `weak`, `moderate`, `marked`, `strong` | — |
| `ppp:textureDirectionality` | 2 / 3 | `partlyOriented` | — |
| `ppp:translucency` | 0 / 3 | `opaque`, `translucent`, `transparent` | — |

Manque commun à toutes : des exemplaires sur un second régime de perception (en main, en vrai, sous une autre lumière ; E5).

**Hors lot (V1)** : types `attente` (saillance, distributions d'attention, régime d'exploration, intensité perceptive : spec §9.9) et `ppp:assemblyMode` (`déprécié`).

**Note sur le joint (B13).** Le contraste de couleur au joint n'a pas de fiche. C'est une assertion de contraste de clarté ou de teinte, dont les deux termes sont les parties qui se rejoignent. Une note l'explique dans `lightnessContrast.yaml` (champ `note_joint`), et les fiches du joint le rappellent dans leur contre-exemple.

## Règles suivies

- Ids : uniquement ceux de l'annexe A de la spec (A12). `ppp:textureDirectionality` y est entré en 2.2.3, les sept candidats des crash tests en 2.3. `ppp:contourContinuity` est inscrit à l'annexe A en série 48 bis (candidat réservé, sans fiche ; T7 décidé) ; aucune fiche ne le cite. Aucune fiche active ne cite un id en `attente`.
- A9 : chaque semi-formel déclare une base qui atteint un formel. Une exception : `ppp:perceptualContrast`, dont la base est la dimension comparée (§9.7 B). (L'intensité, non conforme, est passée en `attente`, T10.)
- A2 : les régions sont des valeurs de l'espace du type, jamais des types. Aucun label de région ne reprend un label de type (« grain », label alternatif de la texture depuis 2.5, n'est le label d'aucune région, T1).
- Exemplaires : objets publics uniquement (Q12), pages vérifiées le 2026-10-10 (dix-huit assertions sur neuf objets en 2.3.2, dont quatre retirées : 0201, 0103, 0301, 0502). Pour une photo, `distance` est celle de la prise de vue, estimée d'après le cadrage si besoin (spec §9.7 H règle 7, T22). Aucun exemplaire ne porte sur un type dont une facette critique est `unknown` dans l'épisode (A5). Un épisode par objet (A5) ; une assertion retirée garde son id (`withdrawn: oui`), qui n'est pas réutilisé. Licence et auteur sont repris tels qu'affichés. Droits **à confirmer par l’éditeur du projet (Q15)**. Aucun objet confidentiel.
- Crédits (2.5, X16, Q15) : chaque objet porte un `credit` (auteur, licence, source, url, date_verification, mention_requise), relevé par l'API de Wikimedia Commons et celle du Met le 2026-10-10. Règle d'usage (Q15, décision de l’éditeur du projet, 2.6) : `usage` `image_reproduite` (les neuf objets, crédit complet ; la page de titre de Moby-Dick depuis la série 17, les trois Malévitch depuis la série 20) ou `lien_seulement` avec `lien_externe` (aucun objet depuis la série 20) ; règle de la série 20 (Q15, X16) : une image hébergée sur Wikimedia Commons avec licence et balise indiquées est utilisable, le doute sur le pays d’origine (Malévitch : Russie) ne bloque plus, il est noté ; pour une image hors Commons seulement, un doute non levé sur l’un des trois (pays d’origine, UE, États-Unis) vaut lien seulement ; `url_telechargement` et `fichier` (série 20) donnent le fichier original et le nom de stockage ; motif dans `motif_usage` ; vérification des droits du 2026-10-11 : `docs/droits-exemples-2026-10-11.md`.

## Vérification

Les vérifications ont été faites en local, sans fichier versionné : tous les `.yaml` se chargent avec PyYAML ; chaque `ppp:` cité est un id de l'annexe A ; chaque région citée (`ppp:<type>/<clé>`) existe dans la fiche de son type ; les `facettes` coïncident avec `familles.yaml` (tout type actif a une famille) ; chaque `inEpisode` existe et chaque épisode a une seule cible, celle des assertions qui le citent (A5) ; chaque épisode déclare les cinq facettes ; aucun label de région ne coïncide avec un label de type (A2) ; chaque semi-formel atteint un formel par sa base (A9) ; aucune fiche active ne cite un id en `attente`. Depuis 2.4 : chaque fiche a `references_statut`, `references` et `etat_de_l_art` (avec le lien vers son groupe) ; chaque entrée a tous ses champs, un rôle et un statut admis ; aucune entrée « vérifiée » n'est sans DOI ou URL ; chaque `reference_id` d'un alignement existe dans `references`.
