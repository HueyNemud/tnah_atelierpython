#!/usr/bin/env python3
# La ligne ci-dessus permet d'exécuter le script sans préciser d'interpréteur.
# Par exemple, si le script est exécutable (chmod +x couplage.py), on peut l'exécuter directement avec ./couplage.py

# Fichier: couplage.py
# Auteur: Atelier Python, master TNAH 2024 de l'École nationale des chartes
# Description: Code complet de l'outil de couplage d'enregistrements en ligne de commande.
# License: domaine public

import argparse
import string
import re
import csv
from nltk.metrics import edit_distance


def main():
    """
    Fonction principale qui effectue le couplage d'enregistrements à partir des fichiers d'entrée.

    Args:
        fichier1 (str): Premier fichier d'enregistrements à coupler.
        fichier2 (str): Second fichier d'enregistrements à coupler.
        fichier_sortie (str): Fichier de sortie contenant la jointure couplée des deux fichiers d'entrée.
        seuil (float): Seuil pour le couplage approximatif.
        verbose (bool): Indique si les détails du couplage doivent être affichés.
    """

    # --------------------
    # Définition des arguments de la ligne de commande à l'aide du module argparse.
    parser = argparse.ArgumentParser(
        description="Un utilitaire simple de couplage d'enregistrements."
    )
    parser.add_argument(
        "fichier1", type=str, help="Premier fichier d'enregistrements à coupler."
    )
    parser.add_argument(
        "fichier2", type=str, help="Second fichier d'enregistrements à coupler."
    )
    parser.add_argument(
        "fichier_sortie",
        type=str,
        help="Fichier de sortie contenant la jointure couplée des deux fichiers d'entrée.",
    )
    parser.add_argument(
        "-s", "--seuil", type=float, help="Seuil pour le couplage approximatif."
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Afficher les détails du couplage."
    )

    # On démarre le parseur pour récupérer les arguments de la ligne de commande...
    args = parser.parse_args()
    # ... puis on les assigne à des variables.
    fichier1: str = args.fichier1
    fichier2: str = args.fichier2
    fichier_sortie: str = args.fichier_sortie
    seuil: float = args.seuil
    verbose: bool = args.verbose

    # --------------------
    # Chargement des enregistrements des fichiers d'entrée.
    # On utilise la fonction charger_enregistrements() puis on sépare les en-têtes des enregistrements.

    enregistrements1 = charger_enregistrements(fichier1)
    enregistrements1_header = enregistrements1[0]
    enregistrements1 = enregistrements1[1:]

    enregistrements2 = charger_enregistrements(fichier2)
    enregistrements2_header = enregistrements2[0]
    enregistrements2 = enregistrements2[1:]

    # --------------------
    # Couplage des enregistrements.
    # On appelle la fonction couplage_multi() avec les enregistrements et le seuil.
    # Pour savoir si on doit effectuer un couplage exact ou approximatif, on vérifie si un seuil a été fourni.
    exact_match = seuil is None
    couplage = couplage_multi(
        enregistrements1, enregistrements2, seuil=seuil, exact_match=exact_match
    )

    # Le couplage est effectué, on peut maintenant afficher les détails du résultat si l'option verbose est activée.
    if verbose:
        affiche_couplage(enregistrements1, enregistrements2, couplage)

    # --------------------
    # Export du résultat.

    # On réalise la jointure des enregistrements couplés que l'on souhaite exporter.
    jointure = jointure_couplage(enregistrements1, enregistrements2, couplage)

    # On reconstitue l'en-tête du fichier de sortie à partir des en-têtes des fichiers d'entrée.
    header_sortie = (
        ["id_1"]
        + [f"{c}_1" for c in enregistrements1_header]
        + ["id_2"]
        + [f"{c}_2" for c in enregistrements2_header]
        + ["score"]
    )

    # On exporte la jointure en CSV dans le fichier fichier_sortie donné en argument.
    export_csv(jointure, header_sortie, fichier_sortie)


def couplage_multi(
    enregistrements1: list[list[str]],
    enregistrements2: list[list[str]],
    seuil: float = 0.0,
    exact_match: bool = False,
) -> list[tuple[int, int]]:
    """
    Effectue un couplage entre deux ensembles d'enregistrements en utilisant un seuil de similarité.

    Args:
        enregistrements1 (list[list[str]]): Liste des enregistrements du premier ensemble.
        enregistrements2 (list[list[str]]): Liste des enregistrements du deuxième ensemble.
        seuil (float, optional): Seuil de similarité. Les couples dont le score de similarité est supérieur ou égal à ce seuil seront considérés comme des correspondances. Par défaut 0.0.
        exact_match (bool, optional): Indique si la similarité doit être calculée en utilisant une correspondance exacte ou une correspondance approximative. Si True, une correspondance exacte est utilisée. Si False, une correspondance approximative est utilisée. Par défaut False.

    Returns:
        list[tuple[int, int]]: Liste des couples d'indices des enregistrements correspondants, avec leur score de similarité.
    """

    couples = []

    if exact_match:
        seuil = 0.0

    for i, a in enumerate(enregistrements1):
        for j, b in enumerate(enregistrements2):
            if exact_match:
                score = score_exact(a, b)
                score = 1.0 - float(score)
            else:
                score = score_approximatif(a, b)

            if decision(score, seuil):
                couples.append((i, j, score))
    return couples


def score_exact(liste1: list[str], liste2: list[str]) -> bool:
    """
    Calcule le score de couplage exact booléen entre deux enregistrements.

    Args:
        enregistrement1 (list[str]): La première liste.
        enregistrement2 (list[str]): La deuxième liste.

    Returns:
        bool: True si les deux listes sont identiques, False sinon.
    """
    return all([liste1[i] == liste2[i] for i in range(len(liste1))])


def score_approximatif(enregistrement1: list[str], enregistrement2: list[str]) -> float:
    """
    Calcule le score de couplage approximatif entre deux enregistrements.

    Le score approximatif est calculé en utilisant la distance d'édition entre chaque paire de champs de type str des deux enregistrements.
    La distance d'édition mesure le nombre minimum d'opérations (insertion, suppression, substitution)
    nécessaires pour transformer une chaîne en une autre.

    Args:
        enregistrement1 (list[str]): La première liste de chaînes de caractères.
        enregistrement2 (list[str]): La deuxième liste de chaînes de caractères.

    Returns:
        float: Le score approximatif entre les deux listes.
    """
    mean = 0.0
    for s1, s2 in zip(enregistrement1, enregistrement2):
        d = edit_distance(s1, s2)
        mean += d
    return mean / len(enregistrement1)


def decision(score: float, seuil: float) -> bool:
    """
    Détermine si le score d'un couplage est un MATCH.

    Args:
        score (float): Le score à évaluer.
        seuil (float): Le seuil à comparer au score.

    Returns:
        bool: True si le score est inférieur ou égal au seuil, False sinon.
    """
    return score <= seuil


def normalisation(s: str) -> str:
    """
    Normalise une chaîne de caractères en effectuant les opérations suivantes :
    - Convertit la chaîne en minuscules
    - Remplace les caractères accentués par leur équivalent non accentué
    - Supprime la ponctuation
    - Remplace les espaces multiples par un seul espace
    - Supprime les espaces en début et fin de chaîne

    Args:
        s (str): La chaîne de caractères à normaliser.

    Returns:
        str: La chaîne de caractères normalisée.
    """
    s = (
        s.lower()
        .translate(str.maketrans("àâäéèêëîïôöùûüÿ", "aaaeeeeiioouuuy"))
        .translate(str.maketrans("", "", string.punctuation))
    )
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def jointure_couplage(
    enregistrements1: list[list[str]],
    enregistrements2: list[list[str]],
    couplage: list[tuple[int, int, float]],
) -> list[list[str]]:
    """
    Effectue une jointure entre deux ensembles d'enregistrements en utilisant un couplage donné.

    Args:
        enregistrements1 (list[list[str]]): Les enregistrements du premier ensemble.
        enregistrements2 (list[list[str]]): Les enregistrements du deuxième ensemble.
        couplage (list[tuple[int, int, float]]): Le couplage utilisé pour la jointure.

    Returns:
        list[list[str]]: La jointure des enregistrements avec les valeurs du couplage ajoutées.

    """
    jointure = []
    for i, j, s in couplage:
        line = []
        line.append(i)
        line.extend(enregistrements1[i])
        line.append(j)
        line.extend(enregistrements2[j])
        line.append(s)
        jointure.append(line)
    return jointure


def charger_enregistrements(fichier: str) -> list[list[str]]:
    """
    Charge les enregistrements à partir d'un fichier CSV.

    Args:
        fichier (str): Le chemin du fichier CSV.

    Returns:
        list[list[str]]: Une liste contenant les enregistrements du fichier CSV.
    """
    with open(fichier, "r") as f:
        data = csv.reader(f, delimiter=",")
        return list(data)


def export_csv(jointure: list[any], colonnes: list[str], fichier_sortie: str) -> None:
    """
    Exporte une jointure au format CSV.

    Args:
        jointure (list[any]): La jointure à exporter.
        colonnes (list[str]): Les noms des colonnes.
        fichier_sortie (str): Le chemin du fichier de sortie.
    """
    with open(fichier_sortie, "w") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(colonnes)
        writer.writerows(jointure)


def affiche_couplage(
    enregistrements1: list[list[str]],
    enregistrements2: list[list[str]],
    couplage: list[tuple[int, int, float]],
):
    """
    Affiche les couples de correspondances entre les enregistrements des deux listes,
    ainsi que le score de correspondance.

    Args:
        enregistrements1 (list[list[str]]): La première liste d'enregistrements.
        enregistrements2 (list[list[str]]): La deuxième liste d'enregistrements.
        couplage (list[tuple[int, int, float]]): La liste des couples de correspondances
            avec leur score.
    """
    for i, j, s in couplage:
        print(
            f"{i}: {enregistrements1[i]} --[MATCH {s:.2f}]-- {j}: {enregistrements2[j]}"
        )


# https://docs.python.org/fr/3/library/__main__.html
# On vérifie que le script est exécuté directement et non pas importé.
if __name__ == "__main__":
    # Si le script est exécuté directement, on appelle la fonction main().
    main()
