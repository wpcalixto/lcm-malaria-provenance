#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# Title:
#     Target-domain confusion matrices, enlarged fonts
# File type:
#     Script
# Purpose:
#     Generates the target-domain confusion matrices with enlarged fonts and fixed physical size.
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
#     - fig8a_cm_resnet50.pdf
#     - fig8b_cm_swint.pdf
#     - xai_resnet_fold5_nii/xai_resnet_fold5_results.csv
#     - xai_swin_fold2_nii/xai_swin_fold2_results.csv
# Outputs:
#     - See docs/file_level_documentation.md
# Dependencies:
#     - gera_R_resultados
#     - gera_fig6_matrizes_dados
# Execution:
#     python figuras_fonte/gera_fig7_matrizes_fonte130.py
# Portability notes:
#     Paths are relative to the root of this component or to the working directory.
# Reproducibility notes:
#     Environment: requirements.txt or environment.yml of this component. Seeds as defined in the code.
# Warnings:
#     None beyond the limitations listed in the README.
# Provenance:
#     Header added in v1.0.0; the code below is identical to the original file (see docs/modified_files.csv).
# ============================================================================
"""Figura 7 (fig8a/b_cm_*.pdf) — mesma figura de gera_fig6_matrizes.py, com TODAS as fontes +30%
(ordem de 2026-09-29: 18 -> 23,4 pt, pois a versao aprovada foi gerada com 18 pt) e a MESMA dimensao
fisica (413,185 x 413,185 pt). Contagens lidas dos mesmos artefatos; nenhuma contagem alterada."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gera_fig6_matrizes_dados import conta, B      # noqa: E402
from gera_R_resultados import matriz_fixa           # noqa: E402

LADO = 413.185 / 72
FS = 18 * 1.3
for csv, arq in [(B + "xai_resnet_fold5_nii/xai_resnet_fold5_results.csv", "fig8a_cm_resnet50.pdf"),
                 (B + "xai_swin_fold2_nii/xai_swin_fold2_results.csv", "fig8b_cm_swint.pdf")]:
    matriz_fixa(conta(csv), r"Predicted label", r"Operational reference label", lado=LADO, fs=FS, arquivo=arq)
