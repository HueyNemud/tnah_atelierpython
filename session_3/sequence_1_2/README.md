# Atelier d'initiation à la reconnaissance d'entités nommées avec spaCy

Activité conçue pour le consortium HumaNum Ariane, pour une formation à Lyon le 9 novembre 2023.

| 🏃 Accès direct aux supports 👇 |
|--------------|
| [![](https://img.shields.io/badge/Pr%C3%A9sentation-Ouvrir%20dans%20Google%20Slides-orange?logo=googleslides)](https://docs.google.com/presentation/d/1_RycfOOeQo8XZNojsx7SzaSDyhepj-8n8w7xMpf9UGI/edit)  [![](https://img.shields.io/badge/Notebook-Ouvrir%20dans%20Google%20Colab-blue?logo=googlecolab)](https://colab.research.google.com/github/jchazalon/hn-ariane-ner-tuto-2023/blob/main/intro-ner-spacy-student.ipynb)  | 

## Contenu de l'activité

Cette activité repose sur 2 ressources pédagogiques autocontenues :
1. un [jeu de *slides*](https://docs.google.com/presentation/d/1_RycfOOeQo8XZNojsx7SzaSDyhepj-8n8w7xMpf9UGI/edit#slide=id.p),
2. un [notebook](https://colab.research.google.com/github/jchazalon/hn-ariane-ner-tuto-2023/blob/main/intro-ner-spacy-student.ipynb) qu'il est possible d'utiliser directement sur Google Colab.

Cette activité devrait durer un peu **moins d'une heure** pour une exploration en surface.

Elle s'adresse à un public de **jeunes chercheurs en sciences humaines et sociales** souhaitant **renforcer leurs compétences en humanités numériques**.

Les **prérequis** sont les suivants :
- Niveau débutant en Python
- Connaissance de Jupyter/Colab (notebooks)
- Connaissance des tâches classiques en TAL
- Notions en apprentissage artificiel (ML)

La **méthode pédagogique** retenue est celle de la résolution d'un problème concret simplifié de bout en bout, de façon à rendre les apprenants autonomes dans la réutilisation de ces connaissances et outils sur des données qui les intéressent.
L'utilisation de la bibliothèque [Spacy](https://spacy.io/) a été retenue pour sa polyvalence, sa maturité et la qualité de sa documentation.

## Sources, licences et auteurs
Cet atelier est largement tiré du cours “[NLP avancé avec Spacy](https://course.spacy.io/fr)” réalisé par [Ines Montani](https://twitter.com/_inesmontani) (créatrice de [Spacy](https://spacy.io/)) sous [licence MIT](https://www.tldrlegal.com/license/mit-license).
Cette licence nous autorise à reprendre, modifier et diffuser son contenu tant que nous indiquons la licence originale :

>The MIT License (MIT)
>Copyright (C) 2019 Ines Montani
>Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Les données de cet atelier sont adaptées du “[French ELTEC NER Open Dataset](http://hdl.handle.net/20.500.11752/OPEN-986)” par Carmen Brando, Francesca Frontini, et Ioana Galleron sous licence [Creative Commons - Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](http://creativecommons.org/licenses/by-sa/4.0/). 

> Brando, Carmen; Frontini, Francesca and Galleron, Ioana, 2022, French ELTEC NER Open Dataset, ILC-CNR for CLARIN-IT repository hosted at Institute for Computational Linguistics "A. Zampolli", National Research Council, in Pisa, [http://hdl.handle.net/20.500.11752/OPEN-986](http://hdl.handle.net/20.500.11752/OPEN-986).

Ce cours et les données associées sont sous licence [Creative Commons - Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](http://creativecommons.org/licenses/by-sa/4.0/).
Pour citer ce travail, merci d'indiquer :

> Consortium HumaNum Ariane, Joseph Chazalon, Atelier d'initiation à l'extraction d'entités nommées, en ligne : <https://github.com/jchazalon/hn-ariane-ner-tuto-2023>, 9 novembre 2023, Lyon.


## Préparation des supports à destination des apprenants
Cette section s'adresse aux concepteurs et mainteneurs de cette activité, ainsi qu'aux personnes souhaitant se baser sur cette activité pour en construire une nouvelle.

### Organisation des fichiers

Fichiers à la racine du dépôt :

- `intro-ner-spacy-student.ipynb` : notebook contenant l'activité, version apprenant (ce fichier est généré automatiquement à partir de la version enseignant ci-dessous)
- `intro-ner-spacy-teacher.ipynb` : notebook content l'activité et les solutions prêtes à être exécutées, à destination des enseignants (ce fichier est utilisé pour générer la version apprenant ci-dessus)
- `Makefile` : script de préparation du notebook apprenant à partir du notebook enseignant
- `Pipefile` : décrit les dépendances Python du projet
- `Pipefile.lock` : liste les versions exactes de chacune des dépendances utilisées
- `README.md` : ce fichier de description
- `requirements.txt` : fichier de dépendances généré automatiquement à partir du fichier `Pipefile.lock`, utilisé pour simplifier l'installation des dépendances sous Google Colab.

Répertoire `dataset/` :

- `French_ELTEC_NER_Open_Dataset.json` : export synthétique du jeu de données “[French ELTEC NER Open Dataset](http://hdl.handle.net/20.500.11752/OPEN-986)” au format JSON, avec seulement les annotations `PER` et `LOC`.
- `test.spacy` : échantillon aléatoire de 30 % du jeu de données au format spaCy Docbin.
- `train.spacy` : échantillon contenant les 70 % restants du jeu de données au format spaCy Docbin.
  
Répertoire `preparation/` :

- `1-chargement-text-ner-matcher.ipynb`: notebook qui illustre le chargement de fichiers, la reconnaissance d'entités nommées, et l'utilisation du `Matcher` spaCy
- `2-preparation-nettoyage-donnees-export-json.ipynb`: notebook de préparation du jeu de données (pour un export au format JSON)
- `3-constructions-exemples-evaluation.ipynb`: notebook montrant comment construire des objets `Example` spaCy et les utiliser pour évaluer la reconnaissance d'entités nommées
- `4-bench-mdls-convert-data-train-model.ipynb`: notebook de comparaison de la performance de différents modèles et d'export du jeu de données de notre format JSON vers le format `Docbin` spaCy
- `5-spacy_ner_finetune_trf_vs_lg_gpu_on_colab.ipynb`: notebook comparant la performance après finetuning rapide sur notre train set du transformer CamemBERT vs core-news-fr-lg, avec un entraînement sur GPU avec Google Colab
- `10-alignement-problems.ipynb`: notebook qui illustre les problèmes d'alignement potentiels entre les prédictions et la vérité terrain
- `11-tentative-annotation-udt.ipynb`: notebook qui illustre une tentative ratée d'annotation des données directement dans le notebook
- `21-hf-transformer-code.ipynb`: notebook qui illustre comment utiliser un modèle HuggingFace pour reconnaître des entités nommées


Répertoire `training-scratch/` :

- `base_config.cfg` : fichier de configuration de base d'exemple utilisé pour réaliser l'entraînement de l'activité
- `config.cfg` : fichier de configuration complété utilisé pour réaliser l'entraînement de l'activité
- `output` : répertoire de stockage du modèle produit ; nous n'avons conservé que le meilleur modèle


Pour faciliter son utilisation directement depuis le dépôt GitHub (bouton "Ouvrir avec Google Colab"), le notebook pour les apprenants est également stocké ici.
Il faut toutefois le régénérer à chaque fois qu'une modification est apportée dans le notebook enseignant.
**🚨 Il ne faut pas modifier directement le notebook apprenant, les modifications seraient perdues à la prochaine régénération.**

### Régénérer le notebook pour les apprenants
Le notebook enseignant contient des cellules avec le tag *"teacher"*. Ces cellules seront supprimées automatiquement.

**Pour générer le notebook apprenant, il suffit d'exécuter la commande suivante :**
```
make
```

Le fichier `intro-ner-spacy-student.ipynb` est alors mis à jour.

Les instructions sont contenues dans le fichier `Makefile`.

N'oubliez pas de publier (*git add, commit, push*) vos modifications après avoir généré les nouveaux fichiers.


### Mise à jour des dépendances et des versions utilisées
Nous utilisons [`pipenv`](https://pipenv.pypa.io) pour gérer les environnements virtuels, et [pyenv](https://github.com/pyenv/pyenv) pour utiliser la même version de Python que sur [Google Colab](https://colab.research.google.com/).

Pour installer localement les dépendances nécessaires, utilisez `pipenv sync`.  
Pour lancer un shell dans l'environnement, utilisez `pipenv shell`.

Pour ajouter ou mettre à jour des dépendances, utilisez les commandes `pipenv install` et `pipenv update`.
Vous pouvez consulter l'aide avec `pipenv -h`.

Si vous modifiez les dépendances, vous devez régénérer le fichier `requirements.txt`, car ce dernier est utilisé pour faciliter l'installation sur Google Colab.
Il suffit d'appeler `pipenv requirements > requirements.txt`.
