#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# Title:
#     Recall and loss curves
# File type:
#     Script
# Purpose:
#     Generates the validation recall and training loss curves per fold in the source domain.
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
#     - GitHub_master-2025/4-redes/2.resnet/normal/kfold_epoch_results.csv
#     - GitHub_master-2025/4-redes/3.swin/swin-sem-optuna/kfold_epoch_results.csv
#     - fig5a_resnet50_recall.pdf
#     - fig5b_swint_recall.pdf
#     - fig5c_resnet50_loss.pdf
#     - fig5d_swint_loss.pdf
# Outputs:
#     - See docs/file_level_documentation.md
# Dependencies:
#     - matplotlib
#     - norma_figuras
#     - pandas
# Execution:
#     python figuras_fonte/gera_fig4_fig5_recall_loss.py
# Portability notes:
#     Paths are relative to the root of this component or to the working directory.
# Reproducibility notes:
#     Environment: requirements.txt or environment.yml of this component. Seeds as defined in the code.
# Warnings:
#     None beyond the limitations listed in the README.
# Provenance:
#     Header added in v1.0.0; the code below is identical to the original file (see docs/modified_files.csv).
# ============================================================================
"""Figuras 5 e 6 — validation recall e training loss por fold, dominio de origem.
Fonte: kfold_epoch_results.csv. Nenhum dado alterado; apenas replotagem sob a norma.
Regra 5: legenda apenas no primeiro painel de cada figura, in-plot."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from norma_figuras import *
from matplotlib.ticker import FormatStrFormatter
import pandas as pd

aplica_rc()
R = pd.read_csv("GitHub_master-2025/4-redes/2.resnet/normal/kfold_epoch_results.csv")
S = pd.read_csv("GitHub_master-2025/4-redes/3.swin/swin-sem-optuna/kfold_epoch_results.csv").iloc[:101]

# paineis lado a lado a 0,485\linewidth: canvas dimensionado para ~8 pt de texto na pagina
LARG, ALT = 3.30*K, 2.05*K

def limites(col):
    v = pd.concat([R[R.fold <= 5][col], S[S.fold <= 5][col]])
    m, M = v.min(), v.max(); folga = 0.06*(M-m)
    return m-folga, M+folga

def painel(df, col, modelo, ylabel, arquivo, ylim, fmt, legenda, loc):
    fig, ax = plt.subplots(figsize=(LARG, ALT))
    for i, f in enumerate([1, 2, 3, 4, 5]):
        d = df[(df.fold == f) & (df.epoch <= 20)].sort_values("epoch")
        ax.plot(d.epoch, d[col], color=COR_FOLD[i], label=r"Fold %d" % f)
    ax.set_xlabel(r"Epoch [-]"); ax.set_ylabel(ylabel)
    ax.set_xlim(1, 20); ax.set_xticks([1, 5, 10, 15, 20]); ax.set_ylim(*ylim)
    ax.yaxis.set_major_formatter(FormatStrFormatter(fmt))
    ax.grid(True, linewidth=0.8, alpha=0.35)
    ax.spines[["top", "right"]].set_visible(False)
    if legenda:                                   # regra 5
        ax.legend(loc=loc, ncol=2, frameon=True, framealpha=0.92, edgecolor="0.7",
                  handlelength=1.8, columnspacing=1.2, borderpad=0.5)
    salva(fig, arquivo)

lr, ll = limites("recall"), limites("loss")
painel(R, "recall", "ResNet50",         r"Recall [-]",       "fig5a_resnet50_recall.pdf", lr, "%.4f", True,  "lower right")
painel(S, "recall", "Swin Transformer", r"Recall [-]",       "fig5b_swint_recall.pdf",    lr, "%.4f", False, None)
painel(R, "loss",   "ResNet50",         r"Training loss [-]","fig5c_resnet50_loss.pdf",   ll, "%.3f", True,  "upper right")
painel(S, "loss",   "Swin Transformer", r"Training loss [-]","fig5d_swint_loss.pdf",      ll, "%.3f", False, None)
print(f"  limites recall [{lr[0]:.4f}, {lr[1]:.4f}] | loss [{ll[0]:.4f}, {ll[1]:.4f}]")
