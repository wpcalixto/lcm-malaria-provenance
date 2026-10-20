#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# Title:
#     Provenance audit map
# File type:
#     Script
# Purpose:
#     Generates the provenance audit map figure.
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
#     - figR8_provenance_audit_map.pdf
# Outputs:
#     - See docs/file_level_documentation.md
# Dependencies:
#     - matplotlib
#     - norma_figuras
# Execution:
#     python figuras_fonte/gera_R8_auditoria.py
# Portability notes:
#     Paths are relative to the root of this component or to the working directory.
# Reproducibility notes:
#     Environment: requirements.txt or environment.yml of this component. Seeds as defined in the code.
# Warnings:
#     None beyond the limitations listed in the README.
# Provenance:
#     Header added in v1.0.0; the code below is identical to the original file (see docs/modified_files.csv).
# ============================================================================
"""Figura R8 (opcional) — mapa da auditoria de proveniencia.

Sem dado novo: cada linha reproduz uma classificacao ja publicada nas Tabelas de auditoria
(tab_optuna-audit, tab_provenance-audit) e na Tabela de parametros instanciados.
Evidencias: logs Optuna e resnet50/swin_optuna_exec.ipynb (busca); caminhos de pre-processamento
(normalizacoes da Tabela de parametros); cellpose.ipynb e creating_annot_v3.ipynb
(CellposeModel sem model_type -> cpsam; min_cell_area=0); src/segmentation.py do deposito
(model_type="cyto2", min_area=80).
Saida estruturada separada em dois objetos: exibicao na interface (app5.jpeg, Confirmed) e arquivo
exportado preservado (cell_results_*.csv / resultados_multiplos_imagens.csv ausentes, Not preserved).
Categorias: Confirmed, Divergent, Not auditable; Not preserved apenas para o arquivo estruturado (ordem final).
"""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from norma_figuras import *
from matplotlib.patches import FancyBboxPatch

LARG = 7.23
CAT = {"Confirmed": OKABE_ITO["azulceu"], "Divergent": OKABE_ITO["amarelo"], "Not auditable": "#D9D9D9", "Not preserved": "#D9D9D9"}

BLOCOS = [
    ("Hyperparameter search", [("Learning rate", "Confirmed"), ("Optimizer", "Confirmed"),
                               ("Weight decay", "Divergent"), ("Loss function", "Divergent"),
                               ("Hold-out isolation", "Divergent")]),
    ("Internal vs external preprocessing", [("Internal normalization", "Divergent"),
                                            ("External normalization", "Divergent"),
                                            ("Grayscale to three channels", "Divergent")]),
    ("Analytical vs application segmentation", [(r"Analytical model \texttt{cpsam}", "Divergent"),
                                                (r"Application model \texttt{cyto2}", "Divergent"),
                                                ("Analytical area threshold 0 px", "Divergent"),
                                                ("Application area threshold 80 px", "Divergent")]),
    ("Reproducibility and preserved records", [("External checkpoints", "Confirmed"),
                                               ("Target-list formation criterion", "Not auditable"),
                                               ("XAI inspected universe", "Not auditable"),
                                               ("Structured output displayed in the app", "Confirmed"),
                                               ("Preserved structured output file", "Not preserved")]),
]

if __name__ == "__main__":
    fig, ax = tela(LARG, 3.05)
    W, DY, H0 = 3.5, 0.225, 0.3
    pos = [(0.05, 3.0), (3.68, 3.0), (0.05, 1.5), (3.68, 1.5)]
    for (titulo, itens), (x, ytop) in zip(BLOCOS, pos):
        ax.text(x, ytop, r"\textbf{%s}" % titulo, ha="left", va="top", fontsize=FONTE)
        for i, (item, cat) in enumerate(itens):
            y = ytop - H0 - i * DY
            ax.plot([x, x + W], [y - DY / 2, y - DY / 2], color="#DDDDDD", lw=1.0)
            ax.text(x + 0.05, y, item, ha="left", va="center", fontsize=FONTE)
            ax.add_patch(FancyBboxPatch((x + W - 1.02, y - 0.085), 1.0, 0.17,
                         boxstyle="round,pad=0,rounding_size=0.05", fc=CAT[cat], ec="none"))
            ax.text(x + W - 0.52, y, cat, ha="center", va="center", fontsize=FONTE)
    ax.set_xlim(0, LARG); ax.set_ylim(0.1, 3.05)
    salva(fig, "figR8_provenance_audit_map.pdf")
