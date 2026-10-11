# Ontologie PPP — Propriétés Perceptuelles Pertinentes
## Version 0.2 — Intégration Alexander & Greimas

> **Changelog v0.2**
> - Restructuration des propriétés formelles selon la tripartition Greimas
>   (eidétique / chromatique / topologique)
> - Enrichissement des propriétés semi-formelles avec les 15 propriétés
>   structurelles de Christopher Alexander (The Nature of Order, 2002)
> - Ajout de la propriété "Vide actif" et "Rugosité" absentes de la v0.1
> - Homogénéisation des formats de fiches
> - Les propriétés attentionnelles sont inchangées (révision prévue en v0.3)

---

## 0. Principes fondateurs

### 0.1 Définition

Une **Propriété Perceptuelle Pertinente (PPP)** est une propriété d'un objet,
d'une image, d'un son ou d'un espace :
- **perceptible** directement ou par attention dirigée
- **attentionnellement active** : le fait d'y prêter attention modifie
  l'expérience de l'objet
- **descriptible** sans recours à un jugement de valeur ou à une émotion

### 0.2 Ce que PPP n'est pas

- Un système de jugement esthétique ("c'est beau")
- Une mesure objective de qualité
- Un vocabulaire émotionnel ("ça émeut")

### 0.3 Critères d'intégration d'une nouvelle propriété

Pour être intégrée à l'ontologie, une propriété doit :
1. Être perceptible (directement ou par attention dirigée)
2. Pouvoir faire l'objet d'une attention distribuée
3. Modifier l'expérience de l'objet lorsqu'on y prête attention
4. Être descriptible indépendamment d'un jugement de valeur

### 0.4 Architecture générale

L'ontologie est organisée en trois familles :
PPP
├── 1. Propriétés formelles
│ ├── 1.1 Catégorie eidétique (formes, contours, lignes)
│ ├── 1.2 Catégorie chromatique (couleurs, valeurs, saturations)
│ └── 1.3 Catégorie topologique (positions, orientations, distributions)
├── 2. Propriétés semi-formelles
│ ├── 2.1 Propriétés d'organisation
│ ├── 2.2 Propriétés de tension
│ └── 2.3 Propriétés de présence
└── 3. Caractéristiques attentionnelles
├── 3.1 Saillance
├── 3.2 Distribution
└── 3.3 Régime d'exploration


---

## 1. Propriétés formelles

> Les propriétés formelles sont directement données à la perception.
> Elles constituent le matériau brut sur lequel opèrent les propriétés
> semi-formelles. Elles sont organisées selon la tripartition de Greimas
> (sémiotique plastique) : eidétique, chromatique, topologique.

---

### 1.1 Catégorie eidétique
*Ce qui relève des formes, contours, lignes, volumes*

#### FORME
- **Définition** : Configuration géométrique ou organique d'un élément perceptible
- **Question attentionnelle** : Quelle est la nature des formes présentes ?
  Sont-elles géométriques, organiques, hybrides ?
- **Exemples** : Cercle parfait, silhouette irrégulière, volume anguleux
- **Contre-exemples** : Une couleur sans forme définie, une texture sans contour
- **Relations** : → Contour, → Échelle, → Symétrie locale

#### CONTOUR
- **Définition** : Qualité de la limite entre une forme et son environnement
- **Question attentionnelle** : Les limites sont-elles nettes, floues,
  interrompues, progressives ?
- **Exemples** : Bord franc d'un objet découpé, lisière floue d'une ombre
- **Contre-exemples** : Une transition de couleur sans changement de forme
- **Relations** : → Forme, → Contraste, → Interpénétration

#### LIGNE
- **Définition** : Élément linéaire perceptible, qu'il soit tracé ou suggéré
- **Question attentionnelle** : Y a-t-il des lignes directrices ?
  Sont-elles continues, brisées, convergentes ?
- **Exemples** : Ligne d'horizon, nervure d'une feuille, joint entre deux matières
- **Contre-exemples** : Une surface uniforme sans direction perceptible
- **Relations** : → Continuité, → Direction, → Tension

#### ÉCHELLE
- **Définition** : Taille relative des éléments entre eux et par rapport
  à l'observateur
- **Question attentionnelle** : Y a-t-il des niveaux d'échelle emboîtés ?
  L'objet révèle-t-il des détails à différentes distances ?
- **Exemples** : Architecture avec détails à l'échelle humaine et à l'échelle
  urbaine, textile avec motif macro et micro
- **Contre-exemples** : Surface uniforme sans variation d'échelle
- **Relations** : → Niveaux d'échelle (Alexander), → Hiérarchie perceptive
- **Note Alexander** : Correspond directement à *Levels of scale* —
  une des propriétés les plus discriminantes de la "vie" perceptive

#### TEXTURE
- **Définition** : Qualité de surface perceptible visuellement ou tactilement
- **Question attentionnelle** : Quelle est la granularité de surface ?
  Est-elle uniforme ou variable ?
- **Exemples** : Grain du bois, trame d'un tissu, surface polie d'un métal
- **Contre-exemples** : Couleur plate sans information de surface
- **Relations** : → Rugosité, → Densité perceptive, → Matière

---

### 1.2 Catégorie chromatique
*Ce qui relève des couleurs, valeurs, saturations, luminosités*

#### TEINTE
- **Définition** : Qualité chromatique d'une couleur (sa position dans
  le spectre)
- **Question attentionnelle** : Quelles teintes sont présentes ?
  Sont-elles proches ou éloignées dans le spectre ?
- **Exemples** : Rouge vif, bleu-vert, ocre
- **Contre-exemples** : Blanc, noir, gris (absence de teinte)
- **Relations** : → Contraste chromatique, → Harmonie

#### VALEUR (LUMINOSITÉ)
- **Définition** : Degré de clarté ou d'obscurité d'une couleur ou d'une surface
- **Question attentionnelle** : Quelle est la gamme des valeurs présentes ?
  Y a-t-il des zones très claires et très sombres ?
- **Exemples** : Clair-obscur, dégradé de gris, ombre portée
- **Contre-exemples** : Surface uniformément éclairée
- **Relations** : → Contraste, → Gradient, → Profondeur perceptive

#### SATURATION
- **Définition** : Intensité ou pureté d'une couleur
- **Question attentionnelle** : Les couleurs sont-elles vives ou atténuées ?
  Y a-t-il des variations de saturation ?
- **Exemples** : Rouge saturé vs rouge désaturé (bordeaux), palette pastel
- **Contre-exemples** : Image en niveaux de gris (saturation nulle)
- **Relations** : → Intensité perceptive, → Contraste

#### LUMINOSITÉ AMBIANTE
- **Définition** : Qualité et quantité de lumière perçue dans l'ensemble
  de la scène ou de l'objet
- **Question attentionnelle** : D'où vient la lumière ? Est-elle uniforme
  ou directionnelle ? Crée-t-elle des zones d'ombre et de lumière ?
- **Exemples** : Lumière rasante qui révèle les reliefs, lumière diffuse
  qui aplatit les formes
- **Contre-exemples** : Objet sans source lumineuse identifiable
- **Relations** : → Valeur, → Contraste, → Profondeur perceptive

---

### 1.3 Catégorie topologique
*Ce qui relève des positions, orientations, distributions dans l'espace*

#### POSITION
- **Définition** : Localisation d'un élément dans l'espace perceptif
- **Question attentionnelle** : Où se situe l'élément ? Est-il central,
  périphérique, en hauteur, en bas ?
- **Exemples** : Élément centré vs décentré, objet en surplomb
- **Contre-exemples** : Élément sans relation spatiale identifiable
- **Relations** : → Centre fort, → Hiérarchie perceptive, → Symétrie

#### ORIENTATION
- **Définition** : Direction dans laquelle un élément est perçu comme
  "pointant" ou s'organisant
- **Question attentionnelle** : Y a-t-il une direction dominante ?
  Les éléments convergent-ils ou divergent-ils ?
- **Exemples** : Lignes de fuite, oblique dynamique, verticalité stable
- **Contre-exemples** : Composition sans direction perceptible
- **Relations** : → Ligne, → Tension, → Continuité

#### DISTRIBUTION
- **Définition** : Manière dont les éléments se répartissent dans l'espace
  perceptif
- **Question attentionnelle** : Les éléments sont-ils regroupés, dispersés,
  régulièrement espacés ?
- **Exemples** : Cluster dense au centre, dispersion uniforme, regroupements
  asymétriques
- **Contre-exemples** : Élément unique sans relation spatiale
- **Relations** : → Densité perceptive, → Rythme, → Non-séparabilité

#### PROFONDEUR PERCEPTIVE
- **Définition** : Sensation de profondeur ou de plan dans un espace
  bidimensionnel ou tridimensionnel
- **Question attentionnelle** : Y a-t-il des plans perceptifs distincts ?
  L'espace semble-t-il plat ou profond ?
- **Exemples** : Superposition de plans, perspective atmosphérique,
  chevauchement de formes
- **Contre-exemples** : Surface plane sans indice de profondeur
- **Relations** : → Valeur, → Échelle, → Gradient

---

## 2. Propriétés semi-formelles

> Les propriétés semi-formelles décrivent la manière dont les propriétés
> formelles s'organisent perceptivement. Elles sont enrichies des
> 15 propriétés structurelles de Christopher Alexander (*The Nature of Order*,
> 2002), intégrées là où elles apportent une nuance absente de la v0.1.
> Elles sont organisées en trois sous-familles :
> organisation, tension, présence.

---

### 2.1 Propriétés d'organisation
*Comment les éléments s'organisent entre eux*

#### HIÉRARCHIE PERCEPTIVE
- **Définition** : Existence de niveaux de dominance entre les éléments :
  certains organisent, d'autres sont organisés
- **Question attentionnelle** : Y a-t-il un élément qui organise les autres ?
  Peut-on identifier des niveaux de subordination ?
- **Exemples** : Titre dominant un texte, forme principale entourée de formes
  secondaires
- **Contre-exemples** : Composition où tous les éléments ont le même poids
- **Relations** : → Centre fort (Alexander), → Saillance, → Distribution
- **Note Alexander** : *Strong centers* — un centre fort n'est pas seulement
  ce qui attire l'œil, c'est ce qui *organise* le reste de la composition

#### NIVEAUX D'ÉCHELLE
- **Définition** : Présence de plusieurs niveaux de détail emboîtés,
  perceptibles à différentes distances ou résolutions
- **Question attentionnelle** : L'objet révèle-t-il des structures à
  différentes échelles ? Y a-t-il des détails dans les détails ?
- **Exemples** : Façade avec détails architecturaux à l'échelle humaine
  et à l'échelle urbaine, motif fractal
- **Contre-exemples** : Surface uniforme sans variation d'échelle
- **Relations** : → Échelle (formel), → Densité perceptive, → Rugosité
- **Note Alexander** : *Levels of scale* — propriété très discriminante
  de la richesse perceptive

#### SYMÉTRIE LOCALE
- **Définition** : Présence de symétries partielles, locales, non nécessairement
  globales
- **Question attentionnelle** : Y a-t-il des zones de symétrie locale ?
  La symétrie est-elle globale ou fragmentée ?
- **Exemples** : Visage humain (symétrie locale imparfaite), ornement
  avec répétitions symétriques locales
- **Contre-exemples** : Symétrie globale parfaite (moins vivante selon
  Alexander), asymétrie totale
- **Relations** : → Répétition alternée, → Régularité, → Rugosité
- **Note Alexander** : Alexander distingue la symétrie locale (vivante)
  de la symétrie globale (souvent froide)

#### RÉPÉTITION ALTERNÉE
- **Définition** : Alternance rythmique de deux éléments ou motifs distincts
- **Question attentionnelle** : Y a-t-il une alternance perceptible ?
  Quel est le rythme de cette alternance ?
- **Exemples** : Colonnade (plein/vide), tissu à rayures (clair/sombre),
  rythme binaire en musique
- **Contre-exemples** : Répétition uniforme sans alternance, séquence
  aléatoire
- **Relations** : → Rythme, → Régularité, → Contraste
- **Note Alexander** : *Alternating repetition* — l'alternance crée
  une tension productive entre répétition et variation

#### INTERPÉNÉTRATION
- **Définition** : Enchevêtrement de deux formes ou espaces qui se pénètrent
  mutuellement sans se confondre
- **Question attentionnelle** : Y a-t-il des zones où deux éléments
  s'interpénètrent ? La limite entre eux est-elle ambiguë ?
- **Exemples** : Figure/fond réversible, arche qui s'intègre dans un mur,
  motifs entrelacés
- **Contre-exemples** : Éléments clairement séparés sans zone de contact
- **Relations** : → Contour, → Ambiguïté perceptive, → Tension
- **Note Alexander** : *Deep interlock & ambiguity* — l'interpénétration
  crée une richesse perceptive par l'ambiguïté productive

#### NON-SÉPARABILITÉ
- **Définition** : Degré d'intégration d'un élément dans son contexte :
  il ne peut être perçu comme isolé sans perdre sa signification perceptive
- **Question attentionnelle** : L'élément semble-t-il appartenir à son
  contexte ou pourrait-il en être extrait sans perte ?
- **Exemples** : Pierre dans un mur de pierres sèches, note dans une mélodie
- **Contre-exemples** : Objet posé sur un fond neutre sans relation
- **Relations** : → Distribution, → Continuité, → Interpénétration
- **Note Alexander** : *Not-separateness* — un élément vivant est toujours
  en relation avec ce qui l'entoure

#### ÉCHO
- **Définition** : Répétition d'une forme, d'une couleur ou d'une structure
  à différentes échelles ou dans différentes parties de la composition
- **Question attentionnelle** : Y a-t-il des formes ou des structures qui
  se répètent à différentes échelles ou en différents endroits ?
- **Exemples** : Motif architectural repris en détail de façade, couleur
  principale reprise en accent
- **Contre-exemples** : Composition sans répétition interne
- **Relations** : → Niveaux d'échelle, → Répétition alternée, → Cohérence
- **Note Alexander** : *Echoes* — les échos créent une cohérence interne
  sans uniformité

---

### 2.2 Propriétés de tension
*Comment les éléments créent des forces perceptives*

#### CONTRASTE PERCEPTIF
- **Définition** : Opposition nette entre deux propriétés perceptibles
  (forme, couleur, texture, valeur...)
- **Question attentionnelle** : Quels sont les contrastes dominants ?
  Sont-ils forts ou atténués ?
- **Exemples** : Noir sur blanc, rugueux contre lisse, grand contre petit
- **Contre-exemples** : Composition monochrome et uniforme
- **Relations** : → Teinte, → Valeur, → Tension, → Saillance
- **Note Alexander** : *Contrast* — le contraste est une des propriétés
  les plus universelles de la vie perceptive

#### TENSION
- **Définition** : Force perceptive créée par une relation non résolue
  entre deux éléments ou deux propriétés
- **Question attentionnelle** : Y a-t-il des zones de tension perceptive ?
  Quels éléments semblent "tirer" dans des directions opposées ?
- **Exemples** : Forme déséquilibrée, couleur complémentaire en opposition,
  ligne interrompue
- **Contre-exemples** : Composition entièrement résolue et équilibrée
- **Relations** : → Contraste, → Orientation, → Interpénétration

#### GRADIENT
- **Définition** : Transition progressive d'une propriété d'un état à un autre
- **Question attentionnelle** : Y a-t-il des transitions progressives ?
  Dans quelle direction vont-elles ?
- **Exemples** : Dégradé de couleur, transition de densité, fondu sonore
- **Contre-exemples** : Transition abrupte, rupture nette
- **Relations** : → Valeur, → Densité perceptive, → Continuité
- **Note Alexander** : *Gradients* — les gradients créent une direction
  perceptive et une sensation de mouvement

#### LIMITE ACTIVE
- **Définition** : Frontière entre deux zones qui ne sépare pas seulement
  mais qui relie et crée une zone de transition perceptivement riche
- **Question attentionnelle** : Les limites entre zones sont-elles actives
  ou passives ? Créent-elles une zone de transition ?
- **Exemples** : Lisière forêt/prairie, cadre d'un tableau qui dialogue
  avec le mur, joint entre deux matières
- **Contre-exemples** : Limite purement fonctionnelle sans richesse perceptive
- **Relations** : → Contour, → Interpénétration, → Gradient
- **Note Alexander** : *Boundaries* — une limite vivante sépare ET relie

#### CONTINUITÉ
- **Définition** : Propriété d'un élément ou d'une séquence à se poursuivre
  perceptivement au-delà des interruptions
- **Question attentionnelle** : Y a-t-il des lignes ou des formes qui
  continuent au-delà de leur interruption visible ?
- **Exemples** : Ligne interrompue que l'œil complète, mélodie dont on
  anticipe la suite
- **Contre-exemples** : Séquence d'éléments sans relation perceptive
- **Relations** : → Ligne, → Orientation, → Tension

---

### 2.3 Propriétés de présence
*Ce qui détermine la qualité de présence perceptive d'un objet*

#### DENSITÉ PERCEPTIVE
- **Définition** : Quantité d'information perceptive par unité de surface
  ou de temps
- **Question attentionnelle** : L'objet est-il dense ou aéré ?
  Y a-t-il des zones de densité variable ?
- **Exemples** : Partition très chargée vs partition épurée, tissu à motifs
  complexes vs tissu uni
- **Contre-exemples** : Surface uniforme sans variation
- **Relations** : → Distribution, → Niveaux d'échelle, → Vide actif

#### INTENSITÉ PERCEPTIVE
- **Définition** : Force ou puissance avec laquelle une propriété s'impose
  à la perception
- **Question attentionnelle** : Quelle est l'intensité des propriétés
  présentes ? Y a-t-il des zones d'intensité maximale ?
- **Exemples** : Couleur saturée, son fort, forme très contrastée
- **Contre-exemples** : Propriétés toutes atténuées, composition en sourdine
- **Relations** : → Saturation, → Contraste, → Saillance

#### RUGOSITÉ
- **Définition** : Présence d'irrégularités, d'imperfections ou
  d'adaptations locales qui augmentent la présence perceptive
- **Question attentionnelle** : Y a-t-il des irrégularités perceptibles ?
  Sont-elles aléatoires ou systématiques ?
- **Exemples** : Irrégularités d'un mur de pierres taillées à la main,
  variations d'un tracé calligraphique, grain d'un enregistrement analogique
- **Contre-exemples** : Surface parfaitement uniforme, reproduction
  numérique sans artefact
- **Relations** : → Texture, → Symétrie locale, → Niveaux d'échelle
- **Note Alexander** : *Roughness* — l'irrégularité n'est pas un défaut
  mais une propriété active qui augmente la vie perceptive.
  **Propriété absente de la v0.1, introduite ici.**

#### VIDE ACTIF
- **Définition** : Zone d'absence, de silence ou de vide qui joue un rôle
  perceptif actif dans la composition
- **Question attentionnelle** : Y a-t-il des zones de vide ? Sont-elles
  actives (elles font quelque chose) ou passives (elles ne font rien) ?
- **Exemples** : Ma (間) en esthétique japonaise, silence en musique,
  espace négatif en design graphique
- **Contre-exemples** : Absence non intentionnelle, fond neutre sans rôle
- **Relations** : → Densité perceptive, → Tension, → Hiérarchie perceptive
- **Note Alexander** : *The void* — le vide est une propriété à part entière,
  pas une absence de propriété. **Propriété absente de la v0.1,
  introduite ici.**

#### SIMPLICITÉ INTERNE
- **Définition** : Économie de moyens perceptifs : l'objet produit une
  expérience riche avec peu d'éléments
- **Question attentionnelle** : L'objet est-il économe ? Y a-t-il des
  éléments superflus perceptivement ?
- **Exemples** : Haïku, objet Shaker, logotype épuré
- **Contre-exemples** : Composition surchargée, redondance perceptive
- **Relations** : → Densité perceptive, → Vide actif, → Hiérarchie perceptive
- **Note Alexander** : *Simplicity & inner calm* — la simplicité n'est pas
  la pauvreté mais l'économie au service de la présence.

---

## 3. Caractéristiques attentionnelles

> Les caractéristiques attentionnelles décrivent comment l'attention
> se mobilise et se distribue lors de l'expérience perceptive.
> Cette famille est inchangée par rapport à la v0.1.
> Une révision est prévue en v0.3 (intégration du carré sémiotique
> et des régimes de valeur de Floch).

---

### 3.1 Saillance

#### SAILLANCE IMMÉDIATE
- **Définition** : Propriété d'un élément à capter l'attention
  sans effort, dès le premier regard
- **Question attentionnelle** : Qu'est-ce qui s'impose immédiatement ?
  Qu'est-ce qui "saute aux yeux" ?
- **Exemples** : Tache de couleur vive sur fond neutre, son fort dans
  un environnement calme
- **Relations** : → Contraste, → Intensité perceptive, → Centre fort

#### SAILLANCE PROGRESSIVE
- **Définition** : Propriété d'un élément à émerger à la perception
  après un temps d'observation ou d'écoute
- **Question attentionnelle** : Qu'est-ce qui apparaît avec le temps ?
  Qu'est-ce qui se révèle à l'attention soutenue ?
- **Exemples** : Détail visible seulement en s'approchant, motif rythmique
  qui émerge après plusieurs écoutes
- **Relations** : → Niveaux d'échelle, → Rugosité, → Régime d'exploration

---

### 3.2 Distribution de l'attention

#### ATTENTION FOCALISÉE
- **Définition** : Mode attentionnel où l'attention se concentre sur
  un élément ou une zone
- **Question attentionnelle** : Y a-t-il un point focal dominant ?
  L'attention est-elle contrainte ou libre ?
- **Relations** : → Centre fort, → Saillance immédiate, → Hiérarchie

#### ATTENTION DISTRIBUÉE
- **Définition** : Mode attentionnel où l'attention se répartit sur
  plusieurs éléments simultanément
- **Question attentionnelle** : L'attention peut-elle se distribuer
  librement ? Y a-t-il plusieurs foyers d'intérêt simultanés ?
- **Relations** : → Distribution, → Non-séparabilité, → Densité perceptive

---

### 3.3 Régime d'exploration

#### EXPLORATION LINÉAIRE
- **Définition** : L'objet guide l'attention selon un parcours orienté
- **Question attentionnelle** : Y a-t-il un parcours perceptif suggéré ?
  Dans quelle direction ?
- **Relations** : → Orientation, → Continuité, → Gradient

#### EXPLORATION LIBRE
- **Définition** : L'objet permet une exploration sans parcours imposé
- **Question attentionnelle** : L'attention peut-elle errer librement ?
  Y a-t-il des points d'entrée multiples ?
- **Relations** : → Distribution, → Vide actif, → Non-séparabilité

---

## 4. Index des relations avec les sources

### 4.1 Correspondances avec Alexander (*The Nature of Order*)

| Propriété Alexander | Propriété PPP v0.2 |
|---|---|
| Levels of scale | Niveaux d'échelle, Échelle |
| Strong centers | Hiérarchie perceptive, Centre fort |
| Boundaries | Limite active |
| Alternating repetition | Répétition alternée |
| Deep interlock & ambiguity | Interpénétration |
| Contrast | Contraste perceptif |
| Roughness | Rugosité *(nouveau)* |
| Echoes | Écho |
| The void | Vide actif *(nouveau)* |
| Simplicity & inner calm | Simplicité interne |
| Not-separateness | Non-séparabilité |
| Gradients | Gradient |
| Local symmetries | Symétrie locale |

> Note : *Deep interlock* et *Roughness* sont deux propriétés distinctes
> chez Alexander. Les propriétés *Inner calm* et *Simplicity* sont
> fusionnées ici en *Simplicité interne*.

---

### 4.2 Correspondances avec Greimas (sémiotique plastique)

| Catégorie Greimas | Propriétés PPP v0.2 |
|---|---|
| Eidétique | Forme, Contour, Ligne, Échelle, Texture |
| Chromatique | Teinte, Valeur, Saturation, Luminosité ambiante |
| Topologique | Position, Orientation, Distribution, Profondeur perceptive |

---

## 5. Propriétés en attente d'intégration

> Ces propriétés ont été identifiées comme pertinentes mais nécessitent
> un travail de définition supplémentaire avant intégration.

- **Matière** : Qualité perceptive du matériau (distinct de la texture)
- **Temporalité** : Propriétés liées à la durée et au changement
- **Résonance** : Propriété d'un élément à activer des associations
  perceptives (à distinguer des associations sémantiques)
- **Régime de valeur** (Floch) : Valeurs pratiques / utopiques /
  ludiques / critiques — prévu pour v0.3

---

## 6. Format de fiche PPP

> Format standard pour décrire une observation avec l'ontologie PPP.

Fiche PPP

Objet observé

[Description courte]

Propriétés formelles identifiées

Eidétique : [liste]
Chromatique : [liste]
Topologique : [liste]
Propriétés semi-formelles identifiées

Organisation : [liste]
Tension : [liste]
Présence : [liste]
Régime attentionnel

Saillance : [immédiate / progressive / mixte]
Distribution : [focalisée / distribuée / variable]
Exploration : [linéaire / libre / mixte]
Notes

[Observations libres, tensions non résolues, questions ouvertes]


---

*Ontologie PPP v0.2 — document de travail*
*Basé sur : Nanay (v0.1), Alexander (The Nature of Order, 2002),*
*Greimas (sémiotique plastique), Floch (prévu v0.3)*