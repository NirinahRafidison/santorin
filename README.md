# Santorin - Machine Learning Translation Pipeline

## Description

Ce projet implémente un pipeline complet de traduction automatique basé sur un modèle HuggingFace.

Le pipeline permet de :

* charger des données textuelles,
* traduire les textes,
* appliquer des traitements,
* évaluer la qualité des traductions (BLEU score).

## Structure du projet

* `src/loaders` : chargement des données
* `src/processors` : prétraitement
* `src/translators` : traduction
* `src/evaluators` : évaluation
* `src/orchestrator` : orchestration du pipeline

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install black pytest
```

## Exécution

```bash
pytest
```

## Tests

Les tests sont réalisés avec pytest.

## Qualité du code

Formatage avec black.

## Auteur

Nirinah Rafidison

## Version Python

Python 3.10
