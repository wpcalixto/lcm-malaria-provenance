#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# Title:
#     Source-domain figure
# File type:
#     Script
# Purpose:
#     Generates the source-domain (NIH) sample panels.
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
#     - C117P78ThinF_IMG_20150930_221048_cell_2.png
#     - C132P93ThinF_IMG_20151004_152045_cell_133.png
#     - C139P100ThinF_IMG_20151005_183601_cell_149.png
#     - C169P130ThinF_IMG_20151119_144354_cell_156.png
#     - C182P143NThinF_IMG_20151201_172607_cell_26.png
#     - C187P148NThinF_IMG_20151203_153410_cell_149.png
# Outputs:
#     - See docs/file_level_documentation.md
# Dependencies:
#     - PIL
#     - norma_figuras
#     - numpy
# Execution:
#     python figuras_fonte/gera_fig3_dominio_origem.py
# Portability notes:
#     Paths are relative to the root of this component or to the working directory.
# Reproducibility notes:
#     Environment: requirements.txt or environment.yml of this component. Seeds as defined in the code.
# Warnings:
#     The NIH Malaria Dataset images are not included; obtain them from the U.S. National Library of Medicine.
# Provenance:
#     Header added in v1.0.0; the code below is identical to the original file (see docs/modified_files.csv).
# ============================================================================
"""Figura 3 — dominio de origem (NIH), paineis (a) e (b).

Painel (a): as MESMAS 18 celulas do arquivo historico, recuperadas por correlacao
            contra as 27.558 imagens do conjunto NIH (correlacao >= 0,9964, segundo
            colocado <= 0,981 em todos os 18 casos). Reconstruido a partir das
            imagens-fonte; nao ha upsampling do PNG antigo.
Painel (b): mesma celula e mesmo recorte do notebook original
            (metricas.ipynb, celula ec=15): C33P1thinF_IMG_20150619_114756a_cell_179,
            recorte (60,75)-(120,135), caixa vermelha.

Sem titulo interno. Em (a) permanecem apenas os identificadores de classe.
"""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from norma_figuras import *
from PIL import Image, ImageDraw
import numpy as np

NIH = "/private/tmp/nih/cell_images"

# --- painel (a): grade 3x6, colunas 0-2 infectadas, colunas 3-5 nao infectadas ---
INFECTADAS = ["C82P43ThinF_IMG_20150817_124728_cell_12.png",
              "C37BP2_thinF_IMG_20150620_133111a_cell_86.png",
              "C68P29N_ThinF_IMG_20150819_134712_cell_35.png",
              "C187P148NThinF_IMG_20151203_153410_cell_149.png",
              "C132P93ThinF_IMG_20151004_152045_cell_133.png",
              "C99P60ThinF_IMG_20150918_141620_cell_57.png",
              "C48P9thinF_IMG_20150721_161055_cell_185.png",
              "C139P100ThinF_IMG_20151005_183601_cell_149.png",
              "C182P143NThinF_IMG_20151201_172607_cell_26.png"]
NAO_INFECTADAS = ["C203ThinF_IMG_20151029_105443_cell_204.png",
                  "C117P78ThinF_IMG_20150930_221048_cell_2.png",
                  "C78P39ThinF_IMG_20150606_103630_cell_121.png",
                  "C4thin_original_IMG_20150608_170016_cell_96.png",
                  "C204ThinF_IMG_20151029_110627_cell_254.png",
                  "C203ThinF_IMG_20151029_105443_cell_74.png",
                  "C169P130ThinF_IMG_20151119_144354_cell_156.png",
                  "C38P3thinF_original_IMG_20150621_112227_cell_3.png",
                  "C239ThinF_IMG_20151127_113150_cell_71.png"]

LADO, VAO = 150, 12                      # ladrilho e vao, em pixels
MW = 6*LADO + 5*VAO                      # 960
MH = 3*LADO + 2*VAO                      # 474

mosaico = Image.new("RGB", (MW, MH), "white")
for lin in range(3):
    for col in range(6):
        if col < 3:
            f = os.path.join(NIH, "Parasitized", INFECTADAS[lin*3 + col])
        else:
            f = os.path.join(NIH, "Uninfected", NAO_INFECTADAS[lin*3 + col - 3])
        t = Image.open(f).convert("RGB").resize((LADO, LADO), Image.LANCZOS)
        mosaico.paste(t, (col*(LADO+VAO), lin*(LADO+VAO)))

LARG = 6.40                              # canvas; artigo exibe a 0,92\linewidth
ALT_MOS = LARG * MH / MW
FAIXA = 0.40
ALT = ALT_MOS + FAIXA
DPI = MW / LARG                          # 150: raster embutido 1:1, sem reamostragem

aplica_rc()
fig = plt.figure(figsize=(LARG, ALT))
ax = fig.add_axes([0, 0, 1, ALT_MOS/ALT]); ax.axis("off")
ax.imshow(np.asarray(mosaico), interpolation="nearest")
c1 = (3*LADO + 2*VAO)/2 / MW
c2 = (3*(LADO+VAO) + (3*LADO + 2*VAO)/2) / MW
y = ALT_MOS/ALT + 0.10*FAIXA/ALT
fig.text(c1, y, r"Infected",   ha="center", va="bottom", fontsize=FONTE)
fig.text(c2, y, r"Uninfected", ha="center", va="bottom", fontsize=FONTE)
fig.savefig("amostra-imagens.pdf", dpi=DPI)
plt.close(fig); print(f"  gerado: amostra-imagens.pdf  (raster {MW}x{MH} px)")

# --- painel (b): celula com a regiao marcada e a ampliacao, sem titulo interno ---
CEL = os.path.join(NIH, "Parasitized", "C33P1thinF_IMG_20150619_114756a_cell_179.png")
x0, y0 = 60, 75
x1, y1 = x0 + 60, y0 + 60
img = Image.open(CEL).convert("RGB")
recorte = img.crop((x0, y0, x1, y1))
marcada = img.copy(); ImageDraw.Draw(marcada).rectangle([(x0, y0), (x1, y1)],
                                                        outline="red", width=2)
fig, axes = plt.subplots(1, 2, figsize=(6.40, 3.40))
for a, im in zip(axes, (marcada, recorte)):
    a.imshow(np.asarray(im)); a.axis("off")
fig.subplots_adjust(left=0, right=1, top=1, bottom=0, wspace=0.06)
fig.savefig("zoom-parasita.pdf", dpi=300)
plt.close(fig); print("  gerado: zoom-parasita.pdf")
