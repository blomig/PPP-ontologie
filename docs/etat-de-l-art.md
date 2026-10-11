# PPP — État de l’art (court)

**Version** : 1.2 — 2026-10-10 — branche `spec-v2` (1.1 : §5 bis, classifications de la texture : Tamura, Mori et Yamawaki 1978 ; 1.2 : renvoi à l’état de l’art par type)
**Par type** : l’état de l’art et la bibliographie de chacun des 26 types actifs, avec le statut de vérification de chaque référence, sont dans [`bibliographie-par-type.md`](bibliographie-par-type.md) (spec §9.7 P) ; les fiches les reprennent (champs `references`, `etat_de_l_art`).
**Objet** : situer l’ontologie PPP par rapport aux travaux dont elle hérite ou dont elle se distingue. Pour chaque source : ce que PPP **reprend**, et ce en quoi PPP **se distingue**.
**Règle** : seules figurent des références vérifiées (auteur, titre, année, éditeur ou revue, DOI ou URL quand disponible ; vérification faite le 2026-10-08). Aucun numéro de page n’est cité pour une thèse précise : on renvoie à l’ouvrage, au chapitre ou à l’article. La bibliographie complète est en fin de document (§7).

---

## 1. Nanay : esthétique de l’attention, propriétés formelles et semi-formelles

**Nanay 2016** (*Aesthetics as Philosophy of Perception*) applique l’appareil de la philosophie de la perception aux questions d’esthétique. Trois éléments comptent pour PPP :

1. **Attention distribuée / focalisée.** Dans certaines expériences esthétiques paradigmatiques, l’attention est *focalisée quant à l’objet* et *distribuée quant aux propriétés* : on regarde un seul objet, mais on se rend disponible à un grand nombre de ses propriétés. Nanay appelle cela « attention esthétique » (déjà dans Nanay 2015, *JCS*). Le dernier chapitre traite des cas inverses, où l’attention n’est **pas** distribuée (identification à des personnages de fiction).
2. **Propriétés esthétiquement pertinentes** (ch. 4). Plutôt que de chercher à définir la catégorie floue des « propriétés esthétiques », Nanay parle des propriétés *pertinentes pour l’évaluation esthétique*. C’est l’ancêtre direct du « P » de PPP.
3. **Semi-formalisme** (ch. 5). Le formalisme (seules comptent les propriétés formelles : formes, couleurs, lignes de la surface) est intenable. Mais Nanay propose que les propriétés esthétiquement pertinentes soient **semi-formelles** : des propriétés qui **dépendent constitutivement** de propriétés formelles, tout en étant plus larges qu’elles (elles peuvent aussi engager des propriétés non perceptuelles, p. ex. les propriétés « design-scène » d’une image, ou en musique des propriétés qui dépendent des propriétés formelles et des émotions).

Les suites : Nanay 2018 (*The Monist*) étend l’analyse aux scènes ordinaires ; Nanay 2019 (*Aesthetics: A Very Short Introduction*) reprend la thèse attentionnelle pour un public large ; Lopes, Nanay & Riggle 2022 (*Aesthetic Life and Why It Matters*) traitent de la vie esthétique ordinaire ; Nanay 2023 (*Mental Imagery*) fournit une théorie de l’imagerie mentale utile pour le cas limite des récits (voir §2.4).

**Discussions critiques.**
- **Stokes 2016** (*NDPR*) : si l’attention esthétique est « focalisée sur l’objet, distribuée sur les propriétés », elle est bien plus répandue que Nanay ne le dit (recherche visuelle, expertise perceptive). Elle ne caractérise donc pas, à elle seule, l’esthétique.
- **Irvin, Schellekens, Nanay & Smith 2019** (symposium, *Estetika*) : Irvin soutient que l’attention distribuée est courante dans des activités non esthétiques, et que le caractère esthétique de l’expérience dépend aussi du but, de l’attitude et des propriétés prises en compte ; Nanay répond.
- **Richards 2020** (*JCS*) : l’attention esthétique se porte souvent sur des **intra-objets** (des parties perceptives propres de l’objet), pas sur l’objet entier. La condition « focalisée sur un objet » est donc trop grossière.
- **Richards 2016** (*Philosophical Psychology*) : contre Nanay 2015 (*Frontiers in Psychology*), l’attribution des propriétés esthétiquement pertinentes ne survient pas sur la seule expérience perceptive. Elle dépend aussi d’un **contexte approprié** (titre, catégorie d’œuvre ; cf. la « galerie des indiscernables » de Danto).
- **Cuccuru 2018** (*Estetika*) : partant de la conception de l’attention comme « sélection pour une tâche » (Wayne Wu), elle propose de caractériser l’attention esthétique comme « sélection pour la sélection ».
- Recensions de l’ouvrage : Hopkins 2017 (*BJA*), entre autres.

**Ce que PPP reprend.**
(a) Le critère de pertinence : une propriété *joue le rôle* de PPP si y prêter attention fait une différence à l’expérience.
(b) La stratification **formel → semi-formel** sous la forme d’une relation de dépendance constitutive explicite (`dependsOn`, base déclarée).
(c) La distribution de l’attention comme **paramètre d’un épisode**, sur deux axes : objets et propriétés.

**En quoi PPP se distingue.**
(1) PPP n’adopte pas comme thèse de son noyau que l’expérience esthétique *est* l’attention distribuée : la thèse est contestée (Stokes, Irvin, Richards, Cuccuru), et PPP n’a pas besoin d’une définition de l’esthétique. La distribution est une **variable descriptive** de l’épisode, pas un critère d’entrée.
(2) Suivant Richards 2020, l’épisode doit pouvoir cibler une **partie** de l’objet, pas seulement l’objet entier.
(3) Suivant Richards 2016, la base de dépendance d’une propriété semi-formelle peut inclure, **si elle est déclarée**, des facteurs non perceptuels (catégorie d’œuvre au sens de Walton 1970, contexte d’usage). C’est l’endroit précis où le périmètre doit être tranché (voir `questions-pour-l-editeur.md`).
(4) Chez Nanay, la pertinence est définie *relativement à l’évaluation esthétique*. PPP en garde la structure (« ça fait une différence »), mais **ne type ni le sens, ni la valeur** de cette différence : c’est la neutralité axiologique (§6 et spec §0.4).

---

## 2. Propriétés esthétiques perçues et contenu perceptuel

### 2.1 Sibley et ses héritiers
**Sibley 1959** : les concepts esthétiques (gracieux, délicat, criard…) ne sont pas gouvernés par des conditions non esthétiques suffisantes. Les appliquer demande du goût, une sensibilité. **Levinson 1984** : les propriétés esthétiques **surviennent** sur des propriétés non esthétiques, perceptuelles notamment. **Zangwill 2000 ; 2001** défend un **formalisme modéré** : certaines œuvres ont des propriétés esthétiques purement formelles, d’autres non.
*PPP reprend* : la survenance (une PPP semi-formelle dépend d’une base) et la distinction entre propriétés de base et propriétés d’organisation.
*PPP se distingue* : beaucoup de concepts sibleyens sont **épais**, c’est-à-dire à la fois descriptifs et évaluatifs (« criard »). PPP n’admet dans son cœur que des types dont la dimension descriptive peut être isolée et dont les régions ne portent pas de valence. Le statut des propriétés expressives (« froid », « calme ») reste une décision de périmètre.

### 2.2 Contenu riche ou pauvre
**Siegel 2010** défend la thèse du contenu **riche** : l’expérience visuelle représente aussi des propriétés de haut niveau (types naturels, causalité), argument par contraste phénoménal. **Bayne 2009** argumente dans le même sens. Appliqué à l’esthétique : **Stokes 2014** (pénétration cognitive et perception de l’art) et **Stokes 2018** soutiennent que des propriétés esthétiques sont parfois représentées perceptuellement. **Logue 2018** juge les arguments non concluants dans les deux sens et suggère qu’il n’y a peut-être pas de fait en la matière. **Majeed 2018** nie que les effets gestaltistes établissent la perception de propriétés esthétiques de haut niveau.
*PPP reprend* : rien ne l’oblige à trancher. PPP **décrit des types et leur base de dépendance**, et laisse ouverte la question de savoir si une PPP semi-formelle est *perçue* au sens strict ou *saisie à partir de* ce qui est perçu. C’est un choix délibéré d’engagement minimal.
*PPP se distingue* : le critère d’entrée « perceptible » de v0.1/v0.2 est trop fort tant que ce débat n’est pas tranché. La spec v2 le remplace par « **ancré perceptuellement** » : type formel, ou type semi-formel dont la base contient au moins un type formel.

### 2.3 Gestalt
**Wagemans et al. 2012** font le bilan d’un siècle de recherches sur le groupement perceptif et l’organisation figure/fond. C’est la référence empirique pour les types d’**organisation** (groupement, continuité, figure/fond) que v0.2 range parmi les semi-formels.
*PPP reprend* : ces types ont des corrélats expérimentaux. Des énoncés réfutables peuvent donc s’y appuyer.
*PPP se distingue* : PPP ne modélise pas les mécanismes. Il nomme des qualités d’organisation dans un vocabulaire d’atelier.

### 2.4 Art non perceptuel et récits (cas limite)
**Shelley 2003** : l’existence d’un art « non perceptuel » (art conceptuel, et par extension la littérature) oblige à rejeter, soit l’idée que les œuvres ont des propriétés esthétiques, soit l’idée que ces propriétés sont perceptuelles. Shelley choisit d’abandonner la seconde. Le dernier chapitre de **Nanay 2016** (attention non distribuée, personnages de fiction) et **Nanay 2023** (imagerie mentale) offrent une voie intermédiaire : des contenus narratifs qui mobilisent une **imagerie quasi perceptive**.
*Conséquence pour PPP* : les récits sont le cas limite du périmètre. Ce document ne le tranche pas (voir `questions-pour-l-editeur.md`, Q1).

---

## 3. Espaces conceptuels et dimensions intégrales / séparables

**Gärdenfors 2000** (*Conceptual Spaces*) : une propriété est une **région** (convexe dans le cas naturel) d’un **domaine**. Un domaine est un ensemble de dimensions de qualité **intégrales** (couleur : teinte, saturation, luminosité). Les concepts combinent plusieurs domaines, avec des **poids de saillance** qui dépendent du contexte. **Gärdenfors 2014** (*The Geometry of Meaning*) en tire une sémantique lexicale : les adjectifs y renvoient typiquement à des régions d’un seul domaine. La distinction intégral / séparable vient de la psychologie expérimentale de **Garner 1974**.
*PPP reprend* : type = domaine ou dimension ; étiquette verbale (« chargé ») = région, pas sous-type (axiome A2) ; `integralWith` / `separableFrom` ; échelles explicites. La comparaison de deux objets (CQ12) devient une distance dans un espace.
*PPP se distingue* : (1) la plupart des espaces PPP sont **ordinaux ou nominaux**, pas métriques ; PPP ne présuppose pas de métrique. (2) Les poids de saillance de Gärdenfors appartiennent au *concept* ; dans PPP, la pondération attentionnelle appartient à l’**épisode** (P3), ce qui rapproche Gärdenfors de Nanay sans les confondre. (3) Les relateurs (assemblage, contraste) n’ont pas d’analogue simple dans un espace de qualités d’un seul porteur.

---

## 4. Ontologies fondationnelles et méthode

**DOLCE** (Masolo et al. 2003 ; Borgo et al. 2022) distingue la **qualité** individuelle (la couleur de *cette* rose), qui inhère à une entité, sa **valeur** (quale) et l’**espace de qualités** où se situe le quale. Engagement « descriptif », orienté vers les catégories cognitives et linguistiques.
*PPP reprend* : le triplet qualité / quale / espace (patron P1) et la posture descriptive.
*PPP se distingue* : PPP n’importe pas tout DOLCE. Il en garde la distinction qualité/valeur et l’inhérence, et ajoute des sortes propres : relateur esthétique, épisode attentionnel, strate formel/semi-formel.

**UFO** (Guizzardi 2005 ; Guizzardi et al. 2022) : *moments* (tropes) intrinsèques, c’est-à-dire qualités et modes, et **relateurs** qui médient plusieurs entités. Les **structures de qualités** de UFO reprennent explicitement Gärdenfors (cf. aussi Guizzardi, Masolo & Borgo 2006). UFO type aussi les universaux selon la rigidité : *kind*, *role*, *phase*.
*PPP reprend* : le patron P2 Relator (mode d’assemblage, contraste) ; « être PPP » comme **rôle** anti-rigide ; les structures de qualités.
*PPP se distingue* : PPP reste semi-informel dans ce cycle, sans OntoUML ni OWL. La pertinence n’est pas un rôle joué par un objet mais par une **qualité dans un épisode**.

**OntoClean** (Guarino & Welty 2002 ; 2009) : méta-propriétés (rigidité, identité, unité, dépendance) et contraintes sur la subsomption (un anti-rigide ne subsume pas un rigide).
*PPP reprend* : les étiquettes OntoClean de la fiche de type et l’axiome A3.

**BFO** (Arp, Smith & Spear 2015) et les **patrons de conception** (Gangemi & Presutti 2009) sont cités pour la méthode. PPP retient les patrons Entity–Quality–Value, n-aire / relateur et Situation. Il n’adopte pas BFO comme ontologie fondationnelle : l’engagement réaliste fort de BFO sur les universaux va au-delà de ce dont PPP a besoin.

---

## 5. Ontologies et vocabulaires du domaine

- **CIDOC CRM** (ISO 21127:2023 ; version communautaire 7.1.3) : ontologie de référence du patrimoine, centrée sur les événements. Elle offre `E26 Physical Feature`, `E54 Dimension` (grandeurs mesurées) et `E55 Type` (`P2 has type`). Elle ne modélise ni les qualités perçues, ni l’attention.
  *Pont* : les types PPP peuvent être exposés comme `E55 Type` pour annoter des objets décrits en CRM.
  *Distinction* : une qualité perçue PPP n’est pas une `E54 Dimension` mesurée.
- **Getty AAT** : thésaurus dont la facette *Physical Attributes* rassemble les « caractéristiques perceptibles ou mesurables » des matériaux et artefacts (texture, dureté, forme, motifs de décor).
  *Reprise* : source de **labels** et d’alignements (`skos:closeMatch` à terme).
  *Distinction* : l’AAT est un thésaurus. Il ne type ni les sortes (qualité, relateur, épisode), ni les espaces de valeurs, ni la dépendance formel → semi-formel.
- **ICON** (Sartini et al. 2023) : ontologie des **interprétations** d’œuvres selon les niveaux de Panofsky (pré-iconographique, iconographique, iconologique), alignée sur CIDOC CRM, VIR, DOLCE.
  **VIR** (Carboni & de Luca 2019) : extension de CIDOC CRM pour les représentations visuelles, qui distingue l’objet de l’acte interprétatif.
  *Reprise* : la séparation entre l’**objet** et l’**acte** qui lui attribue quelque chose, analogue à la séparation PPP entre assertion et épisode.
  *Distinction* : ICON et VIR portent sur le **sujet et le sens** des œuvres, PPP sur leurs qualités perceptuelles et leur organisation. Le niveau pré-iconographique de Panofsky est le point de contact.
- **Emotion Ontology** (Hastings et al. 2011) : ontologie des phénomènes affectifs, dans l’écosystème BFO.
  *Distinction* : PPP exclut les émotions de son cœur. Si un outil veut relier une PPP à une réponse affective, il le fait par un pointeur depuis l’épisode, pas par un type PPP.
- **PATO** et le patron **Entité–Qualité** (Gkoutos et al. 2004) : en bio-informatique, un phénotype se décrit comme une entité + une qualité (+ une valeur), avec des qualités relationnelles.
  *Reprise* : c’est l’exemple le plus éprouvé, à grande échelle, du patron P1. Il montre qu’un vocabulaire de qualités séparé des entités reste réutilisable entre domaines, ce qui est l’argument du test de transfert.

**Constat.** À notre connaissance (recherche non exhaustive, octobre 2026), aucune ontologie publiée ne combine : (i) des qualités perceptuelles typées par sorte (qualité / relateur / épisode), (ii) une strate formel → semi-formel avec base de dépendance déclarée, (iii) un épisode attentionnel distinct des qualités d’objet, (iv) des espaces de valeurs explicites et (v) une neutralité axiologique contrôlée. C’est l’originalité revendiquée de PPP, à confirmer par une recherche bibliographique plus large.

---

## 5 bis. Classifications de propriétés perceptives : la texture (ajout du 2026-10-10)

**Tamura, Mori et Yamawaki 1978** (« Textural features corresponding to visual perception », *IEEE Trans. SMC* 8(6), 460–473). Le résumé de l'éditeur nomme six propriétés de base de la texture, formulées comme **mesures calculées** sur une image : *coarseness*, *contrast*, *directionality*, *line-likeness*, *regularity*, *roughness*. Elles ont été comparées, par corrélation de rang, aux classements de sujets humains sur 16 textures de l'album de Brodatz. Les sources secondaires concordent : la correspondance est bonne pour les trois premières, plus faible pour les trois autres, et *regularity* et *roughness* sont des combinaisons des autres mesures. Le texte intégral n'a pas été lu : définitions vérifiées sur le résumé et sur deux sources secondaires (notes de cours COMPSCI 708 de l'Université d'Auckland ; critique de M. A. Ruzon, Stanford CS328B).
*PPP reprend* : le découpage en dimensions séparées, et trois correspondances (spec §9.7 O ; tableau détaillé dans `fiches/QUESTIONS-A-TRANCHER.md`, T1). *coarseness* ≈ `ppp:texture` (taille des reliefs, `skos:closeMatch`) ; *directionality* ≈ nouveau candidat `ppp:textureDirectionality` (`skos:closeMatch`) ; *contrast*, *line-likeness*, *regularity*, *roughness* : `skos:relatedMatch` vers des types existants (contraste de clarté entre parties d'une surface, orientation de la texture, irrégularité locale, texture), sans nouvel id.
*PPP se distingue* : un type PPP est une qualité **perçue**, à régions définies par des repères publics, et non une mesure ; aucun alignement n'est déclaré exact, et les mesures ne fournissent pas les régions. Leur fragilité aux changements d'échelle et d'éclairage de l'image (relevée par Ruzon) rejoint la prudence de la spec sur la texture jugée sur photo (§9.3).

**Autres classifications repérées** (proposition, non intégrées ; liste et références dans `fiches/QUESTIONS-A-TRANCHER.md`, T20) : Haralick et al. 1973 (mesures GLCM, non perceptives) ; Amadasun et King 1989 ; Rao et Lohse 1996 et Bhushan, Rao et Lohse 1997 (dimensions perçues et lexique de la texture) ; MPEG-7 (Manjunath et al. 2001) ; Liu et Picard 1996 ; Wölfflin 1915 (catégories de style) ; Munsell 1905 (teinte, valeur, chroma).

---

## 6. Épistémologie : Popper et Lakatos

**Popper** (*Logik der Forschung*, 1934 ; trad. *The Logic of Scientific Discovery*) : un énoncé est scientifique s’il est **réfutable**. On corrobore, on ne vérifie pas. **Lakatos 1978** : un **programme de recherche** a un **noyau dur**, protégé par une heuristique négative, et une **ceinture protectrice** d’hypothèses auxiliaires qu’on ajuste. Il est **progressif** s’il prédit des faits nouveaux, dont certains sont corroborés. Il est **dégénérescent** s’il ne fait qu’absorber les anomalies par des ajustements *ad hoc*.
*PPP reprend* : la structure noyau / ceinture et les critères de progressivité et de dégénérescence, appliqués à une ontologie. Les « faits » sont ici des accords inter-observateurs, des séparabilités prédites sur des nuanciers, des transferts réussis entre régimes (spec §0.2).
*PPP se distingue* : une ontologie n’est pas une théorie empirique au sens strict. Seuls certains de ses énoncés sont testables, et la spec les isole explicitement.

---

## 7. Bibliographie (références vérifiées le 2026-10-08 ; ajouts du 2026-10-10 datés)

- Arp, R., Smith, B. & Spear, A. D. (2015). *Building Ontologies with Basic Formal Ontology*. MIT Press. DOI 10.7551/mitpress/9780262527811.001.0001
- Bayne, T. (2009). Perception and the reach of phenomenal content. *The Philosophical Quarterly*, 59(236), 385–404. DOI 10.1111/j.1467-9213.2009.631.x
- Borgo, S., Ferrario, R., Gangemi, A., Guarino, N., Masolo, C., Porello, D., Sanfilippo, E. M. & Vieu, L. (2022). DOLCE: A descriptive ontology for linguistic and cognitive engineering. *Applied Ontology*, 17(1), 45–69. DOI 10.3233/AO-210259
- Carboni, N. & de Luca, L. (2019). An ontological approach to the description of visual and iconographical representations. *Heritage*, 2(2), 1191–1210. DOI 10.3390/heritage2020078
- CIDOC CRM : ISO 21127:2023, *Information and documentation — A reference ontology for the interchange of cultural heritage information*. https://www.iso.org/standard/85100.html ; version communautaire 7.1.3 : https://cidoc-crm.org/html/cidoc_crm_v7.1.3.html
- Cuccuru, K. (2018). Aesthetic attention: A proposal to pay it more attention. *Estetika: The European Journal of Aesthetics*, 55(2), 155–179. DOI 10.33134/eeja.175
- Amadasun, M. & King, R. (1989). Textural features corresponding to textural properties. *IEEE Transactions on Systems, Man, and Cybernetics*, 19(5), 1264–1274. DOI 10.1109/21.44046 (vérifié le 2026-10-10)
- Bhushan, N., Rao, A. R. & Lohse, G. L. (1997). The texture lexicon: Understanding the categorization of visual texture terms and their relationship to texture images. *Cognitive Science*, 21(2), 219–246. DOI 10.1207/s15516709cog2102_4 (vérifié le 2026-10-10)
- Gangemi, A. & Presutti, V. (2009). Ontology design patterns. In S. Staab & R. Studer (dir.), *Handbook on Ontologies* (2e éd.), Springer, 221–243. DOI 10.1007/978-3-540-92673-3_10
- Gärdenfors, P. (2000). *Conceptual Spaces: The Geometry of Thought*. MIT Press. DOI 10.7551/mitpress/2076.001.0001
- Gärdenfors, P. (2014). *The Geometry of Meaning: Semantics Based on Conceptual Spaces*. MIT Press. DOI 10.7551/mitpress/9629.001.0001
- Garner, W. R. (1974). *The Processing of Information and Structure*. Lawrence Erlbaum ; rééd. Psychology Press, 2014. DOI 10.4324/9781315802862
- Getty Research Institute, *Art & Architecture Thesaurus*, facette « Physical Attributes » : http://vocab.getty.edu/aat/300264087
- Gkoutos, G. V., Green, E. C. J., Mallon, A.-M., Hancock, J. M. & Davidson, D. (2004). Using ontologies to describe mouse phenotypes. *Genome Biology*, 6(1), R8. DOI 10.1186/gb-2004-6-1-r8
- Guarino, N. & Welty, C. (2002). Evaluating ontological decisions with OntoClean. *Communications of the ACM*, 45(2), 61–65. DOI 10.1145/503124.503150
- Guarino, N. & Welty, C. A. (2009). An overview of OntoClean. In *Handbook on Ontologies* (2e éd.), Springer, 201–220. DOI 10.1007/978-3-540-92673-3_9
- Guizzardi, G. (2005). *Ontological Foundations for Structural Conceptual Models*. Thèse de doctorat, Université de Twente (CTIT PhD Thesis Series 05-74). https://research.utwente.nl/en/publications/ontological-foundations-for-structural-conceptual-models/
- Guizzardi, G., Masolo, C. & Borgo, S. (2006). In defense of a trope-based ontology for conceptual modeling: An example with the foundations of attributes, weak entities and datatypes. In *Conceptual Modeling – ER 2006*, LNCS 4215, Springer, 112–125. DOI 10.1007/11901181_10
- Guizzardi, G., Botti Benevides, A., Fonseca, C. M., Porello, D., Almeida, J. P. A. & Prince Sales, T. (2022). UFO: Unified Foundational Ontology. *Applied Ontology*, 17(1), 167–210. DOI 10.3233/AO-210256
- Haralick, R. M., Shanmugam, K. & Dinstein, I. (1973). Textural features for image classification. *IEEE Transactions on Systems, Man, and Cybernetics*, SMC-3(6), 610–621. DOI 10.1109/TSMC.1973.4309314 (vérifié le 2026-10-10)
- Hastings, J., Ceusters, W., Smith, B. & Mulligan, K. (2011). The Emotion Ontology: Enabling interdisciplinary research in the affective sciences. In *Modeling and Using Context (CONTEXT 2011)*, LNCS 6967, Springer, 119–123. DOI 10.1007/978-3-642-24279-3_14
- Hopkins, R. (2017). *Aesthetics as Philosophy of Perception*, by Bence Nanay [recension]. *The British Journal of Aesthetics*, 57(3), 340–344. DOI 10.1093/aesthj/ayw047
- Irvin, S., Schellekens, E., Nanay, B. & Smith, M. (2019). Is psychology relevant to aesthetics? A symposium. *Estetika: The European Journal of Aesthetics*, 56(1), 87–138. DOI 10.33134/eeja.185
- Lakatos, I. (1978). *The Methodology of Scientific Research Programmes* (Philosophical Papers, vol. 1, J. Worrall & G. Currie dir.). Cambridge University Press. DOI 10.1017/CBO9780511621123
- Levinson, J. (1984). Aesthetic supervenience. *The Southern Journal of Philosophy*, 22(S1), 93–110. DOI 10.1111/j.2041-6962.1984.tb01552.x
- Logue, H. (2018). Can we visually experience aesthetic properties? In A. Bergqvist & R. Cowan (dir.), *Evaluative Perception*, Oxford University Press. DOI 10.1093/oso/9780198786054.003.0003
- Liu, F. & Picard, R. W. (1996). Periodicity, directionality, and randomness: Wold features for image modeling and retrieval. *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 18(7), 722–733. DOI 10.1109/34.506794 (vérifié le 2026-10-10)
- Lopes, D. M., Nanay, B. & Riggle, N. (2022). *Aesthetic Life and Why It Matters*. Oxford University Press. DOI 10.1093/oso/9780197625798.001.0001
- Majeed, R. (2018). Do gestalt effects show that we perceive high-level aesthetic properties? *Analysis*, 78(3), 440–450. DOI 10.1093/analys/any002
- Manjunath, B. S., Ohm, J.-R., Vasudevan, V. V. & Yamada, A. (2001). Color and texture descriptors. *IEEE Transactions on Circuits and Systems for Video Technology*, 11(6), 703–715. DOI 10.1109/76.927424 (vérifié le 2026-10-10)
- Masolo, C., Borgo, S., Gangemi, A., Guarino, N. & Oltramari, A. (2003). *WonderWeb Deliverable D18: Ontology Library (final)*. ISTC-CNR. http://www.loa.istc.cnr.it/old/Papers/D18.pdf
- Munsell, A. H. (1905). *A Color Notation*. Boston : G. H. Ellis ; 2e éd. 1907, Project Gutenberg n° 26054, https://www.gutenberg.org/ebooks/26054 (vérifié le 2026-10-10)
- Nanay, B. (2015). Aesthetic attention. *Journal of Consciousness Studies*, 22(5–6), 96–118. https://philpapers.org/rec/NANAA-2
- Nanay, B. (2015). Cognitive penetration and the gallery of indiscernibles. *Frontiers in Psychology*, 5, 1527. DOI 10.3389/fpsyg.2014.01527
- Nanay, B. (2016). *Aesthetics as Philosophy of Perception*. Oxford University Press. DOI 10.1093/acprof:oso/9780199658442.001.0001
- Nanay, B. (2018). The aesthetic experience of artworks and everyday scenes. *The Monist*, 101(1), 71–82. DOI 10.1093/monist/onx037
- Nanay, B. (2019). *Aesthetics: A Very Short Introduction*. Oxford University Press. DOI 10.1093/actrade/9780198826613.001.0001
- Nanay, B. (2023). *Mental Imagery: Philosophy, Psychology, Neuroscience*. Oxford University Press. DOI 10.1093/oso/9780198809500.001.0001
- Popper, K. (1934). *Logik der Forschung*. Springer, Vienne ; trad. angl. *The Logic of Scientific Discovery*, Hutchinson, 1959 ; rééd. Routledge. DOI (rééd. Routledge) 10.4324/9780203994627
- Rao, A. R. & Lohse, G. L. (1996). Towards a texture naming system: Identifying relevant dimensions of texture. *Vision Research*, 36(11), 1649–1669. DOI 10.1016/0042-6989(95)00202-2 (vérifié le 2026-10-10)
- Richards, B. (2016). Cognitive penetrability, context, and aesthetics: Nanay and Danto on the Gallery of Indiscernibles. *Philosophical Psychology*, 29(7), 981–992. DOI 10.1080/09515089.2016.1219126
- Richards, B. (2020). Forests, trees, and aesthetic attention: A reply to Nanay. *Journal of Consciousness Studies*, 27(11–12), 81–98.
- Sartini, B., Baroncini, S., van Erp, M., Tomasi, F. & Gangemi, A. (2023). ICON: An ontology for comprehensive artistic interpretations. *Journal on Computing and Cultural Heritage*, 16(3). DOI 10.1145/3594724
- Ruzon, M. A. Critique de Tamura, Mori et Yamawaki (1978), cours CS328B, Stanford ; copie : https://cmp.felk.cvut.cz/cmp/courses/dzo/resources/course_texture_tomasi/critiques/tamura78.html (source secondaire, consultée le 2026-10-10)
- Shelley, J. (2003). The problem of non-perceptual art. *The British Journal of Aesthetics*, 43(4), 363–378. DOI 10.1093/bjaesthetics/43.4.363
- Sibley, F. (1959). Aesthetic concepts. *The Philosophical Review*, 68(4), 421–450. DOI 10.2307/2182502
- Siegel, S. (2010). *The Contents of Visual Experience*. Oxford University Press. DOI 10.1093/acprof:oso/9780195305296.001.0001
- Stokes, D. (2014). Cognitive penetration and the perception of art. *Dialectica*, 68(1), 1–34. DOI 10.1111/1746-8361.12049
- Stokes, D. (2016). Recension de B. Nanay, *Aesthetics as Philosophy of Perception*. *Notre Dame Philosophical Reviews*, 2016.08.10. https://ndpr.nd.edu/reviews/aesthetics-as-philosophy-of-perception/
- Stokes, D. (2018). Rich perceptual content and aesthetic properties. In A. Bergqvist & R. Cowan (dir.), *Evaluative Perception*, Oxford University Press. DOI 10.1093/oso/9780198786054.003.0002
- Tamura, H., Mori, S. & Yamawaki, T. (1978). Textural features corresponding to visual perception. *IEEE Transactions on Systems, Man, and Cybernetics*, 8(6), 460–473. DOI 10.1109/TSMC.1978.4309999 (vérifié le 2026-10-10 : métadonnées Crossref, résumé IEEE Xplore ; texte intégral non lu)
- Université d'Auckland, COMPSCI 708, « CBIR: Texture Features » (notes de cours, G. Gimel'farb) : https://www.cs.auckland.ac.nz/courses/compsci708s1c/lectures/Glect-html/topic4c708FSC.htm (source secondaire, consultée le 2026-10-10)
- Wagemans, J., Elder, J. H., Kubovy, M., Palmer, S. E., Peterson, M. A., Singh, M. & von der Heydt, R. (2012). A century of Gestalt psychology in visual perception: I. Perceptual grouping and figure–ground organization. *Psychological Bulletin*, 138(6), 1172–1217. DOI 10.1037/a0029333
- Walton, K. L. (1970). Categories of art. *The Philosophical Review*, 79(3), 334–367. DOI 10.2307/2183933
- Wölfflin, H. (1915). *Kunstgeschichtliche Grundbegriffe: Das Problem der Stilentwickelung in der neueren Kunst*. Munich : F. Bruckmann. Fac-similé : Universitätsbibliothek Heidelberg, DOI 10.11588/diglit.27250 (vérifié le 2026-10-10)
- Zangwill, N. (2000). In defence of moderate aesthetic formalism. *The Philosophical Quarterly*, 50(201), 476–493. DOI 10.1111/1467-9213.00201
- Zangwill, N. (2001). *The Metaphysics of Beauty*. Cornell University Press. DOI 10.7591/9781501711350

*Non discutés ici* : Alexander (*The Nature of Order*) et Greimas (sémiotique plastique), qu’utilise v0.2. Ils restent des **sources de candidats** (spec §7). Leur statut normatif (Alexander) ou sémiotique (Greimas) les tient hors du noyau.
