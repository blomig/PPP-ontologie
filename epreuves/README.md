# Journal des épreuves

Ce dossier est le journal des épreuves de PPP : **un fichier par épreuve**, `epreuves/<nnnn>-<type-visé>.md` (par exemple `0001-texture.md`). Le numéro est unique et n'est jamais réattribué. `0000-modele.md` est le **modèle** à copier : ce n'est pas une épreuve.

Le journal est aussi affiché sur le site : une page du journal liste les épreuves, et chaque fiche renvoie à ses épreuves (spécification §13 et X8). Le fichier du dépôt fait foi.

## Pourquoi un journal

Le changelog dit ce qui a changé ; les tickets disent ce qui a été signalé. Le journal garde l'épreuve elle-même, pour qu'on puisse vérifier que le seuil a été fixé avant (§9.7 M) et refaire l'épreuve (§9.7 N).

## Format

Chaque fichier contient en tête un bloc YAML (bloc de code `yaml`, après la ligne de commentaire du modèle), suivi d'un texte libre court. Champs :

| Champ | Contenu | Écrit |
|---|---|---|
| `id` | `epreuve-<nnnn>`, le numéro du fichier | avant |
| `nature` | `programme` (compte pour le statut) ou `exploratoire` (informe, ne compte pas) | avant |
| `types`, `enonces` | les types visés (`ppp:…`) et leurs énoncés (`E1`…) | avant |
| `protocole` | ce qui est montré, à qui, dans quelles conditions, quelle question est posée | avant |
| `seuil` | le résultat qui corrobore, et celui qui ouvre une anomalie | avant |
| `seuil_fixe_le` | la date du commit de la partie « avant » | avant |
| `objets` | les objets montrés : des **objets publics** seulement (identifiants du registre, `ppp-a:…` ou objets de `fiches/exemplaires.yaml`) | avant |
| `observateurs` | nombre, pseudonymes (jamais de nom ni d'adresse), indépendants de l'équipe ou non | avant |
| `versions` | versions de la fiche, de la page publiée et du matériel montré (§9.7 G) | avant |
| `resultats` | les **résultats bruts** (ou un lien vers eux), sans les résumer à leur seule conclusion | après |
| `consequence` | `corroboré`, `anomalie ouverte`, `réfutation reproduite` (§9.7 N) ou `aucune (exploratoire)` | après |
| `tickets` | les tickets liés (`ticket-<nnnn>`) | avant ou après |

## Règle d'écriture

1. La partie « avant » est écrite et **commitée avant l'épreuve** ; la date de ce commit est `seuil_fixe_le`. On n'y touche plus ensuite.
2. La partie « après » (`resultats`, `consequence`) s'ajoute à la suite, dans un autre commit.
3. Une épreuve **sans seuil fixé avant** est `exploratoire` : elle informe la fiche, elle **ne compte pas pour le statut**. Une épreuve `programme` compte pour le statut si son seuil a été fixé avant et ses objets sont publics.
4. Une épreuve qui vise un énoncé contesté cite le ticket.
