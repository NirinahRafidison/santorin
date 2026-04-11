# Santorin - Machine Learning Translation Pipeline

## Description

Ce projet implémente un pipeline complet de traduction automatique basé sur un modèle HuggingFace.

Le pipeline permet de :
- charger des données textuelles,
- appliquer des traitements,
- traduire les textes (français → anglais),
- évaluer la qualité des traductions avec des métriques (BLEU, chrF).

Le modèle utilisé est : **Helsinki-NLP/opus-mt-fr-en**

---

## Structure du projet

- `src/loaders` : chargement des données
- `src/processors` : prétraitement
- `src/translators` : traduction avec HuggingFace
- `src/evaluators` : évaluation des performances
- `src/orchestrator` : orchestration du pipeline

- `data/` : fichiers d’entrée
- `output/` : résultats générés

---

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install black pytest transformers torch sacrebleu sentencepiece
