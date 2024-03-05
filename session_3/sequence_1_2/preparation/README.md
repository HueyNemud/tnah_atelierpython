# Contenu de ce répertoire
Ce répertoire contient des notebooks de brouillon utilisés lors de la préparation de cette activité.

- `1-chargement-text-ner-matcher.ipynb`: notebook qui illustre le chargement de fichiers, la reconnaissance d'entités nommées, et l'utilisation du matcher spaCy
- `2-preparation-nettoyage-donnees-export-json.ipynb`: notebook de préparation du jeu de données (pour un export au format JSON)
- `3-constructions-exemples-evaluation.ipynb`: notebook montrant comment construire des objets Example spaCy et les utiliser pour évaluer la reconnaissance d'entités nommées
- `4-bench-mdls-convert-data-train-model.ipynb`: notebook de comparaison de la performance de différents modèles et d'export du jeu de données de notre format JSON vers le format Docbin spaCy
- `5-spacy_ner_finetune_trf_vs_lg_gpu_on_colab.ipynb`: notebook comparant la performance après finetuning rapide sur notre train set du transformer CamemBERT vs core-news-fr-lg, avec un entraînement sur GPU avec Google Colab
- `10-alignement-problems.ipynb`: notebook qui illustre les problèmes d'alignement potentiels entre les prédictions et la vérité terrain
- `11-tentative-annotation-udt.ipynb`: notebook qui illustre une tentative ratée d'annotation des données directement dans le notebook
- `21-hf-transformer-code.ipynb`: notebook qui illustre comment utiliser un modèle HuggingFace pour reconnaître des entités nommées