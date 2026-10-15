# Couverture des questions de compétence par les fiches

Une question de compétence est une question à laquelle l’ontologie doit savoir répondre (par exemple : où se situe cet objet sur l’échelle d’une qualité ?). Ce tableau dit, pour chacune, quelles fiches disent y répondre. Certaines questions portent sur la manière de noter une observation, pas sur une qualité : aucune fiche ne peut y répondre seule. Les lignes suivent l’ordre de la spécification.

*Généré par `python3 fiches/couverture_cq.py --ecrire` ; ne pas corriger à la main. Les questions viennent de la spécification (§6). « Fiches qui disent y répondre » : la fiche nomme la question dans son champ `cq_couvertes` ; le tableau ne juge pas si c’est fondé. Une fiche est « publique » quand le site la publie ; les autres sont « en préparation ». « Couverte par un champ du patron » : pour quelques questions, un champ que toute fiche doit remplir (le patron de fiche, `PPP_FicheType.md`) y répond ; le tableau compte les fiches où ce champ est réellement rempli.*

**50 questions** ; **37 fiches** (29 publiques, 8 en préparation).

## Par question

| Question | Énoncé (début) | Fiches publiques qui disent y répondre | Fiches en préparation qui disent y répondre | Couverte par un champ du patron |
|---|---|---|---|---|
| CQ1 | Quelles qualités perceptives de cet objet peuvent faire l’objet d’une attention ? | `contour`, `curvature`, `distribution`, `hue`, `hueContrast`, `hueCount`, `hueRange`, `jointLevelOffset`, `jointSpacing`, `lightness`, `lightnessContrast`, `lightnessRange`, `localIrregularity`, `negativeSpace`, `outlineIndentation`, `partNesting`, `perceivedDepth`, `perceivedSize`, `perceptualContrast`, `perceptualDensity`, `saturation`, `saturationRange`, `scaleContrast`, `subsurfaceDepth`, `surfaceGloss`, `symmetry`, `texture`, `textureDirectionality`, `translucency` | `elementaryShapeCount`, `odourCharacter`, `odourIntensity`, `pitchClarity`, `soundAttack`, `soundDecay`, `soundSharpness`, `textureContrast` | — |
| CQ2 | Pour une qualité donnée, où se situe l’objet sur son espace de valeurs ? | `contour`, `curvature`, `distribution`, `hue`, `hueContrast`, `hueCount`, `hueRange`, `jointLevelOffset`, `jointSpacing`, `lightness`, `lightnessContrast`, `lightnessRange`, `localIrregularity`, `negativeSpace`, `outlineIndentation`, `partNesting`, `perceivedDepth`, `perceivedSize`, `perceptualContrast`, `perceptualDensity`, `saturation`, `saturationRange`, `scaleContrast`, `subsurfaceDepth`, `surfaceGloss`, `symmetry`, `texture`, `textureDirectionality`, `translucency` | `elementaryShapeCount`, `odourCharacter`, `odourIntensity`, `pitchClarity`, `soundAttack`, `soundDecay`, `soundSharpness`, `textureContrast` | — |
| CQ3 | Cette qualité est-elle une propriété du tout, d’une partie, ou d’une relation entre … | — | — | arité, porteur : 29 fiches publiques sur 29, 8 en préparation sur 8 |
| CQ4 | Quelles qualités sont intégrales (on ne juge pas l’une sans l’autre) et lesquelles sont … | — | — | — |
| CQ4a | Pour chaque type du cœur : non applicable / applicable non pertinent / applicable et … | `perceptualDensity`, `texture` | — | — |
| CQ4b | Si pertinent : quelle valeur, dans quel format (étiquette verbale, ordinal, numérique) … | `perceptualDensity`, `texture` | — | — |
| CQ4c | La carte est-elle complète vis-à-vis du TBox courant : chaque type a-t-il l’un des cinq … | `perceptualDensity`, `texture` | — | — |
| CQ4d | Si deux objets ont des cartes distinctes, sont-ils perceptivement discernables ? … | `perceptualDensity`, `texture` | — | — |
| CQ4e | Peut-on comparer deux cartes dimension par dimension (écart, transfert, nuancier) ? | `perceptualDensity`, `texture` | — | — |
| CQ5 | Dans cet échange ou cette observation, à quelles propriétés l’attention s’est-elle portée … | — | — | — |
| CQ6 | Lesquelles ont fait une différence (pertinence effective, rôle PPP) ? | — | — | — |
| CQ7 | L’attention était-elle focalisée sur un objet et distribuée sur plusieurs de ses … | — | — | — |
| CQ8 | Deux personnes parlent-elles de la même qualité, ou de deux qualités distinctes sous le … | — | — | relation confusableWith : 24 fiches publiques sur 29, 4 en préparation sur 8 |
| CQ8a | Par quelles qualités et quelles relations entre parties cette forme se caractérise-t-elle … | `hueContrast`, `jointLevelOffset`, `jointSpacing`, `lightnessContrast`, `perceptualContrast`, `scaleContrast` | `elementaryShapeCount`, `textureContrast` | — |
| CQ8b | Quelles qualités formelles décrivent le joint entre ces deux matières (espacement, … | `jointLevelOffset`, `jointSpacing`, `lightnessContrast`, `perceptualContrast` | — | — |
| CQ8c | Une configuration du poster se décrit-elle entièrement par des types déjà là (limite, … | — | — | — |
| CQ8d | Quelles qualités perceptives une configuration de joint tend-elle à produire (contraste … | — | — | — |
| CQ8e | Les qualités du joint suffisent-elles à décrire les configurations du poster pour les … | — | — | — |
| CQ8f | Une qualité du joint se reprend-elle d’une paire de matières à une autre sans changer de … | — | — | — |
| CQ9 | Quelles qualités / quels modes sont déclarés pertinents pour ce projet ? | — | — | — |
| CQ10 | Quelle valeur visée sur chaque dimension retenue ? | — | — | — |
| CQ11 | Qu’est-ce qui est explicitement hors cadrage perceptif ? | — | — | — |
| CQ12a | Quelle(s) PPP ce nuancier fait-il varier ? Lesquelles sont tenues (autant que possible) … | `lightnessContrast`, `perceptualDensity`, `texture` | — | — |
| CQ12b | Quelle est l’étendue visée — les pôles, le pas, les trous dans l’espace de valeurs ? | `perceptualDensity`, `texture` | — | — |
| CQ12c | Deux échantillons adjacents diffèrent-ils sur l’axe déclaré, ou aussi sur une autre … | `perceptualDensity`, `texture` | — | — |
| CQ12d | La prochaine itération est-elle : aller plus loin sur le même axe, interpoler, changer … | `perceptualDensity`, `texture` | — | — |
| CQ12e | Les dimensions co-variées sont-elles intégrales (on ne peut pas varier l’une sans … | `perceptualDensity`, `texture` | — | — |
| CQ12 | En quoi deux objets (référence vs proto, proto A vs proto B, échantillon n vs n+1) … | — | — | — |
| CQ13 | L’écart porte-t-il sur le type de qualité, sur la valeur, ou sur l’épisode (cible, … | — | — | — |
| CQ14 | Peut-on transférer la valeur d’une qualité d’un objet vers un autre objet / un proto ? | `perceptualDensity` | — | — |
| CQ15 | Quelles unités sont combinables (qualité, valeur, configuration, régime) ? | — | — | — |
| CQ16 | Quelle opération d’exploration s’applique à quelle unité (« augmenter », « fragmenter », … | — | — | — |
| CQ19 | Cette mention textuelle (« trop chargé », « ça saute aux yeux ») se résout-elle en un … | — | — | — |
| CQ20 | Cette annotation d’image et cette phrase d’atelier sont-elles la même assertion, ou deux … | — | — | — |
| CQ21 | Quels objets / images du corpus partagent une configuration PPP donnée (requête par types … | — | — | — |
| CQ22 | L’identifiant d’un type est-il stable à travers les outils (fiche humaine, annotateur, … | — | — | — |
| CQ23 | Cette proposition est-elle évaluable dans K (vrai, faux, non tranché à propos d’un objet) … | `perceptualDensity` | — | — |
| CQ24 | Quelles dimensions PPP peuvent servir d’attributs de partition pour expanser C ? | `perceptualDensity` | — | — |
| CQ25 | Quelle connaissance K (fiche, type, contrainte) autorise ou interdit une conjonction dans … | — | — | — |
| CQ16a | Ce type s’applique-t-il, sans redéfinition, à un tableau ? à un ustensile de cuisine ? à … | `perceptualDensity` | — | transfert : 29 fiches publiques sur 29, 8 en préparation sur 8 |
| CQ16b | Ce qui ne se transfère pas est-il un type du cœur, ou un fait d’application (cette … | — | — | — |
| CQ16c | Une fiche tableau / cuisine / high-tech peut-elle se remplir avec les mêmes cases qu’une … | — | — | — |
| CQ17 | Pourquoi ce terme entre-t-il dans le cœur (test Nanay + non-redondance + transfert) ? | — | — | nanay, transfert, relations : 27 fiches publiques sur 29, 4 en préparation sur 8 |
| CQ18 | Ce terme est-il un type de qualité, une région de valeurs, une relation, une gestalt, ou … | — | — | — |
| CQ26 | Ce type est-il formel ou semi-formel ? S’il est semi-formel, quelle est sa base de … | — | — | strate, base_dependance : 29 fiches publiques sur 29, 8 en préparation sur 8 |
| CQ27 | Cette base contient-elle des facteurs non perceptuels (catégorie d’œuvre, titre, … | — | — | base_dependance.facteurs_non_perceptuels : 29 fiches publiques sur 29, 8 en préparation sur 8 |
| CQ28 | Ce label, cette région, cette définition passent-ils le test de neutralité (§0.4) ? Cette … | — | — | — |
| CQ29 | Quels énoncés testables (E1–E6) ce type engage-t-il ? Lesquels ont été mis à l’épreuve, … | — | — | enonces_testables : 29 fiches publiques sur 29, 8 en préparation sur 8 |
| CQ30 | Dans cet épisode, quelle est la cible (objet ou partie), sous quelles conditions et par … | — | — | — |
| CQ31 | Dans quelles conditions de perception (présentation, lumière, distance, angle, durée ; … | — | — | conditions_critiques : 25 fiches publiques sur 29, 8 en préparation sur 8 (en partie) |

## Exemplaires par fiche publique

Un exemplaire place un objet réel (photo publiée) sur l’échelle d’une qualité : il illustre CQ1 et CQ2 pour cette qualité. Les exemplaires ne nomment pas de question ; le tableau ne leur en attribue pas d’autre. « Relus » : vérifiés par la relecture avant publication.

| Fiche publique | Questions nommées | Exemplaires | dont relus |
|---|---|---|---|
| `contour` | CQ1, CQ2 | 4 | 4 |
| `curvature` | CQ1, CQ2 | 4 | 4 |
| `distribution` | CQ1, CQ2 | 4 | 3 |
| `hue` | CQ1, CQ2 | 3 | 3 |
| `hueContrast` | CQ1, CQ2, CQ8a | 4 | 4 |
| `hueCount` | CQ1, CQ2 | 5 | 4 |
| `hueRange` | CQ1, CQ2 | 5 | 5 |
| `jointLevelOffset` | CQ1, CQ2, CQ8a, CQ8b | 2 | 1 |
| `jointSpacing` | CQ1, CQ2, CQ8a, CQ8b | 5 | 3 |
| `lightness` | CQ1, CQ2 | 3 | 3 |
| `lightnessContrast` | CQ1, CQ2, CQ8a, CQ8b, CQ12a | 5 | 5 |
| `lightnessRange` | CQ1, CQ2 | 4 | 4 |
| `localIrregularity` | CQ1, CQ2 | 3 | 3 |
| `negativeSpace` | CQ1, CQ2 | 3 | 3 |
| `outlineIndentation` | CQ1, CQ2 | 5 | 5 |
| `partNesting` | CQ1, CQ2 | 4 | 4 |
| `perceivedDepth` | CQ1, CQ2 | 5 | 5 |
| `perceivedSize` | CQ1, CQ2 | 1 | 1 |
| `perceptualContrast` | CQ1, CQ2, CQ8a, CQ8b | 4 | 3 |
| `perceptualDensity` | CQ1, CQ2, CQ4a, CQ4b, CQ4c, CQ4d, CQ4e, CQ12a, CQ12b, CQ12c, CQ12d, CQ12e, CQ14, CQ16a, CQ23, CQ24 | 3 | 3 |
| `saturation` | CQ1, CQ2 | 5 | 2 |
| `saturationRange` | CQ1, CQ2 | 3 | 3 |
| `scaleContrast` | CQ1, CQ2, CQ8a | 4 | 3 |
| `subsurfaceDepth` | CQ1, CQ2 | 3 | 3 |
| `surfaceGloss` | CQ1, CQ2 | 6 | 5 |
| `symmetry` | CQ1, CQ2 | 3 | 3 |
| `texture` | CQ1, CQ2, CQ4a, CQ4b, CQ4c, CQ4d, CQ4e, CQ12a, CQ12b, CQ12c, CQ12d, CQ12e | 4 | 4 |
| `textureDirectionality` | CQ1, CQ2 | 3 | 3 |
| `translucency` | CQ1, CQ2 | 3 | 3 |

## Questions qu’aucune fiche publique ne dit couvrir (32 sur 50)

CQ3, CQ4, CQ5, CQ6, CQ7, CQ8, CQ8c, CQ8d, CQ8e, CQ8f, CQ9, CQ10, CQ11, CQ12, CQ13, CQ15, CQ16, CQ19, CQ20, CQ21, CQ22, CQ25, CQ16b, CQ16c, CQ17, CQ18, CQ26, CQ27, CQ28, CQ29, CQ30, CQ31

Cette liste mélange deux sortes de questions :
- des **questions sur la manière de noter une observation** (qui regarde, quoi, dans quel échange, pour quel projet, à partir de quel texte) : CQ5, CQ6, CQ7, CQ9, CQ10, CQ11, CQ19, CQ20, CQ21, CQ22, CQ30. Elles relèvent du modèle des observations (assertions et épisodes, spec §9.3), pas d’une fiche ;
- des **questions sur les qualités elles-mêmes**, qu’une fiche pourrait déclarer : les autres. Parmi elles, CQ3, CQ8, CQ17, CQ26, CQ27, CQ29, CQ31 ont déjà un champ du patron qui y répond (colonne de droite) ; le champ `cq_couvertes` des fiches ne les nomme pas encore.
