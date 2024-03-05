# Contenu de ce répertoire

- `French_ELTEC_NER_Open_Dataset.json` : export synthétique du jeu de données “[French ELTEC NER Open Dataset](http://hdl.handle.net/20.500.11752/OPEN-986)” au format JSON, avec seulement les annotations `PER` et `LOC`.
- `test.spacy` : échantillon aléatoire de 30 % du jeu de données au format spaCy Docbin.
- `train.spacy` : échantillon contenant les 70 % restants du jeu de données au format spaCy Docbin.

Les données de cet atelier sont adaptées du “[French ELTEC NER Open Dataset](http://hdl.handle.net/20.500.11752/OPEN-986)” par Carmen Brando, Francesca Frontini, et Ioana Galleron sous licence [Creative Commons - Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](http://creativecommons.org/licenses/by-sa/4.0/).

Les notebooks suivants ont été utilisés pour préparer les données :

- `2-preparation-nettoyage-donnees-export-json.ipynb`: notebook de préparation du jeu de données (pour un export au format JSON)
- `4-bench-mdls-convert-data-train-model.ipynb`: notebook de comparaison de la performance de différents modèles et d'export du jeu de données de notre format JSON vers le format Docbin spaCy

