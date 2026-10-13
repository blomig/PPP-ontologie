# Participer à PPP

Merci de votre intérêt. PPP est une ontologie publique et contestable : chaque remarque est lue, et reçoit une réponse motivée.

## Ouvrir un ticket

Tout passe par un **ticket GitHub**, ouvert avec l'un des formulaires du dépôt (https://github.com/blomig/PPP-ontologie/issues/new/choose, ou *Issues* → *New issue*). Le site (https://blomig.github.io/PPP-ontologie) renvoie vers le formulaire de chaque geste. Il faut un compte GitHub. Un formulaire par type de ticket :

| Formulaire | Pour | Ce qu'il faut |
|---|---|---|
| Suggérer un type | un aspect perceptible qu'aucune fiche ne décrit | rien de plus : ouvert à tous |
| Signaler un mot qui juge ou une mauvaise traduction | un mot qui évalue au lieu de décrire, une ambiguïté, une erreur de traduction | rien de plus : ouvert à tous |
| Signaler une erreur | une référence fautive, un crédit d'image, une coquille, un lien mort | rien de plus : ouvert à tous |
| Suggérer un objet | un objet public pour les épreuves (page publique obligatoire ; la date peut rester « je ne sais pas » si « Quelle version exactement ? » permet de retrouver l'objet ; l'objet peut être une photo publiée : c'est alors l'image elle-même, avec son lien précis et son crédit, sans avoir à identifier ce qu'elle montre) | ouvert à tous ; une page publique de l'objet |
| Contester un exemple ou un énoncé | une assertion ou un énoncé, avec une observation reproductible | observation reproductible |
| Ajouter une assertion | une assertion sur un objet déjà au registre | observation décrite |
| Signaler une anomalie | un cas reproductible que la fiche ne prévoit pas | observation reproductible |
| Publier une réfutation | une épreuve dont le protocole et le seuil ont été fixés avant | protocole et résultats |
| Proposer un type | une fiche complète au patron `PPP_FicheType.md` | fiche complète |

Le contenu minimal de chaque formulaire est celui de `docs/gouvernance.md` (section 2.4).

## Ce qui se passe ensuite

1. **Dans la semaine**, l'équipe juge si le ticket est recevable (le contenu minimal est là).
2. Un ticket recevable est versé dans `tickets/` comme fichier (`tickets/<numéro>-<type>.md`) et reste ouvert jusqu'à sa décision, ou jusqu'à l'épreuve qui le traite. Un ticket presque complet peut recevoir le label `précision-demandée` : l'équipe pose sa question avec une date limite, et sans réponse à cette date le ticket est fermé, avec la possibilité d'en ouvrir un nouveau. Un ticket non recevable est fermé avec son motif ; un ticket traité porte le label `accepté` ou `rejeté`.
3. Chaque décision est motivée publiquement ; un changement de la spécification ou d'une fiche est noté au changelog ; une épreuve va au journal des épreuves (`epreuves/`, format dans `epreuves/README.md`), affiché sur le site.

Un ticket simplement ouvert ne change rien sur le site : seul un ticket recevable peut faire passer un exemple ou une fiche à « contesté ».

## Règles

- **Pas de données personnelles** : un ticket est public. Pas d'adresse électronique ; un pseudonyme suffit.
- **Décrire, ne pas juger** : les fiches décrivent ce qu'on perçoit ; « beau », « réussi » ne décrivent pas un aspect.
- **Objets publics seulement** : un objet confidentiel n'est pas recevable ; une image n'est reproduite que si sa licence est réellement libre et vérifiée, ou, en miniature avec son crédit complet, si sa licence permet gratuitement et sans autorisation de la copier et de l'afficher, pour tout usage, même commercial (par exemple la licence Unsplash).
- **Sources vérifiables** : une référence se donne avec son DOI ou son adresse.

## Modifications directes (*pull requests*)

*Position de travail, à trancher* : l'équipe est fermée ; une proposition de modification directe est lue comme un ticket (elle reçoit une réponse motivée) ; l'équipe reporte elle-même les changements acceptés, et le commit cite le ticket.

## Licences

En contribuant, vous versez votre contribution sous les licences du projet : contenu CC BY 4.0 (`LICENSE-CONTENT.md`), code MIT (`LICENSE`) ; titulaire et mention de copyright : `LICENSE`. Aucun accord de contribution n'est à signer. Avec votre accord, l'équipe vous ajoute à `CONTRIBUTORS.md`, sous le nom ou le pseudonyme que vous choisissez.
