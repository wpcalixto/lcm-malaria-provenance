#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# Title:
#     Target-domain figure
# File type:
#     Script
# Purpose:
#     Generates the target-domain (LCMG) field-of-view and annotation panels.
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
#     - imagens-alemanha/ann_dir/train/2022_03_21_11_02_59_40.png
#     - imagens-alemanha/img_dir/train/2022_03_21_11_02_59_40.bmp
#     - img_lcm.pdf
#     - img_lcm.png
#     - mascara_boundinbox.pdf
# Outputs:
#     - See docs/file_level_documentation.md
# Dependencies:
#     - PIL
#     - numpy
# Execution:
#     python figuras_fonte/gera_fig4_dominio_alvo.py
# Portability notes:
#     Paths are relative to the root of this component or to the working directory.
# Reproducibility notes:
#     Environment: requirements.txt or environment.yml of this component. Seeds as defined in the code.
# Warnings:
#     None beyond the limitations listed in the README.
# Provenance:
#     Header added in v1.0.0; the code below is identical to the original file (see docs/modified_files.csv).
# ============================================================================
"""Figura 4 — dominio-alvo (LCMG), paineis (a) e (b).

Correspondencia provada, nao inferida:
  img_lcm.png             = imagens-alemanha/img_dir/train/2022_03_21_11_02_59_40.bmp
                            reduzido para 1224x647 (bilinear, MAE = 0,94 nivel de cinza)
  mascara_boundinbox.png  = imagens-alemanha/ann_dir/train/2022_03_21_11_02_59_40.png
                            (identidade pixel a pixel verificada)

Painel (a): o mesmo raster historico, apenas encapsulado em PDF, sem reamostragem.
Painel (b): as duas caixas da anotacao desenhadas como contorno sobre o MESMO campo
            de visao de (a), nas cores originais da fonte -- (250,50,83) e (250,250,55).
Nenhum texto dentro da arte.
"""
import os
from PIL import Image, ImageDraw
import numpy as np

BMP = "imagens-alemanha/img_dir/train/2022_03_21_11_02_59_40.bmp"
ANN = "imagens-alemanha/ann_dir/train/2022_03_21_11_02_59_40.png"
ESPESSURA = 8                      # px, sobre a grade 2048x1088

# (a) — encapsulamento direto, sem reamostragem
a = Image.open("img_lcm.png").convert("RGB")
a.save("img_lcm.pdf", resolution=360.0)
print(f"  gerado: img_lcm.pdf  (raster {a.size[0]}x{a.size[1]} px)")

# (b) — contornos da anotacao sobre o campo de visao
campo = Image.open(BMP).convert("RGB")
ann = np.asarray(Image.open(ANN).convert("RGB"))
desenho = ImageDraw.Draw(campo)
for cor in [(250, 50, 83), (250, 250, 55)]:
    m = (ann == np.array(cor)).all(-1)
    ys, xs = np.nonzero(m)
    desenho.rectangle([(int(xs.min()), int(ys.min())), (int(xs.max()), int(ys.max()))],
                      outline=cor, width=ESPESSURA)
    print(f"    caixa {cor}: x[{xs.min()},{xs.max()}] y[{ys.min()},{ys.max()}]")
campo.save("mascara_boundinbox.pdf", resolution=602.0)
print(f"  gerado: mascara_boundinbox.pdf  (raster {campo.size[0]}x{campo.size[1]} px)")
