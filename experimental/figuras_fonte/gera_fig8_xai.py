#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# Title:
#     XAI composite figure
# File type:
#     Script
# Purpose:
#     Reassembles the preserved XAI composites without re-running explainability methods.
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
#     - RESNET_FN_XAI.pdf
#     - RESNET_FN_XAI.png
#     - SWIN_FN_XAI.pdf
#     - SWIN_FN_XAI.png
# Outputs:
#     - See docs/file_level_documentation.md
# Dependencies:
#     - PIL
#     - norma_figuras
#     - numpy
# Execution:
#     python figuras_fonte/gera_fig8_xai.py
# Portability notes:
#     Paths are relative to the root of this component or to the working directory.
# Reproducibility notes:
#     Environment: requirements.txt or environment.yml of this component. Seeds as defined in the code.
# Warnings:
#     The preserved XAI composite images used as input are not included in this record.
# Provenance:
#     Header added in v1.0.0; the code below is identical to the original file (see docs/modified_files.csv).
# ============================================================================
"""Figura 8 — remontagem dos composites historicos de XAI, sem reexecutar XAI.

Os arrays brutos de atribuicao nao foram preservados (as pastas gradcam/,
integrated_gradients/ e occlusion/ estao vazias). Logo, este script NAO regera
mapa nenhum: ele apenas recorta os 20 paineis ja existentes em cada composite,
pixel a pixel, e os remonta sem os titulos internos.

Nada e reamostrado: os recortes de 358x358 px entram no PDF na escala 1:1
(dpi = largura do mosaico em px / largura da tela em polegadas).

A paleta jet dos mapas e propriedade do artefato historico e permanece como
esta; converte-la a partir do raster seria uma transformacao nao auditavel.

Os identificadores de coluna aparecem apenas no primeiro painel; o segundo
reserva a mesma faixa em branco, para que as linhas dos dois paineis fiquem
rigorosamente alinhadas lado a lado (as duas grades sao identicas: colunas
388-745, 810-1167, 1234-1591, 1656-2013; linhas 77-434, 523-880, 968-1325,
1414-1771, 1860-2217).
"""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from norma_figuras import *
from PIL import Image
import numpy as np

COLUNAS = [(388, 745), (810, 1167), (1234, 1591), (1656, 2013)]
LINHAS  = [(77, 434), (523, 880), (968, 1325), (1414, 1771), (1860, 2217)]
IDENT   = [r"Original", r"Grad-CAM", "Integrated\nGradients", r"Occlusion"]
VAO     = 24                       # px entre paineis
LARG    = 7.82                     # polegadas; artigo exibe a 0,48\textwidth
FAIXA   = 0.58                     # polegadas reservadas aos identificadores

LP = COLUNAS[0][1] - COLUNAS[0][0] + 1
AP = LINHAS[0][1] - LINHAS[0][0] + 1
MW = 4*LP + 3*VAO
MH = 5*AP + 4*VAO


def remonta(origem, destino, com_identificadores):
    fonte = Image.open(origem).convert("RGBA")
    fundo = Image.new("RGBA", fonte.size, (255, 255, 255, 255))
    plano = Image.alpha_composite(fundo, fonte).convert("RGB")

    mosaico = Image.new("RGB", (MW, MH), "white")
    for li, (y0, y1) in enumerate(LINHAS):
        for ci, (x0, x1) in enumerate(COLUNAS):
            mosaico.paste(plano.crop((x0, y0, x1+1, y1+1)),
                          (ci*(LP+VAO), li*(AP+VAO)))

    alt_mos = LARG * MH / MW
    alt = alt_mos + FAIXA
    aplica_rc()
    fig = plt.figure(figsize=(LARG, alt))
    ax = fig.add_axes([0, 0, 1, alt_mos/alt]); ax.axis("off")
    ax.imshow(np.asarray(mosaico), interpolation="nearest")
    if com_identificadores:
        for ci, rot in enumerate(IDENT):
            cx = (ci*(LP+VAO) + LP/2) / MW
            fig.text(cx, alt_mos/alt + 0.06*FAIXA/alt, rot,
                     ha="center", va="bottom", fontsize=FONTE, linespacing=1.25)
    fig.savefig(destino, dpi=MW/LARG)
    plt.close(fig)
    print(f"  gerado: {destino}  (raster {MW}x{MH} px, 1:1)")


remonta("RESNET_FN_XAI.png", "RESNET_FN_XAI.pdf", True)
remonta("SWIN_FN_XAI.png",   "SWIN_FN_XAI.pdf",   False)
