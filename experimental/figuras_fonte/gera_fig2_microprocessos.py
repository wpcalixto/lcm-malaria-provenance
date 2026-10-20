#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# Title:
#     Integrated pipeline workflow (draft)
# File type:
#     Script
# Purpose:
#     Generates a draft of the microprocess workflow of the integrated pipeline.
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
#     - pipeline_mum-xai.pdf
# Outputs:
#     - See docs/file_level_documentation.md
# Dependencies:
#     - norma_figuras
# Execution:
#     python figuras_fonte/gera_fig2_microprocessos.py
# Portability notes:
#     Paths are relative to the root of this component or to the working directory.
# Reproducibility notes:
#     Environment: requirements.txt or environment.yml of this component. Seeds as defined in the code.
# Warnings:
#     The final Figures 1 and 2 of the article were produced in Microsoft Visio; this script generates a draft only.
# Provenance:
#     Header added in v1.0.0; the code below is identical to the original file (see docs/modified_files.csv).
# ============================================================================
"""Microprocess workflow of the integrated computational pipeline (MUM-XAI).
Mesma identidade grafica do fluxograma global. Reconstruido do metodo e do codigo."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from norma_figuras import *

W, H = 7.90, 5.72
fig, ax = tela(W, H)
XA, XB = 1.92, 5.62
w, h = 2.80, 0.40
wd, hd = 2.94, 0.72

terminador(ax, XA, 5.24, 1.16, 0.34, r"START")
dado    (ax, XA, 4.72, w, 0.48, "Submitted microscopy\nimage")
decisao (ax, XA, 3.98, wd, hd, "Is the input a\nfield of view?")
processo(ax, 1.00, 3.18, 1.44, 0.42, "Direct crop\ninput")
processo(ax, 2.92, 3.30, 1.52, 0.34, "Cell segmentation")
processo(ax, 2.92, 2.86, 1.52, 0.34, "Crop generation")
processo(ax, XA, 2.24, w, h, "Checkpoint loading (.pth)")
processo(ax, XA, 1.68, w, h, "Classification with ResNet50\nor Swin Transformer")

seta(ax,(XA,5.07),(XA,4.96)); seta(ax,(XA,4.48),(XA,4.34))
seta(ax,(XA-wd/2,3.98),(1.00,3.98),(r"No",0,0.13)); seta(ax,(1.00,3.98),(1.00,3.39))
seta(ax,(XA+wd/2,3.98),(3.44,3.98),(r"Yes",0,0.13))
linha(ax,[3.44,3.44],[3.98,3.62]); linha(ax,[3.44,2.92],[3.62,3.62])
seta(ax,(2.92,3.62),(2.92,3.47))
seta(ax,(2.92,3.13),(2.92,3.03))
seta(ax,(1.00,2.97),(1.00,2.58)); linha(ax,[1.00,2.92],[2.58,2.58])
seta(ax,(2.92,2.69),(2.92,2.58)); seta(ax,(XA,2.58),(XA,2.44))
seta(ax,(XA,2.04),(XA,1.88))

linha(ax,[XA+w/2,3.86],[1.68,1.68]); linha(ax,[3.86,3.86],[1.68,5.10])
seta(ax,(3.86,5.10),(XB-wd/2,5.10))

decisao (ax, XB, 5.10, wd, hd, "Attribution-method\nselection")
mw = 1.14
for xm, rot in [(4.36,"Grad-CAM"), (5.62,"Integrated\nGradients"), (6.88,"Occlusion")]:
    processo(ax, xm, 4.28, mw, 0.44, rot)
    seta(ax,(XB,4.74),(xm,4.52))
    seta(ax,(xm,4.06),(xm,3.86))
linha(ax,[4.36,6.88],[3.86,3.86]); seta(ax,(XB,3.86),(XB,3.72))
processo(ax, XB, 3.50, 3.10, h, "Spatial reconstruction and highlighting\nof cells predicted as infected")
seta(ax,(XB,3.30),(XB,3.12)); linha(ax,[5.02,6.90],[3.12,3.12])
seta(ax,(5.02,3.12),(5.02,2.96)); seta(ax,(6.90,3.12),(6.90,2.96))
dado(ax, 5.02, 2.72, 1.62, 0.48, "Visual outputs\nper image")
dado(ax, 6.90, 2.72, 1.56, 0.48, "Structured output\n(implemented)")
seta(ax,(5.02,2.48),(5.02,2.26)); seta(ax,(6.90,2.48),(6.90,2.26))
linha(ax,[5.02,6.90],[2.26,2.26]); seta(ax,(XB,2.26),(XB,2.08))
terminador(ax, XB, 1.90, 1.16, 0.34, r"END")

ax.set_ylim(1.38, H)
salva(fig, "pipeline_mum-xai.pdf")
