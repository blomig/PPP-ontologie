# PPP — Fiche d'exemplaire (gabarit)

**Version** : 1.0 — 2026-10-11 — spec v2.7 (§9.3, §9.7 G et H, §13, X16, Q12, Q15)

*Pourquoi une fiche d'exemplaire standard.* Les tests sur objets publics demandaient s'il en fallait une : **oui**. Un exemplaire réunit quatre choses qu'on doit pouvoir relire ensemble : l'objet public, les conditions dans lesquelles on l'a regardé, les assertions par type, et le crédit de l'image. Ce gabarit dit les champs ; les données vivent dans **`fiches/exemplaires.yaml`**, qui est le **registre des objets** de PPP (il n'existe pas d'autre registre dans le dépôt). Une fiche d'exemplaire est une vue de ce registre pour un objet : ses entrées `objets`, `episodes` et `assertions`.

**Règles.**
- **Objets publics seulement** (Q12). Le dépôt public ne contient que des objets publics ; il n'a pas de statut « interne ». Un objet interne n'est jamais publié et n'existe pas côté public : les objets internes vivent hors du dépôt public, et rien du dépôt ne renvoie à eux.
- **Images** (Q15) : lien seulement par défaut ; reproduite seulement si la licence est réellement libre, vérifiée, avec le crédit complet (`credit.usage`, `credit.lien_externe`, `credit.motif_usage`) (série 20 : une image hébergée sur Wikimedia Commons avec licence et balise indiquées est utilisable ; X16).
- **Un ticket n'écrit jamais dans `exemplaires.yaml`.** Un ticket `objet-suggere` recevable donne, après instruction par l'équipe, une entrée d'**objet seul** (id et crédit) ; les assertions s'ajoutent ensuite, par l'équipe ou par un ticket `assertion-exemplaire` (ajout) ou `contestation` (`docs/gouvernance.md`).
- Une assertion est ordinaire et contestable (§13) ; `doute: oui` est un champ éditorial (X17).

## 1. Objet

```yaml
objets:
  - id: app:<slug>                 # id d'application (§9.7 I), stable, jamais réattribué
    description: "<ce qu'est l'objet, sans jugement de valeur>"
    createur: "<nom, ou « inconnu »>"            # nouveau champ proposé (v1.0) ; aujourd'hui dans `description`
    date: "<date ou période, ou « inconnue »>"   # nouveau champ proposé (v1.0) ; « inconnue » admise seulement si `variante` identifie l'objet
    variante: "<version, exemplaire, état, édition : ce qui identifie exactement l'objet vu>"   # nouveau champ proposé (v1.0) ; libellé public « Quelle version exactement ? »
    institution: "<institution et n° d'inventaire, s'il y en a>"
    page_objet: "<page publique de l'objet, ou null avec la raison en commentaire>"
    image: "<page de l'image>"
    licence_affichee: "<licence de l'image>"
    auteur_image: "<auteur de la photo>"
    sorte_objet: "<tableau, objet conçu, matériau exposé…>"   # aujourd'hui `regime` (renommage proposé, docs/reponses-maquette-serie8.md)
    parties: ["#<partie>"]
    droits: "<ligne courte : licence, auteur, usage>"
    credit:                        # X16, Q15
      auteur: "…"
      licence: "…"
      source: "…"
      url: "…"
      url_telechargement: "…"     # facultatif : fichier original (série 20)
      fichier: "…"                # facultatif : nom de stockage, si image_reproduite (série 20)
      date_verification: "AAAA-MM-JJ"
      mention_requise: "…"         # telle que la licence la demande
      usage: lien_seulement        # image_reproduite | lien_seulement (défaut)
      lien_externe: "…"            # obligatoire si lien_seulement
      motif_usage: "…"             # pourquoi ce mode (licence vérifiée, où, quand)
```

## 2. Conditions de perception (épisode)

Un épisode par objet et par façon de regarder (A5 : un épisode, une cible). Vocabulaire : spec §9.7 H.

```yaml
episodes:
  - id: ppp-e:<slug>
    target: app:<slug>
    observedUnder:                 # régime complet (§9.7 H) : les cinq facettes, `unknown` si inconnue
      presentation: screen         # inHand | tableTop | wallOrShowcase | screen | printedImage | inSitu | walkThrough | unknown
      lumiere: unknown
      distance: room               # contact | near (<1 m) | room (1–5 m ; « plusieurs mètres », « dans une pièce ») | far (>5 m) | unknown
      angle: unknown
      duree: exam
    note_distance: "<comment la distance est estimée (règle 7 : pour une image, la prise de vue)>"
    usesModality: [vision]
    observer: "<l'équipe, ou un pseudonyme ; nombre d'observateurs>"
    date: "AAAA-MM-JJ"
```

## 3. Assertions par type

```yaml
assertions:
  - id: ppp-a:<slug>-<nn>          # opaque, jamais réattribué
    about: app:<slug>#<partie>      # ou l'objet entier
    assertedType: ppp:<type>
    cardStatus: applicable et pertinent
    inRegion: ppp:<type>/<clé>
    inEpisode: ppp-e:<slug>
    modality: vision
    source: photo                   # photo | objet | …
    doute: non                      # oui si l'auteur juge l'exemplaire discutable (X17)
    note: "<ce qui justifie la région, factuel>"
    ontologyVersion: "<version de l’ontologie au moment de l’assertion>"
```

Champs communs (`assertedBy`, `epistemicStatus`, `withdrawn`) : bloc `commun` du registre.

La relecture des assertions et des objets est consignée dans `fiches/exemplaires.yaml`, sous la clé `relecture_explicative` (`assertions`, `objets`, `a_relire`, `a_reconfirmer` ; clé nommée `valide_par_le_professeur` jusqu'à la série 8). Une assertion compte pour les paliers de publication (X17) seulement si elle y est relue.

## 4. Ce qu'une fiche d'exemplaire affiche (site)

L'objet (description, créateur, date, variante, lien public) ; l'image selon `credit.usage`, avec le crédit complet ; les conditions de perception ; une ligne par assertion (type, région, doute, note, statut épistémique). Rien d'interne.
