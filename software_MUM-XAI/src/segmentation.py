#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# Title:
#     Cell segmentation
# File type:
#     Module
# Purpose:
#     Runs Cellpose segmentation on a field of view and extracts cell crops.
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
#     - cellpose
#     - numpy
#     - skimage
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
import numpy as np
from PIL import Image
from skimage import measure
from cellpose import models as cp_models, core as cp_core

CELLPOSE_MODEL = None


def get_cellpose_model():
    global CELLPOSE_MODEL
    if CELLPOSE_MODEL is None:
        gpu = cp_core.use_gpu()
        CELLPOSE_MODEL = cp_models.CellposeModel(
            gpu=gpu,
            model_type="cyto2",
        )
        print(f"Cellpose inicializado (gpu={gpu})")
    return CELLPOSE_MODEL


def run_cellpose_and_crop(image_pil, min_area=80, max_cells=150):
    model = get_cellpose_model()
    img_rgb = np.array(image_pil)

    channels = [0, 0]

    masks, flows, styles = model.eval(
        img_rgb,
        channels=channels,
        batch_size=8,
        flow_threshold=0.4,
        cellprob_threshold=0.0,
        normalize={"tile_norm_blocksize": 0},
    )

    regions = measure.regionprops(masks)
    crops = []

    for reg in regions:
        if reg.area < min_area:
            continue
        y0, x0, y1, x1 = reg.bbox
        crop = image_pil.crop((x0, y0, x1, y1))
        crop_224 = crop.resize((224, 224))

        crops.append(
            {
                "crop": crop_224,
                "bbox": (y0, x0, y1, x1),
                "label": reg.label,
            }
        )

        if len(crops) >= max_cells:
            break

    if masks.max() > 0:
        mask_viz = (masks.astype(np.float32) / masks.max() * 255)
    else:
        mask_viz = masks.astype(np.float32)
    mask_viz = mask_viz.astype(np.uint8)
    mask_viz_pil = Image.fromarray(mask_viz)

    return crops, mask_viz_pil
