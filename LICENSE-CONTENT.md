# Licence du contenu

Copyright (c) 2026 Lomig Unger et contributeurs du projet PPP

L’ontologie PPP et ses contenus sont mis à disposition sous la licence
**Creative Commons Attribution 4.0 International (CC BY 4.0)**.

Texte officiel de la licence : https://creativecommons.org/licenses/by/4.0/

Titulaire des droits : Lomig Unger (décision de l'éditeur du projet, série 13), avec la mention ci-dessus. Auteurs à créditer (CC BY 4.0, section 3(a)(1)(A)(i)) : Lomig Unger et Grok Bot, comme dans `CITATION.cff` ; Grok Bot y figure au titre du crédit, pas comme titulaire. Équipe et contributeurs : `CONTRIBUTORS.md`.

Pour réutiliser ce contenu, reprenez (CC BY 4.0, section 3(a)(1)) : le nom des auteurs, la mention de copyright ci-dessus, un renvoi à la licence CC BY 4.0 (adresse ci-dessus), un renvoi à l'exclusion de garantie de la licence (section 5), l'adresse du contenu dans la mesure du possible, et l'indication de vos modifications. Forme de citation : `docs/comment-citer.md`.

## Périmètre

Tout le contenu du dépôt est sous licence, y compris les fiches qui ne sont pas encore publiées sur le site (série 13). Sont couverts par CC BY 4.0 :
- la spécification (`PPP_Specification.md`), la fiche de type (`PPP_FicheType.md`) et la fiche d’exemplaire (`PPP_FicheExemplaire.md`) ;
- les types, fiches, régions, relations et assertions de l’ontologie, quel que soit leur format (Markdown, YAML, exports) ;
- les documents de `docs/` et les versions antérieures (`3fichierspourlarflexionsurlontologieppp/`) ;
- les textes et contenus du site et du jeu de cartes.

Le **code** du site et des outils est sous licence MIT (voir `LICENSE`).

Aucun accord de contribution n’est demandé : les contributions sont versées sous ces mêmes licences.

## Images d’exemplaires : hors CC BY 4.0

Les images d’exemplaires **ne sont pas sous la licence du projet**. Chacune garde **sa propre licence**, celle que donne sa source, et son crédit doit être repris tel quel (spécification X16, Q15). Une image n’est stockée et reproduite que si sa licence est réellement libre et vérifiée (`credit.usage: image_reproduite` dans `fiches/exemplaires.yaml`) ; les autres objets sont montrés par un lien vers leur source, sans copie (`lien_seulement`).

Le crédit de référence est le champ `credit` de chaque objet dans `fiches/exemplaires.yaml` (une seule source ; date de vérification et mention requise y figurent). État au 2026-10-11, recopié de ce champ, pour les neuf images reproduites (cinq stockées par la maquette dans `maquette/images/exemplaires/` et suivies par Git, vignettes de Wikimedia Commons sans recadrage ni retouche ; la page de titre de Moby-Dick, retenue en série 17, est dans ce dossier mais pas encore suivie ; les trois Malévitch, reproduits depuis la série 20, restent à stocker : critère de l’éditeur du projet, image hébergée sur Commons avec licence et balise indiquées, le doute sur le pays d’origine ne bloquant plus ; détail : `docs/droits-exemples-2026-10-11.md`) :

| Objet | Auteur de l’image | Licence de l’image | Source |
|---|---|---|---|
| `app:met-2011-201` | The Metropolitan Museum of Art (photographie du musée, don à Wikimedia Commons, programme Open Access) | CC0 1.0 (aucune mention exigée ; mention d’usage proposée : « The Metropolitan Museum of Art, 2011.201 (CC0) ») | https://commons.wikimedia.org/wiki/File:MET_DP342675.jpg |
| `app:shap-wells-granite` | Jim Barton | CC BY-SA 2.0 (https://creativecommons.org/licenses/by-sa/2.0) | https://commons.wikimedia.org/wiki/File:Granite_on_display,_Shap_Wells_Hotel_-_geograph.org.uk_-_1531324.jpg (depuis geograph.org.uk, photo n° 1531324) |
| `app:san-vitale-ravenne` | © José Luiz Bernardes Ribeiro | CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0) | https://commons.wikimedia.org/wiki/File:Vault_mosaic_-_San_Vitale_-_Ravenna_2016_(2).jpg |
| `app:commons-beuchaer-gestockt` | Reiner Flassig | CC BY-SA 2.0 de (https://creativecommons.org/licenses/by-sa/2.0/de/deed.en) | https://commons.wikimedia.org/wiki/File:Beuchaer-gestockt.jpg |
| `app:commons-corduroy-fabric` | ArielGlenn | CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0) | https://commons.wikimedia.org/wiki/File:Corduroy_fabric.jpg |
| `app:melville-moby-dick-1851-titre` | page imprimée de 1851 (Herman Melville, Harper & Brothers) ; numérisation attribuée à la Beinecke Library, Yale University (selon Commons ; provenance non confirmée) | domaine public (`{{PD-old-100-expired}}` ; aucune mention exigée ; mention d’usage proposée : « Herman Melville, Moby-Dick; or, The Whale, New York, Harper & Brothers, 1851, page de titre ; exemplaire de la Beinecke Library, Yale University (selon Commons) ; image Wikimedia Commons, domaine public ») | https://commons.wikimedia.org/wiki/File:Moby-Dick_FE_title_page.jpg |
| `app:malevich-white-on-white-1918` | Kazimir Malévitch (auteur de l’œuvre) ; photo : non nommé (reproduction fidèle ; source déclarée : The Museum of Modern Art) | domaine public (`{{PD-Art\|PD-old-auto-expired\|deathyear=1935}}` ; aucune mention exigée ; mention d’usage proposée : « Kazimir Malévitch, Composition suprématiste. Blanc sur blanc, 1918, The Museum of Modern Art, New York ; image Wikimedia Commons, domaine public ») | https://commons.wikimedia.org/wiki/File:Kazimir_Malevich_-_%27Suprematist_Composition-_White_on_White%27,_oil_on_canvas,_1918,_Museum_of_Modern_Art.jpg |
| `app:malevich-black-square-1915` | Kazimir Malévitch (auteur de l’œuvre) ; photo : non nommé (reproduction fidèle ; source déclarée : galerie Tretiakov, Moscou) | domaine public (`{{PD-Art\|PD-Russia-expired}}` ; aucune mention exigée ; mention d’usage proposée : « Kazimir Malévitch, Carré noir, 1915, galerie Tretiakov, Moscou ; image Wikimedia Commons, domaine public ») | https://commons.wikimedia.org/wiki/File:Kazimir_Malevich,_1915,_Black_Suprematic_Square,_oil_on_linen_canvas,_79.5_x_79.5_cm,_Tretyakov_Gallery,_Moscow.jpg |
| `app:malevich-red-square-1915` | Sailko (photo, « Own work ») ; version éclaircie par Philafrenzy (2013, historique du fichier Commons : original téléversé par Sailko le 2011-09-20 ; fichier actuel téléversé le 2013-05-06 par Philafrenzy, commentaire « brighten a little. ») ; œuvre de Kazimir Malévitch (« Carré rouge, 1915, Musée russe ») | CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0) ; titre du fichier : « Kazimir malevich, quadrato rosso (realismo del pittore di una campagnola in due dimensioni), 1915 » | https://commons.wikimedia.org/wiki/File:Kazimir_malevich,_quadrato_rosso_(realismo_del_pittore_di_una_campagnola_in_due_dimensioni),_1915.JPG |

Pour une image sous CC BY-SA : une adaptation (recadrage, retouche) se diffuse sous la même licence, et la modification doit être signalée. En cas d’écart entre ce tableau et `fiches/exemplaires.yaml`, c’est `exemplaires.yaml` qui fait foi.
