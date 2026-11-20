# `fiches/` — fiches de types PPP

**État** : statut éditorial, statut épistémique et nombre de fiches sont calculés depuis les fiches par `fiches/compte.py` dans le bloc ci-dessous (`python3 fiches/compte.py --verifier` dit si ce bloc est périmé, `python3 fiches/compte.py --ecrire` le régénère). **Rien n'est validé au sens de la spec** : la structure est proposée, et aucun accord entre observateurs n'est déclaré. La relecture explicative relit les champs en langage courant des fiches et des exemplaires (`relecture_explicative`) ; ce qui reste à relire est dans `a_relire` et `a_reconfirmer` de chaque fiche.

<!-- compte:debut (calculé par fiches/compte.py ; ne pas corriger à la main) -->
- **49 fiches de type actives** ; **48 sans point bloquant** (`bloque_par` vide) : 37 à explicabilité validée par la relecture explicative (`bitterness`, `contour`, `curvature`, `distribution`, `hardnessToTouch`, `hue`, `hueContrast`, `hueCount`, `hueRange`, `jointLevelOffset`, `jointSpacing`, `lightness`, `lightnessContrast`, `lightnessRange`, `localIrregularity`, `negativeSpace`, `odourCharacter`, `odourIntensity`, `outlineIndentation`, `partNesting`, `perceivedDepth`, `perceivedPitch`, `perceivedSize`, `perceivedWeight`, `perceptualDensity`, `pitchClarity`, `saturation`, `saturationRange`, `soundAttack`, `soundDecay`, `soundSharpness`, `subsurfaceDepth`, `symmetry`, `texture`, `textureContrast`, `textureDirectionality`, `translucency`), 3 au langage courant validé avec exemple concret manquant (`perceptualContrast`, `scaleContrast`, `surfaceGloss`), 8 en attente de la relecture explicative (champs à valider ou à re-confirmer : `astringency`, `flavourComponentCount`, `flavourDominance`, `flavourIntensity`, `hardnessInMouth`, `oralPungency`, `oralThickness`, `tastePersistence`) ; **1 bloquée** : `elementaryShapeCount` par une question à trancher ; dont **4 minimales** (créées en 2.5 à partir des verdicts des crash tests 01 et 02) : `hueCount`, `lightnessRange`, `outlineIndentation`, `saturationRange`.
- **Références** : 49 fiches sur 49 en ont (242 références distinctes, comptées par DOI ou URL : 35 vérifiée sur la source, 207 vérifiée sur résumé ou source secondaire) ; sans référence : —.
- **Relecture explicative en attente** (`a_relire` ou `a_reconfirmer` non vides), bloquées comprises : 9 fiches (`astringency`, `elementaryShapeCount`, `flavourComponentCount`, `flavourDominance`, `flavourIntensity`, `hardnessInMouth`, `oralPungency`, `oralThickness`, `tastePersistence`).
- **Sans aucun exemplaire** : 19 fiches (`astringency`, `bitterness`, `elementaryShapeCount`, `flavourComponentCount`, `flavourDominance`, `flavourIntensity`, `hardnessInMouth`, `hardnessToTouch`, `odourCharacter`, `odourIntensity`, `oralPungency`, `oralThickness`, `perceivedPitch`, `perceivedWeight`, `pitchClarity`, `soundAttack`, `soundDecay`, `soundSharpness`, `tastePersistence`).
- **Fiches publiques (règle de première publication, paliers 1 et 2)** : 40 fiches publiques (`bitterness`, `contour`, `curvature`, `distribution`, `hardnessToTouch`, `hue`, `hueContrast`, `hueCount`, `hueRange`, `jointLevelOffset`, `jointSpacing`, `lightness`, `lightnessContrast`, `lightnessRange`, `localIrregularity`, `negativeSpace`, `odourCharacter`, `odourIntensity`, `outlineIndentation`, `partNesting`, `perceivedDepth`, `perceivedPitch`, `perceivedSize`, `perceivedWeight`, `perceptualContrast`, `perceptualDensity`, `pitchClarity`, `saturation`, `saturationRange`, `scaleContrast`, `soundAttack`, `soundDecay`, `soundSharpness`, `subsurfaceDepth`, `surfaceGloss`, `symmetry`, `texture`, `textureContrast`, `textureDirectionality`, `translucency`) ; publiable : `contour`, `curvature`, `distribution`, `hardnessToTouch`, `hue`, `hueContrast`, `hueCount`, `hueRange`, `jointSpacing`, `lightness`, `lightnessContrast`, `lightnessRange`, `localIrregularity`, `negativeSpace`, `odourCharacter`, `outlineIndentation`, `partNesting`, `perceivedDepth`, `perceivedPitch`, `perceptualContrast`, `pitchClarity`, `saturation`, `saturationRange`, `scaleContrast`, `soundAttack`, `subsurfaceDepth`, `surfaceGloss`, `symmetry`, `textureContrast`, `translucency` ; publiable avec exemplaires incomplets : `bitterness`, `jointLevelOffset`, `odourIntensity`, `perceivedSize`, `perceivedWeight`, `perceptualDensity`, `soundDecay`, `soundSharpness`, `texture`, `textureDirectionality` ; pas publiable : 9 fiches (détail : `python3 fiches/compte.py --paliers`).
- **Familles de lecture** : 8 (`forme` 11 types, `couleur` 9 types, `matiere` 7 types, `organisation` 10 types, `toucher` 9 types, `son` 5 types, `odorat` 2 types, `gout` 9 types) ; types sans famille : — ; introduction en attente de la relecture explicative : —.
- **Statuts des 49 fiches actives** : statut éditorial `candidat` 49 ; statut épistémique `non éprouvé` 49 ; fiches réservées hors liste active (`reserve/`) : `perceptualIntensity` (`attente`).
<!-- compte:fin -->

Les points ouverts sont dans `QUESTIONS-A-TRANCHER.md` (questions à trancher, chacune avec une position de travail) et dans `docs/questions-crash-tests.md` (questions issues des crash tests).

## Contenu

| Fichier | Rôle |
|---|---|
| `<id sans préfixe>.yaml` | une fiche de type active par fichier, au format de `PPP_FicheType.md` (spec §12, exigence « fiches lisibles par machine ») ; YAML pur |
| `en/` | textes anglais des fiches, champ par champ, avec l’empreinte du texte français traduit |
| `reserve/` | fiches de types passés en `attente` (spec §9.9), gardées pour trace, hors liste active et non tenues à jour |
| `familles.yaml` | registre des familles de lecture (spec §9.7 L, exigence « familles navigables ») : clé, labels, introduction, appartenance |
| `exemplaires.yaml` | objets publics, épisodes et assertions proposés comme exemplaires (spec §9.3, §9.7 G) |
| `compte.py` | calcule les deux blocs de ce README depuis les fiches (comptes ; conditions critiques par fiche) ; `--verifier` les contrôle, `--ecrire` les régénère, `--paliers` détaille le palier de publication de chaque fiche |
| `couverture_cq.py` | couverture des questions de compétence de la spec (§6) par les fiches |
| `export_skos.py` | export SKOS des fiches publiques (Turtle et JSON-LD) |
| `QUESTIONS-A-TRANCHER.md` | questions à trancher, avec position de travail ; ce qui est tranché dans le cadre de la spec y est marqué |

**Champs de travail** (hors patron, à retirer une fois la fiche validée) :
- `a_relire` : champs préremplis, à vérifier en relecture explicative (ancien nom : `a_valider_par_la_relecture`) ;
- `relecture_explicative` (ancien nom : `valide_par_la_relecture`) : relecture explicative, avec `date` (AAAA-MM-JJ) et `champs` (liste des champs relus et corrigés en langage courant). Une relecture n'est ni une épreuve ni un changement de statut éditorial ;
- `manques` : ce qui manque à la fiche ;
- `source_de_la_fiche` : d'où vient la fiche ;
- `statut_note` ;
- `note_joint` ;
- `dimension_comparee_regle` ;
- `meme_echelle_que` ;
- `avertissement_label` (par exemple pour la netteté du bord), `note_categories` (par exemple pour la teinte), `note_reference` (taille perçue), `note_dimension` (contraste d'échelle) ;
- `note_conditions` (v2.3.1) : pourquoi ces facettes sont critiques, et ce qui ne l'est que pour une modalité ;
- `note_echelle` (par exemple pour l’éventail des teintes), `note_porteur` (par exemple pour la courbure), `note_base` (par exemple pour l’emboîtement) (v2.3.2) ;
- `bloque_par` (v2.3.1) : questions ouvertes (à trancher, ou issues des crash tests) qui empêchent de finir la fiche ; vide si rien ne bloque ;
- `a_reconfirmer` (dans `relecture_explicative` d'une fiche ou de `exemplaires.yaml` ; `champ`, `avant`, `apres`, `raison`) : phrase validée puis corrigée au minimum, à re-confirmer par la relecture explicative.

**Champs du patron ajoutés en 2.4** (spec §0.1 point 7, §9.7 P ; exigence « références visibles ») : `references_statut`, `references` (citation, DOI ou URL, rôle, statut de vérification, date, ce qui a été vu, ce que PPP en reprend et n'en reprend pas) et `etat_de_l_art` (renvoi à `docs/bibliographie-par-type.md`). Le compte des références est dans le bloc calculé en tête. En 2.6, le texte appelle chaque référence par `[[id]]` (spec §9.7 P, point 4 bis) et le renvoi au groupe est dans `etat_de_l_art_renvoi` (`docs/bibliographie-par-type.md#groupe-…`). Dans `alignements_externes`, `reference_id` renvoie à une entrée de `references` (par exemple `tamura1978`).

**Champ du patron ajouté en 2.3** : `conditions_critiques` (spec §9.7 H, et §9.4, contrainte sur la cardinalité du porteur) : facettes de la condition de perception dont la région dépend fortement ; si une facette critique vaut `unknown` dans l’épisode, l’assertion est « non tranché », sans région. Le tableau calculé « Conditions critiques par fiche », plus bas, donne les facettes de chaque fiche ; « — » : aucune facette ne s’y impose.

**Champ du patron ajouté en 2.2.3** : `alignements_externes` (spec §9.7 O) : rapprochement avec une classification publiée (`skos:closeMatch` ou `skos:relatedMatch`, référence vérifiée).

## Avancement

États de travail (calculés par `fiches/compte.py`) : **explicabilité validée par la relecture explicative** = tous les champs du patron remplis, langage courant validé par la relecture explicative (elle juge que la fiche s’explique à un lecteur), `bloque_par` vide ; des questions ouvertes non bloquantes peuvent rester. **langage courant validé ; exemple concret manquant** = comme la précédente, mais la relecture explicative juge que la fiche ne s’explique pas sans un exemple concret, qui reste à trouver (`manques`). **en attente de la relecture explicative** = `bloque_par` vide, mais des champs attendent sa validation ou sa re-confirmation (`a_relire` ou `a_reconfirmer` non vides) ; cet état passe avant les deux précédents : une fiche dont des phrases changées attendent la relecture explicative n’a plus son explicabilité validée. **bloquée** = langage courant validé, structure remplie aussi loin que possible, une question ouverte (à trancher, ou issue des crash tests) empêche de la finir. **minimale** = l’une des quatre fiches créées en 2.5 comme « fiches minimales » à partir des verdicts des crash tests 01 et 02 : par les champs, rien ne les distingue d’une autre fiche ; « minimale » dit ici leur origine, pas un manque de plus. Ce n’est pas l’état « rédigée » ou « minimale » que le site calcule sur les champs (définition, question attentionnelle, contre-exemple, repères, au moins un exemplaire par région sur deux régimes de perception, énoncés d’accord et de neutralité déclarés ; spec §12, exigence « fiche rédigée ou minimale »).

Palier de publication (spec §12, exigence « première publication : trois paliers ») : **publiable**, **publiable avec exemplaires incomplets** ou **pas publiable**, calculé par `python3 fiches/compte.py --paliers` ; les fiches des deux premiers paliers sont publiques.

## Conditions critiques par fiche

Toutes les fiches actives, comme dans le bloc des comptes, avec leur état de travail et leur palier de publication. « Conditions critiques » : facettes déclarées dans `conditions_critiques` ; quand la définition du type fixe une facette (`conditions_fixees`), elle est donnée à la suite. « Régions avec exemplaire relu » : régions de la fiche illustrées par au moins un exemplaire relu en relecture explicative ; pour le toucher, l’ouïe, l’odorat et le goût, des épisodes proposés « à réaliser » ou des repères de région peuvent en tenir lieu pour la publication (`--paliers`), et ne sont pas comptés ici.

<!-- x12:debut (calculé par fiches/compte.py ; ne pas corriger à la main) -->
| Fiche | État | Publication | Conditions critiques | Régions avec exemplaire relu |
|---|---|---|---|---|
| `astringency` | en attente de la relecture explicative | pas publiable | `avant` | 0 / 4 |
| `bitterness` | explicabilité validée par la relecture explicative | publiable avec exemplaires incomplets | `nez` | 0 / 4 |
| `contour` | explicabilité validée par la relecture explicative | publiable | `distance` | 3 / 3 |
| `curvature` | explicabilité validée par la relecture explicative | publiable | `angle`, `distance` | 3 / 3 |
| `distribution` | explicabilité validée par la relecture explicative | publiable | — | 2 / 3 |
| `elementaryShapeCount` | bloquée par une question à trancher | pas publiable | `distance`, `angle`, `presentation` | 0 / 4 |
| `flavourComponentCount` | en attente de la relecture explicative | pas publiable | `nez`, `moment` | 0 / 4 |
| `flavourDominance` | en attente de la relecture explicative | pas publiable | `nez`, `moment`, `temperature_bouchee`, `avant` | 0 / 9 |
| `flavourIntensity` | en attente de la relecture explicative | pas publiable | `nez`, `moment`, `temperature_bouchee`, `avant` | 0 / 4 |
| `hardnessInMouth` | en attente de la relecture explicative | pas publiable | `moment` ; fixée par la définition : `moment` = `firstBite` | 0 / 4 |
| `hardnessToTouch` | explicabilité validée par la relecture explicative | publiable | `geste`, `temperature_objet` | 0 / 4 |
| `hue` | explicabilité validée par la relecture explicative | publiable | `presentation` | 6 / 6 |
| `hueContrast` | explicabilité validée par la relecture explicative | publiable | `presentation` | 4 / 4 |
| `hueCount` | explicabilité validée par la relecture explicative | publiable | `presentation`, `distance` | 3 / 3 |
| `hueRange` | explicabilité validée par la relecture explicative | publiable | `presentation`, `distance` | 3 / 3 |
| `jointLevelOffset` | explicabilité validée par la relecture explicative | publiable avec exemplaires incomplets | `angle`, `distance` | 2 / 3 |
| `jointSpacing` | explicabilité validée par la relecture explicative | publiable | `distance` | 2 / 3 |
| `lightness` | explicabilité validée par la relecture explicative | publiable | `presentation` | 5 / 5 |
| `lightnessContrast` | explicabilité validée par la relecture explicative | publiable | `presentation` | 4 / 4 |
| `lightnessRange` | explicabilité validée par la relecture explicative | publiable | `presentation`, `lumiere`, `distance` | 3 / 3 |
| `localIrregularity` | explicabilité validée par la relecture explicative | publiable | `distance`, `angle` | 3 / 3 |
| `negativeSpace` | explicabilité validée par la relecture explicative | publiable | — | 3 / 3 |
| `odourCharacter` | explicabilité validée par la relecture explicative | publiable | `distance` | 0 / 11 |
| `odourIntensity` | explicabilité validée par la relecture explicative | publiable avec exemplaires incomplets | `distance`, `exposition` | 0 / 4 |
| `oralPungency` | en attente de la relecture explicative | pas publiable | `avant` | 0 / 4 |
| `oralThickness` | en attente de la relecture explicative | pas publiable | `moment`, `temperature_bouchee` ; fixée par la définition : `moment` = `firstContact` | 0 / 4 |
| `outlineIndentation` | explicabilité validée par la relecture explicative | publiable | `angle`, `distance` | 3 / 3 |
| `partNesting` | explicabilité validée par la relecture explicative | publiable | `distance` | 3 / 3 |
| `perceivedDepth` | explicabilité validée par la relecture explicative | publiable | `presentation`, `distance`, `angle` | 3 / 3 |
| `perceivedPitch` | explicabilité validée par la relecture explicative | publiable | `production`, `bruit_de_fond` | 0 / 3 |
| `perceivedSize` | explicabilité validée par la relecture explicative | publiable avec exemplaires incomplets | `presentation`, `distance` | 2 / 4 |
| `perceivedWeight` | explicabilité validée par la relecture explicative | publiable avec exemplaires incomplets | `geste` | 0 / 3 |
| `perceptualContrast` | langage courant validé ; exemple concret manquant | publiable | `distance` | 3 / 4 |
| `perceptualDensity` | explicabilité validée par la relecture explicative | publiable avec exemplaires incomplets | `distance` | 3 / 5 |
| `pitchClarity` | explicabilité validée par la relecture explicative | publiable | `production`, `bruit_de_fond` | 0 / 3 |
| `saturation` | explicabilité validée par la relecture explicative | publiable | `presentation` | 2 / 4 |
| `saturationRange` | explicabilité validée par la relecture explicative | publiable | `presentation`, `lumiere` | 3 / 3 |
| `scaleContrast` | langage courant validé ; exemple concret manquant | publiable | `distance` | 3 / 4 |
| `soundAttack` | explicabilité validée par la relecture explicative | publiable | `production` | 0 / 3 |
| `soundDecay` | explicabilité validée par la relecture explicative | publiable avec exemplaires incomplets | `production` | 0 / 3 |
| `soundSharpness` | explicabilité validée par la relecture explicative | publiable avec exemplaires incomplets | `presentation`, `production` | 0 / 3 |
| `subsurfaceDepth` | explicabilité validée par la relecture explicative | publiable | `lumiere`, `angle` | 3 / 3 |
| `surfaceGloss` | langage courant validé ; exemple concret manquant | publiable | `lumiere`, `angle` | 4 / 4 |
| `symmetry` | explicabilité validée par la relecture explicative | publiable | `angle` | 3 / 3 |
| `tastePersistence` | en attente de la relecture explicative | pas publiable | `nez` ; fixée par la définition : `moment` = `residual` | 0 / 3 |
| `texture` | explicabilité validée par la relecture explicative | publiable avec exemplaires incomplets | `distance` | 3 / 4 |
| `textureContrast` | explicabilité validée par la relecture explicative | publiable | `distance` | 1 / 4 |
| `textureDirectionality` | explicabilité validée par la relecture explicative | publiable avec exemplaires incomplets | `distance` | 2 / 3 |
| `translucency` | explicabilité validée par la relecture explicative | publiable | `lumiere`, `presentation` | 3 / 3 |
<!-- x12:fin -->

**Hors lot (V1)** : types `attente` (saillance, distributions d'attention, régime d'exploration, intensité perceptive : spec §9.9) et `ppp:assemblyMode` (`déprécié`, sans fiche).

**Note sur le joint.** Le contraste de couleur au joint n'a pas de fiche. C'est une assertion de contraste de clarté ou de teinte, dont les deux termes sont les parties qui se rejoignent. Une note l'explique dans `lightnessContrast.yaml` (champ `note_joint`), et les fiches du joint le rappellent dans leur contre-exemple.

## Règles suivies

- Ids : uniquement ceux de l'annexe A de la spec (contrainte §9.4 : tout id cité par une fiche est défini). Aucune fiche active ne cite un id en `attente`.
- Strate (contrainte §9.4) : chaque semi-formel déclare une base qui atteint un formel. Une exception : `ppp:perceptualContrast`, dont la base est la dimension comparée (§9.7 B).
- Régions (contrainte §9.4 : une région de valeurs n’est pas un sous-type) : les régions sont des valeurs de l'espace du type, jamais des types ; aucun label de région ne reprend un label de type.
- Exemplaires : objets publics uniquement (décision sur les épreuves : elles se font sur des objets publics). Pour une photo, `distance` est celle de la prise de vue, estimée d'après le cadrage si besoin (spec §9.7 H). Chaque épisode a une seule cible (contrainte §9.4 sur la cardinalité du porteur) ; une assertion retirée garde son id (`withdrawn: oui`), qui n'est pas réutilisé. Licence et auteur sont repris tels qu'affichés par la source. Les droits restent à confirmer (question ouverte de la spec sur les droits et la provenance des exemplaires). Aucun objet confidentiel.
- Crédits (spec §12, exigence « droits et crédits ») : chaque objet porte un `credit` (auteur, licence, source, url, date_verification, mention_requise), relevé sur la page de la source. Règle d'usage : `usage` `image_reproduite` (crédit complet) ou `lien_seulement` avec `lien_externe` ; une image hébergée sur Wikimedia Commons avec licence et balise indiquées est utilisable, un doute sur le pays d’origine y est noté sans bloquer ; pour une image hors de Wikimedia Commons, un doute non levé (pays d’origine, Union européenne, États-Unis) vaut lien seulement ; `url_telechargement` et `fichier` donnent le fichier original et le nom de stockage ; motif dans `motif_usage` ; vérification des droits du 2026-10-11 : `docs/droits-exemples-2026-10-11.md`.

## Vérification

Les vérifications ont été faites en local, sans fichier versionné : tous les `.yaml` se chargent avec PyYAML ; chaque `ppp:` cité est un id de l'annexe A ; chaque région citée (`ppp:<type>/<clé>`) existe dans la fiche de son type ; les `facettes` coïncident avec `familles.yaml` (tout type actif a une famille) ; chaque `inEpisode` existe et chaque épisode a une seule cible, celle des assertions qui le citent ; chaque épisode déclare les cinq facettes ; aucun label de région ne coïncide avec un label de type ; chaque semi-formel atteint un formel par sa base ; aucune fiche active ne cite un id en `attente`. Depuis 2.4 : chaque fiche a `references_statut`, `references` et `etat_de_l_art` (avec le lien vers son groupe) ; chaque entrée a tous ses champs, un rôle et un statut admis ; aucune entrée « vérifiée » n'est sans DOI ou URL ; chaque `reference_id` d'un alignement existe dans `references`. `python3 fiches/compte.py --verifier` contrôle les deux blocs calculés de ce README.
