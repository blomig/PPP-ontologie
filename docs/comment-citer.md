# Comment citer PPP

*Document de PPP, spec v2.8 (§13, « Comment citer »). Rédigé le 2026-10-11 ; forme de citation unifiée en v2.8 (une seule forme, celle de `CITATION.cff`). Texte proposé pour la page « Comment citer » du site (structure de la maquette : ontologie, fiche, version, assertion, date de consultation, licence). Les métadonnées lisibles par machine sont dans `CITATION.cff` (Citation File Format 1.2.0, validé avec `cffconvert --validate`).*

## Citer l'ontologie

> Unger, Lomig et Grok Bot. *PPP — Propriétés Perceptuelles Pertinentes : spécification d'ontologie*, version 2.8, 2026-10-11. Licence CC BY 4.0. https://github.com/blomig/PPP-ontologie.

- **Auteurs** : Lomig Unger et Grok Bot (l'équipe du projet, §13).
- **Titre** : « PPP — Propriétés Perceptuelles Pertinentes : spécification d'ontologie », le `title` de `CITATION.cff`.
- **Version** : toujours indiquer la version de la spécification contre laquelle on cite (X6). Elle figure en tête de `PPP_Specification.md` et, sur le site, en pied de page.
- **Date** : celle de la version (en-tête de la spécification).
- **Adresse** : dépôt public `PPP-ontologie`, https://github.com/blomig/PPP-ontologie ; site (GitHub Pages) : https://blomig.github.io/PPP-ontologie (adresses retenues par l'éditeur du projet, série 10 ; constat du 2026-10-11 à 14 h 58, heure de Paris : les deux adresses répondent 404 sans connexion, ce qui ne prouve pas l'absence d'un dépôt privé ; elles sont donc données comme adresses retenues). Le dépôt de travail est privé ; son adresse n'est pas citée.
- **Identifiant pérenne** : aucun DOI à ce jour ; il reste à renseigner, car il dépend de Zenodo (l'adresse du site est retenue : voir « Adresse »). *Position de travail, à trancher* : archiver le dépôt public dans Zenodo, qui attribue un DOI à chaque *release* GitHub et lit `CITATION.cff` (GitHub Docs, « Referencing and citing content », https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content ; Zenodo, « CITATION.cff file », https://help.zenodo.org/docs/github/describe-software/citation-file/ ; consultés le 2026-10-11 : Zenodo n'accède qu'aux dépôts publics ; un fichier `.zenodo.json`, s'il existe, prend le pas sur `CITATION.cff`). Aucun DOI n'est inventé ici.

## Citer une fiche (un type)

> « Densité perceptive » (`ppp:perceptualDensity`), dans Unger, Lomig et Grok Bot, *PPP — Propriétés Perceptuelles Pertinentes : spécification d'ontologie*, version 2.8, 2026-10-11, fichier `fiches/perceptualDensity.yaml`. Licence CC BY 4.0. https://github.com/blomig/PPP-ontologie.

- Citer l'**identifiant** (`ppp:…`), qui ne change jamais, en plus du label, qui peut changer (X1).
- Pour une région : `<identifiant du type>/<clé>`, par exemple `ppp:texture/smooth` (X1).
- Ajouter la version de l’ontologie au moment de l’assertion (`ontologyVersion`) quand on cite un énoncé, une assertion ou une épreuve (§9.7 G).

## Citer une version

- La version de la spécification suffit pour citer l'ontologie ; le changelog dit ce qui a changé d'une version à l'autre.
- Un identifiant n'est jamais réattribué : un type déprécié reste citable sous son identifiant, avec un renvoi vers son remplaçant (A11).
- Une épreuve cite trois versions : la fiche, la page publiée, le matériel montré (§9.7 G).

## Citer une épreuve

> Épreuve `epreuve-0001` (exploratoire), journal des épreuves de *PPP — Propriétés Perceptuelles Pertinentes : spécification d'ontologie*, version 2.8, 2026-10-11, fichier `epreuves/0001-<type-visé>.md`.

- Le journal des épreuves est affiché sur le site (une page du journal, et un renvoi depuis chaque fiche ; décision de la série 10) ; le fichier `epreuves/<nnnn>-<type-visé>.md` du dépôt fait foi. Indiquer la nature (`programme` ou `exploratoire`) : une épreuve exploratoire ne compte pas pour le statut.
- Exemple seulement : aucune épreuve n'est encore publiée au journal.

## Citer une assertion ou un exemple

> Assertion `ppp-a:pilote-0102` (`ppp:texture/smooth`), dans *PPP — Propriétés Perceptuelles Pertinentes : spécification d'ontologie*, version 2.8, 2026-10-11, fichier `fiches/exemplaires.yaml`. Image : crédit de l'objet (auteur, titre, licence, adresse) tel qu'il figure dans « Droits et crédits ».

- L'identifiant de l'assertion (`ppp-a:…`) est opaque et stable (X1).
- **L'image n'est pas sous la licence de l'ontologie** : elle garde sa propre licence, et son crédit doit être repris tel quel (X16, Q15). Une image en lien seulement n'est pas reproduite.

## Date de consultation

Pour une page du site, indiquer la date de consultation avec la version : « consulté le AAAA-MM-JJ, version 2.8 ». *Position de travail* : la spécification ne fixait pas de règle ; celle-ci suit l'usage des citations de ressources en ligne.

## Licence et attribution

- Ontologie, spécification, fiches et documents : **CC BY 4.0** (`LICENSE-CONTENT.md`). L'attribution est obligatoire : auteurs, titre, version, adresse, licence, et mention des modifications si on en a fait.
- Code du site et des outils : **MIT** (`LICENSE`).
- `CITATION.cff` ne déclare que `license: CC-BY-4.0` (série 14) : en CFF 1.2.0, une liste de licences est admise mais signifie « au choix » (guide du schéma, champ `license` : relation OR) ; `[CC-BY-4.0, MIT]` laisserait reprendre le contenu sous MIT. La licence MIT du code y figure en commentaire.
- Formulation d'attribution courte, pour une réutilisation : « D'après Unger, Lomig et Grok Bot, *PPP — Propriétés Perceptuelles Pertinentes : spécification d'ontologie*, version 2.8, 2026-10-11, CC BY 4.0, https://github.com/blomig/PPP-ontologie ; modifié » (retirer « modifié » si rien n'a été changé).
- Titulaire des droits (`LICENSE`, `LICENSE-CONTENT.md`) : Lomig Unger, mention « Copyright (c) 2026 Lomig Unger et contributeurs du projet PPP » (décision de l'éditeur du projet). Les deux auteurs de la citation (Lomig Unger et Grok Bot, `CITATION.cff`) sont ceux à créditer : pour Grok Bot, co-auteur, c'est une mention de crédit, pas un titre juridique. Équipe et rôles : `CONTRIBUTORS.md`.
- CC BY 4.0 (section 3(a)(1)) demande de reprendre, s'ils sont fournis : les auteurs, la mention de copyright, un renvoi à la licence, un renvoi à l'exclusion de garantie, l'adresse du contenu ; et d'indiquer les modifications. `LICENSE-CONTENT.md` les donne.
- Les images d'exemplaires gardent leur propre licence (tableau dans `LICENSE-CONTENT.md`, crédit de référence dans `fiches/exemplaires.yaml`).
