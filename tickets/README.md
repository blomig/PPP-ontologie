# Registre des tickets

Ce dossier garde la trace de chaque ticket du dépôt public une fois jugé : **un fichier par ticket**, `tickets/<nnnn>-<type>.md`, où `<nnnn>` est le numéro du ticket GitHub sur quatre chiffres (par exemple `0042-contestation.md` pour le ticket GitHub n° 42). Le numéro est unique et n'est jamais réattribué ; le fichier ne change pas de nom quand l'état change, pour que les liens restent stables. Règles complètes : `docs/gouvernance.md`, section 2.

## Quand un fichier est créé

- Le ticket GitHub reçoit à l'ouverture le label de son type et `reçu` ; aucun fichier n'existe encore.
- L'équipe juge la recevabilité dans les sept jours. Le fichier est créé quand le ticket est jugé **recevable**, ou **rejeté** (non recevable, hors périmètre, ou précision demandée restée sans réponse).
- Pendant une **précision demandée** (label `précision-demandée`), il n'y a pas encore de fichier ; la date de la demande et la date limite y sont reportées à sa création. `reçu` et `précision-demandée` sont donc des étiquettes GitHub, jamais des valeurs du champ `etat` d'un fichier.
- À la décision, le fichier passe `traité`, avec l'issue `accepté` ou `rejeté` et le motif ; le ticket GitHub reçoit les mêmes labels et il est fermé.

## Format d'une entrée

En-tête YAML entre deux lignes `---`, puis le texte du visiteur et, sous un titre `## Réponse`, la réponse datée de l'équipe. Champs communs :

```yaml
id: ticket-<nnnn>
type: objet-suggere          # un des neuf types de docs/gouvernance.md 2.4
etat: recevable              # recevable | traité
issue: null                  # accepté | rejeté (si etat = traité)
motif: null                  # obligatoire si etat = traité
recu_le: "AAAA-MM-JJ"
precision_demandee_le: null
reponse_attendue_avant: null
recevable_le: null
traite_le: null
source: github
github_issue: <numéro>
auteur: null                 # pseudonyme facultatif, jamais d'adresse électronique
langue: fr
cible: []
version_spec: "…"
version_fiche: null
liens: []
```

Plus les champs propres au type (contenu minimal, `docs/gouvernance.md` 2.4 et 2.5).

Les exemples de `docs/gouvernance.md` (section 2.5) sont fictifs, nommés `exemple-<nn>-<type>`, et n'existent que dans ce document : aucun fichier de ce dossier n'emploie le préfixe `exemple-`.
