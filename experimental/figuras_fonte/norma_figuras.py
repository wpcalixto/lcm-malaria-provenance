#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# Title:
#     Figure construction rules
# File type:
#     Module
# Purpose:
#     Implements the figure construction rules (fonts, sizes, palette and export) used by the figure scripts.
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
"""Norma de construcao de figuras do projeto (12 regras do guide for authors).

1  PDF vetorial, 300 dpi para componentes raster, fontes embutidas.
2  Sem titulo dentro da figura: o titulo vive no \\caption.
3  Idioma ingles, capitalizacao do artigo (sentence case).
4  Multi-painel: uma imagem por painel, montagem no .tex via subfigure.
5  Multi-painel: legenda apenas no primeiro painel, in-plot.
6  Sem texto explicativo dentro da figura.
7  Cor fixa por entidade, do inicio ao fim do artigo.
8  Marcador fixo por modelo: ResNet50 circulo, Swin Transformer losango.
9  Um unico tamanho de fonte para letras, numeros e simbolos.
10 Fonte entre 18 e 22 pt no arquivo-fonte.
11 Simbolos renderizados pelo proprio LaTeX; unidades entre colchetes.
12 Paleta Okabe-Ito, hex fixos.
"""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, FancyArrowPatch

# --- regra 10: fonte unica, dentro de [18, 22] ---
FONTE = 19   # tipografia interna nominal de 19 pt (revisao mais recente do protocolo)

# --- regra 12: Okabe-Ito, hex fixos ---
OKABE_ITO = {
    "preto":    "#000000",
    "laranja":  "#E69F00",
    "azulceu":  "#56B4E9",
    "verde":    "#009E73",
    "amarelo":  "#F0E442",
    "azul":     "#0072B2",
    "vermelhao":"#D55E00",
    "roxo":     "#CC79A7",
}
# --- regra 7: cor fixa por entidade ---
COR_FOLD  = [OKABE_ITO["azul"], OKABE_ITO["vermelhao"], OKABE_ITO["verde"],
             OKABE_ITO["roxo"], OKABE_ITO["laranja"]]        # Fold 1..5, todo o artigo
COR_MODELO = {"ResNet50": OKABE_ITO["azul"], "Swin Transformer": OKABE_ITO["vermelhao"]}
# --- regra 8: marcador fixo por modelo, aplicavel apenas onde a figura ja usa marcadores ---
MARCA_MODELO = {"ResNet50": "o", "Swin Transformer": "D"}

# --- regra 7: cor fixa por dominio, do inicio ao fim do artigo ---
COR_DOMINIO = {"Source domain":    OKABE_ITO["azul"],
               "Target domain":    OKABE_ITO["laranja"],
               "Auxiliary domain": OKABE_ITO["verde"]}
TINTA_DOMINIO = {"Source domain": "#E6F0F8", "Target domain": "#FDF1E0",
                 "Auxiliary domain": "#E6F4EF"}

# --- regras 9 e 11: um tamanho so; simbolos pelo proprio LaTeX, familia do artigo ---
def aplica_rc():
    plt.rcParams.update({
        "text.usetex": True,
        "text.latex.preamble": r"\usepackage{txfonts}",   # regra 11: mesma fonte de texto e de matematica do elsarticle[times]
        "font.family": "serif",
        "font.size": FONTE, "axes.labelsize": FONTE, "axes.titlesize": FONTE,
        "xtick.labelsize": FONTE, "ytick.labelsize": FONTE, "legend.fontsize": FONTE,
        "axes.linewidth": 1.6, "lines.linewidth": 2.4,
        "xtick.major.width": 1.6, "ytick.major.width": 1.6,
        "pdf.fonttype": 42, "savefig.dpi": 300, "figure.dpi": 300,
    })

def salva(fig, arquivo):
    """Regra 1: PDF vetorial, 300 dpi, fontes embutidas."""
    fig.savefig(arquivo, bbox_inches="tight", pad_inches=0.02, dpi=300)
    plt.close(fig); print(f"  gerado: {arquivo}")

# ===================== fluxogramas: convencao unica =====================
LW = 2.2
C_PROC = "#EAF2FA"; C_DEC = "#FDF0E3"; C_TERM = "#E7E7E7"; C_DADO = "#EDF6EE"
C_TRANSV = "#F3E8F5"; BORDA = "#333333"; SETA = "#333333"

def _txt(ax, x, y, s):
    ax.text(x, y, s, ha="center", va="center", fontsize=FONTE, zorder=5, linespacing=1.3)

def terminador(ax, x, y, w, h, s):
    ax.add_patch(FancyBboxPatch((x-w/2, y-h/2), w, h,
        boxstyle="round,pad=0,rounding_size=%.3f" % (h/2),
        fc=C_TERM, ec=BORDA, lw=LW, zorder=3)); _txt(ax, x, y, s)

def processo(ax, x, y, w, h, s, cor=None):
    ax.add_patch(FancyBboxPatch((x-w/2, y-h/2), w, h, boxstyle="square,pad=0",
        fc=cor or C_PROC, ec=BORDA, lw=LW, zorder=3)); _txt(ax, x, y, s)

def decisao(ax, x, y, w, h, s):
    ax.add_patch(Polygon([(x, y+h/2), (x+w/2, y), (x, y-h/2), (x-w/2, y)], closed=True,
        fc=C_DEC, ec=BORDA, lw=LW, zorder=3)); _txt(ax, x, y, s)

def dado(ax, x, y, w, h, s):
    d = w*0.12
    ax.add_patch(Polygon([(x-w/2+d, y+h/2), (x+w/2, y+h/2), (x+w/2-d, y-h/2), (x-w/2, y-h/2)],
        closed=True, fc=C_DADO, ec=BORDA, lw=LW, zorder=3)); _txt(ax, x, y, s)

def seta(ax, p0, p1, rot=None, tracejada=False):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=20, lw=LW,
        color=SETA, zorder=2, shrinkA=0, shrinkB=0,
        linestyle=(0, (3, 2)) if tracejada else "solid"))
    if rot:
        mx, my = (p0[0]+p1[0])/2, (p0[1]+p1[1])/2
        ax.text(mx+rot[1], my+rot[2], rot[0], fontsize=FONTE, ha="center", va="center",
                bbox=dict(fc="white", ec="none", pad=1.0), zorder=6)

def linha(ax, xs, ys):
    ax.plot(xs, ys, color=SETA, lw=LW, zorder=2)

def faixa(ax, x, y, w, h, cor, borda=None):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.06",
        fc=cor, ec=borda or "none", lw=1.4 if borda else 0, zorder=0))

def rotulo_faixa(ax, x, y, s, cor="#555555"):
    ax.text(x, y, s, rotation=90, ha="center", va="center",
            fontsize=FONTE, style="italic", color=cor, zorder=1)

K = 18 / 7.4      # escala de tela fixa (definida com a fonte de 18 pt); a subida para 19 pt, ordem de
                  # 2026-09-29, altera so a tipografia nominal, sem mudar a largura fisica das telas

def tela(w, h):
    aplica_rc()
    fig, ax = plt.subplots(figsize=(w*K, h*K))
    ax.set_xlim(0, w); ax.set_ylim(0, h); ax.axis("off")
    return fig, ax
