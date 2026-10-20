#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# Title:
#     Flowchart style
# File type:
#     Module
# Purpose:
#     Defines the graphical identity shared by the flowchart figures.
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
#     - matplotlib
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
"""Identidade grafica unica dos fluxogramas do artigo."""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, FancyArrowPatch

FONTE = 7.4
plt.rcParams.update({"font.family":"serif","font.size":FONTE,"pdf.fonttype":42})
LW = 0.9
C_PROC = "#EAF2FA"; C_DEC = "#FDF0E3"; C_TERM = "#E7E7E7"; C_DADO = "#EDF6EE"
BORDA = "#333333"; SETA = "#333333"

def _txt(ax,x,y,s,fs=FONTE):
    ax.text(x,y,s,ha="center",va="center",fontsize=fs,zorder=5,linespacing=1.25)

def terminador(ax,x,y,w,h,s):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle="round,pad=0,rounding_size=%.3f"%(h/2),
        fc=C_TERM,ec=BORDA,lw=LW,zorder=3)); _txt(ax,x,y,s)

def processo(ax,x,y,w,h,s,cor=None):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle="square,pad=0",
        fc=cor or C_PROC,ec=BORDA,lw=LW,zorder=3)); _txt(ax,x,y,s)

def decisao(ax,x,y,w,h,s):
    ax.add_patch(Polygon([(x,y+h/2),(x+w/2,y),(x,y-h/2),(x-w/2,y)],closed=True,
        fc=C_DEC,ec=BORDA,lw=LW,zorder=3)); _txt(ax,x,y,s,FONTE-0.4)

def dado(ax,x,y,w,h,s):
    d=w*0.12
    ax.add_patch(Polygon([(x-w/2+d,y+h/2),(x+w/2,y+h/2),(x+w/2-d,y-h/2),(x-w/2,y-h/2)],
        closed=True,fc=C_DADO,ec=BORDA,lw=LW,zorder=3)); _txt(ax,x,y,s)

def seta(ax,p0,p1,rot=None,tracejada=False,rad=0.0):
    ax.add_patch(FancyArrowPatch(p0,p1,arrowstyle="-|>",mutation_scale=8,lw=LW,
        color=SETA,zorder=2,shrinkA=0,shrinkB=0,
        linestyle=(0,(3,2)) if tracejada else "solid",
        connectionstyle=f"arc3,rad={rad}"))
    if rot:
        mx,my=(p0[0]+p1[0])/2,(p0[1]+p1[1])/2
        ax.text(mx+rot[1],my+rot[2],rot[0],fontsize=FONTE-0.6,ha="center",va="center",
                bbox=dict(fc="white",ec="none",pad=0.6),zorder=6)

def faixa(ax,x,y,w,h,rotulo,cor):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0,rounding_size=0.06",
        fc=cor,ec="none",alpha=0.55,zorder=0))
    ax.text(x+0.10,y+h-0.12,rotulo,fontsize=FONTE-0.4,style="italic",
            ha="left",va="top",color="#555555",zorder=1)

def tela(w,h):
    fig,ax=plt.subplots(figsize=(w,h))
    ax.set_xlim(0,w); ax.set_ylim(0,h); ax.axis("off")
    return fig,ax
