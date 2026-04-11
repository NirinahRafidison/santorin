# Santorin - Machine Translation Pipeline

Santorin est un pipeline modulaire de traduction automatique du français vers l’anglais, basé sur un modèle HuggingFace.  
Le projet charge des données textuelles, les nettoie, les traduit automatiquement, puis évalue la qualité des traductions à l’aide de métriques standards comme BLEU et chrF.

## Description

Ce projet a été conçu dans une logique de structuration de projet Python moderne.  
Il sépare les responsabilités en plusieurs modules spécialisés afin de rendre le code plus lisible, maintenable et facilement extensible.

Le pipeline prend en entrée un fichier de données textuelles, applique un modèle de traduction automatique, enregistre les résultats générés dans un répertoire de sortie, puis calcule des scores d’évaluation pour mesurer la qualité des traductions obtenues.

## Fonctionnalités

- Chargement de données depuis des fichiers JSON ou CSV
- Prétraitement et nettoyage des données textuelles
- Traduction automatique avec un modèle HuggingFace
- Évaluation de la qualité des traductions avec BLEU et chrF
- Sauvegarde des résultats dans un fichier de sortie
- Architecture modulaire basée sur un orchestrateur central

## Architecture du projet

Le projet est organisé autour des modules suivants :

- `src/loaders` : chargement des données d’entrée
- `src/processors` : nettoyage et préparation des données
- `src/translators` : traduction automatique avec HuggingFace
- `src/evaluators` : calcul des métriques d’évaluation
- `src/orchestrator` : orchestration complète du pipeline

Le répertoire `data/` contient les fichiers d’entrée, tandis que `output/` reçoit les résultats générés par le pipeline.

## Modèle utilisé

Le pipeline utilise le modèle :

- `Helsinki-NLP/opus-mt-fr-en`

Ce modèle permet de traduire automatiquement du français vers l’anglais.

## Technologies utilisées

- Python 3.10+
- HuggingFace Transformers
- PyTorch
- SentencePiece
- SacreBLEU
- pytest
- black

## Installation

Créer un environnement virtuel puis installer les dépendances :

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install transformers torch sentencepiece sacrebleu pytest black
