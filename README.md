# PPP — Propriétés perceptuelles pertinentes

Les propriétés perceptuelles pertinentes (PPP) forment un vocabulaire ouvert pour décrire un objet, une image, un son ou un espace : sa forme, ses couleurs, la manière dont il est organisé. Elles décrivent, elles ne jugent pas : aucune fiche ne dit si c'est beau. Leur but est de fournir des descripteurs universels des caractéristiques perceptuelles des objets, celles qui peuvent jouer un rôle dans notre évaluation esthétique, d'où le mot pertinentes. Cette évaluation couvre un champ beaucoup plus large, celui des valeurs, que nous laissons volontairement à part.

> **Version de travail.** Ce dépôt est publié pour être discuté. Les fiches sont des propositions : aucune n'a encore été mise à l'épreuve, et plusieurs sont incomplètes. Vos remarques nous aident à corriger avant une première version stable.

Site : [blomig.github.io/PPP-ontologie](https://blomig.github.io/PPP-ontologie/) · Dépôt : [github.com/blomig/PPP-ontologie](https://github.com/blomig/PPP-ontologie)

## Par où commencer

Lisez d'abord le [glossaire](docs/public/glossaire.md), une page. Puis ouvrez l'une des sept fiches :

- **Contraste de clarté** : regardez seulement le clair et le sombre, comme sur une photo en noir et blanc. Entre deux zones, l'écart va de deux gris voisins au noir sur du blanc.
- **Clarté** : une seule zone paraît-elle très sombre, sombre, moyenne, claire ou très claire ? La couleur ne compte pas ici.
- **Taille perçue** : à côté de votre corps, la chose paraît-elle plus petite que le bout du doigt (comme un grain de riz), tenir dans la main (comme une tasse), être à l'échelle du corps (comme une chaise) ou le dépasser (comme une maison) ?
- **Densité perceptive** : pour sa taille, la chose contient-elle peu ou beaucoup d'éléments distincts ?
- **Texture** : à la vue ou sous la main, la surface paraît-elle lisse, ou ses reliefs sont-ils fins, moyens ou gros ?
- **Teinte** : de quelle couleur est cette zone : rouge, orange, jaune, vert, bleu ou violet ? Un rose pâle et un rouge sombre ont la même teinte, rouge.
- **Orientation de la texture** : les reliefs vont-ils tous dans le même sens (un velours côtelé), seulement par endroits, ou dans tous les sens ?

Les fiches sont dans le dossier [`fiches/`](fiches/), à la racine du dépôt.

## Comment se lit une fiche

Chaque fiche décrit un seul aspect de ce qu'on perçoit. Elle commence par une **définition** en mots de tous les jours. Vient ensuite une **question à se poser en regardant** : c'est le cœur de la fiche. Puis des **exemples** d'objets publics, visibles en ligne, avec la valeur retenue. Un **contre-exemple** montre enfin ce que la fiche ne décrit pas, pour éviter les confusions. La fiche donne aussi les valeurs possibles, son état d'avancement et ses sources.

Aucune fiche ne donne de note. « Dense » ou « lisse » ne sont ni des qualités ni des défauts.

## Participer

Pour participer, il faut un **compte GitHub** (gratuit). Chaque demande devient un **ticket** public, une courte demande écrite. L'équipe répond toujours, en donnant ses raisons. Dans la semaine qui suit sa réception, elle dit si le ticket est recevable, c'est-à-dire s'il contient le nécessaire ; un ticket recevable reste ouvert jusqu'à l'épreuve qui le traite. Quatre gestes sont ouverts à tous, sans compétence technique :

- **Suggérer un type** : un aspect perceptible qu'aucune fiche ne décrit encore. Donnez un nom, une phrase et deux exemples. Dites aussi quelle fiche s'en approche le plus, et ce qui lui manque.
- **Signaler un mot qui juge ou une mauvaise traduction** : un mot qui évalue au lieu de décrire, une phrase ambiguë.
- **Signaler une erreur** : une référence fausse, un crédit d'image, une coquille, un lien mort.
- **Suggérer un objet public** pour nos essais : voir le [formulaire de suggestion d'objet](docs/public/formulaire-objet.md).

Vous pouvez aussi **contester un exemple** : décrivez l'objet et la façon dont vous l'avez regardé, et proposez une autre valeur.

Ne mettez jamais d'adresse électronique ni de données personnelles dans un ticket : il est public. Un pseudonyme suffit.

## Citer

Le projet est tenu par Lomig Unger et Grok Bot ; éditeur du projet : Lomig Unger.

Citez toujours la version :

> Unger, Lomig et Grok Bot. *PPP — Propriétés Perceptuelles Pertinentes : spécification d'ontologie*, version 2.8, 2026-10-11. Licence CC BY 4.0. https://github.com/blomig/PPP-ontologie

Pour une fiche, ajoutez son nom et son identifiant, par exemple « Densité perceptive » (`ppp:perceptualDensity`). L'identifiant ne change jamais, même si le nom change.

## Licence

Tout le contenu du dépôt est sous licence, y compris les fiches qui ne sont pas encore publiées sur le site.

Les fiches, la spécification, les textes et les documents sont sous licence **CC BY 4.0** (voir [LICENSE-CONTENT.md](LICENSE-CONTENT.md)). Vous pouvez les réutiliser, à condition de nommer les auteurs, de garder la mention des droits et un lien vers la licence, de rappeler qu'elle exclut toute garantie, de donner l'adresse du projet et de dire ce que vous avez changé. Le détail est dans [LICENSE-CONTENT.md](LICENSE-CONTENT.md).

Le code du site et des outils est sous licence **MIT** (voir [LICENSE](LICENSE)).

Les images d'exemples ne sont pas sous licence CC BY 4.0 : chacune garde sa propre licence, celle que donne sa source, et son crédit doit être repris tel quel. Une image n'est reproduite que si sa licence est vraiment libre ; sinon, la fiche donne seulement un lien vers sa source. Si vous modifiez une image sous licence CC BY-SA (recadrage, retouche), la nouvelle version doit rester sous cette même licence, et vous devez signaler la modification.
