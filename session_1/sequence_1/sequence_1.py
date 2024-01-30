# Python 3.10
# Code à compléter de la séquence n°1.
# Les questions (Q1, Q2, etc.) correspondent à celles du fichier sequence_1.md.


# --------------------
# ✏️ Q1.

lacroix_1841 = [
    "Lacroix (Paul), (pseudo Bibliophile Jacob)",
    "membre du comité des chartes",
    "Martyrs, 47",
]
lacroix_1844 = [
    "Lacroix (Paul), (pseudo Bibliophile Jacob)",
    "membre du comité des chartes",
    "Martyrs, 47",
]

# La fonction score_exact prend en paramètre deux listes de chaînes de caractères et renvoie le booléen vrai si elles sont identiques, et faux sinon.
# Notez l'utilisation d'autres annotations de type pour indiquer le type des paramètres et du retour de la fonction.
# Ces annotations sont facultatives mais permettent d'obtenir des messages d'erreur plus précis en cas d'erreur,
# ainsi que de faciliter la lecture du code, par vous-même et par les autres.
# Essayez dans le reste de cet atelier de toujours utiliser les annotations de type !


def score_exact(enregistrement1: list[str], enregistrement2: list[str]) -> bool:
    # 🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️
    # 🏗️ CODE À COMPLÉTER
    ...


# Testez la fonction score_exact sur les deux entrées lacroix_1841 et lacroix_1844.
score = score_exact(lacroix_1841, lacroix_1844)
print("Les entrées sont-elles identiques ?", score)


# --------------------
# ✏️ Q2.


# Pour normaliser une chaîne de caractères, on peut :
# 1. la mettre en minuscules. On peut utiliser la méthode lower() des chaînes de caractères.
# 2. supprimer les accents. On peut utiliser la méthode translate() des chaînes de caractères.
#    Cette méthode prend en paramètre un dictionnaire de traduction, qui peut être construit avec la fonction str.maketrans(),
#    qui prend en paramètre deux chaînes de caractères de même longueur contenant l'une les caractères accentués à remplacer et l'autre les caractères de remplacement sans accents.
# 3. supprimer la ponctuation, parenthèses, etc. On peut aussi utiliser les méthodes translate() et str.maketrans() pour cela.
#    À noter que la constante string.punctuation (du module string, à importer) contient la liste des caractères de ponctuation.
# 4. supprimer les éventuels espaces en double. On peut utiliser la méthode replace() des chaînes de caractères.
# 5. supprimer les espaces en début et fin de chaîne. On peut utiliser la méthode strip() des chaînes de caractères.


def normalisation(champ: str) -> str:
    # 🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️
    # 🏗️ CODE À COMPLÉTER
    ...


# Vérifiez que votre fonction normalisation fonctionne décommentant les ligne suivante.
# lacroix_1841 = [
#     "lacroix (paul, (bibliophile jacob",
#     "membre du comite des chartes",
#     "martyrs 47",
# ]
# lacroix_1844 = [
#     "Lacroix Paul. (Bibliophile jacob",
#     "membre du comité des chartes",
#     "Martyrs, 47",
# ]
# norm_1841 = normalisation(" ".join(lacroix_1841))
# norm_1844 = normalisation(" ".join(lacroix_1844))
# print("Normalisation :", norm_1841, '--', norm_1844)


# --------------------
# ✏️ Q4.

# 🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️
# 🏗️ CODE À COMPLÉTER

# --------------------
# ✏️ Q5.

lacroix_1841 = [
    "lacrox (paul, (bibliophile iaco",
    "membre du coniite des chartes",
    "martirs 4I",
]
lacroix_1844 = [
    "Lacroix Paul. (Bibliophile jacob",
    "membre du com. des chartes",
    "Martyrs, 47",
]


# Pour calculer les scores entre les champs deux à deux, on peut utiliser le fait que les listes ont la même longueur.
# On peut donc utiliser range(len(liste1)) pour générer les indices des éléments de la liste,
# puis d'utiliser ces indices pour accéder aux éléments des deux listes.
# Une solution plus "pythonic" consiste à utiliser une boucle for en conjonction avec la fonction zip() pour parcourir les deux listes en parallèle.
def score_approximatif(liste1: list[str], liste2: list[str]) -> float:
    # 🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️
    # 🏗️ CODE À COMPLÉTER
    ...


# Testez votre fonction avec les deux entrées lacroix_1841 et lacroix_1844, sans normaliser les champs, puis en les normalisant.
# 🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️
# 🏗️ CODE À COMPLÉTER


# --------------------
# ✏️ Q6.


# Pour décider si deux entrées sont couplées, on peut utiliser un seuil de distance d'édition.
# Si la distance d'édition est inférieure ou égale au seuil, on considère que les entrées sont couplées.
# Sinon, on considère qu'elles ne sont pas couplées.
def decision(score: float, seuil: float) -> bool:
    # 🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️
    # 🏗️ CODE À COMPLÉTER
    ...


# Décommentez la ligne suivante pour tester votre fonction.
# print("Match ?", decision(score_approximatif(norm_1841, norm_1844), 10.0))


# --------------------
# ✏️ Q7.

# La fonction couplage prend en paramètre deux enregistrements (représentés par des listes de chaînes de caractères)
# et un seuil de distance d'édition.
# Elle renvoie vrai si les deux enregistrements sont couplés, faux sinon.
# Pour cela, elle calcule le score approximatif entre les deux enregistrements, puis décide si les enregistrements sont couplés en fonction du seuil.

# **BONUS** : Ajoutez un paramètre booleén exact_match qui indique si on veut utiliser un couplage exact ou approximatif.
# Utilisez la syntaxe `exact_match: bool = False` pour indiquer que le paramètre est optionnel et vaut False par défaut.
# Si exact_match vaut True, la fonction doit utiliser un couplage exact et appelera la fonction score_exact qui reverra un score booléen.
# Pour adapter la prise de décision, deux options sont possibles :
# - utiliser la fonction `decision` déjà écrite. Il faut dans ce cas convertir le score booléen en float, l'inverser (1 - score), puis appeler la fonction `decision` avec un seuil fixé à 0.0.
# - réaliser un test booléen sur le score directement dans la fonction `couplage` et renvoyer le résultat du test.

# Décommentez la ligne suivante et complétez le corps de la fonction.
# def couplage(enregistrement1: list[str], enregistrement2: list[str], ...) -> bool:
#   🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️🏗️
#   🏗️ CODE À COMPLÉTER


# Décommentez les ligne suivante pour tester votre fonction.
# print(lacroix_1841)
# print(lacroix_1844)
# print("Match?", couplage(lacroix_1841, lacroix_1844, 5.0, exact_match=False))
