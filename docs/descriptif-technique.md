# PPP — descriptif technique du dépôt

*Modèle de `docs/descriptif-technique.md` du dépôt public. L'accueil du dépôt est `README.md` ; ce document décrit le contenu du dépôt pour qui veut s'y retrouver.*

Ontologie descriptive des propriétés perceptuelles pertinentes pour l'esthétique : un vocabulaire ouvert pour décrire ce qu'on perçoit d'un objet (forme, couleur, matière, organisation), sans juger. Elle est conduite comme un programme de recherche : chaque fiche porte des énoncés testables, et peut être contestée.

> **Version de travail.** Les fiches sont des propositions : aucune n'a encore été mise à l'épreuve, plusieurs sont incomplètes.

Site : https://blomig.github.io/PPP-ontologie (GitHub Pages). Dépôt : https://github.com/blomig/PPP-ontologie.

## Contenu du dépôt

- `PPP_Specification.md` : la spécification (buts, périmètre, règles, gouvernance au §13).
- `PPP_FicheType.md` : le patron d'une fiche de type ; `PPP_FicheExemplaire.md` : le gabarit d'une fiche d'exemplaire.
- `fiches/` : les fiches de type (un fichier YAML par type), le registre des objets (`exemplaires.yaml`), les familles de lecture (`familles.yaml`), l'avancement (`README.md`).
- `docs/` : bibliographie par type, état de l'art, gouvernance, comment citer.
- `tickets/` : les tickets reçus, convertis en fichiers ; `epreuves/` : le journal des épreuves, un fichier par épreuve (format : `epreuves/README.md`), aussi affiché sur le site (page du journal, et renvoi depuis chaque fiche).
- `site/` : le site publié par GitHub Pages.

## Participer

Ouvrez un ticket avec l'un des formulaires du dépôt (onglet *Issues*, « New issue ») : il faut un compte GitHub. Quatre formulaires sont ouverts à tous, sans compétence technique : suggérer un type, signaler un mot qui juge ou une mauvaise traduction, signaler une erreur, suggérer un objet. Les autres demandent une observation reproductible ou une fiche complète. Détail : `CONTRIBUTING.md`, à la racine du dépôt.

## Citer

Citez toujours la version. Auteurs, titre, version et date : `CITATION.cff` (bouton « Cite this repository » de GitHub) ; formes détaillées : `docs/comment-citer.md`.

## Licences

Contenu (spécification, fiches, documents) : CC BY 4.0 (`LICENSE-CONTENT.md`). Code du site et des outils : MIT (`LICENSE`). Titulaire et mention de copyright : `LICENSE` ; équipe et contributeurs : `CONTRIBUTORS.md`. Tout le dépôt est sous licence, y compris les fiches pas encore publiées sur le site. Les images d'exemplaires gardent leur propre licence (tableau dans `LICENSE-CONTENT.md`).
