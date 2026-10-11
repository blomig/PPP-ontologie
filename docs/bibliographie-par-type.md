# Bibliographie et état de l'art par type ou groupe de types

*Bibliographie publique de PPP, spec v2.7 (§9.7 P). Recherches et vérifications faites du 2026-10-10 au 2026-10-11 ; chaque entrée porte son statut de vérification. Complète [`etat-de-l-art.md`](etat-de-l-art.md), qui traite des sources du cadre (Nanay, Gärdenfors, OntoClean, Popper, Lakatos…) et de la texture (§5 bis).*

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
- **Ancres stables** (spec §9.7 P, point 4) : chaque groupe a une ancre `groupe-…`, posée par une balise `<a id="…"></a>` au-dessus de son titre ; une fiche y renvoie par `etat_de_l_art_renvoi: docs/bibliographie-par-type.md#groupe-…`. Les ancres ne changent pas quand le titre change. Liste : `groupe-texture` (texture et ses cousins), `groupe-couleur`, `groupe-forme` (forme et contour), `groupe-organisation`, `groupe-matiere` (reflets, transparence, profondeur dans la matière), `groupe-joint` (joint et assemblage), `groupe-etagement` (étagement en plans), `groupe-contrastes` ; hors groupes de types : `groupe-sources-generales`, `groupe-non-verifiees`, `groupe-spec` ; sous-sections : `brillance-categorisations`, `refs-2-5` ; gouvernance des ontologies ouvertes : `groupe-gouvernance`. Les anciennes ancres (`texture-et-ses-cousins`, `couleur`, `forme-et-contour`, `organisation`, `matiere`, `joint-et-assemblage`, `etagement-en-plans`, `contrastes`) restent comme alias ; ne plus les employer.

<a id="groupe-texture"></a>
<a id="texture-et-ses-cousins"></a>
## Texture et ses cousins

Les classifications de la texture viennent surtout de la vision par ordinateur (mesures calculées sur une image, comparées ou non à des jugements humains) et, plus rarement, de la psychologie (dimensions et lexique perçus). PPP s'en sert pour des alignements (§9.7 O), jamais pour ses régions.

**Types** : `ppp:texture`, `ppp:textureDirectionality`, `ppp:localIrregularity`.

- `ppp:texture` : La perception de la texture est étudiée depuis les années 1970 en vision par ordinateur et en psychologie. Tamura, Mori et Yamawaki (1978) ont proposé six mesures calculées sur une image, comparées à des jugements humains ; la *coarseness* (le caractère plus ou moins gros du grain) correspond à la taille des reliefs. Rao et Lohse (1996) et Bhushan, Rao et Lohse (1997) ont cherché les dimensions perçues et le lexique de la texture. Les mesures de Haralick et al. (1973) servent à classer des images par calcul, sans viser la perception.
- `ppp:textureDirectionality` : La direction commune des reliefs est l'une des six dimensions de Tamura, Mori et Yamawaki (1978), mesurée sur une image (*directionality*). Liu et Picard (1996) en font l'une des trois composantes d'un modèle d'image (périodicité, direction, caractère aléatoire). Aucune source trouvée ne limite l'orientation aux reliefs, comme le fait PPP (T26).
- `ppp:localIrregularity` : La régularité d'une texture est une dimension de Tamura, Mori et Yamawaki (1978), mais composée d'autres mesures ; Liu et Picard (1996) traitent le caractère aléatoire d'une texture comme une composante séparée. Aucune source trouvée ne nomme l'écart local à une régularité comme qualité perçue. La base du type reste ouverte (T11).

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
  - statut : *vérifiée sur la source* ; vérifié sur : ppp:hue : texte du Project Gutenberg n° 26054 lu pour les passages cités : « Color has three dimensions » (§ 8 : teinte, valeur, chroma) ; cinq teintes principales (R, Y, G, B, P) et cinq intermédiaires (YR, GY, BG, PB, RP) ; glossaire, « BROWN.--A dark color, inclined to red or yellow… » et « PINK.--A red color of low chroma, but high luminosity, inclining toward purple » ; texte non lu en entier | ppp:lightness : texte du Project Gutenberg n° 26054 lu pour le passage cité : « Color has three dimensions » (§ 8) : la teinte, la valeur (« the amount of light », la quantité de lumière) et le chroma (la pureté) ; texte non lu en entier | ppp:saturation : texte du Project Gutenberg n° 26054 lu pour le passage cité : « Color has three dimensions » (§ 8) : la teinte, la valeur et le chroma (« the purity or CHROMA », la pureté) ; texte non lu en entier | ppp:hueRange : texte du Project Gutenberg n° 26054 lu pour les passages cités : « a circuit of hues » (un cercle de teintes, chapitre I) ; cinq teintes principales et cinq intermédiaires ; texte non lu en entier ;
  - usage : `ppp:hue` (alimente); `ppp:lightness` (alimente); `ppp:saturation` (alimente); `ppp:hueRange` (alimente).
- Berlin, B. & Kay, P. (1969). Basic Color Terms. Berkeley : University of California Press. https://openlibrary.org/works/OL64565W
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : notice Open Library (titre, auteurs, éditeur, 1969, OCLC 56215) ; ouvrage non lu ; la liste des onze catégories est lue dans Kay (2015, kay2015) ;
  - usage : `ppp:hue` (discute).
- CIE (2018). CIE 015:2018 Colorimetry, 4th Edition. Vienne : Commission Internationale de l'Éclairage. https://doi.org/10.25039/TR.015.2018
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées et résumé Crossref (observateurs de référence, illuminants, coordonnées d'espace couleur, écarts de couleur) ; texte payant non lu ;
  - usage : `ppp:hue` (contraste); `ppp:lightness` (contraste); `ppp:saturation` (contraste).
- CIE S 017:2020, ILV : International Lighting Vocabulary, 2e éd., entrée 17-23-076 « CIE 1976 L*a*b* colour space ». Vienne : CIE (accès libre en ligne, e-ILV). https://cie.co.at/eilvterm/17-23-076
  - statut : *vérifiée sur la source* ; vérifié sur : entrée lue en ligne le 2026-10-10 : espace couleur CIELAB, coordonnées L*, a*, b* ; note 1 : correspondants approchés de la clarté (L*, « CIE 1976 lightness »), du chroma (« CIE 1976 a,b chroma ») et de la teinte (« CIE 1976 a,b hue angle », h_ab = arctan(b*/a*)) ;
  - usage : `ppp:hue` (contraste) ; `ppp:lightness` (contraste) ; `ppp:saturation` (contraste) ; ajoutée en 2.5 comme appui vérifié des grandeurs mesurées homonymes (angle de teinte, L*, chroma), à la place de CIE 015:2018 non lue.
- Gilchrist, A. (2006). Seeing Black and White. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780195187168.001.0001
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé de l’éditeur lu (OpenAlex, 2026-10-10) : la lumière renvoyée par une surface ne révèle pas sa nuance de gris ; selon l’éclairage, une surface de n’importe quel gris peut renvoyer n’importe quelle quantité de lumière ; le livre fait l’historique des recherches et des théories de la clarté ; contenu non lu ;
  - usage : `ppp:lightness` (discute).
- Fairchild, M. D. (2013). Color Appearance Models. Wiley. https://doi.org/10.1002/9781118653128
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref (titre, auteur, 2013) ; contenu non lu ;
  - usage : `ppp:saturation` (discute).

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

### Catégorisations de la brillance (spec 2.5)
<a id="brillance-categorisations"></a>

Recherche du 2026-10-10, avant de fixer les labels de région de `ppp:surfaceGloss` : existe-t-il une catégorisation reconnue des **niveaux** de brillance perçue ?

| Source | Ce qu'elle contient (vérifié) | Statut | Ce que PPP en fait |
|---|---|---|---|
| Hunter 1937 | six **sortes** de brillance : *specular gloss* (brillant spéculaire), *sheen* (lustre aux angles rasants), *contrast gloss* (brillance de contraste), *absence-of-bloom gloss* (absence de voile), *distinctness-of-reflected-image gloss* (netteté de l'image réfléchie), *absence-of-surface-texture gloss* (absence de texture de surface) | résumé | des sortes, pas des niveaux ; `skos:relatedMatch` avec la netteté de l'image réfléchie |
| Hunter & Harold 1987 | manuel de la mesure de l'aspect (2e éd.) | comptes rendus (métadonnées) ; contenu non lu | rien de plus que Hunter 1937 |
| ISO 2813:2014 | géométries de mesure 20°, 60°, 85° | page de l'éditeur ; texte payant | classes « haute / moyenne / basse brillance » par angle : **non vérifiées** |
| ASTM D523-14(2018) | géométries 60°, 20°, 85° ; « Little information about the relation of numerical-to-perceptual intervals of specular gloss has been published » (§ 5.3) | sections lues sur la page de l'éditeur | aucune classe de niveaux |
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
- `ppp:perceptualContrast` : Pour la lumière, le contraste calculé (rapport de luminances : combien de fois une zone est plus lumineuse qu’une autre) ne s’accorde avec le contraste perçu que pour des images simples ; dans une image complexe, le contraste perçu varie d’un endroit à l’autre (Peli 1990, résumé lu), et des observateurs qui comparent deux photographies jugent laquelle est la plus contrastée (Haun et Peli 2013). Aucune source trouvée ne propose un contraste perçu général, valable pour toute dimension comparée (recherches du 2026-10-10 et du 2026-10-11 : Crossref, Semantic Scholar, OpenAlex). Les sources des contrastes spécialisés sont dans leurs fiches.

**Références** :

- Tamura, H., Mori, S. & Yamawaki, T. (1978). Textural features corresponding to visual perception. IEEE Transactions on Systems, Man, and Cybernetics, 8(6), 460–473. https://doi.org/10.1109/TSMC.1978.4309999
  - statut : *vérifiée sur résumé ou source secondaire* ; vérifié sur : métadonnées Crossref et résumé IEEE Xplore ; deux sources secondaires (docs/etat-de-l-art.md §5 bis) ; texte intégral non lu ;
  - usage : `ppp:textureContrast` (discute); `ppp:lightnessContrast` (alimente).
- Munsell, A. H. (1905). A Color Notation. Boston : G. H. Ellis ; 2e éd. 1907, Project Gutenberg n° 26054. https://www.gutenberg.org/ebooks/26054
  - statut : *vérifiée sur la source* ; vérifié sur : texte du Project Gutenberg n° 26054 lu pour les passages cités : « Color has three dimensions » (§ 8) ; « a circuit of hues » (un cercle de teintes, chapitre I) ; cinq teintes principales et cinq intermédiaires ; texte non lu en entier ;
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

<a id="groupe-sources-generales"></a>
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
