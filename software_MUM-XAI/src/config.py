#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# Title:
#     Configuration
# File type:
#     Configuration helper
# Purpose:
#     Defines the checkpoint paths and the computation device used by MUM-XAI.
# Repository:
#     lcm-malaria-provenance, component software_MUM-XAI
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
#     Apache-2.0
# Citation:
#     If you use this code, please cite:
#     Premebida, S. M., Pereira, G. Q., Wiedemann, P., Martins, M. S. R., & Calixto, W. P. (2026). Low-Cost Microscope dataset, code, and model checkpoints for Computational provenance in external evaluation of deep learning for malaria microscopy (Version 1.0.0) [Data set and software]. Zenodo. https://doi.org/10.5281/zenodo.23505452
# Related publication:
#     Computational provenance in external evaluation of deep learning for malaria microscopy (DOI not yet available).
# Inputs:
#     - resnet_fold5.pth
#     - swin_fold2.pth
# Outputs:
#     - See docs/file_level_documentation.md
# Dependencies:
#     - torch
# Execution:
#     Imported by other files of this component; not executed directly.
# Portability notes:
#     Paths are relative to the root of this component or to the working directory.
# Reproducibility notes:
#     Environment: requirements.txt or environment.yml of this component. Seeds as defined in the code.
# Warnings:
#     None beyond the limitations listed in the README.
# Provenance:
#     Header added in v1.0.0; the code below is identical to the original file (see docs/modified_files.csv).
# ============================================================================
# src/config.py

from pathlib import Path
import torch

# Detecta GPU ou CPU
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Caminho raiz do projeto (MUM-XAI/)
ROOT_DIR = Path(__file__).resolve().parents[1]

# Pasta de modelos
MODELS_DIR = ROOT_DIR / "models"

# Caminho completo para os modelos .pth
RESNET_CKPT_PATH = MODELS_DIR / "resnet_fold5.pth"
SWIN_CKPT_PATH   = MODELS_DIR / "swin_fold2.pth"

# Classes
CLASS_NAMES = ["uninfected", "infected"]
