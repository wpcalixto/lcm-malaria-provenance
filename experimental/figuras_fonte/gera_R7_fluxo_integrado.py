#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# Title:
#     Integrated workflow figure
# File type:
#     Script
# Purpose:
#     Generates the panels with the preserved visual outputs of the integrated MUM-XAI execution.
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
#     - app1.jpeg
#     - app4.jpeg
# Outputs:
#     - See docs/file_level_documentation.md
# Dependencies:
#     - PIL
#     - numpy
# Execution:
#     python figuras_fonte/gera_R7_fluxo_integrado.py
# Portability notes:
#     Paths are relative to the root of this component or to the working directory.
# Reproducibility notes:
#     Environment: requirements.txt or environment.yml of this component. Seeds as defined in the code.
# Warnings:
#     The application screenshots used as input are not included in this record.
# Provenance:
#     Header added in v1.0.0; the code below is identical to the original file (see docs/modified_files.csv).
# ============================================================================
"""Figura R7 — saidas visuais preservadas da execucao integrada (MUM-XAI).

Fonte unica: as capturas de tela preservadas da aplicacao (app1.jpeg, dominio-alvo,
campo 2022_03_21_11_02_58_64.bmp; app4.jpeg, dominio auxiliar, campo id_00m1onu6hj.jpg).
Nao reexecuta a aplicacao. Cada painel e recortado pixel a pixel, sem reamostragem, e
encapsulado em PDF a 300 dpi: inserido na largura natural, a resolucao efetiva e 300 dpi.
"""
import numpy as np
from PIL import Image

DPI = 300
# caixas aproximadas (x0, y0, x1, y1) de cada painel na captura; a borda exata e detectada abaixo
FONTES = {
    "target": ("app1.jpeg", {"original": (490, 144, 862, 345), "mask": (864, 144, 1236, 345),
                             "attribution": (490, 379, 862, 581), "reconstruction": (864, 379, 1236, 581)}),
    "auxiliary": ("app4.jpeg", {"original": (494, 125, 869, 407), "mask": (871, 125, 1246, 407),
                                "attribution": (494, 442, 869, 725), "reconstruction": (871, 442, 1246, 725)}),
}


def apara(a, lim=245):
    """Remove as margens brancas da interface; mantem apenas o painel de imagem."""
    fundo = (a > lim).all(axis=2)
    ys = np.where(~(fundo.mean(axis=1) > 0.97))[0]
    xs = np.where(~(fundo.mean(axis=0) > 0.97))[0]
    return a[ys[0]:ys[-1] + 1, xs[0]:xs[-1] + 1]


if __name__ == "__main__":
    for dom, (arq, caixas) in FONTES.items():
        im = np.asarray(Image.open(arq).convert("RGB"))
        ps = {n: apara(im[y0:y1, x0:x1]) for n, (x0, y0, x1, y1) in caixas.items()}
        # corte central comum por linha: paineis da mesma linha com dimensao identica
        h = min(p.shape[0] for p in ps.values()); w = min(p.shape[1] for p in ps.values())
        for nome, p in ps.items():
            oy, ox = (p.shape[0] - h) // 2, (p.shape[1] - w) // 2
            p = p[oy:oy + h, ox:ox + w]
            saida = f"figR7_{dom}_{nome}.pdf"
            Image.fromarray(p).save(saida, "PDF", resolution=DPI)
            print(f"  gerado: {saida}  {w}x{h} px  -> {w/DPI:.3f} x {h/DPI:.3f} in a {DPI} dpi")
