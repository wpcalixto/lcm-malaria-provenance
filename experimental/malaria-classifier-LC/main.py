#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# Title:
#     Training entry point
# File type:
#     Script
# Purpose:
#     Entry point that configures and launches k-fold training of the classifier package.
# Repository:
#     lcm-malaria-provenance, component experimental
# Version:
#     v1.0.0
# Date:
#     2026-10-20
# Developer:
#     Prof. Wesley Pacheco Calixto
# Authors:
#     Sthefanie Monica Premebida, Federal University of Technology - Parana, Brazil, ORCID 0000-0002-8964-2119
#     Gabrielly Queiroz Pereira, State University of Ponta Grossa, Brazil, ORCID 0000-0003-2663-0783
#     Philipp Wiedemann, Department of Biotechnology, Mannheim University of Applied Sciences, Germany
#     Marcella Scoczynski R. Martins, Federal University of Technology - Parana, Brazil, ORCID 0000-0002-5716-4968
#     Wesley Pacheco Calixto, Institute of Systems and Robotics, University of Coimbra, Portugal, ORCID 0000-0002-1928-4432
# Corresponding author:
#     Wesley Pacheco Calixto, wesley.pacheco@isr.uc.pt, Institute of Systems and Robotics, University of Coimbra
# License:
#     MIT
# Citation:
#     If you use this code, please cite:
#     Premebida, S. M., Pereira, G. Q., Wiedemann, P., Martins, M. S. R., & Calixto, W. P. (2026). Low-Cost Microscope dataset, code, and model checkpoints for Computational provenance in external evaluation of deep learning for malaria microscopy (Version 1.0.0) [Data set and software]. Zenodo. https://doi.org/10.5281/zenodo.23505452
# Related publication:
#     Computational provenance in external evaluation of deep learning for malaria microscopy (DOI not yet available).
# Inputs:
#     - See docs/file_level_documentation.md
# Outputs:
#     - See docs/file_level_documentation.md
# Dependencies:
#     - malaria_classifier
#     - torch
# Execution:
#     python malaria-classifier-LC/main.py
# Portability notes:
#     Paths are relative to the root of this component or to the working directory.
# Reproducibility notes:
#     Environment: requirements.txt or environment.yml of this component. Seeds as defined in the code.
# Warnings:
#     None beyond the limitations listed in the README.
# Provenance:
#     Header added in v1.0.0; the code below is identical to the original file (see docs/modified_files.csv).
# ============================================================================
import torch
from malaria_classifier.transforms import get_transforms, get_dataloader
from malaria_classifier.models.resnet_model import ResNet50Model
from malaria_classifier.models.swin_model import SwinModel
from malaria_classifier.train import run_kfold_training

if __name__ == "__main__":
    dataset_path = "./dataset"  # ajuste esse caminho conforme seu projeto
    img_size = 224
    batch_size = 32
    num_epochs = 10
    k_folds = 5
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    train_tf, val_tf = get_transforms(img_size)
    dataloader, class_to_idx = get_dataloader(dataset_path, train_tf, batch_size)

    # Teste com ResNet
    print("Treinando ResNet50...")
    run_kfold_training(ResNet50Model, dataloader.dataset, k_folds, batch_size, num_epochs=num_epochs, device=device)

    # Teste com Swin
    print("Treinando Swin Transformer...")
    run_kfold_training(SwinModel, dataloader.dataset, k_folds, batch_size, num_epochs=num_epochs, device=device)