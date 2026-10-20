#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# Title:
#     Heatmap reconstruction
# File type:
#     Module
# Purpose:
#     Reconstructs the field-of-view heatmap from cell-level attribution maps.
# Repository:
#     lcm-malaria-provenance, component software_MUM-XAI
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
#     Apache-2.0
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
#     - PIL
#     - cv2
#     - numpy
# Execution:
#     Imported by other files of this component; not executed directly.
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
from PIL import Image

def reconstruct_full_heatmap(original_pil, cells_with_heatmaps):
    orig = np.array(original_pil).astype(np.float32) / 255.0
    h, w, _ = orig.shape

    heat_canvas = np.zeros((h, w), dtype=np.float32)

    for cell in cells_with_heatmaps:
        y0, x0, y1, x1 = cell["bbox"]
        h_box = y1 - y0
        w_box = x1 - x0
        heat = cell["heatmap"]

        heat_resized = cv2.resize(heat, (w_box, h_box))
        heat_canvas[y0:y1, x0:x1] = np.maximum(
            heat_canvas[y0:y1, x0:x1],
            heat_resized,
        )

    if heat_canvas.max() > 0:
        heat_canvas = heat_canvas / heat_canvas.max()

    heat_color = cv2.applyColorMap(
        (heat_canvas * 255).astype(np.uint8), cv2.COLORMAP_JET
    )
    heat_color = cv2.cvtColor(heat_color, cv2.COLOR_BGR2RGB) / 255.0

    alpha = 0.5
    overlay = (1 - alpha) * orig + alpha * heat_color
    overlay = np.clip(overlay, 0, 1)

    overlay_pil = Image.fromarray((overlay * 255).astype(np.uint8))
    return overlay_pil
