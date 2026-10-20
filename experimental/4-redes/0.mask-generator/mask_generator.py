#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# Title:
#     Filled mask generator
# File type:
#     Script
# Purpose:
#     Generates filled binary masks from annotation images of the LCMG fields of view.
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
#     - See docs/file_level_documentation.md
# Outputs:
#     - See docs/file_level_documentation.md
# Dependencies:
#     - cv2
#     - numpy
# Execution:
#     python 4-redes/0.mask-generator/mask_generator.py
# Portability notes:
#     Paths are relative to the root of this component or to the working directory.
# Reproducibility notes:
#     Environment: requirements.txt or environment.yml of this component. Seeds as defined in the code.
# Warnings:
#     None beyond the limitations listed in the README.
# Provenance:
#     Header added in v1.0.0; the code below is identical to the original file (see docs/modified_files.csv).
# ============================================================================
import cv2
import numpy as np
import os
from pathlib import Path

# ========================
# CONFIGURAÇÕES
# ========================
INPUT_DIR  = r"C:\Users\sthem\OneDrive\Documentos\GitHub\master-2025\3-Datasets\img-lcm\IC-mask-amanda\masked\val"
OUTPUT_DIR = r"C:\Users\sthem\OneDrive\Documentos\GitHub\master-2025\3-Datasets\img-lcm\IC-mask-amanda\masked\val_masks"
MIN_AREA   = 50  # ignora manchas muito pequenas

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ========================
# FUNÇÃO PARA CRIAR MÁSCARA PREENCHIDA
# ========================
def create_filled_mask(img_path, output_dir):
    # Carregar imagem anotada
    img_bgr = cv2.imread(str(img_path), cv2.IMREAD_COLOR)
    if img_bgr is None:
        print(f"[ERRO] Não consegui ler {img_path}")
        return
    
    # Converter para RGB
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # Definir intervalo para vermelho (ajuste se necessário)
    lower_red = np.array([150, 0, 0])
    upper_red = np.array([255, 80, 80])

    # Criar máscara para vermelho
    mask = cv2.inRange(img_rgb, lower_red, upper_red)

    # Fechar pequenos buracos da borda (ajuda a evitar vazamentos)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=3)

    # Encontrar contornos
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Criar máscara preenchida
    filled_mask = np.zeros_like(mask)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area >= MIN_AREA:  # ignora manchas muito pequenas
            cv2.drawContours(filled_mask, [cnt], -1, 255, thickness=cv2.FILLED)

    # Salvar no diretório de saída
    stem = Path(img_path).stem
    save_path = Path(output_dir) / f"{stem}_mask.png"
    cv2.imwrite(str(save_path), filled_mask)

    print(f"[OK] Máscara criada: {save_path}")

# ========================
# LOOP EM TODAS AS IMAGENS
# ========================
def main():
    input_path = Path(INPUT_DIR)
    files = []
    for ext in ("*.bmp", "*.BMP"):
        files.extend(input_path.rglob(ext))  # busca recursiva

    print(f"[INFO] Encontradas {len(files)} imagens.")
    for img_path in files:
        create_filled_mask(img_path, OUTPUT_DIR)

    print(f"[FIM] Processadas: {len(files)} imagens. Saída: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
