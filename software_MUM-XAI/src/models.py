#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# Title:
#     Model loading
# File type:
#     Module
# Purpose:
#     Loads the ResNet50 and Swin Transformer checkpoints and custom .pth models.
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
#     - captum
#     - torch
#     - torchvision
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
import io
import torch
import torch.nn as nn
from torchvision.models import resnet50
from torchvision.models.swin_transformer import swin_t
from captum.attr import LayerGradCam
from .config import DEVICE

def load_resnet_model(ckpt_path: str):
    model = resnet50(weights=None)
    model.fc = nn.Linear(model.fc.in_features, 2)

    state = torch.load(ckpt_path, map_location=DEVICE)
    model.load_state_dict(state)

    for m in model.modules():
        if isinstance(m, nn.ReLU):
            m.inplace = False

    model.to(DEVICE)
    model.eval()

    gradcam_layer = model.layer4[-1]
    gradcam_obj = LayerGradCam(model, gradcam_layer)

    return model, gradcam_obj


def load_swin_model(ckpt_path: str):
    swin = swin_t(weights=None)
    num_features = swin.head.in_features
    swin.head = nn.Linear(num_features, 2)

    state = torch.load(ckpt_path, map_location=DEVICE)
    swin.load_state_dict(state)

    swin.to(DEVICE)
    swin.eval()

    swin_layer = swin.features[0][0]
    gradcam_obj = LayerGradCam(swin, swin_layer)

    return swin, gradcam_obj


def load_custom_model_from_pth(pth_file, base_model: str):
    state = torch.load(io.BytesIO(pth_file.read()), map_location=DEVICE)

    if base_model == "ResNet50":
        model = resnet50(weights=None)
        model.fc = nn.Linear(model.fc.in_features, 2)
        model.load_state_dict(state)

        for m in model.modules():
            if isinstance(m, nn.ReLU):
                m.inplace = False

        model.to(DEVICE)
        model.eval()
        gradcam_layer = model.layer4[-1]
        gradcam_obj = LayerGradCam(model, gradcam_layer)

    elif base_model == "Swin-T":
        model = swin_t(weights=None)
        num_features = model.head.in_features
        model.head = nn.Linear(num_features, 2)
        model.load_state_dict(state)
        model.to(DEVICE)
        model.eval()
        swin_layer = model.features[0][0]
        gradcam_obj = LayerGradCam(model, swin_layer)

    else:
        raise ValueError("Modelo base não suportado para custom .pth")

    return model, gradcam_obj