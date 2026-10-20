#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# Title:
#     Target-domain confusion matrices
# File type:
#     Script
# Purpose:
#     Generates the target-domain confusion matrices from the preserved XAI result tables.
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
#     - matplotlib
#     - norma_figuras
#     - numpy
#     - pandas
# Execution:
#     python figuras_fonte/gera_fig6_matrizes.py
# Portability notes:
#     Paths are relative to the root of this component or to the working directory.
# Reproducibility notes:
#     Environment: requirements.txt or environment.yml of this component. Seeds as defined in the code.
# Warnings:
#     None beyond the limitations listed in the README.
# Provenance:
#     Header added in v1.0.0; the code below is identical to the original file (see docs/modified_files.csv).
# ============================================================================
"""Figura 7 — confusion matrices do dominio-alvo, rotulos operacionais originais.
Contagens recalculadas dos artefatos; nenhuma contagem alterada."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from norma_figuras import *
import numpy as np, pandas as pd

aplica_rc()
B = "GitHub_master-2025/3-Datasets/img-lcm/"
def conta(path):
    d = pd.read_csv(path); y, p = d.true_idx.values, d.pred_idx.values
    return np.array([[int(((y==0)&(p==0)).sum()), int(((y==0)&(p==1)).sum())],
                     [int(((y==1)&(p==0)).sum()), int(((y==1)&(p==1)).sum())]])

def painel(M, arquivo):
    fig, ax = plt.subplots(figsize=(3.06*K, 2.75*K))   # paineis a 0,485\linewidth
    # regra 1: desenho vetorial; nenhum componente raster (imshow) na figura
    from matplotlib.patches import Rectangle
    from matplotlib import colormaps
    azuis = colormaps["Blues"]
    lim = M.max()/2
    for i in range(2):
        for j in range(2):
            ax.add_patch(Rectangle((j-0.5, i-0.5), 1, 1,
                         fc=azuis(M[i, j]/M.max()), ec="white", lw=1.5))
    ax.set_xlim(-0.5, 1.5); ax.set_ylim(1.5, -0.5); ax.set_aspect("equal")
    for i in range(2):
        for j in range(2):
            ax.text(j, i, r"%s" % f"{M[i,j]:,}".replace(",", "\\,"),
                    ha="center", va="center", fontsize=FONTE,
                    color="white" if M[i, j] > lim else "black")
    ax.set_xticks([0, 1]); ax.set_xticklabels([r"Uninfected", r"Infected"])
    ax.set_yticks([0, 1]); ax.set_yticklabels([r"Uninfected", r"Infected"], rotation=90, va="center")
    ax.set_xlabel(r"Predicted label"); ax.set_ylabel(r"Operational reference label")
    ax.tick_params(length=0)
    for s in ax.spines.values(): s.set_visible(False)
    salva(fig, arquivo)

painel(conta(B+"xai_resnet_fold5_nii/xai_resnet_fold5_results.csv"), "fig8a_cm_resnet50.pdf")
painel(conta(B+"xai_swin_fold2_nii/xai_swin_fold2_results.csv"),     "fig8b_cm_swint.pdf")
