# Bibliographie et état de l'art par type ou groupe de types

*Bibliographie publique de PPP, spec v2.7 (§9.7 P). Recherches et vérifications faites du 2026-10-10 au 2026-10-12 ; chaque entrée porte son statut de vérification. Complète [`etat-de-l-art.md`](etat-de-l-art.md), qui traite des sources du cadre (Nanay, Gärdenfors, OntoClean, Popper, Lakatos…) et de la texture (§5 bis).*

## Méthode

- **Règle** (spec §0.2, §9.7 P, X15) : tout emprunt à un travail existant est cité ; aucune référence n'est inventée ; une source non vérifiée est marquée comme telle.
- **Outils** : Crossref (recherche et notice par DOI), OpenAlex (résumés), Semantic Scholar, PubMed, Open Library (livres anciens), pages des éditeurs et des organismes (ISO, ASTM, OQLF, Académie française), Project Gutenberg.
- **Statuts de vérification** :
  - *vérifiée sur la source* : le contenu cité a été lu dans la source elle-même ;
  - *vérifiée sur résumé ou source secondaire* : l'existence de la référence (auteurs, titre, date, support, DOI ou notice) et son objet ont été vérifiés sur une notice, un résumé ou une source secondaire ; le texte intégral n'a pas été lu. Le champ « vérifié sur » dit exactement quoi ;
  - *non vérifiée* : rien de cela ; la référence n'est jamais présentée comme vérifiée.
- **Rôles** : *fonde* (le type ou la structure en dépend), *alimente* (fournit des distinctions, des repères ou des alignements repris), *discute* (position discutée ou en partie écartée), *contraste* (notion voisine dont PPP se distingue, par exemple une norme de mesure).
- Ce que PPP reprend ou non de chaque source est écrit dans les fiches (`references`, champs `reprend` et `ne_reprend_pas`). Ce document donne la vue par groupe.
- Les références ont été limitées à des sources solides (2 à 6 par groupe). Une recherche sans résultat est notée « aucune source trouvée », avec la date.
- **Ancres stables** (spec §9.7 P, point 4) : chaque groupe a une ancre `groupe-…`, posée par une balise `<a id="…"></a>` au-dessus de son titre ; une fiche y renvoie par `etat_de_l_art_renvoi: docs/bibliographie-par-type.md#groupe-…`. Les ancres ne changent pas quand le titre change. Liste : `groupe-texture` (texture et ses cousins), `groupe-couleur`, `groupe-forme` (forme et contour), `groupe-organisation`, `groupe-matiere` (reflets, transparence, profondeur dans la matière), `groupe-joint` (joint et assemblage), `groupe-etagement` (étagement en plans), `groupe-contrastes`, `groupe-toucher` (proposition de famille, sans fiche), `groupe-son` et `groupe-odorat` (propositions de familles, série 41, sans fiche), `groupe-gout` (proposition de famille, séries 71 et 72, texture en bouche comprise, sans fiche) ; hors groupes de types : `groupe-sources-generales`, `groupe-non-verifiees`, `groupe-spec` ; sous-sections : `brillance-categorisations`, `refs-2-5`, `mesures-couleur` (série 55), `mesures-matiere` (série 56), `mesures-forme` (série 57), `mesures-organisation` (série 58), `mesures-derniers-groupes` (série 59), `mesures-preparation` (série 61), `mesures-irregularite-interieur` (série 67) ; gouvernance des ontologies ouvertes : `groupe-gouvernance`. Les anciennes ancres (`texture-et-ses-cousins`, `couleur`, `forme-et-contour`, `organisation`, `matiere`, `joint-et-assemblage`, `etagement-en-plans`, `contrastes`) restent comme alias ; ne plus les employer.

<a id="groupe-texture"></a>
<a id="texture-et-ses-cousins"></a>
## Texture et ses cousins

Les classifications de la texture viennent surtout de la vision par ordinateur (mesures calculées sur une image, comparées ou non à des jugements humains) et, plus rarement, de la psychologie (dimensions et lexique perçus). PPP s'en sert pour des alignements (§9.7 O), jamais pour ses régions.

**Types** : `ppp:texture`, `ppp:textureDirectionality`, `ppp:localIrregularity`.

- `ppp:texture` : La perception de la texture est étudiée depuis les années 1970 en vision par ordinateur et en psychologie. Tamura, Mori et Yamawaki (1978) ont proposé six mesures calculées sur une image, comparées à des jugements humains ; la *coarseness* (le caractère plus ou moins gros du grain) correspond à la taille des reliefs. Rao et Lohse (1996) et Bhushan, Rao et Lohse (1997) ont cherché les dimensions perçues et le lexique de la texture. Les mesures de Haralick et al. (1973) servent à classer des images par calcul, sans viser la perception.
- `ppp:textureDirectionality` : La direction commune des reliefs est l'une des six dimensions de Tamura, Mori et Yamawaki (1978), mesurée sur une image (*directionality*). Liu et Picard (1996) en font l'une des trois composantes d'un modèle d'image (périodicité, direction, caractère aléatoire). Aucune source trouvée ne limite l'orientation aux reliefs, comme le fait PPP (T26).
- `ppp:localIrregularity` : La régularité d'une texture est une dimension de Tamura, Mori et Yamawaki (1978), mais composée d'autres mesures ; Liu et Picard (1996) traitent le caractère aléatoire d'une texture comme une composante séparée. Aucune source trouvée ne nomme l'écart local à une régularité comme qualité perçue. La base du type reste ouverte (T11). Série 67 (2026-10-17) : la portée s'étend à l'intérieur visible d'une matière (bulles, fils, nuages). Aucune étude de perception sur les bulles ou les inclusions n'a été trouvée ; la perception des matières translucides et transparentes est étudiée (Fleming et Bülthoff 2005 ; Motoyoshi 2010 ; revue de Gigilashvili et al. 2021), le modèle des filtres minces de Metelli (1974) convient mal à un volume, et Fleming, Jäkel et Maloney (2011) montrent que les déformations dues à un objet transparent épais servent d'indice. Pour séparer une bulle d'une piqûre, la parallaxe de mouvement (Cutting et Vishton 1995) et le reflet qui reste entier sont des positions de travail. La transparence est une condition d'accès à l'intérieur, pas une base du type. Les normes du verre comptent des défauts (sous-section `mesures-irregularite-interieur`) ; ASTM C162 donne le vocabulaire d'atelier (*seed*, *blister*, *cord*, *stone*).

**Références** :

- Tamura, H., Mori, S. & Yamawaki, T. (1978). Textural features corresponding to visual perception. IEEE Transactions on Systems, Man, and Cybernetics, 8(6), 460–473. https://doi.org/10.1109/TSMC.1978.4309999
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé IEEE Xplore ; deux sources secondaires (docs/etat-de-l-art.md §5 bis) ; texte intégral non lu ;
  - usage : `ppp:texture` (alimente); `ppp:textureDirectionality` (alimente); `ppp:localIrregularity` (discute).
- Rao, A. R. & Lohse, G. L. (1996). Towards a texture naming system: Identifying relevant dimensions of texture. Vision Research, 36(11), 1649–1669. https://doi.org/10.1016/0042-6989(95)00202-2
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé lu (OpenAlex, 2026-10-10) : vingt sujets notent et classent 56 images de l’album de Brodatz ; trois dimensions perçues de la texture (répétitif ou non ; contrasté et non orienté ou peu contrasté et orienté ; granuleux, grossier et peu complexe ou non) ; texte intégral non lu ;
  - usage : `ppp:texture` (discute).
- Bhushan, N., Rao, A. R. & Lohse, G. L. (1997). The texture lexicon: Understanding the categorization of visual texture terms and their relationship to texture images. Cognitive Science, 21(2), 219–246. https://doi.org/10.1207/s15516709cog2102_4
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé lu (OpenAlex, 2026-10-10) : classement des mots anglais de la texture en onze groupes, de « random » à « repetitive » ; trois dimensions (répétitif ou non, orientation linéaire ou circulaire, simple ou complexe) ; forte association entre mots et images de texture ; texte intégral non lu ;
  - usage : `ppp:texture` (discute).
- Haralick, R. M., Shanmugam, K. & Dinstein, I. (1973). Textural features for image classification. IEEE Transactions on Systems, Man, and Cybernetics, SMC-3(6), 610–621. https://doi.org/10.1109/TSMC.1973.4309314
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé lu (OpenAlex, 2026-10-10) : mesures de texture calculées sur les dépendances spatiales des niveaux de gris, appliquées à la classification de photos de grès, de photos aériennes et d’images satellite ; texte intégral non lu ;
  - usage : `ppp:texture` (contraste).
- Liu, F. & Picard, R. W. (1996). Periodicity, directionality, and randomness: Wold features for image modeling and retrieval. IEEE Transactions on Pattern Analysis and Machine Intelligence, 18(7), 722–733. https://doi.org/10.1109/34.506794
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé lu (OpenAlex, 2026-10-10) : modèle d’image (décomposition de Wold) en trois composantes orthogonales, « periodicity », « directionality » et « randomness », présentées comme approchant les trois dimensions les plus importantes de la perception de la texture ; texte intégral non lu ;
  - usage : `ppp:textureDirectionality` (discute); `ppp:localIrregularity` (discute).
- Gigilashvili, D., Thomas, J.-B., Hardeberg, J. Y. & Pedersen, M. (2021). Translucency perception: A review. Journal of Vision, 21(8), 4. https://doi.org/10.1167/jov.21.8.4
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé lu (2026-10-17) : le phénomène perçu dépend des conditions d’observation ; texte intégral non lu ;
  - usage : `ppp:localIrregularity` (alimente).
- Fleming, R. W., Jäkel, F. & Maloney, L. T. (2011). Visual perception of thick transparent materials. Psychological Science, 22(6), 812–820. https://doi.org/10.1177/0956797611408734
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé lu (2026-10-17) : les déformations dues aux objets transparents épais servent d’indices ; les bulles ne sont pas traitées ; texte intégral non lu ;
  - usage : `ppp:localIrregularity` (alimente).
- ASTM C162-23. Standard Terminology of Glass and Glass Products. West Conshohocken (PA) : ASTM International. https://doi.org/10.1520/C0162-23
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées (page de l’ASTM, Crossref) ; définitions de *seed*, *blister*, *cord* et *stone* lues sur une source secondaire ; texte non lu ;
  - usage : `ppp:localIrregularity` (discute ; vocabulaire d’atelier seulement).
- Metelli (1974), Fleming et Bülthoff (2005), Motoyoshi (2010) (notices : groupe matière) et Cutting et Vishton (1995) (notice : groupe étagement) : usage étendu à `ppp:localIrregularity` en série 67.

<a id="groupe-couleur"></a>
<a id="couleur"></a>
## Couleur

Les trois dimensions teinte, clarté, saturation reprennent l'organisation du système de Munsell ; la colorimétrie de la CIE fournit les grandeurs mesurées homonymes (L*, C*, angle de teinte), que PPP ne reprend pas comme régions.

**Types** : `ppp:hue`, `ppp:lightness`, `ppp:saturation`, `ppp:hueRange`, `ppp:lightnessRange`, `ppp:saturationRange`, `ppp:hueCount`.

- `ppp:hue` : La teinte est l'une des trois dimensions de Munsell (1905), avec la valeur (la clarté) et le chroma (la saturation) ; Munsell en compte dix, le système suédois NCS quatre couleurs élémentaires et des intermédiaires (Hård et Sivik 1981, d'après Hering), le dictionnaire américain ISCC-NBS dix-sept plages (Kelly et Judd 1955), et la colorimétrie de la CIE en calcule un correspondant approché, l'angle de teinte (vocabulaire international de l'éclairage, entrée « CIELAB »). Berlin et Kay (1969) trouvent onze catégories de couleur de base, dont six chromatiques en plus du brun et du rose (Kay 2015) ; Munsell et ISCC-NBS traitent le brun et le rose comme des couleurs d'une teinte, sombres ou claires.
- `ppp:lightness` : La clarté correspond à la valeur du système de Munsell (1905), « la quantité de lumière » d'une couleur selon lui, et la colorimétrie de la CIE en calcule un correspondant approché, L* (vocabulaire international de l'éclairage). Gilchrist (2006) consacre un livre à la perception du clair et du sombre ; son résumé rappelle que la lumière renvoyée par une surface ne dit pas, à elle seule, si elle est blanche, grise ou noire, puisqu'elle dépend de l'éclairage (livre non lu). PPP ne reprend aucune échelle mesurée : les régions sont des repères perçus.
- `ppp:saturation` : La saturation correspond au chroma du système de Munsell (1905) et au chroma C* de la colorimétrie CIE. Les modèles d'apparence des couleurs font l'objet d'un ouvrage de Fairchild (2013), non lu ici. PPP retient une seule dimension perçue, à repères publics.
- `ppp:hueRange` : Le système de Munsell (1905) situe les teintes sur un cercle ; l'éventail des teintes d'une zone s'y lit comme une distance sur ce cercle. Aucune source trouvée ne propose une qualité perçue de l'écart des teintes dans une même zone, distincte du contraste entre deux zones et du nombre de couleurs. Les teintes et le cercle sont ceux de la teinte (six teintes, T6, tranché par l’éditeur du projet le 2026-10-11).
- `ppp:lightnessRange` (2.5) : Tamura, Mori et Yamawaki (1978) calculent l’étalement des niveaux de gris à l’intérieur d’une texture (leur *contrast*), proche de ce type ; Chubb, Econopouly et Landy (1994) montrent, sur des textures faites de petites cases grises, que la vue peut distinguer deux plages de même gris moyen et de même dispersion selon la répartition de leurs gris (résumé lu) ; Virtanen, Saarela et Olkkonen (2026) étudient l’effet de la variation de clarté, de chroma (saturation) et de teinte d’une plage sur la couleur moyenne perçue. Aucune source trouvée ne nomme des degrés perçus de cet écart.
- `ppp:saturationRange` (2.5) : Virtanen, Saarela et Olkkonen (2026) étudient l’effet de la variation de chroma (saturation), de clarté et de teinte d’une plage sur la couleur moyenne perçue. Aucune autre source trouvée (recherche du 2026-10-10 : Crossref, OpenAlex) ne propose une qualité perçue de l’écart des saturations dans une même zone, ni des degrés de cet écart.
- `ppp:hueCount` (2.5) : Halberda, Sires et Feigenson (2006) montrent que l’on regroupe des points par couleur et que l’on dénombre environ trois de ces ensembles d’un coup d’œil. Aucune source trouvée ne propose une qualité perçue du nombre de teintes d’une zone, ni des degrés. Les teintes comptées sont les catégories de la teinte (T6).

**Références** :

- Munsell, A. H. (1905). A Color Notation. Boston : G. H. Ellis ; 2e éd. 1907, Project Gutenberg n° 26054. https://www.gutenberg.org/ebooks/26054
  - statut : *vérifiée sur la source* ; vérifié sur : ppp:hue : texte du Project Gutenberg n° 26054 lu pour les passages cités : « Color has three dimensions » (paragraphe 8 : teinte, valeur, chroma) ; cinq teintes principales (R, Y, G, B, P) et cinq intermédiaires (YR, GY, BG, PB, RP) ; glossaire, « BROWN.--A dark color, inclined to red or yellow… » et « PINK.--A red color of low chroma, but high luminosity, inclining toward purple » ; texte non lu en entier | ppp:lightness : texte du Project Gutenberg n° 26054 lu pour le passage cité : « Color has three dimensions » (paragraphe 8) : la teinte, la valeur (« the amount of light », la quantité de lumière) et le chroma (la pureté) ; texte non lu en entier | ppp:saturation : texte du Project Gutenberg n° 26054 lu pour le passage cité : « Color has three dimensions » (paragraphe 8) : la teinte, la valeur et le chroma (« the purity or CHROMA », la pureté) ; texte non lu en entier | ppp:hueRange : texte du Project Gutenberg n° 26054 lu pour les passages cités : « a circuit of hues » (un cercle de teintes, chapitre I) ; cinq teintes principales et cinq intermédiaires ; texte non lu en entier ;
  - usage : `ppp:hue` (alimente); `ppp:lightness` (alimente); `ppp:saturation` (alimente); `ppp:hueRange` (alimente).
- Berlin, B. & Kay, P. (1969). Basic Color Terms. Berkeley : University of California Press. https://openlibrary.org/works/OL64565W
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : notice Open Library (titre, auteurs, éditeur, 1969, OCLC 56215) ; ouvrage non lu ; la liste des onze catégories est lue dans Kay (2015, kay2015) ;
  - usage : `ppp:hue` (discute).
- CIE (2018). CIE 015:2018 Colorimetry, 4th Edition. Vienne : Commission Internationale de l'Éclairage. https://doi.org/10.25039/TR.015.2018
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées et résumé Crossref (observateurs de référence, illuminants, coordonnées d'espace couleur, écarts de couleur) ; texte payant non lu ;
  - usage : `ppp:hue` (contraste); `ppp:lightness` (contraste); `ppp:saturation` (contraste).
- CIE S 017:2020, ILV : International Lighting Vocabulary, 2e éd., entrée 17-23-076 « CIE 1976 L*a*b* colour space ». Vienne : CIE (accès libre en ligne, e-ILV). https://cie.co.at/eilvterm/17-23-076
  - statut : *vérifiée sur la source* ; vérifié sur : entrée lue en ligne le 2026-10-10 : espace couleur CIELAB, coordonnées L*, a*, b* ; note 1 : correspondants approchés de la clarté (L*, « CIE 1976 lightness »), du chroma (« CIE 1976 a,b chroma ») et de la teinte (« CIE 1976 a,b hue angle », hab = arctan(b*/a*)) ;
  - usage : `ppp:hue` (contraste) ; `ppp:lightness` (contraste) ; `ppp:saturation` (contraste) ; ajoutée en 2.5 comme appui vérifié des grandeurs mesurées homonymes (angle de teinte, L*, chroma), à la place de CIE 015:2018 non lue.
- Gilchrist, A. (2006). Seeing Black and White. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780195187168.001.0001
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé de l’éditeur lu (OpenAlex, 2026-10-10) : la lumière renvoyée par une surface ne révèle pas sa nuance de gris ; selon l’éclairage, une surface de n’importe quel gris peut renvoyer n’importe quelle quantité de lumière ; le livre fait l’historique des recherches et des théories de la clarté ; contenu non lu ;
  - usage : `ppp:lightness` (discute).
- Fairchild, M. D. (2013). Color Appearance Models. Wiley. https://doi.org/10.1002/9781118653128
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref (titre, auteur, 2013) ; contenu non lu ;
  - usage : `ppp:saturation` (discute).

<a id="mesures-couleur"></a>
### Mesures associées du groupe couleur (rubrique `mesure`)

Rubrique `mesure` des fiches publiques de couleur (`hue`, `lightness`, `saturation`, `hueContrast`, `lightnessContrast`, `hueCount`, `hueRange`, `lightnessRange`, `saturationRange`), gabarit de `proposition-rubrique-mesure.md` (document de travail, non publié). Sources vérifiées le 2026-10-16 ; titres dans leur langue d’origine. Déjà cités dans les fiches : CIE 015:2018 (`cie015`) et l’entrée e-ILV 17-23-076 (`cie_ilv_cielab`).

- CIE S 017:2020, ILV, entrée 17-23-077 « CIE 1976 L*a*b* colour difference ». https://cie.co.at/eilvterm/17-23-077
  - statut : *vérifiée sur la source* (entrée lue : distance euclidienne entre deux stimuli dans CIELAB) ;
  - usage : `hueContrast`, `lightnessContrast` (contraste ; méthode voisine non retenue).
- ISO/CIE 11664-6:2022. Colorimetry — Part 6: CIEDE2000 colour-difference formula. https://www.iso.org/standard/82662.html
  - statut : *vérifiée sur résumé ou source secondaire* (page de l’ISO lue le 2026-10-16, résumé ; présentation de la CIE : corrections selon la clarté, le chroma, la teinte ; objets réfléchissants ou transmettants ; ni sources de lumière ni reflets spéculaires) ;
  - usage : `hueContrast` (contraste ; mesure associée indirecte).
- ASTM D2244-23. Standard Practice for Calculation of Color Tolerances and Color Differences from Instrumentally Measured Color Coordinates. https://store.astm.org/d2244-23.html
  - statut : *vérifiée sur résumé ou source secondaire* (Scope sections 1.1 et 1.2 et Significance and Use sections 5.1 et 5.2 lus) ;
  - usage : `hueContrast`, `lightnessContrast` (contraste ; méthode voisine non retenue : petites différences et tolérances).
- CIE S 017:2020, ILV, entrées 17-22-073 « saturation » et 17-22-074 « chroma ». https://cie.co.at/eilvterm/17-22-073 ; https://cie.co.at/eilvterm/17-22-074
  - statut : *vérifiée sur la source* (entrées lues le 2026-10-16 : la saturation se juge par rapport à la luminosité propre de la zone, le chroma par rapport à une zone éclairée de même qui paraît grise ou blanche) ;
  - usage : `saturation` (contraste) ; la fiche suit ce que la CIE appelle chroma ; homonyme rétabli.
- ASTM D1535-14(2018). Standard Practice for Specifying Color by the Munsell System. https://store.astm.org/d1535-14r18.html
  - statut : *vérifiée sur résumé ou source secondaire* (Scope section 1.1 lu) ;
  - usage : `hue`, `lightness`, `saturation` (contraste ; mesure associée proche).
- NIST, OSAC Lexicon, « Value (V) », d’après ANSI/ASTM E1732. https://www.nist.gov/glossary-term/41071
  - statut : *vérifiée sur la source* (valeur Munsell de 0 à 10) ;
  - usage : `lightness` (contraste).
- Peli, E. (1990). Contrast in complex images. Journal of the Optical Society of America A, 7(10), 2032–2040. https://doi.org/10.1364/JOSAA.7.002032
  - statut : *vérifiée sur résumé ou source secondaire* (Crossref, résumé OpenAlex) ;
  - usage : `lightnessContrast` (contraste ; mesure associée indirecte : contraste de luminance).

*English version.* Associated measurements of the colour group (`mesure` section), for the public colour entries listed above; sources checked on 2026-10-16; titles in their original language.

- CIE S 017:2020, ILV, entry 17-23-077 “CIE 1976 L*a*b* colour difference”: *checked against the source* (entry read); use: `hueContrast`, `lightnessContrast` (neighbouring method, not retained).
- ISO/CIE 11664-6:2022, Colorimetry — Part 6: CIEDE2000 colour-difference formula: *ISO page read on 2026-10-16* (abstract); use: `hueContrast` (indirect associated measurement).
- ASTM D2244-23, Standard Practice for Calculation of Color Tolerances and Color Differences from Instrumentally Measured Color Coordinates: *public scope read* (sections 1.1, 1.2, 5.1 and 5.2); use: `hueContrast`, `lightnessContrast` (neighbouring method, not retained: small differences and tolerances).
- CIE S 017:2020, ILV, entries 17-22-073 “saturation” and 17-22-074 “chroma”: *checked against the source* (entries read on 2026-10-16); use: `saturation`; the entry follows what the CIE calls chroma; homonym restored.
- ASTM D1535-14(2018), Standard Practice for Specifying Color by the Munsell System: *public scope read* (section 1.1); use: `hue`, `lightness`, `saturation` (close associated measurement).
- NIST, OSAC Lexicon, “Value (V)”, after ANSI/ASTM E1732: *checked against the source*; use: `lightness`.
- Peli, E. (1990), Contrast in complex images, JOSA A 7(10), 2032–2040: *checked on abstract*; use: `lightnessContrast` (indirect associated measurement: luminance contrast).

<a id="groupe-forme"></a>
<a id="forme-et-contour"></a>
## Forme et contour

Pour la netteté du bord, la courbure, la symétrie et la taille, les sources trouvées sont des études de psychophysique ou de psychologie expérimentale. Aucune ne fixe des régions perçues ; elles appuient le découpage en types ou une décision ouverte.

**Types** : `ppp:contour`, `ppp:curvature`, `ppp:symmetry`, `ppp:perceivedSize`, `ppp:outlineIndentation`, `ppp:elementaryShapeCount` (2.8, candidat).

- `ppp:contour` : La netteté d’un bord est étudiée en psychophysique, la mesure de ce que l’on perçoit : Mather et Smith (2002) mesurent à quel point on distingue deux degrés de flou, et montrent que cette distinction est grossière. En vision par ordinateur, Elder et Zucker (1998) estiment le flou d’un bord sur une image. Aucune source trouvée ne fixe des régions perçues de netteté ; l’échelle reste ouverte (T7).
- `ppp:outlineIndentation` (2.5) : Attneave (1957) a fait juger la complexité de formes non figuratives par de nombreux sujets et a rapporté ces jugements à des caractères physiques mesurables des formes (début du texte lu ; résultats non lus) ; PPP n’en reprend pas le mot « complexité », qui porte un jugement de valeur (spec §9.10), mais un caractère visible de la silhouette. Aucune source trouvée ne nomme des degrés perçus de la découpure.
- `ppp:curvature` : La courbure est étudiée en psychophysique (la mesure de ce que l’on perçoit), à la vue comme au toucher. Pont, Kappers et Koenderink (1997) montrent qu’au toucher, distinguer deux courbures dépend surtout de la longueur de contact, ce qui va dans le sens d’un jugement local, sur un tronçon déclaré (T30). Aucune source trouvée ne propose des régions perçues de courbure.
- `ppp:symmetry` : La perception de la symétrie a une littérature abondante : Treder (2010) en fait la revue, centrée sur la symétrie bilatérale (en miroir, de part et d’autre d’un axe). Koning et Wagemans (2009) montrent que symétrie et répétition se détectent différemment selon qu’elles portent sur un objet ou sur deux, ce qui touche directement T9 (la répétition par glissement, ou translation). Wagemans et al. (2012) situent la symétrie parmi les facteurs de groupement.
- `ppp:perceivedSize` : Konkle et Oliva (2011) montrent que les objets réels ont une taille vue « canonique » (celle à laquelle on tend à les dessiner ou à les imaginer), proportionnelle au logarithme de leur taille supposée dans le monde : elle croît avec cette taille, mais de moins en moins vite. Cela appuie une taille perçue rapportée à un repère (ici le corps de l’observateur, T8), plutôt qu’à la place que l’objet occupe dans le champ de vision (l’angle visuel).
- `ppp:elementaryShapeCount` : Biederman (1987) décrit la reconnaissance des objets comme un découpage de l’image en un assemblage de volumes simples, tirés d’un petit répertoire (blocs, cylindres, coins, cônes) ; voir aussi Hoffman et Richards (1984), « Parts of recognition » (titre seulement, contenu non lu). Pour le compte lui-même, les travaux sur la perception du nombre distinguent dénombrer, saisir d’un coup un petit nombre et estimer une quantité sans compter : Kaufman et al. (1949) définissent la « numérosité » comme ce qu’on discrimine d’une collection sans la compter ; Mandler et Shebo (1982) étudient la saisie immédiate d’un petit nombre (titre seulement) ; Dehaene (1992) en fait la revue. Ces travaux portent sur des collections d’éléments séparés, pas sur les volumes qui composent un objet. Aucune source trouvée (recherche du 2026-10-11 sur Crossref, OpenAlex et PubMed) ne fixe des régions perçues du nombre de formes simples nécessaires.

**Références** :

- Mather, G. & Smith, D. R. R. (2002). Blur discrimination and its relation to blur-mediated depth perception. Perception, 31(10), 1211–1219. https://doi.org/10.1068/p3254
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (OpenAlex) ;
  - usage : `ppp:contour` (alimente).
- Elder, J. H. & Zucker, S. W. (1998). Local scale control for edge detection and blur estimation. IEEE Transactions on Pattern Analysis and Machine Intelligence, 20(7), 699–716. https://doi.org/10.1109/34.689301
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (OpenAlex) ;
  - usage : `ppp:contour` (contraste).
- Pont, S. C., Kappers, A. M. L. & Koenderink, J. J. (1997). Haptic curvature discrimination at several regions of the hand. Perception & Psychophysics, 59(8), 1225–1240. https://doi.org/10.3758/BF03214210
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé PubMed (PMID 9401457) ;
  - usage : `ppp:curvature` (alimente).
- Treder, M. S. (2010). Behind the looking-glass: A review on human symmetry perception. Symmetry, 2(3), 1510–1543. https://doi.org/10.3390/sym2031510
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé lu (OpenAlex, 2026-10-10) : revue des travaux sur la perception de la symétrie ; la vue extrait la symétrie bilatérale avec beaucoup d’aisance ; la détection de la symétrie est un processus souple, en interaction avec d’autres ; article en accès libre, texte intégral non lu ;
  - usage : `ppp:symmetry` (alimente).
- Koning, A. & Wagemans, J. (2009). Detection of symmetry and repetition in one and two objects. Experimental Psychology, 56(1), 5–17. https://doi.org/10.1027/1618-3169.56.1.5
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé ;
  - usage : `ppp:symmetry` (discute).
- Wagemans, J., Elder, J. H., Kubovy, M., Palmer, S. E., Peterson, M. A., Singh, M. & von der Heydt, R. (2012). A century of Gestalt psychology in visual perception: I. Perceptual grouping and figure–ground organization. Psychological Bulletin, 138(6), 1172–1217. https://doi.org/10.1037/a0029333
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé lu (OpenAlex, 2026-10-10) : bilan d’un siècle de psychologie de la Gestalt ; principes de groupement, classiques (proximité, similarité, destin commun, bonne continuité, fermeture, symétrie, parallélisme) et nouveaux ; recherches actuelles sur le groupement et l’organisation figure-fond ; texte intégral non lu ;
  - usage : `ppp:symmetry` (alimente).
- Konkle, T. & Oliva, A. (2011). Canonical visual size for real-world objects. Journal of Experimental Psychology: Human Perception and Performance, 37(1), 23–37. https://doi.org/10.1037/a0020413
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé lu (OpenAlex, 2026-10-10) : les objets réels ont une taille vue constante à laquelle on les dessine, les imagine et préfère les voir ; elle est proportionnelle au logarithme de leur taille supposée dans le monde, et se caractérise mieux par le rapport entre l’objet et le cadre qui l’entoure que par un angle visuel fixe ;
  - usage : `ppp:perceivedSize` (alimente).
- Biederman, I. (1987). Recognition-by-components: A theory of human image understanding. Psychological Review, 94(2), 115–147. https://doi.org/10.1037/0033-295X.94.2.115
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé lu (OpenAlex, 2026-10-11) : la reconnaissance découpe l'image en un petit nombre de volumes simples (blocs, cylindres, coins, cônes) ; texte non lu ;
  - usage : `ppp:elementaryShapeCount` (alimente).
- Kaufman, E. L., Lord, M. W., Reese, T. W. & Volkmann, J. (1949). The discrimination of visual number. The American Journal of Psychology, 62(4), 498–525. https://doi.org/10.2307/1418556
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref (page initiale 498) et début du texte (OpenAlex, 2026-10-11) : la « numérosité » est ce qu'on discrimine d'une collection sans compter ; résultats non lus ;
  - usage : `ppp:elementaryShapeCount` (discute).
- Mandler, G. & Shebo, B. J. (1982). Subitizing: An analysis of its component processes. Journal of Experimental Psychology: General, 111(1), 1–22. https://doi.org/10.1037/0096-3445.111.1.1
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et notice PubMed (PMID 6460833), sans résumé, 2026-10-11 ; contenu non lu (titre seulement) ;
  - usage : `ppp:elementaryShapeCount` (contraste).
- Dehaene, S. (1992). Varieties of numerical abilities. Cognition, 44(1–2), 1–42. https://doi.org/10.1016/0010-0277(92)90049-N
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé lu (PubMed, PMID 1511583, 2026-10-11) : revue du dénombrement, de la saisie immédiate d'un petit nombre et de l'estimation d'une quantité ; texte non lu ;
  - usage : `ppp:elementaryShapeCount` (contraste).
- Hoffman, D. D. & Richards, W. A. (1984) : référence complète dans « Organisation » ; usage : `ppp:elementaryShapeCount` (contraste ; titre seulement, contenu non lu).

<a id="mesures-forme"></a>
### Mesures associées du groupe forme (rubrique `mesure`)

Rubrique `mesure` des fiches publiques de forme (`contour`, `curvature`, `outlineIndentation`, `symmetry`, `perceivedSize`), gabarit de `proposition-rubrique-mesure.md` ; sources consultées le 2026-10-16. Elder et Zucker (1998), déjà listés plus haut, gardent leur notice ; leur usage s’étend à la rubrique `mesure` de `contour` (mesure associée indirecte ; `reprend` et `ne_reprend_pas` mis à jour en série 57 bis). Aucun seuil n’est repris.

- ISO 80000-3:2019. Quantities and units — Part 3: Space and time. https://www.iso.org/standard/64974.html
  - statut : *vérifiée sur résumé ou source secondaire* (page de l’ISO lue le 2026-10-16 ; extrait public, aperçu iTeh : rayon de courbure, 3-1.12 ; courbure, 3-2) ;
  - usage : `curvature` (courbure géométrique ; mesure associée indirecte), `perceivedSize` (dimensions en mètres ; mesure associée indirecte) (contraste ; la norme définit les grandeurs sans décrire de procédé de mesure).
- ISO 9276-6:2008. Representation of results of particle size analysis — Part 6: Descriptive and quantitative representation of particle shape and morphology. https://www.iso.org/standard/39389.html
  - statut : *vérifiée sur résumé ou source secondaire* (résumé public et extrait public lus ; définitions de la solidité et de la convexité via Particle Technology Labs) ;
  - usage : `outlineIndentation` (contraste ; mesure associée proche).
- Zabrodsky, H., Peleg, S. & Avnir, D. (1995). Symmetry as a continuous feature. IEEE Transactions on Pattern Analysis and Machine Intelligence, 17(12), 1154–1166. https://doi.org/10.1109/34.476508
  - statut : *vérifiée sur résumé ou source secondaire* (Crossref, résumé OpenAlex) ;
  - usage : `symmetry` (contraste ; mesure associée indirecte, non normalisée).

*English version.* Associated measurements of the shape group (`mesure` section), for the entries listed above; sources checked on 2026-10-16; titles in their original language. Elder and Zucker (1998), listed above, keep their record; use extended to `contour` (indirect associated measurement).

- ISO 80000-3:2019, Quantities and units — Part 3: Space and time: *ISO page read on 2026-10-16; public extract (iTeh preview) read* (3-1.12, 3-2); use: `curvature` (indirect associated measurement), `perceivedSize` (indirect associated measurement); the standard defines the quantities without describing a measurement procedure.
- ISO 9276-6:2008, Representation of results of particle size analysis — Part 6: Descriptive and quantitative representation of particle shape and morphology: *public abstract and extract read*; definitions via Particle Technology Labs; use: `outlineIndentation` (close associated measurement).
- Zabrodsky, H., Peleg, S. & Avnir, D. (1995), Symmetry as a continuous feature, IEEE TPAMI 17(12), 1154–1166: *checked on abstract*; use: `symmetry` (indirect associated measurement, not standardised).

<a id="groupe-organisation"></a>
<a id="organisation"></a>
## Organisation

Densité, distribution, espace négatif et emboîtement relèvent de l'organisation perceptive (gestalt) ; la revue de Wagemans et al. (2012) en fait le bilan.

**Types** : `ppp:perceptualDensity`, `ppp:distribution`, `ppp:negativeSpace`, `ppp:partNesting`.

- `ppp:perceptualDensity` : Durgin (1995) étudie la densité de texture perçue, qu’il distingue du nombre d’éléments et de leur répartition, et montre qu’elle s’adapte : après une longue exposition, la densité vue change. La densité au sens physique (masse volumique) est un homonyme. Aucune source trouvée ne fixe des régions perçues de densité.
- `ppp:distribution` : Clark et Evans (1954) proposent, d'après le titre de leur article, la distance au plus proche voisin comme mesure de la répartition des individus d'une population (texte non lu) ; PPP ne reprend aucune mesure, et ses régions (groupé, aléatoire, régulier) sont des repères perçus, pas tirés de l'article. Wagemans et al. (2012) font le bilan d'un siècle de recherches sur le groupement perceptif, dont le groupement par proximité (résumé lu).
- `ppp:negativeSpace` : L'espace négatif touche à l'organisation figure-fond. Rubin (1915, *Synsoplevede Figurer*) est un ouvrage classique sur les figures vues (titre ; notice seule, contenu non lu) ; Wagemans et al. (2012) font le bilan des recherches sur le groupement perceptif et l'organisation figure-fond (résumé lu). Aucune source trouvée ne nomme une qualité perçue des espaces laissés libres lus comme des formes ; la base reste ouverte (T11).
- `ppp:partNesting` : La perception de structures hiérarchiques (des parties dans des parties) est étudiée depuis Navon (1977), qui compare traits globaux et locaux (l’ensemble et les détails), et Palmer (1977), qui décrit la représentation perceptive comme hiérarchique. Hoffman et Richards (1984) étudient la décomposition d’une forme en parties. Aucune source trouvée ne fixe des régions perçues du nombre de niveaux.

**Références** :

- Durgin, F. H. (1995). Texture density adaptation and the perceived numerosity and distribution of texture. Journal of Experimental Psychology: Human Perception and Performance, 21(1), 149–169. https://doi.org/10.1037/0096-1523.21.1.149
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (OpenAlex) ;
  - usage : `ppp:perceptualDensity` (alimente).
- Clark, P. J. & Evans, F. C. (1954). Distance to nearest neighbor as a measure of spatial relationships in populations. Ecology, 35(4), 445–453. https://doi.org/10.2307/1931034
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref (titre, revue, pages) ; aucun résumé (Crossref, OpenAlex, 2026-10-10) ; texte non lu ;
  - usage : `ppp:distribution` (alimente).
- Wagemans, J., Elder, J. H., Kubovy, M., Palmer, S. E., Peterson, M. A., Singh, M. & von der Heydt, R. (2012). A century of Gestalt psychology in visual perception: I. Perceptual grouping and figure–ground organization. Psychological Bulletin, 138(6), 1172–1217. https://doi.org/10.1037/a0029333
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé lu (OpenAlex, 2026-10-10) : bilan d’un siècle de psychologie de la Gestalt ; principes de groupement, classiques (proximité, similarité, destin commun, bonne continuité, fermeture, symétrie, parallélisme) et nouveaux ; recherches actuelles sur le groupement et l’organisation figure-fond ; texte intégral non lu ;
  - usage : `ppp:distribution` (alimente); `ppp:negativeSpace` (alimente).
- Rubin, E. (1915). Synsoplevede Figurer. Copenhague : Gyldendal. https://openlibrary.org/works/OL42725131W
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : notice Open Library (titre, auteur, 1915, Gyldendal ; pas de description) ; contenu non lu ;
  - usage : `ppp:negativeSpace` (discute).
- Navon, D. (1977). Forest before trees: The precedence of global features in visual perception. Cognitive Psychology, 9(3), 353–383. https://doi.org/10.1016/0010-0285(77)90012-3
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref (titre, revue) ; résumé non disponible, texte non lu ;
  - usage : `ppp:partNesting` (discute).
- Palmer, S. E. (1977). Hierarchical structure in perceptual representation. Cognitive Psychology, 9(4), 441–474. https://doi.org/10.1016/0010-0285(77)90016-0
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref (titre, revue) ; résumé non disponible, texte non lu ;
  - usage : `ppp:partNesting` (alimente).
- Hoffman, D. D. & Richards, W. A. (1984). Parts of recognition. Cognition, 18(1–3), 65–96. https://doi.org/10.1016/0010-0277(84)90022-2
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et notice PubMed (PMID 6543164), sans résumé ; contenu non lu ;
  - usage : `ppp:partNesting` (discute).

<a id="groupe-matiere"></a>
<a id="matiere"></a>
## Matière : reflets, transparence, profondeur dans la matière

Brillance, transparence et profondeur dans la matière sont étudiées en perception des matériaux, surtout depuis les années 2000. Les normes de mesure (ISO 2813, ASTM D1003) définissent des grandeurs homonymes, que PPP distingue de la qualité vue.

**Types** : `ppp:surfaceGloss`, `ppp:translucency`, `ppp:subsurfaceDepth`.

- `ppp:surfaceGloss` : La brillance perçue a une littérature récente : Pellacini, Ferwerda et Greenberg (2000) dégagent ses dimensions perçues à partir de jugements humains ; Motoyoshi et al. (2007) relient le brillant perçu à des mesures simples calculées sur l'image ; Fleming (2014) soutient que la vue reconnaît les matériaux à leur aspect, sans retrouver leurs propriétés physiques. Hunter (1937) distingue six sortes de brillance, dont la netteté de l'image réfléchie, voisine de ce type ; Leloup et al. (2014) rappellent que la mesure de brillant faite par un appareil ne prédit pas bien la brillance vue, et Fleming, Dror et Adelson (2003) que le jugement dépend de l'éclairage. Dans ce qui en a été lu (résumés, pages d'éditeur), aucune ne nomme des niveaux perçus. La mesure de brillant des normes (ISO 2813, ASTM D523) porte le même nom sans être ce type ; le mot « brillance » est aussi l'ancien nom de la luminance (OQLF, Académie française).
- `ppp:translucency` : La perception de la transparence a été modélisée par Metelli (1974) pour des filtres minces ; Fleming et Bülthoff (2005) montrent que les indices de ce modèle ne valent pas pour les objets translucides pleins ; Motoyoshi (2010) étudie les indices d’image qui distinguent translucide et transparent. La mesure de la lumière transmise (transmittance) et du trouble (ASTM D1003) est un homonyme.
- `ppp:subsurfaceDepth` : Fleming et Bülthoff (2005) décrivent la lumière qui entre dans une matière translucide, s’y diffuse et ressort, et l’aspect doux qui en résulte ; Fleming (2014) en fait un cas de la perception des matériaux. Aucune source trouvée ne nomme une qualité perçue de la profondeur à laquelle le regard paraît entrer dans la matière ; savoir s’il faut distinguer une ou deux profondeurs sous la surface reste ouvert (C4).

**Références** :

- Pellacini, F., Ferwerda, J. A. & Greenberg, D. P. (2000). Toward a psychophysically-based light reflection model for image synthesis. In Proceedings of the 27th Annual Conference on Computer Graphics and Interactive Techniques (SIGGRAPH 2000), ACM Press, 55–64. https://doi.org/10.1145/344779.344812
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (Semantic Scholar) ;
  - usage : `ppp:surfaceGloss` (alimente).
- Motoyoshi, I., Nishida, S., Sharan, L. & Adelson, E. H. (2007). Image statistics and the perception of surface qualities. Nature, 447(7141), 206–209. https://doi.org/10.1038/nature05724
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé PubMed (PMID 17443193) ;
  - usage : `ppp:surfaceGloss` (alimente).
- Fleming, R. W. (2014). Visual perception of materials and their properties. Vision Research, 94, 62–75. https://doi.org/10.1016/j.visres.2013.11.004
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (OpenAlex) ;
  - usage : `ppp:surfaceGloss` (alimente); `ppp:subsurfaceDepth` (discute).
- ISO 2813:2014. Paints and varnishes — Determination of gloss value at 20°, 60° and 85°. Genève : ISO. https://www.iso.org/standard/56807.html
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : page de l'éditeur (résumé : méthode de mesure du brillant des revêtements, géométries 20°, 60° ou 85°, revêtements non texturés sur substrat plan et opaque) ; texte payant non lu ;
  - usage : `ppp:surfaceGloss` (contraste).
- Office québécois de la langue française, Grand dictionnaire terminologique, fiches « brillance » (peinture, contrôle de la qualité des peintures, 1983) et « luminance lumineuse » (photométrie, 1993). https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8885899/brillance ; https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8876545/luminance-lumineuse
  - statut : *vérifiée sur la source* ; vérifié sur : fiches lues en ligne le 2026-10-10. Fiche 8885899 « brillance » (peinture, 1983) : appellation ancienne, encore quelquefois utilisée, de la luminosité d’une surface qui émet un rayonnement lumineux ; la CIE ne retient que « luminosité » ; emploi déconseillé pour la confusion entre « brillance » (réflexion diffuse) et « brillant » (réflexion régulière). Fiche 8876545 « luminance lumineuse » : « brillance », marqué désuet, ancien nom de la luminance lumineuse, encore en usage en astronomie ;
  - usage : `ppp:surfaceGloss` (contraste).
- Académie française, Dictionnaire de l'Académie française, 9e édition, article « brillance ». https://www.dictionnaire-academie.fr/article/A9B2144
  - statut : *vérifiée sur la source* ; vérifié sur : article lu en ligne : physique, astronomie, « on dit plutôt Luminance » ;
  - usage : `ppp:surfaceGloss` (contraste).
- Metelli, F. (1974). The perception of transparency. Scientific American, 230(4), 90–98. https://doi.org/10.1038/scientificamerican0474-90
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref ; résumé non disponible ; décrit comme modèle des filtres minces par une source secondaire (résumé de Fleming et Bülthoff 2005) ; texte non lu ;
  - usage : `ppp:translucency` (discute).
- Fleming, R. W. & Bülthoff, H. H. (2005). Low-level image cues in the perception of translucent materials. ACM Transactions on Applied Perception, 2(3), 346–382. https://doi.org/10.1145/1077399.1077409
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (OpenAlex) ;
  - usage : `ppp:translucency` (alimente); `ppp:subsurfaceDepth` (alimente).
- Motoyoshi, I. (2010). Highlight–shading relationship as a cue for the perception of translucent and transparent materials. Journal of Vision, 10(9), 6. https://doi.org/10.1167/10.9.6
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (Semantic Scholar) ;
  - usage : `ppp:translucency` (alimente).
- ASTM D1003-21. Standard Test Method for Haze and Luminous Transmittance of Transparent Plastics. West Conshohocken : ASTM International. https://store.astm.org/d1003-21.html
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : page de l'éditeur (domaine d'application, usage : mesure du trouble et de la transmittance lumineuse) ; texte payant non lu ;
  - usage : `ppp:translucency` (contraste).

<a id="mesures-matiere"></a>
### Mesures associées du groupe matière (rubrique `mesure`)

Rubrique `mesure` des fiches publiques de surface et de matière (`surfaceGloss`, `translucency`, `subsurfaceDepth`, et, rangées au groupe texture, `texture`, `textureDirectionality`, `localIrregularity`), gabarit de `proposition-rubrique-mesure.md` ; sources consultées le 2026-10-16. Les références déjà listées plus haut (ISO 2813, ASTM D523, ASTM D1003) gardent leur notice ; leur usage s’étend à la rubrique `mesure`. Aucun seuil n’est repris.

- ASTM D5767-18. Standard Test Method for Instrumental Measurement of Distinctness-of-Image (DOI) Gloss of Coated Surfaces. https://store.astm.org/d5767-18.html
  - statut : *vérifiée sur résumé ou source secondaire* (Scope, sections 1.1 à 1.3 et 4.2 à 4.5, lus sur la page de l’éditeur ; texte payant non lu) ;
  - usage : `surfaceGloss` (contraste ; mesure associée proche : netteté de l’image réfléchie).
- ASTM E430-19. Standard Test Methods for Measurement of Gloss of High-Gloss Surfaces by Abridged Goniophotometry. https://store.astm.org/e0430-19.html
  - statut : *vérifiée sur résumé ou source secondaire* (Scope, sections 1.1 à 1.3, lu sur la page de l’éditeur ; texte payant non lu) ;
  - usage : `surfaceGloss` (contraste).
- ISO 14782:2021. Plastics — Determination of haze for transparent materials. https://www.iso.org/standard/81840.html
  - statut : *vérifiée sur résumé ou source secondaire* (page de l’ISO lue le 2026-10-16, résumé ; confirmée en 2026) ;
  - usage : `translucency` (contraste ; mesure associée proche, avec ASTM D1003).
- ISO 13468-1:2019. Plastics — Determination of the total luminous transmittance of transparent materials — Part 1: Single-beam instrument. https://www.iso.org/standard/77312.html
  - statut : *vérifiée sur résumé ou source secondaire* (page de l’ISO lue le 2026-10-16, résumé ; confirmée en 2024) ;
  - usage : `translucency` (contraste ; mesure associée indirecte).
- ISO 21920-2:2021. Geometrical product specifications (GPS) — Surface texture: Profile — Part 2: Terms, definitions and surface texture parameters. https://www.iso.org/standard/72226.html
  - statut : *vérifiée sur résumé ou source secondaire* (page de l’ISO lue : remplace ISO 4287:1997, retirée le 2021-12-20 avec son amendement 1:2009 et ses rectificatifs 1:1998 et 2:2005, ainsi qu’ISO 13565-2 et -3 ; elle-même au stade « à réviser », 90.92 du 2025-10-07, une ISO/CD 21920-2 en préparation) ;
  - usage : `texture` (contraste ; mesure associée indirecte : rugosité de profil) ; `localIrregularity` (méthode voisine non retenue).
- ISO 25178-2:2021. Geometrical product specifications (GPS) — Surface texture: Areal — Part 2: Terms, definitions and surface texture parameters. https://www.iso.org/standard/74591.html
  - statut : *vérifiée sur résumé ou source secondaire* (page de l’ISO et sommaire de l’extrait public lus ; symboles d’après NPL, Measurement Good Practice Guide No. 116 (2010), table 1, fondé sur le projet ISO 25178-2 ; noms confirmés par le sommaire public de l’édition 2021) ;
  - usage : `texture` (Sa, Sal), `textureDirectionality` (Str, Std) (contraste ; mesures associées proches) ; `localIrregularity` (méthode voisine non retenue).
- Petzing, J., Coupland, J. & Leach, R. K. (2010). The Measurement of Rough Surface Topography using Coherence Scanning Interferometry. Measurement Good Practice Guide No. 116. Teddington : National Physical Laboratory. https://eprintspublications.npl.co.uk/4833/1/mgpg116.pdf
  - statut : *vérifiée sur la source* (guide lu en partie : table 1, « The S parameter set ») ;
  - usage : `texture`, `textureDirectionality`, `localIrregularity` (contraste ; symboles des paramètres surfaciques).
- Jensen, H. W., Marschner, S. R., Levoy, M. & Hanrahan, P. (2001). A practical model for subsurface light transport. SIGGRAPH 2001, ACM, 511–518. https://doi.org/10.1145/383259.383319
  - statut : *vérifiée sur résumé ou source secondaire* (Crossref, résumé OpenAlex) ;
  - usage : `subsurfaceDepth` (contraste ; mesure associée indirecte, non normalisée : propriétés optiques mesurées par image).

<a id="mesures-irregularite-interieur"></a>
#### Irrégularité locale dans l’intérieur d’une matière (série 67)

Rubrique `mesure` de `localIrregularity` après l’élargissement à l’intérieur visible d’une matière ; recherche du 2026-10-17. Toujours aucune méthode robuste : ces textes comptent des défauts par rapport à un verre sans bulle et ne disent pas où l’intérieur s’écarte de sa propre régularité ; ils sont non retenus. Aucun seuil n’est repris.

- ISO 10110-18:2018. Optics and photonics — Preparation of drawings for optical elements and systems — Part 18: Stress birefringence, bubbles and inclusions, homogeneity, and striae. https://www.iso.org/standard/68155.html
  - statut : *vérifiée sur résumé ou source secondaire* (page de l’ISO lue le 2026-10-17 : publiée en 2018-12, confirmée en 2023 ; extrait public lu : définitions 3.2, notation 6.2) ; elle remplace ISO 10110-3:1996, retirée, qui n’est pas citée comme norme en vigueur ;
  - usage : `localIrregularity` (contraste ; méthode voisine non retenue).
- ISO 12543-6:2021. Glass in building — Laminated glass and laminated safety glass — Part 6: Appearance. https://www.iso.org/standard/75501.html
  - statut : *vérifiée sur résumé ou source secondaire* (page de l’ISO lue le 2026-10-17, 3e édition, remplace l’édition 2011 ; extrait public lu : domaine d’application, définitions 3.1 et 3.3) ;
  - usage : `localIrregularity` (contraste ; méthode voisine non retenue).
- ISO 12123:2018. Optics and photonics — Specification of raw optical glass. https://www.iso.org/standard/69905.html
  - statut : *vérifiée sur résumé ou source secondaire* (page de l’ISO lue le 2026-10-17 : 3e édition, confirmée en 2024 ; extrait public lu : définition de la bulle, section 4.8) ;
  - usage : `localIrregularity` (contraste ; méthode voisine non retenue).
- SCHOTT (2016). TIE-28: Bubbles and Inclusions in Optical Glass. Technical Information, version de mai 2016. https://media.schott.com/api/public/content/8c15c0495a52451e82bf70b480b0874d?download=true&v=47ebbb91
  - statut : *vérifiée sur la source* (PDF de l’éditeur lu, sections 4 et 5 : fond noir, lumière de côté, bulles vues comme des points brillants ; aire totale pour 100 cm³ ; concentration traitée à part) ;
  - usage : `localIrregularity` (contraste ; méthode voisine non retenue ; le montage d’observation sert d’exemple de lumière qui révèle l’intérieur).

*English version.* Local irregularity in the interior of a material (series 67): `mesure` section of `localIrregularity` after its widening to the visible interior of a material; search of 2026-10-17. Still no robust method: these texts count defects against bubble-free glass and do not say where the interior departs from its own regularity; they are not retained. No threshold is taken over. ISO 10110-18:2018 (replaces the withdrawn ISO 10110-3:1996), ISO 12543-6:2021 and ISO 12123:2018: *checked on abstract or secondary source* (ISO pages and public previews read on 2026-10-17); SCHOTT TIE-28 (May 2016): *checked on the source* (sections 4 and 5).

*English version.* Associated measurements of the material group (`mesure` section), for the entries listed above; sources checked on 2026-10-16; titles in their original language. ISO 2813, ASTM D523 and ASTM D1003, listed above, keep their records.

- ASTM D5767-18, Standard Test Method for Instrumental Measurement of Distinctness-of-Image (DOI) Gloss of Coated Surfaces: *checked on abstract or secondary source* (sections 1.1–1.3 and 4.2–4.5 on the publisher’s page); use: `surfaceGloss` (close associated measurement).
- ASTM E430-19, Standard Test Methods for Measurement of Gloss of High-Gloss Surfaces by Abridged Goniophotometry: *checked on abstract or secondary source* (sections 1.1–1.3 on the publisher’s page); use: `surfaceGloss`.
- ISO 14782:2021, Plastics — Determination of haze for transparent materials: *ISO page read on 2026-10-16* (abstract); use: `translucency` (close associated measurement, with ASTM D1003).
- ISO 13468-1:2019, Plastics — Determination of the total luminous transmittance of transparent materials — Part 1: Single-beam instrument: *ISO page read on 2026-10-16* (abstract); use: `translucency` (indirect associated measurement).
- ISO 21920-2:2021, Geometrical product specifications (GPS) — Surface texture: Profile — Part 2: Terms, definitions and surface texture parameters: *ISO page read* (replaces ISO 4287:1997, withdrawn on 2021-12-20; itself “to be revised”, stage 90.92, 2025-10-07); use: `texture` (indirect associated measurement); `localIrregularity` (not retained).
- ISO 25178-2:2021, Geometrical product specifications (GPS) — Surface texture: Areal — Part 2: Terms, definitions and surface texture parameters: *ISO page and public table of contents read*; symbols after NPL GPG 116, Table 1; use: `texture` (Sa, Sal), `textureDirectionality` (close associated measurements); `localIrregularity` (not retained).
- Petzing, J., Coupland, J. & Leach, R. K. (2010), The Measurement of Rough Surface Topography using Coherence Scanning Interferometry, NPL Measurement Good Practice Guide No. 116: *checked against the source* (Table 1 read); use: `texture`, `textureDirectionality`, `localIrregularity` (symbols of the areal parameters, after the draft ISO 25178-2).
- Jensen, H. W., Marschner, S. R., Levoy, M. & Hanrahan, P. (2001), A practical model for subsurface light transport, SIGGRAPH 2001, 511–518: *checked on abstract*; use: `subsurfaceDepth` (indirect associated measurement, not standardised).

### Catégorisations de la brillance (spec 2.5)
<a id="brillance-categorisations"></a>

Recherche du 2026-10-10, avant de fixer les labels de région de `ppp:surfaceGloss` : existe-t-il une catégorisation reconnue des **niveaux** de brillance perçue ?

| Source | Ce qu'elle contient (vérifié) | Statut | Ce que PPP en fait |
|---|---|---|---|
| Hunter 1937 | six **sortes** de brillance : *specular gloss* (brillant spéculaire), *sheen* (lustre aux angles rasants), *contrast gloss* (brillance de contraste), *absence-of-bloom gloss* (absence de voile), *distinctness-of-reflected-image gloss* (netteté de l'image réfléchie), *absence-of-surface-texture gloss* (absence de texture de surface) | résumé | des sortes, pas des niveaux ; `skos:relatedMatch` avec la netteté de l'image réfléchie |
| Hunter & Harold 1987 | manuel de la mesure de l'aspect (2e éd.) | comptes rendus (métadonnées) ; contenu non lu | rien de plus que Hunter 1937 |
| ISO 2813:2014 | géométries de mesure 20°, 60°, 85° | page de l'éditeur ; texte payant | classes « haute / moyenne / basse brillance » par angle : **non vérifiées** |
| ASTM D523-14(2018) | géométries 60°, 20°, 85° ; « Little information about the relation of numerical-to-perceptual intervals of specular gloss has been published » (section 5.3) | sections lues sur la page de l'éditeur | aucune classe de niveaux |
| Pellacini et al. 2000 ; Fleming et al. 2003 ; Wendt et al. 2010 ; Leloup et al. 2014 | dimensions perçues de la brillance ; rôle de l'éclairage, du mouvement et de la disparité ; perception multidimensionnelle, la mesure spéculaire ne suffit pas | résumés | aucune ne nomme de niveaux perçus |

**Conclusion.** Aucune catégorisation reconnue des niveaux ne convient : labels « mat / satiné / brillant / miroir » (décision de l’éditeur du projet), clés inchangées.

**Références ajoutées** :

- Hunter, R. S. (1937). Methods of determining gloss. Journal of Research of the National Bureau of Standards, 18(1), 19 et suiv. https://doi.org/10.6028/jres.018.006
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (OpenAlex) : six sortes de brillance (specular gloss, sheen, contrast gloss, absence-of-bloom gloss, distinctness-of-reflected-image gloss, absence-of-surface-texture gloss) ; texte intégral non lu ;
  - usage : `ppp:surfaceGloss` (alimente ; `skos:relatedMatch`).
- Hunter, R. S. & Harold, R. W. (1987). The Measurement of Appearance, 2e éd. New York : Wiley.
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : comptes rendus (Color Research & Application 13(3), 1988, https://doi.org/10.1002/col.5080130317 ; B. Rigg, Journal of the Society of Dyers and Colourists 104, 1988, https://doi.org/10.1111/j.1478-4408.1988.tb01167.x) ; livre non lu ;
  - usage : aucun champ de fiche (repérée).
- ASTM D523-14(2018). Standard Test Method for Specular Gloss. ASTM International. https://store.astm.org/d0523-14r18.html
  - statut : *vérifiée sur la source* ; vérifié sur : sections 1.1 (géométries 60°, 20° et 85°) et 5.1–5.4 (signification et usage) lues sur la page de l’éditeur ; DOI de la série : 10.1520/D0523 (Crossref) ;
  - usage : `ppp:surfaceGloss` (contraste ; phrase citée dans `grandeur_physique_homonyme`).
- Fleming, R. W., Dror, R. O. & Adelson, E. H. (2003). Real-world illumination and the perception of surface reflectance properties. Journal of Vision, 3(5), 3. https://doi.org/10.1167/3.5.3
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé : l’estimation de la réflectance (dont la brillance) est fiable sous un éclairage réaliste, et se dégrade sinon ;
  - usage : `ppp:surfaceGloss` (alimente).
- Wendt, G., Faul, F., Ekroll, V. & Mausfeld, R. (2010). Disparity, motion, and color information improve gloss constancy performance. Journal of Vision, 10(9), 7. https://doi.org/10.1167/10.9.7
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé : le mouvement, la disparité et la couleur améliorent la constance de la brillance perçue ;
  - usage : `ppp:surfaceGloss` (alimente).
- Leloup, F. B., Obein, G., Pointer, M. R. & Hanselaer, P. (2014). Toward the soft metrology of surface gloss: A review. Color Research & Application, 39(6), 559–570 (en ligne 2013). https://doi.org/10.1002/col.21846
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref (en ligne 2013) et résumé : la perception de la brillance est multidimensionnelle, et le brillancemètre spéculaire ne donne pas une base fiable pour estimer l’aspect brillant ;
  - usage : `ppp:surfaceGloss` (alimente).


### Références ajoutées en 2.5 (épreuves de la spec 2.5)
<a id="refs-2-5"></a>

- Virtanen, L., Saarela, T. & Olkkonen, M. (2026). Complex interactions between lightness, chroma, and hue in color ensemble perception. Vision Research, 246, 108868. https://doi.org/10.1016/j.visres.2026.108868
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (OpenAlex) : effet de la variation spatiale de clarté, de chroma et de teinte d'une plage de couleur sur la couleur moyenne perçue ; texte non lu ;
  - usage : `ppp:lightnessRange`, `ppp:saturationRange` (discute).
- Chubb, C., Econopouly, J. & Landy, M. S. (1994). Histogram contrast analysis and the visual segregation of IID textures. Journal of the Optical Society of America A, 11(9), 2350. https://doi.org/10.1364/JOSAA.11.002350
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé lu en entier (OpenAlex, 2026-10-10) : méthode psychophysique (analyse du contraste d’histogramme) ; textures de petites cases unies, de gris tirés au hasard ; à gris moyen et variance fixés, deux textures se distinguent seulement si la moyenne d’une certaine fonction des gris diffère ; texte non lu ;
  - usage : `ppp:lightnessRange` (alimente).
- Tamura, Mori et Yamawaki (1978), déjà listée (texture) : usage ajouté, `ppp:lightnessRange` (alimente ; `skos:relatedMatch` *contrast*).
- Halberda, J., Sires, S. A. & Feigenson, L. (2006). Multiple spatially overlapping sets can be enumerated in parallel. Psychological Science, 17(7), 572–576. https://doi.org/10.1111/j.1467-9280.2006.01746.x
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (OpenAlex) : devant des points de nombreuses couleurs mêlés, les adultes sélectionnent des sous-ensembles par couleur et en dénombrent environ trois d’un seul coup d’œil ; texte non lu ;
  - usage : `ppp:hueCount` (alimente).
- Attneave, F. (1957). Physical determinants of the judged complexity of shapes. Journal of Experimental Psychology, 53(4), 221–227. https://doi.org/10.1037/h0043921
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et début du texte (OpenAlex) : jugements de complexité de formes non figuratives par de nombreux sujets, rapportés à des caractéristiques physiques mesurables des formes ; résultats non lus ;
  - usage : `ppp:outlineIndentation` (alimente).
- Recherche sans autre résultat (2026-10-10, Crossref et OpenAlex) : qualité perçue de l'écart des saturations dans une zone (`ppp:saturationRange`).

<a id="mesures-organisation"></a>
### Mesures associées du groupe organisation (rubrique `mesure`)

Rubrique `mesure` des fiches publiques d’organisation (`distribution`, `negativeSpace`, `partNesting`, `perceptualDensity`), gabarit de `proposition-rubrique-mesure.md` ; recherche du 2026-10-16. `negativeSpace` et `partNesting` : aucune méthode robuste, aucune source de mesure citée. Clark et Evans (1954), déjà listés plus haut, gardent leur notice ; leur usage s’étend à la rubrique `mesure` de `distribution` (mesure associée indirecte, décrite d’après Krebs, ci-dessous ; article original non lu). Aucun seuil n’est repris.

- Krebs, C. J. (1999). Ecological Methodology, 2e éd. Menlo Park : Benjamin/Cummings, chap. 6 « Spatial Pattern and Indices of Dispersion », p. 191 et suiv. Lu dans la version révisée du chapitre pour la 3e édition en préparation (PDF de l’auteur, 2017) ; édition imprimée non consultée. https://www.zoology.ubc.ca/~krebs/downloads/krebs_chapter_06_2017.pdf
  - statut : *vérifiée sur la source* (chapitre lu en partie : présentation de l’indice de Clark et Evans, effet des bords) ;
  - usage : `distribution` (contraste ; source secondaire de la mesure associée indirecte).
- Rosenholtz, R., Li, Y. & Nakano, L. (2007). Measuring visual clutter. Journal of Vision, 7(2), 17. https://doi.org/10.1167/7.2.17
  - statut : *vérifiée sur résumé ou source secondaire* (Crossref, résumé OpenAlex ; rapprochement avec la densité perceptive : position de travail) ;
  - usage : `perceptualDensity` (contraste ; méthode voisine non retenue).

*English version.* Associated measurements of the organisation group (`mesure` section); search of 2026-10-16; titles in their original language. `negativeSpace` and `partNesting`: no robust method, no measurement source cited. Clark and Evans (1954), listed above, keep their record; use extended to `distribution` (indirect associated measurement, described after Krebs; original article not read).

- Krebs, C. J. (1999), Ecological Methodology, 2nd ed., Menlo Park: Benjamin/Cummings, ch. 6 “Spatial Pattern and Indices of Dispersion”, p. 191 ff. Read in the revised version of the chapter for the forthcoming 3rd edition (author’s PDF, 2017); printed edition not consulted: *checked against the source* (chapter read in part); use: `distribution` (secondary source for the indirect associated measurement).
- Rosenholtz, R., Li, Y. & Nakano, L. (2007), Measuring visual clutter, Journal of Vision 7(2), 17: *checked on abstract*; use: `perceptualDensity` (neighbouring method, not retained).

<a id="groupe-joint"></a>
<a id="joint-et-assemblage"></a>
## Joint et assemblage

Aucune source perceptive trouvée sur l'écart ou le décalage vus au joint. Les sources trouvées viennent de l'architecture (théorie du détail, culture tectonique) et engagent souvent une valeur : PPP les discute sans les reprendre.

**Types** : `ppp:jointSpacing`, `ppp:jointLevelOffset`.

- `ppp:jointSpacing` : En architecture, le détail de construction a ses textes : l'article de Frascari (1983) s'intitule « The tell-the-tale detail » (« le détail qui raconte ») et paraît dans un recueil de sémiotique (titre seul, contenu non lu) ; Frampton (1995) relit l'architecture moderne comme un art de la construction (description de l'éditeur ; livre non lu). Aucune source perceptive trouvée sur l'écart vu au joint (recherche faite le 2026-10-10 : Crossref, Semantic Scholar) ; les mesures industrielles d'écart et d'affleurement (l'alignement des deux surfaces) ne visent pas une qualité perçue.
- `ppp:jointLevelOffset` : Comme pour l'écart au joint, les seules sources trouvées viennent de l'architecture (Frascari 1983, titre seul ; Frampton 1995, description de l'éditeur), et rien de ce qui en a été lu ne vise une qualité perçue. Aucune source perceptive trouvée sur le décalage de niveau vu au joint (recherche faite le 2026-10-10 : Crossref, Semantic Scholar).

**Références** :

- Frascari, M. (1983). The tell-the-tale detail. In Semiotics 1981, Springer, 325–336. https://doi.org/10.1007/978-1-4615-9328-7_32
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref (titre, recueil Semiotics 1981, pages) ; aucun résumé (Crossref, OpenAlex, 2026-10-10) ; texte non lu ;
  - usage : `ppp:jointSpacing` (discute); `ppp:jointLevelOffset` (discute).
- Frampton, K. (1995). Studies in Tectonic Culture: The Poetics of Construction in Nineteenth and Twentieth Century Architecture. Cambridge (MA) : MIT Press. https://openlibrary.org/works/OL80267W
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : notice Open Library (titre, auteur, 1995, MIT Press, OCLC 32131870) avec la description de l’éditeur, lue le 2026-10-10 : la tectonique comme attention à l’architecture en tant que métier de la construction, et l’histoire d’une « poétique de la structure et de la construction » ; recensions indexées par Crossref ; contenu non lu ;
  - usage : `ppp:jointSpacing` (discute); `ppp:jointLevelOffset` (discute).

<a id="groupe-etagement"></a>
<a id="etagement-en-plans"></a>
## Étagement en plans

L'étagement en plans touche à la perception de la profondeur, étudiée depuis longtemps. PPP qualifie l'étagement vu, sans nommer les indices.

**Types** : `ppp:perceivedDepth`.

- `ppp:perceivedDepth` : La perception de l’espace et de la profondeur est étudiée notamment par Gibson (1950) ; Cutting et Vishton (1995) traitent de la perception de l’agencement et des distances. Mather et Smith (2002) montrent que le flou n’est qu’un indice grossier de l’ordre en profondeur. PPP ne nomme pas les indices (ce qui, dans l’image, permet de voir la profondeur) : il qualifie l’étagement vu, et la strate reste ouverte (T25).

**Références** :

- Gibson, J. J. (1950). The Perception of the Visual World. Boston : Houghton Mifflin. https://openlibrary.org/works/OL5589052W
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : notice Open Library (titre, auteur, 1950, Houghton Mifflin, OCLC 560396 ; sujets : perception, vision, perception visuelle, perception de l’espace) ; contenu non lu ;
  - usage : `ppp:perceivedDepth` (discute).
- Cutting, J. E. & Vishton, P. M. (1995). Perceiving layout and knowing distances. In Perception of Space and Motion, Academic Press (Elsevier), 69–117. https://doi.org/10.1016/B978-012240530-3/50005-5
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref (titre court, ouvrage, pages) ; résumé non disponible ; texte non lu ;
  - usage : `ppp:perceivedDepth` (discute).
- Mather, G. & Smith, D. R. R. (2002). Blur discrimination and its relation to blur-mediated depth perception. Perception, 31(10), 1211–1219. https://doi.org/10.1068/p3254
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (OpenAlex) ;
  - usage : `ppp:perceivedDepth` (discute).

<a id="groupe-contrastes"></a>
<a id="contrastes"></a>
## Contrastes (relateurs P2)

Les relateurs de contraste (P2) comparent deux parties sur une dimension. Les sources trouvées traitent de la dimension comparée ou de l'atelier, rarement d'un contraste perçu à degrés.

**Types** : `ppp:textureContrast`, `ppp:hueContrast`, `ppp:lightnessContrast`, `ppp:scaleContrast`, `ppp:perceptualContrast`.

- `ppp:textureContrast` : Les mesures de texture de Tamura, Mori et Yamawaki (1978) permettent de comparer deux surfaces, mais elles ne définissent pas un contraste perçu entre elles. Aucune source trouvée ne propose une échelle perçue du contraste de texture entre deux parties d'un objet ; les labels des régions restent en position de travail (T3).
- `ppp:hueContrast` : Itten (*Kunst der Farbe*, 1961) et Albers (*Interaction of Color*, 1963) sont des ouvrages repérés sur la couleur (notices seules, contenu non lu). Le système de Munsell (1905) situe les teintes sur un cercle (« a circuit of hues », passage lu), ce qui donne un sens à « teintes éloignées ». Aucune source trouvée ne propose une échelle perçue du contraste de teinte entre deux zones ; les labels des régions sont ceux de tous les contrastes (T3).
- `ppp:lightnessContrast` : Le contraste de clarté entre deux zones touche à la perception du clair et du sombre, sujet du livre de Gilchrist (2006), dont le résumé rappelle que la lumière renvoyée par une surface ne dit pas sa nuance de gris (livre non lu). Tamura, Mori et Yamawaki (1978) ont une mesure de contraste calculée sur une image, rapprochée de ce type. Albers (*Interaction of Color*, 1963) est un ouvrage repéré sur l'interaction des couleurs (titre ; contenu non lu).
- `ppp:scaleContrast` : Les illusions de Delboeuf et d’Ebbinghaus, deux illusions de taille connues où un même cercle paraît plus grand ou plus petit selon les figures qui l’entourent, montrent que la taille vue d’un élément dépend des éléments vus avec lui : la taille apparente d’un cercle change avec la taille et la distance des cercles qui l’entourent (Girgus, Coren et Agdern 1972). On parle de contraste de taille quand deux objets paraissent plus différents qu’ils ne sont, d’assimilation quand ils paraissent plus semblables (Mruczek et al. 2017, résumé lu) ; ces jugements peuvent varier selon la culture : une étude trouve l’illusion d’Ebbinghaus plus faible chez des Himba que chez des Anglais (de Fockert et al. 2007). Aucune source trouvée ne propose une échelle perçue de l’écart de taille entre deux éléments vus ensemble (recherches du 2026-10-10 et du 2026-10-11 : Crossref, Semantic Scholar, OpenAlex) ; les labels des régions sont propres à ce contraste (T34).
- `ppp:perceptualContrast` : Pour la lumière, le contraste calculé (contraste de luminance : écart de luminance entre deux zones, rapporté à la luminance moyenne ou à celle du fond) ne s’accorde avec le contraste perçu que pour des images simples ; dans une image complexe, le contraste perçu varie d’un endroit à l’autre (Peli 1990, résumé lu), et des observateurs qui comparent deux photographies jugent laquelle est la plus contrastée (Haun et Peli 2013). Aucune source trouvée ne propose un contraste perçu général, valable pour toute dimension comparée (recherches du 2026-10-10 et du 2026-10-11 : Crossref, Semantic Scholar, OpenAlex). Les sources des contrastes spécialisés sont dans leurs fiches.

**Références** :

- Tamura, H., Mori, S. & Yamawaki, T. (1978). Textural features corresponding to visual perception. IEEE Transactions on Systems, Man, and Cybernetics, 8(6), 460–473. https://doi.org/10.1109/TSMC.1978.4309999
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé IEEE Xplore ; deux sources secondaires (docs/etat-de-l-art.md §5 bis) ; texte intégral non lu ;
  - usage : `ppp:textureContrast` (discute); `ppp:lightnessContrast` (alimente).
- Munsell, A. H. (1905). A Color Notation. Boston : G. H. Ellis ; 2e éd. 1907, Project Gutenberg n° 26054. https://www.gutenberg.org/ebooks/26054
  - statut : *vérifiée sur la source* ; vérifié sur : texte du Project Gutenberg n° 26054 lu pour les passages cités : « Color has three dimensions » (paragraphe 8) ; « a circuit of hues » (un cercle de teintes, chapitre I) ; cinq teintes principales et cinq intermédiaires ; texte non lu en entier ;
  - usage : `ppp:hueContrast` (alimente).
- Itten, J. (1961). Kunst der Farbe. Ravensburg : Otto Maier Verlag (éditeur des éditions allemandes de 1967, 1971 et 1979 ; celui de 1961 non vérifié) ; trad. angl. The Art of Color, New York : Reinhold, 1961. https://openlibrary.org/works/OL3134338W
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : notice Open Library lue le 2026-10-10 (œuvre OL3134338W) : titre, auteur, première publication 1961 ; éditions allemandes chez O. Maier / Otto Maier Verlag, Ravensburg, en 1967, 1971 et 1979 ; éditions anglaises The Art of Color chez Reinhold, New York, dès 1961 ; aucune édition allemande de 1961 n’y est listée, l’éditeur de 1961 n’est donc pas vérifié ; contenu non lu ;
  - usage : `ppp:hueContrast` (discute).
- Albers, J. (1963). Interaction of Color. New Haven : Yale University Press. https://openlibrary.org/works/OL43516944W
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : notice Open Library (titre, auteur, éditeur, 1963, OCLC 30247970 ; pas de description) ; contenu non lu ;
  - usage : `ppp:hueContrast` (discute); `ppp:lightnessContrast` (discute).
- Gilchrist, A. (2006). Seeing Black and White. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780195187168.001.0001
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé de l’éditeur lu (OpenAlex, 2026-10-10) : la lumière renvoyée par une surface ne révèle pas sa nuance de gris ; selon l’éclairage, une surface de n’importe quel gris peut renvoyer n’importe quelle quantité de lumière ; le livre fait l’historique des recherches et des théories de la clarté ; contenu non lu ;
  - usage : `ppp:lightnessContrast` (discute).
- Mruczek, R. E. B., Blair, C. D., Strother, L. & Caplovitz, G. P. (2017). Size Contrast and Assimilation in the Delboeuf and Ebbinghaus Illusions. In The Oxford Compendium of Visual Illusions (p. 262–268). New York : Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199794607.003.0028
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé lu (OpenAlex, 2026-10-11) : dans les illusions de Delboeuf et d’Ebbinghaus, la taille perçue d’un objet dépend de sa taille relative aux objets qui l’entourent ; « contraste de taille » : des objets paraissent plus différents qu’ils ne sont ; « assimilation » : plus semblables ; les mécanismes restent inconnus ; chapitre non lu ;
  - usage : `ppp:scaleContrast` (alimente).
- Girgus, J. S., Coren, S. & Agdern, M. (1972). The interrelationship between the Ebbinghaus and Delboeuf illusions. Journal of Experimental Psychology, 95(2), 453–455. https://doi.org/10.1037/h0033606
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé lu (OpenAlex, 2026-10-11) : la taille apparente du cercle central de l’illusion d’Ebbinghaus varie avec la taille des cercles qui l’entourent ; éloigner ces cercles fait diminuer la taille apparente du cercle central, quelle que soit leur taille ; texte non lu ;
  - usage : `ppp:scaleContrast` (discute).
- de Fockert, J., Davidoff, J., Fagot, J., Parron, C. & Goldstein, J. (2007). More accurate size contrast judgments in the Ebbinghaus Illusion by a remote culture. Journal of Experimental Psychology: Human Perception and Performance, 33(3), 738–742. https://doi.org/10.1037/0096-1523.33.3.738
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé lu (OpenAlex, 2026-10-11) : l’illusion d’Ebbinghaus est moins forte chez les Himba que chez des participants anglais (« English participants »), d’où des jugements de contraste de taille plus exacts ; elle est plus faible quand les figures qui entourent ne ressemblent pas à la cible ; texte non lu ;
  - usage : `ppp:scaleContrast` (discute).
- Peli, E. (1990). Contrast in complex images. Journal of the Optical Society of America A, 7(10), 2032–2040. https://doi.org/10.1364/JOSAA.7.002032
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé lu (OpenAlex, 2026-10-11) : le contraste physique d’images simples (un réseau, une tache sur un fond uniforme) est bien défini et s’accorde avec le contraste perçu, mais pas pour des images complexes, où le contraste perçu varie beaucoup d’un endroit à l’autre ; l’article propose un contraste local calculé par bandes de fréquences spatiales ; texte non lu ;
  - usage : `ppp:perceptualContrast` (contraste).
- Haun, A. M. & Peli, E. (2013). Perceived contrast in complex images. Journal of Vision, 13(13), 3. https://doi.org/10.1167/13.13.3
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé lu (OpenAlex, 2026-10-11) : des observateurs jugent laquelle de deux photographies a le plus de contraste ; le contraste d’ensemble perçu dépend surtout de certaines fréquences spatiales ; les images aux zones sombres plus sombres sont jugées plus contrastées ; texte non lu ;
  - usage : `ppp:perceptualContrast` (discute).

<a id="mesures-derniers-groupes"></a>
### Mesures associées des groupes joint, étagement et contrastes (rubrique `mesure`)

Rubrique `mesure` des dernières fiches publiques (`jointSpacing`, `jointLevelOffset`, `perceivedDepth`, `perceptualContrast`, `scaleContrast`) ; recherche du 2026-10-16. Aucune référence nouvelle : les sources citées sont déjà décrites ailleurs dans ce document, avec leur statut.

- ISO 80000-3:2019 (notice : `mesures-forme`) : usage étendu à `jointSpacing` et `jointLevelOffset` (mesures associées proches ; la norme définit la grandeur sans décrire de procédé de mesure ; aucune norme de pose lue) et à `scaleContrast` (méthode voisine non retenue : rapport des dimensions mesurées).
- Peli (1990) (notice : `mesures-couleur`) : usage étendu à `perceptualContrast` (mesure associée indirecte, dimension de la clarté seulement).
- Mruczek et al. (2017), déjà dans la fiche `scaleContrast` : cité dans la raison de non-retenue (illusions de Delboeuf et d’Ebbinghaus).
- Cutting et Vishton (1995), déjà dans la fiche `perceivedDepth` : cité dans la synthèse « aucune méthode robuste » (indices de profondeur qui se combinent).

*English version.* Associated measurements of the joint, layering and contrast groups (`mesure` section); search of 2026-10-16. No new reference: ISO 80000-3:2019 extended to `jointSpacing`, `jointLevelOffset` (close; the standard defines the quantity without describing a measurement procedure) and `scaleContrast` (ratio of measured dimensions, not retained); Peli (1990) extended to `perceptualContrast` (indirect, lightness dimension only); Mruczek et al. (2017) and Cutting and Vishton (1995), already in their entries, cited in `scaleContrast` and `perceivedDepth` (no robust method).

<a id="groupe-gouvernance"></a>
## Gouvernance des ontologies ouvertes

Sources sur la manière dont des ontologies et vocabulaires ouverts reçoivent les demandes, versionnent et déprécient leurs termes. Ce que PPP en reprend ou non : [`gouvernance.md`](gouvernance.md), section 4. Pages lues le 2026-10-11.

- OBO Foundry. Principles: Overview. https://obofoundry.org/principles/fp-000-summary.html
  - statut : *vérifiée sur la source* ; vérifié sur : page lue le 2026-10-11 (résumé des principes P1 à P20 : ouverture avec attribution, versionnement, lieu d'autorité, maintenance, stabilité des termes, réactivité) ;
  - usage : `docs/gouvernance.md` (alimente).
- OBO Foundry. Principle: Versioning (principle 4). https://obofoundry.org/principles/fp-004-versioning.html
  - statut : *vérifiée sur la source* ; vérifié sur : page lue le 2026-10-11 (chaque version publiée a un identifiant de version ; le contenu d'une version publiée ne change pas) ;
  - usage : `docs/gouvernance.md` (alimente).
- OBO Foundry. Principle: Maintenance (principle 16). https://obofoundry.org/principles/fp-016-maintenance.html
  - statut : *vérifiée sur la source* ; vérifié sur : page lue le 2026-10-11 (répondre aux demandes de la communauté ; un point controversé est écarté ou tranché, avec une note d'éditeur) ;
  - usage : `docs/gouvernance.md` (alimente).
- OBO Foundry. Principle: Term Stability (principle 19). https://obofoundry.org/principles/fp-019-term-stability.html
  - statut : *vérifiée sur la source* ; vérifié sur : page lue le 2026-10-11 (un changement de définition qui change ce qu'elle désigne demande un terme nouveau ; l'ancien est rendu obsolète, avec des indications de remplacement) ;
  - usage : `docs/gouvernance.md` (alimente ; même règle que A11).
- OBO Foundry. Principle: Responsiveness (principle 20). https://obofoundry.org/principles/fp-020-responsiveness.html
  - statut : *vérifiée sur la source* ; vérifié sur : page lue le 2026-10-11 (dispositif public de suivi des demandes obligatoire ; réponse visée sous 2 à 5 jours ouvrés ; consignes de contribution recommandées ; ne pas fermer un ticket sans répondre) ;
  - usage : `docs/gouvernance.md` (alimente ; PPP retient une semaine).
- Schema.org. How We Work. https://schema.org/docs/howwework.html
  - statut : *vérifiée sur la source* ; vérifié sur : page lue le 2026-10-11 (tickets GitHub et groupe communautaire du W3C ; versions nommées ; zone « pending » ; revue par le groupe de pilotage et publication sans objection sous 10 jours ouvrés ; `supersededBy` plutôt que suppression ; aucune propriété obligatoire) ;
  - usage : `docs/gouvernance.md` (alimente, discute).
- Miles, A. & Bechhofer, S. (dir.) (2009). SKOS Simple Knowledge Organization System Reference. Recommandation du W3C, 18 août 2009. https://www.w3.org/TR/skos-reference/
  - statut : *vérifiée sur la source* ; vérifié sur : page lue le 2026-10-11 (statut du document : Recommandation produite par le groupe de travail Semantic Web Deployment ; commentaires sur liste publique ; errata séparés ; liste des propriétés de note, dont `skos:changeNote` et `skos:historyNote`) ;
  - usage : `docs/gouvernance.md` (alimente).
- Isaac, A. & Summers, E. (dir.) (2009). SKOS Simple Knowledge Organization System Primer. Note du W3C, 18 août 2009. https://www.w3.org/TR/skos-primer/
  - statut : *vérifiée sur la source* ; vérifié sur : page lue le 2026-10-11 (`skos:historyNote` : changements importants du sens ou de la forme d'un concept ; `skos:changeNote` : changements fins, pour l'administration et la maintenance ; `skos:editorialNote` : travail éditorial) ;
  - usage : `docs/gouvernance.md` (alimente).
- Citation File Format, version 1.2.0 (README et guide du schéma). https://github.com/citation-file-format/citation-file-format/tree/1.2.0
  - statut : *vérifiée sur la source* ; vérifié sur : README et `schema-guide.md` de l'étiquette 1.2.0 lus le 2026-10-11 (structure d'un `CITATION.cff`, champs `cff-version`, `message`, `title`, `authors`, `type`, `version`, `date-released`, `license`, `repository-code`) ;
  - usage : `CITATION.cff`, `docs/comment-citer.md`.
- GitHub Docs. Syntax for issue forms. https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms
  - statut : *vérifiée sur la source* ; vérifié sur : page lue le 2026-10-11 (formulaires YAML dans `.github/ISSUE_TEMPLATE` ; clés obligatoires `name`, `description`, `body` ; fonction en « public preview ») ;
  - usage : `docs/gouvernance.md` 2.1, `docs/depot-public.md`, modèles `docs/depot-public/ISSUE_TEMPLATE/` (alimente).
- GitHub Docs. Syntax for GitHub's form schema. https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema
  - statut : *vérifiée sur la source* ; vérifié sur : page lue le 2026-10-11 (éléments `markdown`, `input`, `textarea`, `dropdown`, `checkboxes`, `upload` ; `id` en caractères alphanumériques, `-` et `_` ; `required` appliqué seulement dans un dépôt public) ;
  - usage : modèles `docs/depot-public/ISSUE_TEMPLATE/` (alimente).
- GitHub Docs. Configuring issue templates for your repository. https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository
  - statut : *vérifiée sur la source* ; vérifié sur : page lue le 2026-10-11 (`config.yml`, `blank_issues_enabled`, `contact_links` ; ordre des modèles par préfixe numérique) ;
  - usage : `docs/depot-public.md` (alimente).
- GitHub Docs. Referencing and citing content. https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content
  - statut : *vérifiée sur la source* ; vérifié sur : page lue le 2026-10-11 (Zenodo archive un dépôt public et attribue un nouveau DOI à chaque *release* GitHub) ;
  - usage : spec §13 (identifiant pérenne, position de travail), `docs/comment-citer.md` (alimente).
- Zenodo. CITATION.cff file. https://help.zenodo.org/docs/github/describe-software/citation-file/
  - statut : *vérifiée sur la source* ; vérifié sur : page lue le 2026-10-11 (Zenodo lit `CITATION.cff`, sauf si un fichier `.zenodo.json` est présent ; validation recommandée avec cffconvert) ;
  - usage : spec §13, `docs/comment-citer.md` (alimente).
- GitHub Docs. Creating a GitHub Pages site. https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
  - statut : *vérifiée sur la source* ; vérifié sur : page lue le 2026-10-11 (source de publication : une branche et un dossier, ou un workflow GitHub Actions ; le fichier d'entrée est à la racine de la source) ;
  - usage : `docs/depot-public.md` (alimente).

<a id="groupe-toucher"></a>
## Toucher (proposition de famille, série 24 ; une fiche en préparation, série 54)

Références de `famille-toucher-proposition.md` (document du dépôt, non publié) et de `protocole-echantillons-toucher.md` (document du dépôt, non publié) (série 30), vérifiées le 2026-10-12 (métadonnées Crossref, résumés PubMed ou OpenAlex ; notes de la relecture explicative recoupées). Aucune fiche n'existe encore : l'usage renvoie aux types **proposés** (ids non enregistrés).

**Types proposés** (premier lot décidé par l'éditeur du projet le 2026-10-12, séries 27 et 29) : `hardnessToTouch` (dureté au toucher), `coldToTouch` (froid au toucher), `slipperinessToTouch` (glisse au toucher), `perceivedWeight` (poids perçu), `springBack` (retour à la forme), `flexibilityToTouch` (souplesse au pli) ; en réserve : `wetnessToTouch`, `pileThickness`, et, pour les matériaux souples, tombé, gonflant, craquant, viscosité, granularité ; la « main » d'un tissu n'est pas un type. Types existants concernés : `ppp:texture` (le relief au toucher), `ppp:textureContrast`, `ppp:textureDirectionality`, `ppp:localIrregularity`, `ppp:curvature`, `ppp:jointLevelOffset`, `ppp:elementaryShapeCount`.

**Références** :

- Lederman, S. J. & Klatzky, R. L. (1987). Hand movements: A window into haptic object recognition. Cognitive Psychology, 19(3), 342–368. https://doi.org/10.1016/0010-0285(87)90008-9
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et PubMed (PMID 3608405, sans résumé) ; résumé de l'éditeur (ScienceDirect) ; la liste des six procédures exploratoires est lue dans Klatzky et Reed (2009), pas dans l'article ; texte intégral non lu ;
  - usage : famille Toucher, gestes et conditions (fonde) ; `perceivedWeight` (alimente).
- Klatzky, R. L. & Reed, C. L. (2009). Haptic exploration. Scholarpedia, 4(8), 7941. https://doi.org/10.4249/scholarpedia.7941
  - statut : *vérifiée sur la source* ; vérifié sur : page lue le 2026-10-12 (six procédures et propriété associée à chacune ; gestes compatibles ou incompatibles ; avec la vue, on touche surtout pour la matière ; un outil rigide transmet la texture par vibration) ; relue le 2026-10-12 (série 30) : la pression comprend appuyer, plier ou tordre ; le contact statique se fait typiquement avec une grande surface de peau, comme la main entière ; saisir et relâcher diminue la sensation thermique (d'après Green, 2009, non lu) ; on presse plus fort quand on s'attend à un objet rigide ;
  - usage : famille Toucher, conditions (fonde) ; `perceivedWeight` (alimente) ; protocole d'échantillons (`protocole-echantillons-toucher.md`, gestes par type : fonde).
- Klatzky, R. L., Lederman, S. J. & Matula, D. E. (1993). Haptic exploration in the presence of vision. Journal of Experimental Psychology: Human Perception and Performance, 19(4), 726–743. https://doi.org/10.1037/0096-1523.19.4.726
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé PubMed (PMID 8409856) : avec la vue, le toucher intervient souvent pour les jugements de matière difficiles, rarement pour les jugements géométriques ;
  - usage : famille Toucher (alimente) ; protocole d'échantillons (épreuve sans voir : alimente).
- Lederman, S. J. & Klatzky, R. L. (1993). Extracting object properties through haptic exploration. Acta Psychologica, 84(1), 29–40. https://doi.org/10.1016/0001-6918(93)90070-8
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé PubMed (PMID 8237454) : revue ; procédures exploratoires, place relative des propriétés de matière et géométriques ;
  - usage : famille Toucher (alimente).
- Lederman, S. J. & Klatzky, R. L. (2009). Haptic perception: A tutorial. Attention, Perception, & Psychophysics, 71(7), 1439–1459. https://doi.org/10.3758/APP.71.7.1439
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref, résumé et liste des références (page de l'éditeur) ; texte intégral inaccessible depuis la machine ; les travaux qu'il cite ne sont pas repris ;
  - usage : famille Toucher, vue d'ensemble (alimente).
- Hollins, M., Faldowski, R., Rao, S. & Young, F. (1993). Perceptual dimensions of tactile surface texture: A multidimensional scaling analysis. Perception & Psychophysics, 54(6), 697–705. https://doi.org/10.3758/BF03211795
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : résumé PubMed (PMID 8134240) ; Crossref orthographie le premier auteur « Holliins », PubMed « Hollins M » ; rugueux ou lisse et dur ou mou robustes et indépendants ; une troisième dimension, peut-être l'élasticité (*springiness*), d'après un examen après coup ;
  - usage : `hardnessToTouch` (fonde) ; `springBack` (alimente ; seule source directe, une dimension interprétée après coup) ; `ppp:texture` au toucher (alimente).
- Hollins, M., Bensmaïa, S., Karlof, K. & Young, F. (2000). Individual differences in perceptual space for tactile textures: Evidence from multidimensional scaling. Perception & Psychophysics, 62(8), 1534–1544. https://doi.org/10.3758/BF03212154
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé PubMed (PMID 11140177) : rugueux ou lisse et mou ou dur robustes pour tous ; collant ou glissant pèse moins et ne compte que pour certaines personnes ;
  - usage : `hardnessToTouch` (fonde) ; `slipperinessToTouch` (alimente ; risque pour E1).
- Hollins, M. & Risner, S. R. (2000). Evidence for the duplex theory of tactile texture perception. Perception & Psychophysics, 62(4), 695–705. https://doi.org/10.3758/BF03206916
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé PubMed (PMID 10883578) : textures fines perçues par la vibration (doigt en mouvement), textures grossières aussi doigt immobile ; le seuil chiffré est une mesure, non reprise ;
  - usage : `ppp:texture` au toucher (alimente) ; conditions, geste (alimente).
- Picard, D., Dacremont, C., Valentin, D. & Giboreau, A. (2003). Perceptual dimensions of tactile textures. Acta Psychologica, 114(2), 165–184. https://doi.org/10.1016/j.actpsy.2003.08.001
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé PubMed (PMID 14529823) : répertoire de mots du toucher limité mais partagé ; 24 matériaux de sièges automobiles ; au plus quatre dimensions (*soft/harsh*, *thin/thick*, relief, dureté) ;
  - usage : `hardnessToTouch` (alimente) ; `pileThickness` (alimente) ; labels (discute).
- Guest, S., Dessirier, J. M., Mehrabyan, A., McGlone, F., Essick, G., Gescheider, G., Fontana, A., Xiong, R., Ackerley, R. & Blot, K. (2011). The development and validation of sensory and emotional scales of touch perception. Attention, Perception, & Psychophysics, 73(2), 531–550. https://doi.org/10.3758/s13414-010-0037-y
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref (en ligne en 2010) et résumé PubMed (PMID 21264727) : 26 attributs sensoriels et 14 émotionnels, séparés par la source ; facteurs sensoriels *Roughness*, *Slip*, *Pile*, *Firmness* ; émotionnels *Comfort*, *Arousal* ; réponses plus intenses en toucher passif ;
  - usage : `slipperinessToTouch`, `hardnessToTouch`, `pileThickness` (alimente) ; attributs émotionnels (contraste : écartés, hors PPP).
- Bergmann Tiest, W. M. & Kappers, A. M. L. (2006). Analysis of haptic perception of materials by multidimensional scaling and physical measurements of roughness and compressibility. Acta Psychologica, 121(1), 1–20. https://doi.org/10.1016/j.actpsy.2005.04.005
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé PubMed (PMID 16055070) : 124 matériaux, environ quatre dimensions ; rugosité et compressibilité perçues liées aux mesures par une fonction exponentielle ;
  - usage : `hardnessToTouch` (alimente).
- Bergmann Tiest, W. M. & Kappers, A. M. L. (2007). Haptic and visual perception of roughness. Acta Psychologica, 124(2), 177–189. https://doi.org/10.1016/j.actpsy.2006.03.002
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé PubMed (PMID 16684497) : 96 matériaux classés par rugosité à la vue et au toucher ; correspondance avec les mesures à peu près égale ; critères différents selon les personnes ; rugosité perçue distincte de la rugosité mesurée ;
  - usage : `ppp:texture` au toucher, Q13 (discute).
- Bergmann Tiest, W. M. & Kappers, A. M. L. (2009a). Cues for haptic perception of compliance. IEEE Transactions on Haptics, 2(4), 189–199. https://doi.org/10.1109/TOH.2009.16
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (OpenAlex) : rôle de la déformation de la surface ; épaisseur prise en compte ; seuils exprimés par le module de Young ;
  - usage : `hardnessToTouch` (alimente ; homonyme physique : module de Young).
- Bergmann Tiest, W. M. & Kappers, A. M. L. (2009b). Tactile perception of thermal diffusivity. Attention, Perception, & Psychophysics, 71(3), 481–489. https://doi.org/10.3758/APP.71.3.481
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé PubMed (PMID 19304639) : la diffusivité thermique règle la vitesse à laquelle la main perd sa chaleur ; la vitesse de refroidissement initiale est l'indice principal ;
  - usage : `coldToTouch` (alimente) ; conditions, durée (alimente) ; protocole d'échantillons (durée du froid : alimente).
- Bergmann Tiest, W. M. (2010). Tactual perception of material properties. Vision Research, 50(24), 2775–2782. https://doi.org/10.1016/j.visres.2010.10.005
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé PubMed (PMID 20937297) : revue de la rugosité, de la souplesse, du froid et du frottement, et de leurs interactions ;
  - usage : `hardnessToTouch`, `coldToTouch`, `slipperinessToTouch` (fonde).
- Okamoto, S., Nagano, H. & Yamada, Y. (2013). Psychophysical dimensions of tactile perception of textures. IEEE Transactions on Haptics, 6(1), 81–93. https://doi.org/10.1109/TOH.2012.32
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé PubMed (PMID 24808270) : trois dimensions principales (rugueux ou lisse, dur ou mou, froid ou chaud) ; rugosité peut-être grossière et fine ; frottement (humide ou sec, collant ou glissant) ; cinq dimensions « potentielles » ;
  - usage : `hardnessToTouch`, `coldToTouch`, `slipperinessToTouch` (fonde) ; `wetnessToTouch` (alimente).
- Baumgartner, E., Wiebel, C. B. & Gegenfurtner, K. R. (2013). Visual and haptic representations of material properties. Multisensory Research, 26(5), 429–455. https://doi.org/10.1163/22134808-00002429
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé PubMed (PMID 24649528) : 84 matériaux ; notes fortement corrélées entre vue et toucher ; dureté et rugosité dominent dans les deux sens ;
  - usage : Q13 (alimente) ; `hardnessToTouch` (alimente).
- Baumgartner, E., Wiebel, C. B. & Gegenfurtner, K. R. (2015). A comparison of haptic material perception in blind and sighted individuals. Vision Research, 115(B), 238–245. https://doi.org/10.1016/j.visres.2015.02.006
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé PubMed (PMID 25711976) : représentations tactiles des matériaux très proches chez les aveugles de naissance et les voyants aux yeux bandés ;
  - usage : Q13 (alimente).
- Srinivasan, M. A. & LaMotte, R. H. (1995). Tactual discrimination of softness. Journal of Neurophysiology, 73(1), 88–101. https://doi.org/10.1152/jn.1995.73.1.88
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé PubMed (PMID 7714593, résumé tronqué) : surfaces déformables et objets rigides montés sur ressort ; le toucher de la peau suffit pour les premières, pas pour les seconds ;
  - usage : `hardnessToTouch` (alimente ; cas voisin du piège de l'objet creux ou mince : la source traite des objets rigides montés sur ressort, pas des objets creux).
- Ho, H.-N. (2018). Material recognition based on thermal cues: Mechanisms and applications. Temperature, 5(1), 36–55. https://doi.org/10.1080/23328940.2017.1372042
  - statut : *vérifiée sur la source* ; vérifié sur : texte intégral (PMC5902225, CC BY), en ligne le 2017-11-10 ; passages relus le 2026-10-12 : le métal paraît plus froid que le bois à la même température ; le froid ressenti n'est pas la température physique ; *contact coefficient* (racine du produit de la conductivité et de la capacité thermiques) ; le mot « effusivité » ne figure pas dans le passage lu ; relu le 2026-10-12 (texte intégral par Europe PMC) : les températures de départ de la peau et de l'objet décident du sens et de la quantité de chaleur échangée ; le froid est plus net quand on appuie plus fort, et une surface lisse paraît en général plus froide qu'une rugueuse ; un objet épais retire plus de chaleur qu'un mince de la même matière ; ordre inversé entre épais et minces quand la pièce est à 40 °C ; la paume, près du pouce, est plus sensible que le bout des doigts ; refroidissement rapide au contact, puis plus lent ; d'après Katz (1925), l'ordre « plus froid / plus chaud » des matières varie très peu d'une personne à l'autre ;
  - usage : `coldToTouch` (fonde ; contre-exemple, homonymes, et raison du passage à trois régions : pas de région « tiède » pour un objet à la température de la pièce, raisonnement fait d'après l'article) ; protocole d'échantillons (conditions du froid : fonde).
- Ho, H.-N. & Jones, L. A. (2006). Contribution of thermal cues to material discrimination and localization. Perception & Psychophysics, 68(1), 118–128. https://doi.org/10.3758/BF03193662
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé PubMed (PMID 16617836) : discrimination des matériaux par le froid quand leurs propriétés thermiques diffèrent beaucoup ; le résumé ne parle pas d'effusivité ;
  - usage : `coldToTouch` (alimente).
- Jones, L. A. & Ho, H.-N. (2008). Warm or cool, large or small? The challenge of thermal displays. IEEE Transactions on Haptics, 1(1), 53–70. https://doi.org/10.1109/TOH.2008.2
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé PubMed (PMID 27788084) : revue des afficheurs thermiques et des modèles du contact entre la main et l'objet ;
  - usage : `coldToTouch` (alimente).
- Filingeri, D., Fournet, D., Hodder, S. & Havenith, G. (2014). Why wet feels wet? A neurophysiological model of human cutaneous wetness sensitivity. Journal of Neurophysiology, 112(6), 1457–1469. https://doi.org/10.1152/jn.00120.2014
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé PubMed (PMID 24944222) : pas de récepteur de l'humidité ; à même teneur en eau, le froid augmente l'impression de mouillé ;
  - usage : `wetnessToTouch` (alimente).
- Filingeri, D. & Havenith, G. (2015). Human skin wetness perception: Psychophysical and neurophysiological bases. Temperature, 2(1), 86–104. https://doi.org/10.1080/23328940.2015.1008878
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (OpenAlex) : revue ; indices thermiques et mécaniques de l'humidité ;
  - usage : `wetnessToTouch` (alimente).
- Buckingham, G. (2014). Getting a grip on heaviness perception: A review of weight illusions and their probable causes. Experimental Brain Research, 232(6), 1623–1629. https://doi.org/10.1007/s00221-014-3926-9
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé PubMed (PMID 24691760) : illusion taille-poids ; illusions voisines dues à la matière, la température, la couleur, la forme ;
  - usage : `perceivedWeight` (alimente ; contre-exemple) ; protocole d'échantillons (épreuve sans voir : alimente).

Matériaux souples (demande de l’éditeur du projet ; vérifiées le 2026-10-12) :

- Peirce, F. T. (1930). The “handle” of cloth as a measurable quantity. Journal of the Textile Institute Transactions, 21(9), T377–T416. https://doi.org/10.1080/19447023008661529
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (OpenAlex ; page de l'éditeur) : la « main » se juge par des sensations de raideur ou de mollesse (*stiffness or limpness*), de dureté ou de mollesse, de rugosité ou de lissé, la dernière liée au frottement ; la longueur de flexion mesure le tombé ; texte intégral non lu ;
  - usage : `flexibilityToTouch` (alimente ; homonymes : rigidité et longueur de flexion) ; « main » (contraste : jugement d'ensemble, pas un type) ; tombé (alimente).
- Mahar, T. J., Wheelwright, P., Dhingra, R. C. & Postle, R. (1990). Measuring and interpreting fabric low stress mechanical and surface properties, Part V: Fabric handle attributes and quality descriptors. Textile Research Journal, 60(1), 7–17. https://doi.org/10.1177/004051759006000102
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (OpenAlex ; page de l'éditeur) : descripteurs de la main issus du comité japonais de Kawabata (lisse et soyeux, *sleekness* ; gonflant, fermeté, tombé ; fermeté ou dureté, craquant, gonflant pour les costumes) ; préférences différentes selon les pays ;
  - usage : `flexibilityToTouch`, tombé, gonflant, craquant (alimente) ; « main » (contraste : préférences, donc jugement).
- Ahirwar, M. & Behera, B. K. (2022 ; en ligne en 2021). Fabric hand research translates senses into numbers: A review. The Journal of The Textile Institute, 113(11), 2531–2548. https://doi.org/10.1080/00405000.2021.1982190
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (OpenAlex) : la main est la qualité d'un tissu jugée par le toucher, entre les doigts et le pouce ; revue depuis 1930 (évaluation subjective et objective, équations de Kawabata) ;
  - usage : « main » (contraste : définie comme une qualité, un jugement d'ensemble).
- Cavdan, M., Doerschner, K. & Drewing, K. (2021). Task and material properties interactively affect softness explorations along different dimensions. IEEE Transactions on Haptics, 14(3), 603–614. https://doi.org/10.1109/TOH.2021.3069626
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (OpenAlex) : la souplesse ne se réduit pas à la compliance ; les gestes dépendent de la matière, de la qualité jugée et de leur interaction ;
  - usage : `hardnessToTouch`, `flexibilityToTouch` (alimente) ; facette `geste` (alimente).
- Cavdan, M., Drewing, K. & Doerschner, K. (2021). The look and feel of soft are similar across different softness dimensions. Journal of Vision, 21(10), 20. https://doi.org/10.1167/jov.21.10.20
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (OpenAlex) : rappelle, d'après Dövencioğlu et al. (version de 2020), que la souplesse perçue au toucher varie avec la compliance, la viscosité, la granularité et le poil (*furriness*) ; forte correspondance entre toucher, photos et vidéos de la main manipulant la matière ;
  - usage : Q13 (alimente) ; viscosité, granularité, `pileThickness` (alimente).
- Dövencioğlu, D. N., Üstün, F. S., Doerschner, K. & Drewing, K. (2022). Hand explorations are determined by the characteristics of the perceptual space of real-world materials from silk to sand. Scientific Reports, 12, 14785. https://doi.org/10.1038/s41598-022-18901-6
  - statut : *vérifiée sur la source* ; vérifié sur : métadonnées Crossref, résumé (OpenAlex) et passages du texte intégral (PubMed Central, PMC9427999) lus le 2026-10-12 : quatre dimensions liées aux propriétés mécaniques (compliance, viscosité, *surface softness*, granularité), plus la rugosité, chacune liée à des gestes propres ; une balle en caoutchouc reprend sa forme, l'argile garde la sienne ;
  - usage : `hardnessToTouch`, `springBack`, `pileThickness` (alimente) ; viscosité, granularité (alimente) ; facette `geste` (alimente).

**Repérées, pas citées au premier rang** :

- Katz, D. (1925). *Der Aufbau der Tastwelt*. Leipzig : J. A. Barth (Open Library OL1124180W) ; trad. L. E. Krueger, *The World of Touch*, Hillsdale (NJ) : Lawrence Erlbaum, 1989, ISBN 9780805805291. Statut : métadonnées seulement ; contenu connu par Hollins et Risner (2000) et Ho (2018) ; rien ne lui est attribué directement.
- Gibson, J. J. (1962). Observations on active touch. Psychological Review, 69(6), 477–491. https://doi.org/10.1037/h0046962. Statut : métadonnées seulement (PubMed sans résumé) ; rien ne lui est attribué.
- ISO 11036:2020, *Sensory analysis — Methodology — Texture profile*. Statut : page de l'ISO lue par la relecture explicative ; texte non lu. Sert seulement à signaler l'homonyme de domaine « texture » (en analyse sensorielle, elle inclut la dureté) ; le détail des attributs reste à vérifier.
- Jones, L. A. (1986). Perception of force and weight: Theory and research. Psychological Bulletin, 100(1), 29–42. https://doi.org/10.1037/0033-2909.100.1.29. Statut : métadonnées Crossref seulement (aucun résumé trouvé) ; non citée.
- Kawabata, S. (éd.), *The Standardization and Analysis of Hand Evaluation*, 2e éd., Hand Evaluation and Standardization Committee, The Textile Machinery Society of Japan, Osaka (date de la 2e édition non vérifiée) ; réimpr. en annexe de Behery (éd.), *Effect of Mechanical and Physical Properties on Fabric Hand*, Woodhead, 2005, https://doi.org/10.1533/9781845690984.appendix_a. Statut : métadonnées Crossref seulement (réimpression) ; contenu connu par Mahar et al. (1990) ; non citée directement.

### Dureté au toucher : fiche `ppp:hardnessToTouch` (série 54, en préparation)

Fiche rédigée le 2026-10-16 à partir du [ticket n° 4](https://github.com/blomig/PPP-ontologie/issues/4). Références déjà listées ci-dessus et reprises par la fiche : Srinivasan et LaMotte (1995, relu le 2026-10-16 : rôle `fonde`), Bergmann Tiest et Kappers (2006 ; 2009a), Klatzky et Reed (2009). Nouvelles références :

- Harper, R. & Stevens, S. S. (1964). Subjective hardness of compliant materials. Quarterly Journal of Experimental Psychology, 16, 204–215. https://doi.org/10.1080/17470216408416370
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (OpenAlex) lus le 2026-10-16 : neuf matières souples, de l'éponge au bloc de caoutchouc ; la dureté jugée suit une loi de puissance de la dureté physique (force sur enfoncement) ; jugements de mollesse à peu près réciproques ; texte intégral non lu ;
  - usage : `hardnessToTouch` (alimente ; une seule dimension dureté–mollesse ; rubrique `mesure`).

**Mesures associées** (rubrique `mesure` de la fiche, gabarit de la série 53 ; normes payantes, résumés publics seulement) :

- ISO 48-4:2018. Rubber, vulcanized or thermoplastic — Determination of hardness — Part 4: Indentation hardness by durometer method (Shore hardness). https://www.iso.org/standard/74969.html
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : page de l'ISO lue le 2026-10-16 (échelles A, D, AO, AM ; confirmée en 2024) ; texte non lu ;
  - usage : `hardnessToTouch` (contraste ; mesure associée « proche »).
- ASTM D2240-15(2021). Standard Test Method for Rubber Property—Durometer Hardness. ASTM International. https://store.astm.org/d2240-15r21.html
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : page de l'éditeur, Scope sections 1.1 et 1.2 lus le 2026-10-16 (douze types de duromètres, dont A, D, O et OO) ; texte non lu ;
  - usage : `hardnessToTouch` (contraste ; mesure associée « proche »).
- ISO 48-2:2018. Rubber, vulcanized or thermoplastic — Determination of hardness — Part 2: Hardness between 10 IRHD and 100 IRHD. https://www.iso.org/standard/74967.html
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : page de l’ISO lue le 2026-10-16 (résumé) (méthodes N, H, L, M ; dureté apparente des surfaces courbes) ; texte non lu ;
  - usage : `hardnessToTouch` (contraste ; mesure associée « proche »).
- ISO 2439:2008. Flexible cellular polymeric materials — Determination of hardness (indentation technique). https://www.iso.org/standard/42717.html
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : page de l'ISO lue le 2026-10-16 (méthodes A à E ; mousses à cellules ouvertes ; résultats limités aux conditions de l'essai ; confirmée en 2026) ; texte non lu ;
  - usage : `hardnessToTouch` (contraste ; mesure associée « indirecte »).
- ISO 6507-1:2023. Metallic materials — Vickers hardness test — Part 1: Test method. https://www.iso.org/standard/83898.html
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : page de l’ISO lue le 2026-10-16 (résumé) ; texte non lu ;
  - usage : `hardnessToTouch` (contraste ; méthode non retenue : empreinte permanente dans les métaux). Brinell : norme non consultée, rien ne lui est attribué.
- U.S. National Park Service (2023). Mohs Hardness Scale. https://www.nps.gov/articles/mohs-hardness-scale.htm
  - statut : *vérifiée sur la source* ; vérifié sur : page lue le 2026-10-16 (résistance relative à la rayure ; dix minéraux, du talc au diamant) ;
  - usage : `hardnessToTouch` (contraste ; homonyme de domaine, méthode non retenue).

**Poids pour sa taille** (ticket 5, série 73 ; suggestion recevable, suite à confirmer par l'éditeur du projet ; aucune fiche). Références vérifiées le 2026-10-19 (métadonnées Crossref ; résumés OpenAlex ou Europe PMC). Buckingham (2014), plus haut, sert aussi ici (illusions de poids ; usage ajouté : poids pour sa taille, alimente).

- Murray, D. J., Ellis, R. R., Bandomir, C. A. & Ross, H. E. (1999). Charpentier (1891) on the size–weight illusion. *Perception & Psychophysics*, 61(8), 1681–1685. https://doi.org/10.3758/BF03213127
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (Europe PMC, PMID 10598479) : traduction et présentation de Charpentier (1891), première preuve expérimentale de l'illusion taille-poids ; Charpentier lui-même n'est connu que par cette *source secondaire* ;
  - usage : poids pour sa taille (alimente ; contre-exemple).
- Ross, H. E. (1969). When is a weight not illusory? *Quarterly Journal of Experimental Psychology*, 21(4), 346–355. https://doi.org/10.1080/14640746908400230
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (OpenAlex) : masse volumique « non illusoire » propre à la matière (vers 1,7 pour des boîtes, 0,14 pour du polystyrène) ; rôle de l'attente ;
  - usage : poids pour sa taille (alimente ; régions et attente).
- Ellis, R. R. & Lederman, S. J. (1998). The golf-ball illusion: evidence for top-down processing in weight perception. *Perception*, 27(2), 193–201. https://doi.org/10.1068/p270193
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (OpenAlex) : balles de même poids jugées différemment par des golfeurs ;
  - usage : poids pour sa taille (alimente ; attente).
- Ellis, R. R. & Lederman, S. J. (1999). The material-weight illusion revisited. *Perception & Psychophysics*, 61(8), 1564–1576. https://doi.org/10.3758/BF03213118
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (Europe PMC, PMID 10598470) : illusion matière-poids surtout tactile ; absente à 357 g ; abolie par une prise ferme ;
  - usage : poids pour sa taille (alimente ; geste et prise).
- Amazeen, E. L. & Turvey, M. T. (1996). Weight perception and the haptic size–weight illusion are functions of the inertia tensor. *Journal of Experimental Psychology: Human Perception and Performance*, 22(1), 213–232. https://doi.org/10.1037/0096-1523.22.1.213
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (OpenAlex) : lourdeur d'un objet caché manié selon l'inertie de rotation ;
  - usage : poids pour sa taille (alimente ; geste) ; mesure associée « indirecte » (inertie de rotation).
- Flanagan, J. R. & Beltzner, M. A. (2000). Independence of perceptual and sensorimotor predictions in the size–weight illusion. *Nature Neuroscience*, 3(7), 737–741. https://doi.org/10.1038/76701
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (Europe PMC, PMID 10862708) : forces justes, illusion persistante ;
  - usage : poids pour sa taille (alimente ; contre-exemple).
- Peters, M. A. K., Ma, W. J. & Shams, L. (2016). The size–weight illusion is not anti-Bayesian after all: a unifying Bayesian account. *PeerJ*, 4, e2124. https://doi.org/10.7717/peerj.2124
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé (OpenAlex) : inférence de la densité relative, puis du poids ;
  - usage : poids pour sa taille (alimente ; jugement de densité).
- Harshfield, S. P. & DeHardt, D. C. (1970). Weight judgment as a function of apparent density of objects. *Psychonomic Science*, 20(6), 365–366. https://doi.org/10.3758/BF03335692
  - statut : *vérifiée sur résumé ou source secondaire* (métadonnées seules : titre, revue ; aucun résumé trouvé) ;
  - usage : poids pour sa taille (signalée ; rien n'en est repris).
- Stevens, S. S. (1957). On the psychophysical law. *Psychological Review*, 64(3), 153–181. https://doi.org/10.1037/h0046162
  - statut : *vérifiée sur résumé ou source secondaire* (métadonnées seules ; texte non lu ; l'exposant de la lourdeur soulevée n'est **pas vérifié**) ;
  - usage : poids pour sa taille (méthode non retenue : estimation de grandeur par jury, sans série de référence physique).

<a id="groupe-son"></a>
## Son (proposition de famille, séries 41 et 42 ; aucune fiche)

Références de `famille-son-proposition.md` (document de travail, non publié), vérifiées le 2026-10-13 (métadonnées Crossref et Open Library, résumés OpenAlex ou PubMed, pages d'organismes). Aucune fiche n'existe : l'usage renvoie aux types **proposés** (ids non enregistrés). **Statut de lecture** noté pour chaque source : *lu en entier* ; *extraits* (passages lus sur la source elle-même ou sur la page de son éditeur ou de son organisme) ; *extrait d'index* (passage de la source lu seulement tel qu'un moteur de recherche ou une page tierce le cite, la page elle-même n'ayant pas été ouverte : c'est une forme de source secondaire) ; *résumé* ; *source secondaire* (contenu connu par un autre auteur) ; *métadonnées* ; *non vérifié* ; il précise le statut de vérification de la méthode (« vérifiée sur la source » = lu en entier ou extraits ; « vérifiée sur résumé ou source secondaire » = résumé, source secondaire ou métadonnées).

**Types proposés** : `loudness` (force du son ; alternatif : sonie), `perceivedPitch` (hauteur perçue), `pitchClarity` (netteté de la hauteur), `soundSharpness` (acuité du son), `soundAttack` (attaque du son), `soundDecay` (résonance ; alternatif : extinction du son) ; en réserve : `soundGrain`, `soundBeat`, `soundHollowness`.

**Références** :

- Fastl, H. & Zwicker, E. (2007). *Psychoacoustics: Facts and Models* (3e éd.). Berlin, Heidelberg : Springer. https://doi.org/10.1007/978-3-540-68888-4
  - statut de lecture : *métadonnées* (titres et pages des chapitres sur Crossref : ch. 5 *Pitch and Pitch Strength*, ch. 8 *Loudness*, ch. 9 *Sharpness and Sensory Pleasantness*, ch. 10 *Fluctuation Strength*, ch. 11 *Roughness*, ch. 12 *Subjective Duration*, ch. 13 *Rhythm*) ; ch. 5 *lu en partie* (p. 111-112) ; contenu des autres chapitres non lu ;
  - usage : liste des sensations (alimente) ; `loudness`, `perceivedPitch`, `pitchClarity` (alimente) ; `soundGrain`, `soundBeat` (réserve) ; agrément sonore écarté (discute).
- Fastl, H. & Stoll, G. (1979). Scaling of pitch strength. Hearing Research, 1(4), 293–301. https://doi.org/10.1016/0378-5955(79)90002-9
  - statut de lecture : *résumé* ;
  - usage : `pitchClarity` (alimente : la *pitch strength* jugée sur une échelle continue).
- ISO 532-1:2017. *Acoustics — Methods for calculating loudness — Part 1: Zwicker method*. ISO. https://www.iso.org/standard/63077.html ; ISO 532-2:2017, *Part 2: Moore-Glasberg method*, https://www.iso.org/standard/63078.html ; ISO 532-3:2023, *Part 3: Moore-Glasberg-Schlittenlacher method* (sons stationnaires et variables dans le temps), https://www.iso.org/standard/69856.html
  - statut de lecture : *extrait d'index* (domaine des pages de l'ISO, cité par un moteur de recherche ; pour 532-3, aussi l'échantillon public du texte, par la même voie ; pages bloquées aux robots) ; textes non lus ;
  - usage : `loudness`, homonymes physiques (contraste).
- DIN 45692:2009-08. *Messtechnische Simulation der Hörempfindung Schärfe*. DIN. https://doi.org/10.31030/1521326
  - statut de lecture : *extrait d'index* (texte de présentation de la page DIN Media, cité par un moteur de recherche) ; norme non lue ;
  - usage : `soundSharpness` (alimente ; acum en contraste ; le lien à l'« agressivité » est écarté).
- Grey, J. M. (1977). Multidimensional perceptual scaling of musical timbres. The Journal of the Acoustical Society of America, 61(5), 1270–1277. https://doi.org/10.1121/1.381428
  - statut de lecture : *résumé* (OpenAlex) ;
  - usage : `soundAttack`, `soundSharpness` (alimente) ; pas de type « timbre » (fonde).
- McAdams, S., Winsberg, S., Donnadieu, S., De Soete, G. & Krimphoff, J. (1995). Perceptual scaling of synthesized musical timbres: Common dimensions, specificities, and latent subject classes. Psychological Research, 58(3), 177–192. https://doi.org/10.1007/BF00419633
  - statut de lecture : *résumé* (PubMed, PMID 8570786) ;
  - usage : `soundAttack`, `soundSharpness` (alimente) ; pas de type « timbre » (fonde).
- Schaeffer, P. (1966). *Traité des objets musicaux*. Paris : Seuil (coll. « Pierres vives »). ISBN 978-2-02-002608-6 ; Open Library OL1318246W
  - statut de lecture : *métadonnées* (Open Library, par l'ISBN ; éditeur et collection d'après la relecture) ; lu via Chion (*Guide des objets sonores*, 1983 : sections IV et V (art. 58 à 100) lues en entier dans la traduction anglaise de Dack et North ; le reste via Chion) ; avant la série 49 bis, critères connus par *source secondaire* (glossaire EARS ; HAL, hal-00807080) ;
  - usage : `pitchClarity`, `soundAttack` (alimente) ; `soundGrain`, `soundBeat` (réserve) ; écoute réduite (alimente).
- Chion, M. (1983). *Guide des objets sonores. Pierre Schaeffer et la recherche musicale*. Paris : Buchet/Chastel ; INA (coll. « Bibliothèque de recherche musicale »). Trad. angl. *Guide to Sound Objects*, J. Dack et C. North (2009), EARS ; traduction anglaise lue. Open Library OL1880304W
  - statut de lecture : *lu en partie* (sections IV et V (art. 58 à 100) lues en entier dans la traduction anglaise de Dack et North) ; table des matières sur leonardo.info : articles 51 *Site / Gauge*, 89 *Mass*, 90 *Node*, 91 *Striated*, 93 *Harmonic timbre*, 95 *Grain* ; avant la série 50 bis, contenu des articles par *source secondaire* (glossaire EARS, ears.huma-num.fr ; HAL hal-00807080) ;
  - usage : sept critères de la typo-morphologie (alimente) ; cran « hauteur approximative » de `pitchClarity` : rapproché du son cannelé (art. 91) sans en être l’équivalent.
- Chion, M. *Le son*. 1re éd. 1998 (Open Library OL1880301W) ; édition lue par sa table des matières sur la Bibliothèque numérique francophone accessible (notice 52363), date non vérifiée.
  - statut de lecture : *extraits* (table des matières) ;
  - usage : pas de type « timbre » (« Inadéquation de la notion de timbre pour décrire l'objet sonore » : alimente) ; site et calibre (à vérifier).
- Gaver, W. W. (1993a). What in the world do we hear? An ecological approach to auditory event perception. Ecological Psychology, 5(1), 1–29. https://doi.org/10.1207/s15326969eco0501_1
  - statut de lecture : *résumé* (OpenAlex) ; liste des événements de base par *source secondaire* (Houix et al., 2012, relevé de la relecture ; non relu ici) ;
  - usage : facette `production` proposée (alimente ; `liquid` et `airflow` regroupent ses catégories des liquides et des gaz ; `operation` et `voiceOrBreath` sont des ajouts de PPP) ; matière entendue écartée (discute).
- Gaver, W. W. (1993b). How do we hear in the world? Explorations in ecological acoustics. Ecological Psychology, 5(4), 285–313. https://doi.org/10.1207/s15326969eco0504_2
  - statut de lecture : *métadonnées* ; rien ne lui est attribué.
- Houix, O., Lemaitre, G., Misdariis, N., Susini, P. & Urdapilleta, I. (2012). A lexical analysis of environmental sound categories. Journal of Experimental Psychology: Applied, 18(1), 52–80. https://doi.org/10.1037/a0026240
  - statut de lecture : *métadonnées* (Crossref) ; son résumé des catégories de Gaver est connu par la relecture ;
  - usage : source secondaire de Gaver (1993a) (alimente).
- Klatzky, R. L., Pai, D. K. & Krotkov, E. P. (2000). Perception of material from contact sounds. Presence: Teleoperators and Virtual Environments, 9(4), 399–410. https://doi.org/10.1162/105474600566907
  - statut de lecture : *résumé* (OpenAlex) ;
  - usage : `soundDecay` (fonde) ; matière entendue (discute).
- Giordano, B. L. & McAdams, S. (2006). Material identification of real impact sounds: Effects of size variation in steel, glass, wood, and plexiglass plates. The Journal of the Acoustical Society of America, 119(2), 1171–1181. https://doi.org/10.1121/1.2149839
  - statut de lecture : *résumé* (PubMed, PMID 16521778) ;
  - usage : `soundDecay` (alimente) ; matière entendue écartée (discute).
- Lutfi, R. A. & Oh, E. L. (1997). Auditory discrimination of material changes in a struck-clamped bar. The Journal of the Acoustical Society of America, 102(6), 3647–3656. https://doi.org/10.1121/1.420151
  - statut de lecture : *résumé* (OpenAlex) ;
  - usage : matière entendue écartée (discute).
- Schafer, R. M. (1977). *The Tuning of the World*. New York : Knopf (éditeur par source secondaire). Open Library OL751880W
  - statut de lecture : *métadonnées* ; notions (keynote, signal, soundmark ; hi-fi, lo-fi) par *source secondaire* seulement ;
  - usage : paysage sonore écarté (discute) ; facette `bruit_de_fond` (alimente, sans reprise des termes).
- Berglund, B., Lindvall, T. & Schwela, D. H. (dir.) (1999). *Guidelines for Community Noise*. Genève : Organisation mondiale de la santé, ch. 4
  - statut de lecture : *extrait d'index* ;
  - usage : crans de `bruit_de_fond` définis par la voix (appuie : parole intelligible vers 35 dB(A), assez bien comprise à 45, comprise avec effort à 65) ; les dB sont des repères, pas des définitions (T8).
- ISO 8253-1:2010. *Acoustics — Audiometric test methods — Part 1: Pure-tone air and bone conduction audiometry*
  - statut de lecture : *extrait d'index* ;
  - usage : `bruit_de_fond` (contraste seulement : conditions d'une salle d'audiométrie, pas d'une observation ordinaire).

**Non vérifié** : la hauteur virtuelle (Fastl et Zwicker, ch. 5, hors des p. 111-112 lues ; non citée) ; les unités asper et vacil ; la correspondance du cran « hauteur approximative » avec cannelé / nodal / site et calibre (non vérifiée sur le texte ; aucune association faite) ; les licences des sons publiés (Freesound : licences avec clause NC, non permissives au sens de X16).

<a id="groupe-odorat"></a>
## Odorat (proposition de famille, séries 41 et 42 ; aucune fiche)

Références de `famille-odorat-proposition.md` (document de travail, non publié), vérifiées le 2026-10-13 (même méthode et mêmes statuts de lecture que le groupe son). Aucune fiche n'existe.

**Types proposés** : `odourIntensity` (intensité de l'odeur), `odourCharacter` (caractère de l'odeur ; alternatif : qualité de l'odeur) ; en réserve : `odourPersistence` (persistance de l'odeur), `odourReach` (portée de l'odeur), `odourPungency` (piquant au nez), `nasalCooling` (froid au nez ; EN *cooling in the nose*, alternatif *nasal cooling*).

**Références** :

- ISO 5492:2008. *Sensory analysis — Vocabulary* (2e éd.), et Amd 1:2016. ISO. https://www.iso.org/standard/38051.html
  - statut de lecture : *extrait d'index* (domaine et cycle de vie de la page de l'ISO : norme confirmée le 2024-01-13, toujours en vigueur) ; définitions (2.8 intensité, le 2.12 venant de l’édition 1992 ; 3.18 odeur ; 3.32 persistance et 3.33 arôme, numéros non vérifiés) par *source secondaire* (adoption nationale NTP-ISO 5492, en espagnol ; citations dans ISO/TS 16922) ; texte ISO non lu ;
  - usage : `odourIntensity` (fonde) ; `odourPersistence` (homonyme de domaine : contraste) ; arôme rétronasal écarté (contraste).
- Gross-Isseroff, R. & Lancet, D. (1988). Concentration-dependent changes of perceived odor quality. *Chemical Senses*, 13(2), 191–204. https://doi.org/10.1093/chemse/13.2.191
  - statut de lecture : *résumé seulement lu* ;
  - usage : `odourCharacter`, condition critique `distance` (alimente).
- ISO/TS 16922:2022. *Natural gas — Odorization*. ISO. https://www.iso.org/standard/83835.html. Édition en vigueur : 3.1.3 caractère d’odeur, 3.1.4 intensité d’odeur, « magnitude of the perceived odour » (numéros relevés par la relecture ; définition 3.1.4 lue dans l’extrait public de la norme ; reste du texte non lu).
- ISO/TS 16922:2002. *Natural gas — Guidelines for odorizing gases*. ISO. https://www.iso.org/standard/31135.html. **Annulée** (2013, remplacée d’abord par ISO/TR 16922:2013, elle-même remplacée par l’édition 2022, d’après les pages de l’ISO) ; gardée pour ses définitions (3.1.2 et 3.1.3).
  - statut de lecture : *extraits* (échantillon public du texte de l’édition 2002 : 3.1.2 caractère d'odeur, 3.1.3 intensité d'odeur, 3.1.5 fatigue sensorielle, 3.2.1 degré olfactif) ;
  - usage : `odourIntensity` (alimente) ; `odourCharacter` (fonde le label : 3.1.2 « caractère d'odeur ») ; échelle de Sales non reprise (contraste).
- Noble, A. C., Arnold, R. A., Masuda, B. M., Pecore, S. D., Schmidt, J. O. & Stern, P. M. (1984). Progress towards a standardized system of wine aroma terminology. American Journal of Enology and Viticulture, 35(2), 107–109. https://doi.org/10.5344/ajev.1984.35.2.107
  - statut de lecture : *métadonnées* (Crossref, auteurs compris) ;
  - usage : `odourCharacter` (alimente).
- Noble, A. C., Arnold, R. A., Buechsenstein, J., Leach, E. J., Schmidt, J. O. & Stern, P. M. (1987). Modification of a standardized system of wine aroma terminology. American Journal of Enology and Viticulture, 38(2), 143–146. https://doi.org/10.5344/ajev.1987.38.2.143
  - statut de lecture : *résumé* (OpenAlex) ; auteurs vérifiés sur Crossref ; les douze catégories du premier cercle (dont « chimique », « oxydé », « microbiologique », des défauts) par *source secondaire* (relevé de la relecture) ;
  - usage : `odourCharacter` (alimente : descripteurs de source, étalons de référence ; roue non reprise telle quelle : discute).
- Lenoir, J. *Le Nez du Vin*, coffret « Grand modèle 54 arômes ». Éditions Jean Lenoir. https://www.lenez.com/coffret/vin/grand-modele-54/
  - statut de lecture : *extraits* (page « L'histoire » du site de l'éditeur, https://www.lenez.com/l-histoire/, lue : « Fabriqué en France depuis 1981 ») ; page du coffret : *extrait d'index* ;
  - usage : `odourCharacter`, références olfactives (alimente).
- Edwards, M. *Fragrance Wheel*. Fragrances of the World. http://www.fragrancesoftheworld.com/fragrancewheel/
  - statut de lecture : *extrait d'index* (site) et *source secondaire* (Wikipédia, « Fragrance wheel ») ; aucune publication de l'auteur lue ;
  - usage : `odourCharacter` (alimente) ; lecture par « préférences innées » écartée (discute).
- Dravnieks, A. (1985). *Atlas of Odor Character Profiles* (ASTM DS61). Philadelphia : ASTM. ISBN 0-8031-0456-1 ; Open Library OL5099090W ; https://store.astm.org/ds61-eb.html
  - statut de lecture : *métadonnées* (Open Library, par l'ISBN) ; contenu par *source secondaire* : Koulakov et al. (2011, lu en entier : 144 odorants et 15 mélanges, 146 descripteurs, environ 150 personnes) ; environ 160 substances (159 ou 160 selon les notices ; 160 par *extrait d'index*, page de l'ASTM) ;
  - usage : base des études de 1.3 (alimente).
- Zarzo, M. & Stanton, D. T. (2006). Identification of latent variables in a semantic odor profile database using principal component analysis. Chemical Senses, 31(8), 713–724. https://doi.org/10.1093/chemse/bjl013
  - statut de lecture : *résumé* (OpenAlex) ;
  - usage : `odourCharacter` (fonde : pas d'odeurs primaires ; classes).
- Zarzo, M. & Stanton, D. T. (2009). Understanding the underlying dimensions in perfumers' odor perception space as a basis for developing meaningful odor maps. Attention, Perception, & Psychophysics, 71(2), 225–247. https://doi.org/10.3758/APP.71.2.225
  - statut de lecture : *résumé* (PubMed, PMID 19304614) ;
  - usage : `odourCharacter` (alimente : régions définies par des odorants de référence).
- Castro, J. B., Ramanathan, A. & Chennubhotla, C. S. (2013). Categorical dimensions of human odor descriptor space revealed by non-negative matrix factorization. PLoS ONE, 8(9), e73289. https://doi.org/10.1371/journal.pone.0073289
  - statut de lecture : *extraits* (article lu en partie sur le site de l'éditeur : NMF sur la base de Dravnieks, dix dimensions ; les quatre premières nommées *fragrant*, *woody*, *fruity*, *sickening*, ce dernier évaluatif et non repris) ;
  - usage : `odourCharacter` type catégoriel (alimente).
- Khan, R. M., Luk, C.-H., Flinker, A., Aggarwal, A., Lapid, H., Haddad, R. & Sobel, N. (2007). Predicting odor pleasantness from odorant structure: Pleasantness as a reflection of the physical world. The Journal of Neuroscience, 27(37), 10015–10023. https://doi.org/10.1523/JNEUROSCI.1158-07.2007
  - statut de lecture : *résumé* (OpenAlex) ; auteurs et fascicule vérifiés sur Crossref ;
  - usage : plaisance écartée (discute).
- Koulakov, A. A., Kolterman, B. E., Enikolopov, A. G. & Rinberg, D. (2011). In search of the structure of human olfactory space. Frontiers in Systems Neuroscience, 5, 65. https://doi.org/10.3389/fnsys.2011.00065
  - statut de lecture : *lu en entier* (page de l'article chez l'éditeur ; Crossref ne donne que le premier auteur) ;
  - usage : dimensions de l'espace des odeurs, premier axe lié à la plaisance (discute) ; contenu de l'atlas de Dravnieks (alimente).
- Rodrigues, A. E., Nogueira, I. & Faria, R. P. V. (2021). Perfume and flavor engineering: A chemical engineering perspective. Molecules, 26(11), 3095. https://doi.org/10.3390/molecules26113095
  - statut de lecture : *résumé* (OpenAlex) ; auteurs vérifiés sur Crossref ;
  - usage : `odourPersistence`, `odourReach` (contraste : modèles d'évaporation et de diffusion, « trail » d'un parfum ; grandeurs calculées, pas des qualités perçues).
- Dalton, P. & Wysocki, C. J. (1996). The nature and duration of adaptation following long-term odor exposure. Perception & Psychophysics, 58(5), 781–792. https://doi.org/10.3758/BF03213109
  - statut de lecture : *résumé* (PubMed, PMID 8710455) ;
  - usage : facette `exposition` proposée (fonde) ; adaptation écartée comme type (alimente).
- Pellegrino, R., Sinding, C., de Wijk, R. A. & Hummel, T. (2017). Habituation and adaptation to odors in humans. Physiology & Behavior, 177, 13–19
  - statut de lecture : *extrait d'index* ;
  - usage : cran `minutes` de la facette `exposition` (piste : l'habituation est rapide).
- ISO 8589:2007. *Sensory analysis — General guidance for the design of test rooms*
  - statut de lecture : *extrait d'index* ;
  - usage : facette `air` (appui qualitatif ; la norme ne donne aucun seuil, et une pièce aérée n'a pas pour autant un air sans odeur).

**Piste non lue, pas utilisée comme source** : Poucher (1955), *Journal of the Society of Cosmetic Chemists*, 6 (non trouvé sur Crossref). **Non vérifié** : sources perceptives sur la persistance et la portée de l'odeur d'un objet ; « sillage » et « notes » de la parfumerie ; effet de la température sur l'odeur ; terme « piquant » dans ISO 5492 ; unités de l'olfactométrie.

<a id="groupe-gout"></a>
## Goût en bouche (proposition de famille, série 71 ; aucune fiche)

Références de `famille-gout-proposition.md` (document de travail, non publié), vérifiées le 2026-10-19 (Crossref ; résumés sur Europe PMC, OpenAlex ou PubMed ; pages de l'ISO ; Open Library ; site de la CNIL). Même méthode que les groupes son et odorat ; *description de l'éditeur* : présentation et sommaire d'un livre. Aucune fiche n'existe ; la famille n'entre pas dans `fiches/familles.yaml` avant une première fiche (T4). **Série 78** (2026-10-20) : la famille `gout` est inscrite dans `fiches/familles.yaml`, avec neuf fiches en préparation (premier lot et lot CIEL) qui reprennent ces références avec leur statut ; la phrase précédente décrit l'état d'avant.

**Types proposés** : premier lot `bitterness` (amer), `oralPungency` (piquant en bouche), `astringency` (astringence), `hardnessInMouth` (dureté en bouche), `oralThickness` (épaisseur en bouche) (les trois premiers : décision 5a ; `hardnessInMouth` et `oralThickness` : décision de l'éditeur du projet, 2026-10-20, série 76) ; lot CIEL (décision de l'éditeur du projet, 2026-10-20, série 77) : `flavourComplexity` (nombre de composantes ; atelier : complexité), `flavourIntensity` (intensité (goût)), `flavourBalance` (composante dominante ; atelier : équilibre), `tastePersistence` (longueur ; sorti de la réserve) ; en réserve : `sweetness`, `sourness`, `saltiness`, `umami`, `oralCooling` (fraîcheur en bouche), `mouthAroma` (arôme en bouche, voie rétronasale), pétillant, textures en bouche.

**Normes et règlement** :

- ISO 5492:2008, et Amd 1:2016. https://www.iso.org/standard/38051.html — *extraits* (page de l'ISO : confirmée le 2024-01-13) ; numéros des termes repris du groupe odorat, non revérifiés ; texte non lu ; usage : vocabulaire (alimente).
- ISO 3972:2011, *Sensory analysis — Methodology — Method of investigating sensitivity of taste* (3e éd.), et Cor 1:2012. https://www.iso.org/standard/50110.html — *extraits* (aperçu public : domaine, points 3, 5, 7, 8 et tableau 3) ; confirmée le 2023-09-21 ; usage : repères de région (fonde), facettes `temperature_bouchee` et `avant` (alimente), sensibilité des sujets (contraste) ; « sensation métallique » en désaccord avec Lawless et al. (2004).
- ISO 13299:2016, *Sensory analysis — Methodology — General guidance for establishing a sensory profile* (2e éd.). https://www.iso.org/standard/58042.html — *extraits* (résumé, avant-propos, introduction) ; confirmée le 2026-09-08 ; usage : modalité `bouche`, accord (alimente).
- ISO 2173:2003, *Fruit and vegetable products — Determination of soluble solids — Refractometric method*. https://www.iso.org/standard/35851.html — *extrait d'index* (confirmée en 2022) ; usage : mesure associée indirecte du sucré (contraste).
- ISO 750:1998, *Fruit and vegetable products — Determination of titratable acidity*. https://www.iso.org/standard/22569.html — *extraits* (aperçu public : domaine, principe, expression des résultats ; confirmée en 2022) ; usage : mesure associée indirecte de l'acide (contraste).
- Règlement (UE) 2016/679 (RGPD), article 9. https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre2 — *extraits* (paragraphe 1 et début du paragraphe 2) ; usage : note facultative sur l'état de l'observateur (lecture des règles, pas un avis juridique).

**Saveurs** :

- Chandrashekar, J., Hoon, M. A., Ryba, N. J. P. & Zuker, C. S. (2006). The receptors and cells for mammalian taste. *Nature*, 444(7117), 288–294. https://doi.org/10.1038/nature05401 — *résumé*.
- Lindemann, B. (2001). Receptors and transduction in taste. *Nature*, 413(6852), 219–225. https://doi.org/10.1038/35093032 — *métadonnées*.
- Lindemann, B. (2000). A taste for umami. *Nature Neuroscience*, 3(2), 99–100. https://doi.org/10.1038/72153 — *métadonnées*.
- Ikeda, K. (2002). New seasonings. *Chemical Senses*, 27(9), 847–849 (traduction de : Ikeda, K. (1909), *Journal of the Chemical Society of Tokyo*, 30, 820–836, référence connue par *source secondaire* (Society for Research on Umami Taste), article non consulté). https://doi.org/10.1093/chemse/27.9.847 — *métadonnées*.
- Lindemann, B., Ogiwara, Y. & Ninomiya, Y. (2002). The discovery of umami. *Chemical Senses*, 27(9), 843–844. https://doi.org/10.1093/chemse/27.9.843 — *métadonnées*.
- Erickson, R. P. (2008). A study of the science of taste: On the origins and influence of the core ideas. *Behavioral and Brain Sciences*, 31(1), 59–75. https://doi.org/10.1017/S0140525X08003348 — *résumé* (commentaires non lus) ; usage : saveurs de base (discute).
- Running, C. A., Craig, B. A. & Mattes, R. D. (2015). Oleogustus: The unique taste of fat. *Chemical Senses*, 40(7), 507–516. https://doi.org/10.1093/chemse/bjv036 — *résumé*.
- Keast, R. S. J. & Costanzo, A. (2015). Is fat the sixth taste primary? Evidence and implications. *Flavour*, 4, 5. https://doi.org/10.1186/2044-7248-4-5 — *métadonnées*.
- Lapis, T. J., Penner, M. H. & Lim, J. (2016). Humans can taste glucose oligomers independent of the hT1R2/hT1R3 sweet taste receptor. *Chemical Senses*, 41(9), 755–762. https://doi.org/10.1093/chemse/bjw088 — *résumé*.
- Tordoff, M. G. (2001). Calcium: Taste, intake, and appetite. *Physiological Reviews*, 81(4), 1567–1597. https://doi.org/10.1152/physrev.2001.81.4.1567 — *résumé*.
- Ohsu, T., Amino, Y., Nagasaki, H. et al. (2010). Involvement of the calcium-sensing receptor in human taste perception. *Journal of Biological Chemistry*, 285(2), 1016–1022. https://doi.org/10.1074/jbc.M109.029165 — *résumé*.
- Lawless, H. T., Schlake, S., Smythe, J., Lim, J., Yang, H., Chapman, K. & Bolton, B. (2004). Metallic taste and retronasal smell. *Chemical Senses*, 29(1), 25–33. https://doi.org/10.1093/chemse/bjh003 — *résumé* ; usage : test du nez pincé, facette `nez` (fonde).

**Trijumeau, astringence, pétillant, température** :

- Viana, F. (2011). Chemosensory properties of the trigeminal system. *ACS Chemical Neuroscience*, 2(1), 38–50. https://doi.org/10.1021/cn100102c — *résumé*.
- Caterina, M. J., Schumacher, M. A., Tominaga, M., Rosen, T. A., Levine, J. D. & Julius, D. (1997). The capsaicin receptor: a heat-activated ion channel in the pain pathway. *Nature*, 389(6653), 816–824. https://doi.org/10.1038/39807 — *résumé* ; usage : `oralPungency` (fonde).
- Green, B. G. (1996). Chemesthesis: pungency as a component of flavor. *Trends in Food Science & Technology*, 7(12), 415–420. https://doi.org/10.1016/S0924-2244(96)10043-1 — *métadonnées*.
- McKemy, D. D., Neuhausser, W. M. & Julius, D. (2002). Identification of a cold receptor reveals a general role for TRP channels in thermosensation. *Nature*, 416(6876), 52–58. https://doi.org/10.1038/nature719 — *résumé*.
- Breslin, P. A. S., Gilmore, M. M., Beauchamp, G. K. & Green, B. G. (1993). Psychophysical evidence that oral astringency is a tactile sensation. *Chemical Senses*, 18(4), 405–417. https://doi.org/10.1093/chemse/18.4.405 — *résumé* ; usage : `astringency` au premier lot (fonde).
- Green, B. G. (1993). Oral astringency: A tactile component of flavor. *Acta Psychologica*, 84(1), 119–125. https://doi.org/10.1016/0001-6918(93)90078-6 — *résumé*.
- Lee, C. B. & Lawless, H. T. (1991). Time-course of astringent sensations. *Chemical Senses*, 16(3), 225–238. https://doi.org/10.1093/chemse/16.3.225 — *résumé* (dont l'alun à 1 g/l comme matériau de référence) ; usage : sous-qualités (alimente), repère de région de l'astringence (alimente), temps-intensité (non retenue : jugements d'un jury sans référence physique).
- Bajec, M. R. & Pickering, G. J. (2008). Astringency: Mechanisms and perception. *Critical Reviews in Food Science and Nutrition*, 48(9), 858–875. https://doi.org/10.1080/10408390701724223 — *résumé*.
- Chandrashekar, J., Yarmolinsky, D., von Buchholtz, L. et al. (2009). The taste of carbonation. *Science*, 326(5951), 443–445. https://doi.org/10.1126/science.1174601 — *résumé*.
- Cruz, A. & Green, B. G. (2000). Thermal stimulation of taste. *Nature*, 403(6772), 889–892. https://doi.org/10.1038/35002581 — *résumé* ; usage : facette `temperature_bouchee` (fonde).
- Talavera, K., Yasumatsu, K., Voets, T. et al. (2005). Heat activation of TRPM5 underlies thermal sensitivity of sweet taste. *Nature*, 438(7070), 1022–1025. https://doi.org/10.1038/nature04248 — *résumé*.

**Odeur en bouche, flaveur** :

- Rozin, P. (1982). "Taste–smell confusions" and the duality of the olfactory sense. *Perception & Psychophysics*, 31(4), 397–401. https://doi.org/10.3758/BF03202667 — *métadonnées* (pas de résumé publié ; texte non lu).
- Small, D. M., Gerber, J. C., Mak, Y. E. & Hummel, T. (2005). Differential neural responses evoked by orthonasal versus retronasal odorant perception in humans. *Neuron*, 47(4), 593–605. https://doi.org/10.1016/j.neuron.2005.07.022 — *résumé*.
- Lim, J. & Johnson, M. B. (2011). Potential mechanisms of retronasal odor referral to the mouth. *Chemical Senses*, 36(3), 283–289 (en ligne en 2010). https://doi.org/10.1093/chemse/bjq125 — *résumé*.
- Spence, C. (2015a). Multisensory flavor perception. *Cell*, 161(1), 24–35. https://doi.org/10.1016/j.cell.2015.03.007 — *résumé*.
- Spence, C. (2015b). Just how much of what we taste derives from the sense of smell? *Flavour*, 4, 30. https://doi.org/10.1186/s13411-015-0040-2 — *résumé*.

**Observateurs, échelles, méthodes** :

- Bartoshuk, L. M., Duffy, V. B. & Miller, I. J. (1994). PTC/PROP tasting: Anatomy, psychophysics, and sex effects. *Physiology & Behavior*, 56(6), 1165–1171. https://doi.org/10.1016/0031-9384(94)90361-1 — *résumé*.
- Bartoshuk, L. M. (2000). Comparing sensory experiences across individuals: Recent psychophysical advances illuminate genetic variation in taste perception. *Chemical Senses*, 25(4), 447–460. https://doi.org/10.1093/chemse/25.4.447 — *résumé*.
- Kim, U., Jorgenson, E., Coon, H., Leppert, M., Risch, N. & Drayna, D. (2003). Positional cloning of the human quantitative trait locus underlying taste sensitivity to phenylthiocarbamide. *Science*, 299(5610), 1221–1225. https://doi.org/10.1126/science.1080190 — *métadonnées*.
- Spielman, A. I. (1990). Interaction of saliva and taste. *Journal of Dental Research*, 69(3), 838–843. https://doi.org/10.1177/00220345900690030101 — *résumé*.
- Schiffman, S. S. (1997). Taste and smell losses in normal aging and disease. *JAMA*, 278(16), 1357–1362. https://doi.org/10.1001/jama.1997.03550160077042 — *résumé*.
- Vennemann, M. M., Hummel, T. & Berger, K. (2008). The association between smoking and smell and taste impairment in the general population. *Journal of Neurology*, 255(8), 1121–1126. https://doi.org/10.1007/s00415-008-0807-9 — *résumé*.
- Green, B. G., Shaffer, G. S. & Gilmore, M. M. (1993). Derivation and evaluation of a semantic scale of oral sensation magnitude with apparent ratio properties. *Chemical Senses*, 18(6), 683–702. https://doi.org/10.1093/chemse/18.6.683 — *résumé* (OpenAlex).
- Green, B. G., Dalton, P., Cowart, B., Shaffer, G., Rankin, K. & Higgins, J. (1996). Evaluating the 'Labeled Magnitude Scale' for measuring sensations of taste and smell. *Chemical Senses*, 21(3), 323–334. https://doi.org/10.1093/chemse/21.3.323 — *résumé* (OpenAlex).
- Bartoshuk, L. M., Duffy, V. B., Green, B. G. et al. (2004). Valid across-group comparisons with labeled scales: the gLMS versus magnitude matching. *Physiology & Behavior*, 82(1), 109–114. https://doi.org/10.1016/j.physbeh.2004.02.033 — *résumé* ; usage : les échelles à étiquettes classiques ne se comparent pas d'un groupe à l'autre, l'appariement à un repère non gustatif (un son) le permet ; gLMS non retenue comme mesure associée (contraste).
- Pineau, N., Schlich, P., Cordelle, S. et al. (2009). Temporal Dominance of Sensations: Construction of the TDS curves and comparison with time–intensity. *Food Quality and Preference*, 20(6), 450–455. https://doi.org/10.1016/j.foodqual.2009.04.005 — *résumé* (relu le 2026-10-20, série 75 : plusieurs attributs suivis en une seule dégustation ; profils proches du temps-intensité ; *métadonnées* auparavant).
- Szczesniak, A. S. (2002). Texture is a sensory property. *Food Quality and Preference*, 13(4), 215–225. https://doi.org/10.1016/S0950-3293(01)00039-8 — *métadonnées*.
- Lawless, H. T. & Heymann, H. (2010). *Sensory Evaluation of Food: Principles and Practices* (2e éd.). Springer. https://doi.org/10.1007/978-1-4419-6488-5 — *métadonnées* (aucune 3e éd. trouvée).
- Meilgaard, M., Civille, G. V. & Carr, B. T. (1999). *Sensory Evaluation Techniques* (3e éd.). CRC Press. https://doi.org/10.1201/9781439832271 — *métadonnées* ; 6e éd. : Civille, G. V., Carr, B. T. & Osdoba, K. E. (2024), https://doi.org/10.1201/9781003352082 — *métadonnées*.

**Texture en bouche (série 72)** : décision 3b de l'éditeur du projet (2026-10-19), qui fait entrer la texture en bouche dans la famille. Les sources sont vérifiées le 2026-10-19 (Crossref, OpenAlex, page et aperçu public de l'ISO). Types proposés : premier lot `hardnessInMouth`, `oralThickness` (décision de l'éditeur du projet, 2026-10-20, série 76) ; lot suivant `crispness`, `stickiness` ; en réserve `grittiness`, `juiciness`, `creaminess`. Mesure rédigée dans la proposition (7.5) ; les usages « proche » et « non retenue » ci-dessous la reprennent. La série 72 ter ajoute les références d'un éclairage sur la texture en bouche, avec le statut qu'il donne, et des métadonnées revérifiées sur Crossref le 2026-10-19.

- Szczesniak, A. S. (1963). Classification of textural characteristics. *Journal of Food Science*, 28(4), 385–389. https://doi.org/10.1111/j.1365-2621.1963.tb00215.x — *résumé* ; usage : classes mécaniques, géométriques, eau et gras ; caractéristiques primaires et secondaires (alimente les types et les exclusions).
- Brandt, M. A., Skinner, E. Z. & Coleman, J. A. (1963). Texture profile method. *Journal of Food Science*, 28(4), 404–409. https://doi.org/10.1111/j.1365-2621.1963.tb00218.x — *résumé* ; usage : ordre d'apparition, de la première bouchée à la mastication complète (alimente la facette `moment` (choix de relecture, 2026-10-20)).
- Friedman, H. H., Whitney, J. E. & Szczesniak, A. S. (1963). The texturometer — a new instrument for objective texture measurement. *Journal of Food Science*, 28(4), 390–396. https://doi.org/10.1111/j.1365-2621.1963.tb00216.x — *résumé* ; usage : instrument corrélé au jury (méthode trouvée, non classée).
- Szczesniak, A. S., Brandt, M. A. & Friedman, H. H. (1963). Development of standard rating scales for mechanical parameters of texture and correlation between the objective and the sensory methods of texture evaluation. *Journal of Food Science*, 28(4), 397–403. https://doi.org/10.1111/j.1365-2621.1963.tb00217.x — *résumé* ; usage : échelles dont chaque point est un aliment, choisi pour sa disponibilité, sa familiarité et la constance de sa texture (non retenues comme mesure : 7.5 de la proposition).
- Civille, G. V. & Szczesniak, A. S. (1973). Guidelines to training a texture profile panel. *Journal of Texture Studies*, 4(2), 204–223. https://doi.org/10.1111/j.1745-4603.1973.tb00665.x — *résumé* (bref ; détail des échelles non lu).
- Muñoz, A. M. (1986). Development and application of texture reference scales. *Journal of Sensory Studies*, 1(1), 55–83. https://doi.org/10.1111/j.1745-459X.1986.tb00159.x — *résumé* ; usage : révision des échelles, produits de référence remplacés parce qu'ils n'étaient plus disponibles.
- Jowitt, R. (1974). The terminology of food texture. *Journal of Texture Studies*, 5(3), 351–358. https://doi.org/10.1111/j.1745-4603.1974.tb01441.x — *résumé* ; usage : glossaire (labels).
- Bourne, M. C. (1978). Texture profile analysis. *Food Technology*, 32(7), 62–66, 72. Pas de DOI — *métadonnées* (référence relevée dans des bibliographies tierces) ; les définitions détaillées des paramètres de la TPA ne sont lues dans aucune source (**à vérifier** sur le texte) ; Nishinari et al. (2013) et Peleg (2019), *résumés*, ne les donnent pas.
- Bourne, M. C. (2002). *Food Texture and Viscosity: Concept and Measurement* (2e éd. ; 1re éd. 1982). Academic Press. Chapitre : https://doi.org/10.1016/b978-012119062-0/50007-3 — *métadonnées*.
- Nishinari, K., Kohyama, K., Kumagai, H., Funami, T. & Bourne, M. C. (2013). Parameters of texture profile analysis. *Food Science and Technology Research*, 19(3), 519–521. https://doi.org/10.3136/fstr.19.519 — *résumé* (série 72 ter ; *extrait d'index* en série 72) ; usage : les paramètres dépendent des conditions d'essai ; mise en garde pour les liquides (TPA non retenue pour `oralThickness` ; réserve pour `stickiness`).
- ISO 11036:2020. *Sensory analysis — Methodology — Texture profile* (2e éd., remplace ISO 11036:1994). https://www.iso.org/standard/76668.html — *extraits* (aperçu public : définition 3.1, 6.1, 6.2.1, tableau 1, 6.2.3.2, 6.2.3.3, 6.2.4.1 ; 6.4 et annexe A non lues) ; usage : attributs, ordre d'apparition, granularité, fonte (alimente les types candidats).
- Szczesniak (2002), déjà listée plus haut : usage ajouté, la texture comme propriété sensorielle (*métadonnées*).
- Vickers, Z. & Bourne, M. C. (1976). A psychoacoustical theory of crispness. *Journal of Food Science*, 41(5), 1158–1164. https://doi.org/10.1111/j.1365-2621.1976.tb14407.x — *résumé* ; usage : le croquant est surtout acoustique (réserve, recouvrement avec Son).
- Duizer, L. (2001). A review of acoustic research for studying the sensory perception of crisp, crunchy and crackly textures. *Trends in Food Science & Technology*, 12(1), 17–24. https://doi.org/10.1016/S0924-2244(01)00050-4 — *résumé* ; usage : acoustique de la rupture, proche pour `crispness` ; le son passe par les os.
- Shama, F. & Sherman, P. (1973). Identification of stimuli controlling the sensory evaluation of viscosity. II. Oral methods. *Journal of Texture Studies*, 4(1), 111–118. https://doi.org/10.1111/j.1745-4603.1973.tb00657.x — *résumé* ; usage : stimulus de l'épaisseur jugée en bouche (`oralThickness`).
- Kokini, J. L., Kadane, J. B. & Cussler, E. L. (1977). Liquid texture perceived in the mouth. *Journal of Texture Studies*, 8(2), 195–218. https://doi.org/10.1111/j.1745-4603.1977.tb01175.x — *résumé* ; usage : épaisseur, lisse, glisse (`oralThickness` ; traduction du « crémeux »).
- Kilcast, D. & Clegg, S. (2002). Sensory perception of creaminess and its relationship with food structure. *Food Quality and Preference*, 13(7–8), 609–623. https://doi.org/10.1016/S0950-3293(02)00074-5 — *résumé* ; usage : l'onctuosité est un attribut complexe (exclusion du « crémeux »).
- de Wijk, R. A. & Prinz, J. F. (2005). The role of friction in perceived oral texture. *Food Quality and Preference*, 16(2), 121–129. https://doi.org/10.1016/j.foodqual.2004.03.002 — *résumé* ; usage : gras, frottement, onctuosité ; lien avec l'astringence.
- Imai, E., Hatae, K. & Shimada, A. (1995). Oral perception of grittiness: effect of particle size and concentration of the dispersed particles and the dispersion medium. *Journal of Texture Studies*, 26(5), 561–576. https://doi.org/10.1111/j.1745-4603.1995.tb00804.x — *résumé* ; usage : le granuleux dépend de la taille et de la concentration des particules (`grittiness`, réserve).
- Hutchings, J. B. & Lillford, P. J. (1988). The perception of food texture — the philosophy of the breakdown path. *Journal of Texture Studies*, 19(2), 103–115. https://doi.org/10.1111/j.1745-4603.1988.tb00928.x — *résumé* ; usage : texture dynamique (facette `moment` (choix de relecture, 2026-10-20)).
- Lenfant, F., Loret, C., Pineau, N., Hartmann, C. & Martin, N. (2009). Perception of oral food breakdown. The concept of sensory trajectory. *Appetite*, 52(3), 659–667. https://doi.org/10.1016/j.appet.2009.03.003 — *résumé* ; usage : trajectoire de texture ; la TDS est un jugement de jury sans référence physique.
- Guinard, J.-X. & Mazzucchelli, R. (1996). The sensory perception of texture and mouthfeel. *Trends in Food Science & Technology*, 7(7), 213–219. https://doi.org/10.1016/0924-2244(96)10025-X — *métadonnées*.

- Meullenet, J.-F., Lyon, B. G., Carpenter, J. A. & Lyon, C. E. (1998). Relationship between sensory and instrumental texture profile attributes. *Journal of Sensory Studies*, 13(1), 77–93. https://doi.org/10.1111/j.1745-459X.1998.tb00076.x — *résumé* (relu sur OpenAlex le 2026-10-19 : 21 aliments ; dureté r = 0,76, 0,96 après logarithme ; élasticité 0,83 ; pas de corrélation significative pour la cohésion et la mâche dans les données brutes ; mâche r = 0,54, P < 0,05, après logarithmes des deux variables ; rien sur le gommeux) ; usage : TPA proche pour `hardnessInMouth` ; cohésion et mâche non retenues.
- Rosenthal, A. J. (2010). Texture profile analysis — how important are the parameters? *Journal of Texture Studies*, 41(5), 672–684. https://doi.org/10.1111/j.1745-4603.2010.00248.x — *résumé* ; usage : la TPA dépend du réglage (écart).
- Peleg, M. (2019). The instrumental texture profile analysis revisited. *Journal of Texture Studies*, 50(5), 362–368. https://doi.org/10.1111/jtxs.12392 — *résumé* ; usage : réglage, adhésivité (`stickiness`).
- Wood, F. W. (1968). Psychophysical studies on the consistency of liquid foods. *SCI Monograph* 27, 40–49 — *source secondaire* (via van Vliet 2002) ; usage : vitesse de cisaillement choisie pour l'épaisseur (`oralThickness`, proche).
- van Vliet, T. (2002). On the relation between texture perception and fundamental mechanical parameters for liquids and time dependent solids. *Food Quality and Preference*, 13(4), 227–236. https://doi.org/10.1016/S0950-3293(01)00044-1 — *extraits* (passage sur Wood, à relire sur le texte).
- Stokes, J. R., Boehm, M. W. & Baier, S. K. (2013). Oral processing, texture and mouthfeel: from rheology to tribology and beyond. *Current Opinion in Colloid & Interface Science*, 18(4), 349–359. https://doi.org/10.1016/j.cocis.2013.04.010 — *résumé* ; usage : la TPA et la rhéologie ne saisissent que le début de la bouchée ; salive.
- Chen, J. & Stokes, J. R. (2012). Rheology and tribology: two distinctive regimes of food texture sensation. *Trends in Food Science & Technology*, 25(1), 4–12. https://doi.org/10.1016/j.tifs.2011.11.006 — *métadonnées* ; usage : tribologie (`creaminess`, aucune méthode robuste).
- Zampini, M. & Spence, C. (2004). The role of auditory cues in modulating the perceived crispness and staleness of potato chips. *Journal of Sensory Studies*, 19(5), 347–363. https://doi.org/10.1111/j.1745-459x.2004.080403.x — *résumé* ; usage : le son entendu change le croustillant (modalité ouverte de `crispness`).
- Engelen, L., de Wijk, R. A., Prinz, J. F., Janssen, A. M., Weenen, H. & Bosman, F. (2003). The effect of oral and product temperature on the perception of flavor and texture attributes of semi-solids. *Appetite*, 41(3), 273–281. https://doi.org/10.1016/S0195-6663(03)00105-3 — *résumé* ; usage : `temperature_bouchee` critique pour `oralThickness` (l’épaisseur perçue baisse quand le produit est plus chaud) ; `flavourIntensity` (l’intensité des saveurs monte quand le produit est plus chaud ; crème dessert et mayonnaise, à 10, 22 et 35 °C).
- Engelen, L., de Wijk, R. A., van der Bilt, A., Prinz, J. F., Janssen, A. M. & Bosman, F. (2005). Relating particles and texture perception. *Physiology & Behavior*, 86(1–2), 111–117. https://doi.org/10.1016/j.physbeh.2005.06.022 — *résumé* ; usage : `grittiness` (aucune méthode robuste).
- Veyrune, J.-L. & Mioche, L. (2000). Complete denture wearers: electromyography of mastication and texture perception whilst eating meat. *European Journal of Oral Sciences*, 108(2), 83–92. https://doi.org/10.1034/j.1600-0722.2000.90780.x — *résumé* ; usage : juteux noté par jury (`juiciness`) ; dentition et état de l'observateur.

- Brown, W. E., Langley, K. R., Martin, A. & MacFie, H. J. H. (1994). Characterisation of patterns of chewing behaviour in human subjects and their influence on texture perception. *Journal of Texture Studies*, 25(4), 455–468. https://doi.org/10.1111/j.1745-4603.1994.tb00774.x — *résumé* (lu pour l'éclairage ; métadonnées revérifiées sur Crossref le 2026-10-19) ; usage : chacun mâche à sa façon (5.1).
- Kohyama, K., Mioche, L. & Martin, J.-F. (2002). Chewing patterns of various texture foods studied by electromyography in young and elderly populations. *Journal of Texture Studies*, 33(4), 269–283. https://doi.org/10.1111/j.1745-4603.2002.tb01349.x — *résumé* (lu pour l'éclairage ; métadonnées revérifiées sur Crossref le 2026-10-19) ; usage : âge et mastication (5.1).

**Non vérifié (texture)** : les termes de texture d'ISO 5492, dont ISO 5492:2008/Amd 1:2016, 2.40, *tactile after-feel* (renvoi de `residual`) ; ISO 11036:2020, 6.4, 7.2.2 et annexe A ; une source perceptive sur la fonte en bouche ; une corrélation entre l'adhésivité de la TPA et le collant d'un jury ; l'effet de la taille de la bouchée ; une méthode de granulométrie et une méthode du jus de viande.

**Esthétique du goût (contraste)** :

- Korsmeyer, C. (1999). *Making Sense of Taste: Food and Philosophy*. Cornell University Press. ISBN 978-0-8014-3698-7 ; édition numérique : https://doi.org/10.7591/9780801471339 — *description de l'éditeur* et sommaire.
- Sweeney, K. W. (2017). *The Aesthetics of Food: The Philosophical Debate About What We Eat and Drink*. Rowman & Littlefield International. ISBN 978-1-78348-743-1 — *description de l'éditeur* et sommaire.
- Todd, C. (2010). *The Philosophy of Wine: A Case of Truth, Beauty and Intoxication*. Acumen. ISBN 978-1-84465-250-1 — *description de l'éditeur* et sommaire.
- Smith, B. C. (dir.) (2007). *Questions of Taste: The Philosophy of Wine*. Signal Books / Oxford University Press. ISBN 978-0-19-533146-2 — *métadonnées* (Open Library).

**Méthodes de mesure associées (série 71 bis)** : règle de `proposition-rubrique-mesure.md` (document du dépôt, non publié), section 1, point 2 ; toutes indirectes.

- EBC (2020). *Analytica EBC*, méthode 9.8, *Bitterness of Beer (IM)* ; ASBC, *Beer-23A, Beer Bitterness — Bitterness Units (International Method)*. https://brewup.eu/ebc-analytica/beer/bitterness-of-beer-im/9.8 ; https://www.asbcnet.org/Methods/BeerMethods/pages/Beer-23-MasterMethod.aspx — *extrait d'index* (pages de l'EBC, de BrewUp et de l'ASBC) ; texte d'EBC 9.8 par *source secondaire* (copie tierce) ; usage : `bitterness`, bière et moût seulement (contraste).
- ISO 7543-2:1993. *Chillies and chilli oleoresins — Determination of total capsaicinoid content — Part 2: Method using high-performance liquid chromatography*. https://www.iso.org/standard/14328.html — *extraits* (aperçu public : domaine, principe, calcul ; confirmée en 2026) ; usage : `oralPungency`, extrait de piment seulement (contraste).
- ASTA. *Analytical Method 21.3, Pungency of Capsicums and Their Oleoresins (HPLC Method — Preferred)*, révision 2026. https://astaspice.org/resources/asta-method-21-3-2026-pungency-of-capsicums-and-their-oleoresins-hplc-method-preferred — *extrait d'index* ; usage : `oralPungency` (contraste).
- ISO 3513:1995. *Chillies — Determination of Scoville index*. https://www.iso.org/standard/8880.html — *extraits* (aperçu public : domaine, définition 3.1, principe, réactifs, préparation des dilutions ; confirmée en 2024) ; usage : `oralPungency`, seuil de dilution par jury (contraste, comme EN 13725).
- ISO 14502-1:2005. *Determination of substances characteristic of green and black tea — Part 1: Content of total polyphenols in tea — Colorimetric method using Folin-Ciocalteu reagent*. https://www.iso.org/standard/31356.html — *extraits* (aperçu public : domaine, principe, réactifs ; confirmée en 2025) ; usage : `astringency`, thé seulement (contraste).
- ASTM E1909-24. *Standard Guide for Time-Intensity Evaluation of Sensory Attributes*. https://doi.org/10.1520/E1909-24 — *extrait d'index* (page de l'ASTM) ; usage : non retenue (jugements d'un jury sans référence physique).

**Grille CIEL (série 75, note de travail non publiée `note-grille-ciel.md`)** : grille de dégustation du vin (complexité, intensité, équilibre, longueur), proposée comme grille de lecture, sans type ni fiche. Sources vérifiées le 2026-10-20 (Crossref ; résumés sur PubMed, OpenAlex, pages des éditeurs et des dépôts d'universités ; pages des organismes). Usages : grille (usage d'atelier), complexité, intensité, équilibre, longueur. **Série 77** (décision de l'éditeur du projet, 2026-10-20) : les quatre axes deviennent quatre types du lot CIEL (`flavourComplexity`, `flavourIntensity`, `flavourBalance`, `tastePersistence` ; proposition « Goût », 1.10, 2.8 et 7.6) ; les références ci-dessous servent désormais ces types, et la série 77 en ajoute sept, à la fin du bloc.

- Rousselin, Y. (2023). *Le vin pas à pas : apprenez les clés sur le vin, et vivez votre passion !* Ellipses. ISBN 978-2-340-08349-3 — *description de l'éditeur* et sommaire (leçon 45, « la méthode CIEL ») ; contenu de la leçon par *source secondaire* (compte rendu, vinquebec.com, 2024) ; usage : la grille comme méthode d'évaluation de la qualité (contraste).
- Le COAM. *Référentiel de certification « Déguster et évaluer professionnellement le vin »* (France Compétences). https://certifpro.francecompetences.fr/api/fiches/refActivity/24709/485416 — *extraits* ; version du 02/03/2023 (« version 020323 » dans le titre du document) : *métadonnées* ; usage : la grille dans l'enseignement de la dégustation (usage d'atelier).
- WSET (2016). *WSET Level 3 Systematic Approach to Tasting Wine*. https://www.wsetglobal.com/media/3119/wset_l3_wines_sat_en_jun-2016.pdf — *lu en entier* (grille et lexique) ; les quatre critères de qualité par *source secondaire* ; usage : crans descriptifs séparés du jugement de qualité (alimente) ; crans de jury non retenus comme mesure.
- Peynaud, É. & Blouin, J. (2022). *Le goût du vin* (1re éd. Bordas, 1980). Dunod. ISBN 978-2-10-085002-0 — *extraits* (préfaces et sommaire de l'extrait de l'éditeur ; chapitre sur les équilibres des saveurs non lu) ; 5e éd. (2013), p. 87, définition de la caudalie par *source secondaire* ; usage : équilibre des saveurs (alimente).
- Office québécois de la langue française, *Grand dictionnaire terminologique*, « caudalie ». https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/17594568/caudalie — *extraits* (auteur indiqué : INAO, 1972, non consulté) ; usage : caudalie, non retenue comme mesure (jugement chronométré).
- Académie française, *Dictionnaire*, 9e éd., « caudalie ». https://www.dictionnaire-academie.fr/article/A9_0224 — *extrait d'index* ; usage : persistance « gustative » (désaccord avec « aromatique »).
- Jean-Dorize, T. (13 février 2024). « La méthode CIEL : la technique facile pour reconnaître un bon vin ». *Journal des Femmes*. https://cuisine.journaldesfemmes.fr/astuces-termes-et-tournemains/3161000-la-methode-ciel-la-technique-facile-pour-reconnaitre-un-bon-vin/ — *source secondaire* (vérifié le 2026-10-20) ; usage : attribution de la grille au fondateur du COAM, qui la présente lui-même (création et date non vérifiées).
- Nau, J.-Y. (11 décembre 2010). « Caudalie (Houellebecq et « longueurs en bouche ») ». *Slate.fr*. https://www.slate.fr/story/31277/caudalies-houellebecq-vin — *source secondaire* (vérifié le 2026-10-20) ; usage : emploi plus ancien, « codalie », Bulletin de l'INAO n° 86, juillet 1963, p. 19 (bulletin non consulté).
- Charters, S. & Pettigrew, S. (2007). The dimensions of wine quality. *Food Quality and Preference*, 18(7), 997–1007. https://doi.org/10.1016/j.foodqual.2007.04.003 — *résumé* ; usage : la qualité, construit à plusieurs dimensions, terminales ou catalytiques (contraste).
- Parr, W. V., Mouret, M., Blackmore, S., Pelquest-Hunt, T. & Urdapilleta, I. (2011). Representation of complexity in wine: Influence of expertise. *Food Quality and Preference*, 22(7), 647–660. https://doi.org/10.1016/j.foodqual.2011.04.005 — *résumé* et *extraits* (introduction) ; usage : complexité selon l'expertise (contraste).
- Meillon, S., Viala, D., Medel, M., Urbano, C., Guillot, G. & Schlich, P. (2010). Impact of partial alcohol reduction in Syrah wine on perceived complexity and temporality of sensations and link with preference. *Food Quality and Preference*, 21(7), 732–740. https://doi.org/10.1016/j.foodqual.2010.06.005 — *résumé* et *extraits* (introduction ; questionnaire de Medel et al. 2009 par *source secondaire*) ; usage : complexité jugée, liée à la persistance et au nombre d'arômes (alimente) ; questionnaire non retenu comme mesure.
- Medel, M., Viala, D., Meillon, S., Urbano, C. & Schlich, P. (2009). A questionnaire for assessing the perceived complexity of wine: Application to the study of the effect of expertise on perception of wine complexity. Communication orale, 8th Pangborn Sensory Science Symposium, Florence, 26–30 juillet 2009 — *métadonnées* (liste de références de Meillon et al. 2010, sur Crossref, vérifiée le 2026-10-20) ; contenu par *source secondaire* ; usage : questionnaire de complexité, non retenu comme mesure.
- Schlich, P., Medel Maraboli, M., Urbano, C. & Parr, W. V. (2015). Perceived complexity in Sauvignon Blanc wines: influence of domain-specific expertise. *Australian Journal of Grape and Wine Research*, 21(2), 168–178. https://doi.org/10.1111/ajgw.12129 — *résumé* ; usage : complexité liée à l'harmonie et à l'équilibre plutôt qu'à la séparabilité (discute).
- Laing, D. G. & Francis, G. W. (1989). The capacity of humans to identify odors in mixtures. *Physiology & Behavior*, 46(5), 809–814. https://doi.org/10.1016/0031-9384(89)90041-3 — *résumé* ; usage : identification limitée des odeurs d'un mélange (fonde les crans bas de `flavourComplexity`) ; la limite de « trois à quatre » lui est attribuée par Jinks et Laing (2001) (*source secondaire* pour ce chiffre).
- Livermore, A. & Laing, D. G. (1996). Influence of training and experience on the perception of multicomponent odor mixtures. *Journal of Experimental Psychology: Human Perception and Performance*, 22(2), 267–277. https://doi.org/10.1037/0096-1523.22.2.267 — *résumé* ; usage : 3 ou 4 composantes, même entraîné (fonde).
- Laing, D. G., Link, C., Jinks, A. & Hutchinson, I. (2002). The limited capacity of humans to identify the components of taste mixtures and taste–odour mixtures. *Perception*, 31(5), 617–635. https://doi.org/10.1068/p3205 — *résumé* ; usage : au plus trois saveurs identifiées (alimente).
- Marshall, K., Laing, D. G., Jinks, A. & Hutchinson, I. (2006). The capacity of humans to identify components in complex odor–taste mixtures. *Chemical Senses*, 31(6), 539–545. https://doi.org/10.1093/chemse/bjj058 — *résumé* ; usage : deux composantes identifiées dans les mélanges de quatre à six (alimente).
- Hughson, A. L. & Boakes, R. A. (2002). The knowing nose: the role of knowledge in wine expertise. *Food Quality and Preference*, 13(7–8), 463–472. https://doi.org/10.1016/S0950-3293(02)00051-4 — *résumé* ; usage : expertise et vocabulaire (alimente).
- Solomon, G. E. A. (1990). Psychology of novice and expert wine talk. *The American Journal of Psychology*, 103(4), 495. https://doi.org/10.2307/1423321 — *résumé* (une phrase) ; usage : experts et novices.
- Keast, R. S. J. & Breslin, P. A. S. (2003). An overview of binary taste–taste interactions. *Food Quality and Preference*, 14(2), 111–124. https://doi.org/10.1016/S0950-3293(02)00110-6 — *résumé* et *extraits* (introduction, conclusion) ; usage : renforcement, additivité, suppression de mélange (fonde la lecture de l'équilibre comme profil perçu).
- Zamora, M. C., Goldner, M. C. & Galmarini, M. V. (2006). Sourness–sweetness interactions in different media: white wine, ethanol and water. *Journal of Sensory Studies*, 21(6), 601–611. https://doi.org/10.1111/j.1745-459X.2006.00085.x — *résumé* ; usage : l'acide supprime le sucré dans le vin (alimente).
- Fontoin, H., Saucier, C., Teissedre, P.-L. & Glories, Y. (2008). Effect of pH, ethanol and acidity on astringency and bitterness of grape seed tannin oligomers in model wine solution. *Food Quality and Preference*, 19(3), 286–291. https://doi.org/10.1016/j.foodqual.2007.08.004 — *résumé* ; usage : éthanol et pH changent astringence et amertume (alimente).
- Goodstein, E. S., Bohlscheid, J. C., Evans, M. & Ross, C. F. (2014). Perception of flavor finish in model white wine: A time-intensity study. *Food Quality and Preference*, 36, 50–60. https://doi.org/10.1016/j.foodqual.2014.02.012 — *résumé* et *extraits* (introduction, lue le 2026-10-20 sur la page de l'éditeur : « According to a 2001 review by Ebeler, over 1300 compounds have been successfully detected in wine, beer, malt beverages, brandy, and distilled spirits ») ; usage : finale selon la note (alimente) ; temps-intensité non retenu comme mesure ; chiffre d'Ebeler (2001) par *source secondaire* (7.6).
- Baker, A. K. & Ross, C. F. (2014). Wine finish in red wine: The effect of ethanol and tannin concentration. *Food Quality and Preference*, 38, 65–74. https://doi.org/10.1016/j.foodqual.2014.05.014 — *résumé* ; définition de Jackson (2002) par *source secondaire* ; usage : l'éthanol allonge la finale (alimente).
- Jackson, R. S. (2002). *Wine Tasting: A Professional Handbook*. Academic Press. ISBN 0-12-379076-X — *métadonnées* (notices de bibliothèques, vérifiées le 2026-10-20) ; définition de la finale par *source secondaire* (Baker et Ross 2014) ; usage : la finale (alimente).
- Trevisani, M., Smart, D., Gunthorpe, M. J. et al. (2002). Ethanol elicits and potentiates nociceptor responses via the vanilloid receptor-1. *Nature Neuroscience*, 5(6), 546–551. https://doi.org/10.1038/nn0602-852 — *résumé* (PubMed, 2026-10-20) ; usage : l'éthanol active TRPV1 (`oralPungency`, chaleur de l'alcool à éprouver).
- Prescott, J. & Swain-Campbell, N. (2000). Responses to repeated oral irritation by capsaicin, cinnamaldehyde and ethanol in PROP tasters and non-tasters. *Chemical Senses*, 25(3), 239–246. https://doi.org/10.1093/chemse/25.3.239 — *résumé* (PubMed, 2026-10-20) ; usage : l'éthanol irrite la bouche, avec désensibilisation (`oralPungency`).
- Nolden, A. A. & Hayes, J. E. (2015). Perceptual qualities of ethanol depend on concentration, and variation in these percepts associates with drinking frequency. *Chemosensory Perception*, 8(3), 149–157. https://doi.org/10.1007/s12078-015-9196-5 — *résumé* (PubMed, 2026-10-20) ; usage : amertume dominante à 8 et 16 %, brûlure à 32 et 48 % (`oralPungency`, `bitterness`).
- Esteban-Fernández, A., Rocha-Alcubilla, N., Muñoz-González, C., Moreno-Arribas, M. V. & Pozo-Bayón, M. Á. (2016). Intra-oral adsorption and release of aroma compounds following in-mouth wine exposure. *Food Chemistry*, 205, 280–288. https://doi.org/10.1016/j.foodchem.2016.03.030 — *résumé* ; usage : mesure indirecte des odorants relâchés après avoir recraché (piste à évaluer pour `tastePersistence`).

- Jinks, A. & Laing, D. G. (1999). A limit in the processing of components in odour mixtures. *Perception*, 28(3), 395–404. https://doi.org/10.1068/p2898 — *résumé* (PubMed, vérifié le 2026-10-20) ; usage : identification au hasard avec seize odorants (fonde les crans bas de `flavourComplexity`).
- Jinks, A. & Laing, D. G. (1999). Temporal processing reveals a mechanism for limiting the capacity of humans to analyze odor mixtures. *Cognitive Brain Research*, 8(3), 311–325. https://doi.org/10.1016/S0926-6410(99)00034-8 — *résumé* (PubMed, vérifié le 2026-10-20) ; usage : analyse limitée à « environ trois composantes » (fonde le cran « trois »).
- Jinks, A. & Laing, D. G. (2001). The analysis of odor mixtures by humans: evidence for a configurational process. *Physiology & Behavior*, 72(1–2), 51–63. https://doi.org/10.1016/S0031-9384(00)00407-8 — *résumé* (PubMed, vérifié le 2026-10-20) ; usage : limite de trois à quatre (attribuée à Laing et Francis 1989), perception configurale (alimente `flavourComplexity`).
- Stevens, S. S. (1957). On the psychophysical law. *Psychological Review*, 64(3), 153–181. https://doi.org/10.1037/h0046162 — *métadonnées* (Crossref, vérifié le 2026-10-20) ; usage : estimation de grandeur, non retenue comme mesure (lot CIEL).
- Delahunty, C. M., Eyres, G. & Dufour, J.-P. (2006). Gas chromatography-olfactometry. *Journal of Separation Science*, 29(14), 2107–2125. https://doi.org/10.1002/jssc.200500509 — *résumé* (Crossref, vérifié le 2026-10-20) ; usage : CPG-O (fréquence de détection, dilution jusqu'au seuil, intensité directe), mesure indirecte de `flavourComplexity`.
- Clark, C. C. & Lawless, H. T. (1994). Limiting response alternatives in time-intensity scaling: an examination of the halo-dumping effect. *Chemical Senses*, 19(6), 583–594. https://doi.org/10.1093/chemse/19.6.583 — *résumé* (PubMed, vérifié le 2026-10-20) ; usage : la liste des réponses offertes change les notes (piège de `flavourBalance`).
- Pineau et al. (2009), décrit plus haut dans ce groupe : *résumé* et *extraits* de l'introduction (ScienceDirect, vérifié le 2026-10-20) ; usage (série 77 ter) : contraste : dominance attentionnelle, distincte de la force relative (`flavourBalance` porte sur la force relative perçue) ; TDS non retenue comme mesure.
- Visalli, M. & Galmarini, M. V. (2024). Multi-attribute temporal descriptive methods in sensory analysis applied in food science: A systematic scoping review. *Comprehensive Reviews in Food Science and Food Safety*, 23(1), e13294. https://doi.org/10.1111/1541-4337.13294 — *métadonnées* ; *extrait d'index* pour la phrase citée (Crossref, vérifié le 2026-10-20 : titre, auteurs, revue, volume 23, numéro 1, article e13294, janvier 2024, conformes) ; texte non lu (page de l'éditeur fermée ; dépôt HAL hal-04533664 derrière une page anti-robot) ; usage : *source secondaire* pour la définition complète de la dominance de la TDS (« the attribute that triggers the attention (i.e., most striking perception at a given time), not necessarily the most intense », citée par la relecture du 2026-10-20) ; contraste pour `flavourBalance`.

**Non vérifié (grille CIEL)** : qui a créé la grille, et à quelle date (attestée au plus tard en mars 2023) ; invention de la caudalie par Peynaud ; source de 1972 du Grand dictionnaire terminologique et bulletin de l'INAO de 1963 (« codalie ») ; contenu de Medel et al. (2009) ; texte de Jackson (2002) ; persistance d'une saveur (et non d'un arôme) dans le vin ; définition de l'équilibre chez Peynaud (chapitre non lu) ; chiffre « trois à quatre » sur le texte de Laing et Francis (1989) ; tout lien entre le rapport °Brix / acidité et la dominante perçue (série 77).

**Non vérifié** : numéros des termes d'ISO 5492 (persistance, arôme, flaveur, astringence) ; effets de l'adaptation et de l'ordre de dégustation dans les manuels ; repère de région pour le piquant (aucun repère public sûr ; la capsaïcine pure n'est pas proposée) ; mesures physiques de l'astringence ; rapport °Brix / acidité comme indice de saveur ; température de mesure d'ISO 2173:2003 ; « kokumi » et « métallique » pour d'autres sels que le fer.

<a id="mesures-preparation"></a>
### Mesures associées des fiches en préparation (rubrique `mesure`)

Rubrique `mesure` des huit fiches en préparation (`elementaryShapeCount`, `odourCharacter`, `odourIntensity`, `pitchClarity`, `soundAttack`, `soundDecay`, `soundSharpness`, `textureContrast`) ; recherche du 2026-10-16. Aucune méthode robuste : `elementaryShapeCount`, `odourCharacter`, `pitchClarity` (force de hauteur, Fastl et Stoll 1979, non retenue). Les références déjà décrites ailleurs gardent leur notice : McAdams et al. (1995), Grey (1977), Klatzky et al. (2000), Giordano et McAdams (2006), Fastl et Stoll (1979), ISO 25178-2 et NPL GPG 116 (`mesures-matiere`) ; DIN 45692 (statut de lecture mis à jour : page de DIN Media lue). Aucun seuil n’est repris.

- ASTM E544-18. Standard Practice for Referencing Suprathreshold Odor Intensity. https://store.astm.org/e0544-18.html
  - statut : *vérifiée sur résumé ou source secondaire* (page de l’éditeur, résumé et Scope, sections 1.1 à 1.5, lus ; texte payant non lu) ;
  - usage : `odourIntensity` (contraste ; mesure associée proche : intensité rapportée au 1-butanol).
- EN 13725:2022. Stationary source emissions — Determination of odour concentration by dynamic olfactometry and odour emission rate. https://webstore.ansi.org/preview-pages/BSI/preview_30454302.pdf
  - statut : *vérifiée sur résumé ou source secondaire* (extrait public de BS EN 13725:2022, domaine d’application, section 1, lu ; texte payant non lu) ;
  - usage : `odourIntensity` (contraste ; mesure associée indirecte : concentration d’odeur).
- DIN 45692:2009-08. Messtechnische Simulation der Hörempfindung Schärfe. https://doi.org/10.31030/1521326
  - statut : *vérifiée sur résumé ou source secondaire* (page de DIN Media lue le 2026-10-16 ; norme non lue) ;
  - usage : `soundSharpness` (contraste ; mesure associée proche : acuité en acum).

*English version.* Associated measurements of the entries in preparation (`mesure` section); search of 2026-10-16; titles in their original language. No robust method: `elementaryShapeCount`, `odourCharacter`, `pitchClarity` (pitch strength, Fastl and Stoll 1979, not retained). References described elsewhere keep their records.

- ASTM E544-18, Standard Practice for Referencing Suprathreshold Odor Intensity: *public abstract and scope read* (sections 1.1–1.5); use: `odourIntensity` (close associated measurement).
- EN 13725:2022, Stationary source emissions — Determination of odour concentration by dynamic olfactometry and odour emission rate: *public extract read* (scope, section 1); use: `odourIntensity` (indirect associated measurement).
- DIN 45692:2009-08, Messtechnische Simulation der Hörempfindung Schärfe: *DIN Media page read*; standard not read; use: `soundSharpness` (close associated measurement, acum).

<a id="groupe-sources-generales"></a>
<a id="groupe-droits"></a>
## Droits des images d'exemplaires (Q15, X16 ; sources lues, pas un avis juridique)

*Série 20* : ces sources documentent un doute qui ne bloque plus la reproduction des trois Malévitch (critère de l'éditeur du projet : image hébergée sur Wikimedia Commons avec licence et balise indiquées) ; elles restent citées pour la trace du doute.

- Mémorial, *Otkrytyi spisok* (« Liste ouverte »), « Малевич Казимир Северинович (1878) ». https://ru.openlist.wiki/Малевич_Казимир_Северинович_(1878)
  - statut : *vérifiée sur la source* (page lue le 2026-10-11) ; base de données compilée, ici à partir de « données recueillies à Saint-Pétersbourg » : ce n'est pas le dossier lui-même ;
  - reprend : arrestation le 30 septembre 1930 ; le 29 novembre 1930, affaire classée par l'OGPU pour absence d'infraction ; aucune mention de réhabilitation ;
  - usage : doute russe sur les trois Malévitch de `exemplaires.yaml` (`docs/droits-exemples-2026-10-11.md`) ; ne dit pas si la mention « réprimé puis réhabilité » du modèle Commons `PD-Russia-expired` s'applique ; depuis la série 20, ce doute est noté mais ne bloque plus la reproduction (image sur Commons avec licence et balise indiquées, décision de l'éditeur du projet).
- Buksha, K. S., biographie de Kazimir Malévitch, chapitre « Тюрьма ». Texte en ligne : http://sv-scena.ru/Buki/Malyevich.49.html
  - statut : *vérifiée sur résumé ou source secondaire* (texte reproduit sur un site tiers, lu le 2026-10-11 ; édition imprimée non vérifiée) ;
  - reprend : arrestation le 20 septembre 1930, détention jusqu'au 6 décembre (dates divergentes avec la Liste ouverte) ;
  - usage : même doute ; ne parle pas de réhabilitation.
- Galerie Tretiakov, « 15 faits sur Kazimir Malévitch », *Lavrus*. https://lavrus.tretyakov.ru/publications/15-faktov-o-kazimire-maleviche/
  - statut : *vérifiée sur résumé ou source secondaire* (extrait lu le 2026-10-11 par un moteur de recherche) ;
  - reprend : arrestation en septembre 1930, libération au bout de deux mois et demi, aucune preuve trouvée ; mort le 15 mai 1935 ; aucune mention de réhabilitation.

## Sources générales repérées, non attachées à une fiche

- Arnheim, R. (1954). Art and Visual Perception. Berkeley : University of California Press. https://openlibrary.org/works/OL980214W
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : notice Open Library (titre, auteur, 1954, University of California Press, OCLC 256947) ; contenu non lu ;
  - usage : ouvrage général sur la forme vue ; non lu, il n'est attaché à aucune fiche. À lire avant de le citer pour un type.

<a id="groupe-non-verifiees"></a>
## Références non vérifiées, affirmations non vérifiées, sources écartées

- **ISO 2813, avertissement** : `ppp:surfaceGloss` (`grandeur_physique_homonyme`) dit que la norme elle-même avertit que la valeur mesurée ne correspond pas toujours à la brillance vue. Seule la page de présentation de la norme a été lue ; le texte est payant. Affirmation **non vérifiée** (notée dans la fiche, `note_verification`).
- **OQLF, « terme déconseillé »** : l'`avertissement_label` de `ppp:surfaceGloss` attribuait « terme déconseillé » à la fiche GDT « luminance lumineuse ». Vérifié le 2026-10-10 : « emploi déconseillé » figure sur la fiche GDT 8885899 « brillance » (peinture, 1983 : appellation ancienne de la *luminosité* d'une surface qui émet de la lumière ; déconseillée pour la confusion entre « brillance », réflexion diffuse, et « brillant », réflexion régulière) ; la fiche 8876545 « luminance lumineuse » dit « autrefois brillance », « désuet », encore en usage en astronomie ; l'Académie française dit « on dit plutôt Luminance ». Avertissement corrigé en 2.5, puis relu.
- **Attneave (1954)**, « Some informational aspects of visual perception », *Psychological Review*, 61(3), 183–193, DOI 10.1037/h0054663 : examiné comme source possible sur la courbure d'un contour. Le résumé consulté ne porte aucune affirmation sur la courbure ; **écartée** pour `ppp:curvature` tant que le texte n'est pas lu.
- **Joint** : recherche d'une source perceptive sur l'écart et l'affleurement vus au joint (Crossref, Semantic Scholar, 2026-10-10) : rien de pertinent ; les résultats portent sur des mesures industrielles (écart et affleurement, en anglais *gap and flush*) ou sur la construction. Aucune n'est citée.
- **Contraste général, contraste d'échelle** : aucune source trouvée qui propose un contraste perçu général ou un écart de taille perçu à degrés (`ppp:perceptualContrast`, `ppp:scaleContrast` ; recherches du 2026-10-10 et du 2026-10-11). Des sources voisines sont citées depuis le 2026-10-11 : contraste perçu et contraste calculé (Peli 1990 ; Haun et Peli 2013), illusions de contraste de taille (Girgus et al. 1972 ; de Fockert et al. 2007 ; Mruczek et al. 2017). Non retenues : Aglioti, DeSouza et Goodale (1995), *Size-contrast illusions deceive the eye but not the hand* (doi:10.1016/S0960-9822(95)00133-3 ; Crossref et OpenAlex sans résumé, non lu) ; Whittle (1992), *Brightness, discriminability and the “Crispening Effect”* (doi:10.1016/0042-6989(92)90205-W ; sans résumé, non lu ; porte sur la clarté) ; les définitions de Weber et de Michelson n'ont pas été lues dans leur source.

<a id="groupe-spec"></a>
## Sources de la spec (emprunts explicites)

Les emprunts de la spec sont appelés en note dans `PPP_Specification.md` ; la liste complète est dans sa section « Références ». Sources du cadre : voir [`etat-de-l-art.md`](etat-de-l-art.md) §7. Ajouts vérifiés le 2026-10-10 :

- Hatchuel, A. & Weil, B. (2008, date Crossref). C-K design theory: an advanced formulation. *Research in Engineering Design*, 19(4), 181–192. https://doi.org/10.1007/s00163-008-0043-4 — *vérifiée sur résumé ou source secondaire* (métadonnées Crossref).
- Le Masson, P., Weil, B. & Hatchuel, A. (2017). *Design Theory*. Springer. https://doi.org/10.1007/978-3-319-50277-9 — *vérifiée sur résumé ou source secondaire* (métadonnées Crossref).
- Gruber, T. R. (1995). Toward principles for the design of ontologies used for knowledge sharing. *International Journal of Human-Computer Studies*, 43(5–6), 907–928. https://doi.org/10.1006/ijhc.1995.1081 — *vérifiée sur la source* (version de l'auteur, révision 1993, rapport KSL 93-04, https://tomgruber.org/writing/onto-design.pdf, lue le 2026-10-10 : les cinq critères de conception ; version publiée non lue).
- Alexander, C. *The Nature of Order*. Center for Environmental Structure. https://openlibrary.org/works/OL3923607W — *vérifiée sur résumé ou source secondaire* (notice Open Library ; premières éditions datées de 2001 dans la notice).
- Greimas, A. J., Collins, F. & Perron, P. (1989). Figurative semiotics and the semiotics of the plastic arts. *New Literary History*, 20(3), 627 (page initiale). https://doi.org/10.2307/469358 — *vérifiée sur résumé ou source secondaire* (métadonnées Crossref).
- W3C : SHACL https://www.w3.org/TR/shacl/ ; OWL 2 https://www.w3.org/TR/owl2-overview/ ; SPARQL 1.1 https://www.w3.org/TR/sparql11-query/ ; SKOS https://www.w3.org/TR/skos-reference/ — *vérifiée sur la source* (pages consultées le 2026-10-10).
