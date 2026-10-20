#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# Title:
#     Global methodology workflow (draft)
# File type:
#     Script
# Purpose:
#     Generates a draft of the global methodology workflow diagram.
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
#     - fluxo_metodologico_global.pdf
# Outputs:
#     - See docs/file_level_documentation.md
# Dependencies:
#     - norma_figuras
# Execution:
#     python figuras_fonte/gera_fig1_fluxo_global.py
# Portability notes:
#     Paths are relative to the root of this component or to the working directory.
# Reproducibility notes:
#     Environment: requirements.txt or environment.yml of this component. Seeds as defined in the code.
# Warnings:
#     The final Figures 1 and 2 of the article were produced in Microsoft Visio; this script generates a draft only.
# Provenance:
#     Header added in v1.0.0; the code below is identical to the original file (see docs/modified_files.csv).
# ============================================================================
"""Figura 1 — global methodology workflow, macroprocess level.
Reconstruido exclusivamente a partir da Metodologia declarada no manuscrito."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from norma_figuras import *

W, H = 7.78, 6.95
fig, ax = tela(W, H)
XA, XB = 1.98, 5.66
w, h = 2.90, 0.42
wd, hd = 3.04, 0.76

faixa(ax, 0.34, 1.62, 3.32, 5.14, TINTA_DOMINIO["Source domain"], COR_DOMINIO["Source domain"])
rotulo_faixa(ax, 0.44, 4.30, r"Source domain", COR_DOMINIO["Source domain"])
faixa(ax, 3.96, 3.36, 3.42, 3.20, TINTA_DOMINIO["Target domain"], COR_DOMINIO["Target domain"])
rotulo_faixa(ax, 7.28, 4.96, r"Target domain", COR_DOMINIO["Target domain"])
faixa(ax, 3.96, 2.54, 3.42, 0.58, TINTA_DOMINIO["Auxiliary domain"], COR_DOMINIO["Auxiliary domain"])
rotulo_faixa(ax, 7.34, 2.83, r"Auxiliary domain", COR_DOMINIO["Auxiliary domain"])

terminador(ax, XA, 6.62, 1.16, 0.34, r"START")
processo(ax, XA, 6.08, w, h, "Dataset and domain definition")
processo(ax, XA, 5.52, w, h, "Input-unit identification")
decisao (ax, XA, 4.80, wd, hd, "Does the input already\ncontain cell instances?")
processo(ax, 1.22, 4.02, 1.40, 0.42, "Direct input\npreparation")
processo(ax, 2.98, 4.14, 1.52, 0.34, "Cell segmentation")
processo(ax, 2.98, 3.68, 1.52, 0.34, "Crop generation")
processo(ax, XA, 3.06, w, h, "Classifier development")
processo(ax, XA, 2.50, w, h, "Cross-validation and\nreference-checkpoint selection")
processo(ax, XA, 1.90, w, h, "In-domain evaluation")

seta(ax,(XA,6.45),(XA,6.29)); seta(ax,(XA,5.87),(XA,5.73)); seta(ax,(XA,5.31),(XA,5.18))
seta(ax,(XA-wd/2,4.80),(1.22,4.80),(r"Yes",0,0.13)); seta(ax,(1.22,4.80),(1.22,4.23))
seta(ax,(XA+wd/2,4.80),(3.74,4.80),(r"No",0,0.13))
linha(ax,[3.74,3.74],[4.80,4.14]); seta(ax,(3.74,4.14),(2.98+0.76,4.14))
seta(ax,(2.98,3.97),(2.98,3.85))
seta(ax,(1.22,3.81),(1.22,3.40)); linha(ax,[1.22,2.98],[3.40,3.40])
seta(ax,(2.98,3.51),(2.98,3.40)); seta(ax,(XA,3.40),(XA,3.27))
seta(ax,(XA,2.85),(XA,2.71)); seta(ax,(XA,2.29),(XA,2.11))

linha(ax,[XA+w/2,3.82],[1.90,1.90]); linha(ax,[3.82,3.82],[1.90,6.20])
seta(ax,(3.82,6.20),(XB-w/2,6.20))

processo(ax, XB, 6.20, w, h, "Checkpoint application to the\ntarget domain without adaptation")
processo(ax, XB, 5.56, w, h, "Operational-reference construction\nand verification")
processo(ax, XB, 4.92, w, h, "External evaluation with\nfield-level clustered uncertainty")
processo(ax, XB, 4.28, w, h, "Paired architecture comparison")
processo(ax, XB, 3.64, w, h, "Qualitative explainability inspection")
processo(ax, XB, 2.83, w, h, "Integrated-flow execution check")
processo(ax, XB, 2.10, w, h, "Results synthesis")
terminador(ax, XB, 1.56, 1.16, 0.34, r"END")
for y0,y1 in [(5.99,5.77),(5.35,5.13),(4.71,4.49),(4.07,3.85),(3.43,3.04),(2.62,2.31),(1.89,1.73)]:
    seta(ax,(XB,y0),(XB,y1))

ax.add_patch(FancyBboxPatch((1.40,0.72),4.80,0.46,boxstyle="round,pad=0,rounding_size=0.06",
    fc=C_TRANSV,ec=BORDA,lw=LW,ls=(0,(4,2)),zorder=3))
ax.text(3.80,0.95,"Provenance and execution audit --- cross-cutting process",
        ha="center",va="center",fontsize=FONTE,zorder=5)
for x0,y1 in [(2.60,1.69),(4.80,1.89)]:
    seta(ax,(x0,1.18),(x0,y1),tracejada=True)

salva(fig, "fluxo_metodologico_global.pdf")
