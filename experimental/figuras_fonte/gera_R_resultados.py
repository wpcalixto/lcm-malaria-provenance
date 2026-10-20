#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# Title:
#     Results figures R1-R6
# File type:
#     Script
# Purpose:
#     Generates the Results figures (support composition, hold-out confusion matrices, optimization and recall panels).
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
#     - figR1a_overlap_fraction.pdf
#     - figR1b_instances_per_field.pdf
#     - figR2a_holdout_cm_resnet50.pdf
#     - figR2b_holdout_cm_swint.pdf
#     - figR3a_hpo_resnet50.pdf
#     - figR3b_hpo_swint.pdf
# Outputs:
#     - See docs/file_level_documentation.md
# Dependencies:
#     - dados_R
#     - matplotlib
#     - norma_figuras
#     - numpy
#     - pandas
# Execution:
#     python figuras_fonte/gera_R_resultados.py
# Portability notes:
#     Paths are relative to the root of this component or to the working directory.
# Reproducibility notes:
#     Environment: requirements.txt or environment.yml of this component. Seeds as defined in the code.
# Warnings:
#     None beyond the limitations listed in the README.
# Provenance:
#     Header added in v1.0.0; the code below is identical to the original file (see docs/modified_files.csv).
# ============================================================================
"""Figuras novas R1-R6 da secao de Resultados (v18_PT).

Dados: exclusivamente figuras_fonte/dados_R.py, que le os artefatos preservados e confere
cada valor com o publicado. Norma: figuras_fonte/norma_figuras.py.
Uso, a partir da raiz do projeto:  python3 figuras_fonte/gera_R_resultados.py [R1 R2 ...]
"""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from norma_figuras import *
import dados_R as D
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D
from matplotlib import colormaps

aplica_rc()
LARG = 7.23                     # \textwidth [in], medido na compilacao
CINZA = "#555555"
CR, CS = COR_MODELO["ResNet50"], COR_MODELO["Swin Transformer"]
MR, MS = MARCA_MODELO["ResNet50"], MARCA_MODELO["Swin Transformer"]
MARCA_OTIM = {"Adam": "^", "RMSprop": "s", "SGD": "v"}   # distintos de circulo e losango (modelos)


def tela_p(frac, h):
    """Painel que ocupara `frac` de \\linewidth e `h` polegadas na pagina."""
    return plt.subplots(figsize=(frac * LARG * K, h * K))


def limpa(ax):
    for s in ("top", "right"): ax.spines[s].set_visible(False)


def num(n):
    return f"{n:,}".replace(",", r"\,")


def matriz(M, arquivo, xl, yl, ticks=(r"Uninfected", r"Infected")):
    """Mesma convencao da Figura 7 (gera_fig6_matrizes.py): retangulos vetoriais, Blues."""
    fig, ax = plt.subplots(figsize=(3.06 * K, 2.75 * K))
    az = colormaps["Blues"]; lim = M.max() / 2
    for i in range(2):
        for j in range(2):
            ax.add_patch(Rectangle((j - .5, i - .5), 1, 1, fc=az(M[i, j] / M.max()), ec="white", lw=1.5))
            ax.text(j, i, num(int(M[i, j])), ha="center", va="center", fontsize=FONTE,
                    color="white" if M[i, j] > lim else "black")
    ax.set_xlim(-.5, 1.5); ax.set_ylim(1.5, -.5); ax.set_aspect("equal")
    ax.set_xticks([0, 1]); ax.set_xticklabels(ticks)
    ax.set_yticks([0, 1]); ax.set_yticklabels(ticks, rotation=90, va="center")
    ax.set_xlabel(xl); ax.set_ylabel(yl); ax.tick_params(length=0)
    for s in ax.spines.values(): s.set_visible(False)
    return fig, ax


# ------------------------------------------------------------------ R1
def R1(d):
    w = d.frac_recalc.values
    fig, ax = tela_p(0.485, 2.3)
    bins = np.linspace(0, 1, 51)
    ax.hist(w, bins=bins, color=CINZA, ec="white", lw=0.6)
    ax.axvspan(D.TAU_L, D.TAU_U, color=OKABE_ITO["laranja"], alpha=0.25, lw=0)
    for t in (D.TAU_L, D.TAU_U):
        ax.axvline(t, color=OKABE_ITO["laranja"], ls="--", lw=2.0)
    ax.set_yscale("log"); ax.set_ylim(0.7, 8000)
    ax.text(D.TAU_L - 0.015, 4500, r"$\tau_{\mathrm{L}}$", ha="right", va="top")
    ax.text(D.TAU_U + 0.015, 4500, r"$\tau_{\mathrm{U}}$", ha="left", va="top")
    ax.set_xlim(-0.02, 1.02)
    ax.set_xlabel(r"Overlap fraction $\omega$ [-]"); ax.set_ylabel(r"Instances [-]"); limpa(ax)
    salva(fig, "figR1a_overlap_fraction.pdf")

    n = d.groupby("image").size()
    fig, ax = tela_p(0.485, 2.3)
    v, c = np.unique(n.values, return_counts=True)
    ax.bar(v, c, width=0.8, color=CINZA)
    ax.axvline(np.median(n), color="black", ls="--", lw=2.0)
    ax.text(np.median(n) + 0.4, c.max() * 1.02, r"Median", ha="left", va="top")
    ax.set_xticks([10, 13, 16, 19, 22, 25, 28])
    ax.set_xlabel(r"Instances per field [-]"); ax.set_ylabel(r"Fields [-]"); limpa(ax)
    salva(fig, "figR1b_instances_per_field.pdf")


# ------------------------------------------------------------------ R2
R2_LADO = 414.96 / 72    # [in] dimensao fisica da R2 aprovada na v18 (414,96 x 414,96 pt), mantida
R2_FONTE = FONTE * 1.3    # ordem de 2026-09-29: todas as fontes da R2 +30% (19 -> 24,7 pt)


def matriz_fixa(M, xl, yl, lado=R2_LADO, fs=R2_FONTE, ticks=(r"Uninfected", r"Infected"), pad=2 / 72,
                alt=None, nota=None, arquivo=None):
    """Mesma convencao de matriz(), com pagina de dimensao fixa (lado x alt) e fonte fs em todos os
    textos, inclusive a nota opcional sob o eixo. A matriz ocupa o espaco que resta apos os rotulos;
    a pagina nao e recortada. Com `arquivo`, salva o PDF na dimensao exata."""
    alt = alt or lado
    fig = plt.figure(figsize=(lado, alt))
    txt_nota = fig.text(0.5, pad / alt, nota, ha="center", va="bottom", fontsize=fs) if nota else None
    ax = fig.add_axes([0.2, 0.2, 0.75, 0.75])
    az = colormaps["Blues"]; lim = M.max() / 2
    for i in range(2):
        for j in range(2):
            ax.add_patch(Rectangle((j - .5, i - .5), 1, 1, fc=az(M[i, j] / M.max()), ec="white", lw=1.5))
            ax.text(j, i, num(int(M[i, j])), ha="center", va="center", fontsize=fs,
                    color="white" if M[i, j] > lim else "black")
    ax.set_xlim(-.5, 1.5); ax.set_ylim(1.5, -.5)
    ax.set_xticks([0, 1]); ax.set_xticklabels(ticks, fontsize=fs)
    ax.set_yticks([0, 1]); ax.set_yticklabels(ticks, rotation=90, va="center", fontsize=fs)
    ax.set_xlabel(xl, fontsize=fs); ax.set_ylabel(yl, fontsize=fs); ax.tick_params(length=0)
    for s in ax.spines.values(): s.set_visible(False)
    for _ in range(3):   # ajusta a posicao ate os rotulos (e a nota) caberem exatamente na pagina
        fig.canvas.draw(); r = fig.canvas.get_renderer()
        inv = fig.dpi_scale_trans.inverted()
        bb = ax.get_tightbbox(r).transformed(inv)
        p = ax.get_position()
        esq = p.x0 * lado - bb.x0; inf = p.y0 * alt - bb.y0
        m = max(esq, inf) + pad
        base = 0.0
        if txt_nota is not None:   # faixa da nota + um espaco de meia linha
            base = txt_nota.get_window_extent(r).transformed(inv).height + pad + 0.5 * fs / 72
        s = min(lado - m - pad, alt - base - m - pad)
        y0 = alt - pad - s          # matriz alinhada ao topo; sobra vertical fica acima da nota
        ax.set_position([m / lado, y0 / alt, s / lado, s / alt])
    if arquivo:
        fig.savefig(arquivo, dpi=300)       # sem bbox_inches="tight": dimensao fisica exata
        plt.close(fig); print(f"  gerado: {arquivo}")
    return fig, ax


def R2():
    for path, arq in [(D.KR, "figR2a_holdout_cm_resnet50.pdf"), (D.KS, "figR2b_holdout_cm_swint.pdf")]:
        h = D.holdout(path)
        M = np.array([[h["true_negatives"], h["false_positives"]],
                      [h["false_negatives"], h["true_positives"]]])
        fig, _ = matriz_fixa(M, r"Predicted label", r"Reference label")
        fig.savefig(arq, dpi=300)          # sem bbox_inches="tight": dimensao fisica exata
        plt.close(fig); print(f"  gerado: {arq}")


# ------------------------------------------------------------------ R3
def R3():
    tr, ts = D.trials(D.LOG_R), D.trials(D.LOG_S)
    ylim = (min(tr.value.min(), ts.value.min()) - 0.02, 1.005)
    xlim = (8e-7, 1.2e-3)
    for t, cor, arq, leg in [(tr, CR, "figR3a_hpo_resnet50.pdf", True),
                             (ts, CS, "figR3b_hpo_swint.pdf", False)]:
        fig, ax = tela_p(0.32, 2.2)
        for o, m in MARCA_OTIM.items():
            s = t[t.optimizer == o]
            ax.scatter(s.lr, s.value, marker=m, s=90, fc=cor, ec="white", lw=0.8, alpha=0.9, label=o, zorder=3)
        b = t.loc[t.value.idxmax()]
        ax.scatter([b.lr], [b.value], s=420, fc="none", ec="black", lw=2.0, zorder=4)
        ax.set_xscale("log"); ax.set_xlim(*xlim); ax.set_ylim(*ylim)
        yt = np.arange(0.70, 1.001, 0.05)   # marcas fixas: independem do tamanho da fonte
        ax.set_yticks(yt); ax.set_yticklabels(["%.2f" % v for v in yt])
        ax.set_xlabel(r"Learning rate [-]"); ax.set_ylabel(r"Objective value [-]"); limpa(ax)
        if leg:
            hs = [Line2D([], [], ls="none", marker=m, ms=11, mfc=CINZA, mec="white") for m in MARCA_OTIM.values()]
            ax.legend(hs, list(MARCA_OTIM), loc="lower left", frameon=False, handletextpad=0.2, borderaxespad=0.2)
        salva(fig, arq)

    fn0, fn1, fp0, fp1, m0, m1 = D.fold2_swin()
    fig, ax = tela_p(0.32, 2.2)
    x = np.array([0, 1]); w = 0.36
    b0 = ax.bar(x - w / 2, [fn0, fp0], w, fc="white", ec=CS, lw=2.2, hatch="///", label=r"Reference")
    b1 = ax.bar(x + w / 2, [fn1, fp1], w, fc=CS, ec=CS, lw=2.2, label=r"Retraining")
    for bars in (b0, b1):
        for r in bars:
            ax.text(r.get_x() + r.get_width() / 2, r.get_height() + 1.2, str(int(r.get_height())), ha="center", va="bottom")
    ax.set_xticks(x); ax.set_xticklabels([r"False negatives", r"False positives"])
    ax.set_ylabel(r"Instances [-]"); ax.set_ylim(0, 110); limpa(ax)
    ax.legend(loc="upper right", frameon=False, borderaxespad=0.1)
    ax.text(0.98, 0.74, r"Mean recall: %.4f $\rightarrow$ %.4f" % (m0, m1), transform=ax.transAxes, ha="right", va="top")
    salva(fig, "figR3c_fold2_retraining.pdf")


# ------------------------------------------------------------------ R4
def R4(d):
    fc = d.groupby("image").agg(st=("st", "first"), tf=("tf", "first"), n=("relabel", "size"), pos=("relabel", "sum"))
    vz = fc[fc.st != "ok"]; ot = fc[(fc.st == "ok") & (fc.tf != "id")]; ut = fc[(fc.st == "ok") & (fc.tf == "id")]
    g = lambda s: (len(s), int(s.n.sum()), int(s.pos.sum()), int(s.n.sum() - s.pos.sum()))
    V, O, U = g(vz), g(ot), g(ut)
    T = (len(fc), int(fc.n.sum()), int(fc.pos.sum()), int(fc.n.sum() - fc.pos.sum()))
    fig, ax = tela(LARG, 2.75)
    y = {"v": 2.2, "o": 1.45, "u": 0.7}
    processo(ax, 0.68, y["o"], 1.16, 0.9, "%s fields\n%s instances" % (num(T[0]), num(T[1])),
             cor=TINTA_DOMINIO["Target domain"])
    grupos = [("v", "Empty annotation volume\n%d fields, %d instances" % V[:2]),
              ("o", "Non-identity transform\n%d fields, %d instances" % O[:2]),
              ("u", "Annotation with overlap\n%d fields, %s instances" % (U[0], num(U[1])))]
    linha(ax, [1.26, 1.42], [y["o"], y["o"]]); linha(ax, [1.42, 1.42], [y["u"], y["v"]])
    for k, s in grupos:
        processo(ax, 2.72, y[k], 2.2, 0.56, s)
        seta(ax, (1.42, y[k]), (1.62, y[k]))
    rot = {"v": "%d operational negative" % V[3],
           "o": "%d operational positive\n%d operational negative" % (O[2], O[3]),
           "u": "%s operational positive" % num(U[2])}
    for k in "vou":
        processo(ax, 4.97, y[k], 1.9, 0.56, rot[k], cor="#FFFFFF")
        seta(ax, (3.82, y[k]), (4.02, y[k]))
    terminador(ax, 6.6, y["u"], 1.1, 0.8, "Main\nsupport\n%d fields\n%s positive" % (U[0], num(U[2])))
    seta(ax, (5.92, y["u"]), (6.05, y["u"]))
    faixa(ax, 1.62, -0.02, 5.53, 0.34, "#F2F2F2")
    ax.text(4.385, 0.15, "Total operational labels: %s positive, %d negative" % (num(T[2]), T[3]),
            ha="center", va="center", fontsize=FONTE)
    ax.set_xlim(0, LARG); ax.set_ylim(-0.05, 2.55)
    salva(fig, "figR4_target_support_composition.pdf")


# ------------------------------------------------------------------ R5
def R5(d):
    tfa = d.groupby("image").tf_aut.first().value_counts()
    ordem = ["id", "transpose", "flipud"]
    fig, ax = tela_p(0.32, 2.2)
    b = ax.bar(range(3), [tfa.get(k, 0) for k in ordem], color=CINZA, width=0.62)
    for r in b:
        ax.text(r.get_x() + r.get_width() / 2, r.get_height() + 3, str(int(r.get_height())), ha="center", va="bottom")
    ax.set_xticks(range(3)); ax.set_xticklabels([r"\texttt{%s}" % k for k in ordem])
    ax.set_ylabel(r"Fields [-]"); ax.set_ylim(0, 240); limpa(ax)
    salva(fig, "figR5a_automatic_transforms.pdf")

    import pandas as pd
    M = pd.crosstab(d.relabel, d.label_aut).reindex(index=[0, 1], columns=[0, 1], fill_value=0).values
    fig, ax = matriz(M, None, r"Automatic path", r"Imposed path")
    ax.text(0.5, 1.93, r"%d/%s labels changed (%.3f\%%)" % (M[0, 1] + M[1, 0], num(int(M.sum())),
            100 * (M[0, 1] + M[1, 0]) / M.sum()), ha="center", va="top", fontsize=FONTE, clip_on=False)
    salva(fig, "figR5b_label_transition.pdf")

    v = D.suporte(d); va = d[(d.st == "ok") & (d.label_aut == 1)]
    linhas = []
    for nome, col, cor, mk in [("ResNet50", "pred_R", CR, MR), ("Swin Transformer", "pred_S", CS, MS)]:
        linhas.append((nome, "Imposed", cor, mk, True, D.boot_recall(v, "relabel", col)))
        linhas.append((nome, "Automatic", cor, mk, False, D.boot_recall(va, "label_aut", col)))
    fig, ax = tela_p(0.32, 2.2)
    ys = [3.3, 2.7, 1.3, 0.7]
    for yy, (nome, cam, cor, mk, cheio, (r, lo, hi)) in zip(ys, linhas):
        ax.plot([lo, hi], [yy, yy], color=cor, lw=2.4)
        ax.plot([r], [yy], marker=mk, ms=11, mfc=cor if cheio else "white", mec=cor, mew=2.2, ls="none")
    ax.set_yticks(ys); ax.set_yticklabels([l[1] for l in linhas])
    ax.set_ylim(0.2, 3.8); ax.set_xlim(0.024, 0.042); ax.set_xticks([0.025, 0.030, 0.035, 0.040])
    ax.set_xticklabels(["0.025", "0.030", "0.035", "0.040"])
    ax.set_xlabel(r"Recall [-]"); limpa(ax)
    hs = [Line2D([], [], color=CR, marker=MR, ms=10, lw=2.4), Line2D([], [], color=CS, marker=MS, ms=10, lw=2.4)]
    ax.legend(hs, [r"ResNet50", r"Swin Transformer"], loc="upper center", bbox_to_anchor=(0.5, 1.22),
              ncol=2, frameon=False, handlelength=1.4, columnspacing=0.8, handletextpad=0.3)
    salva(fig, "figR5c_recall_by_path.pdf")


R5B_DIM = (414.96 / 72, 470.422 / 72)   # [in] dimensao fisica da R5(b) aprovada na v18, mantida
R5B_FONTE = FONTE * 1.3                 # ordem de 2026-09-29: todas as fontes +30% (19 -> 24,7 pt)


def R5b(d):
    """Somente o painel (b) da R5, com pagina fixa e fontes +30%; (a) e (c) nao sao tocados."""
    import pandas as pd
    M = pd.crosstab(d.relabel, d.label_aut).reindex(index=[0, 1], columns=[0, 1], fill_value=0).values
    nota = r"%d/%s labels changed (%.3f\%%)" % (M[0, 1] + M[1, 0], num(int(M.sum())),
                                               100 * (M[0, 1] + M[1, 0]) / M.sum())
    matriz_fixa(M, r"Automatic path", r"Imposed path", lado=R5B_DIM[0], alt=R5B_DIM[1],
                fs=R5B_FONTE, nota=nota, arquivo="figR5b_label_transition.pdf")


# ------------------------------------------------------------------ R6
def R6(d):
    g = D.por_campo(D.suporte(d))
    fig, ax = tela_p(0.485, 2.1)
    for col, cor, nome, mk in [("R_R", CR, "ResNet50", MR), ("R_S", CS, "Swin Transformer", MS)]:
        x = np.sort(g[col].values); y = np.arange(1, len(x) + 1) / len(x)
        ax.step(np.r_[0, x], np.r_[0, y], where="post", color=cor, lw=2.4, label=nome)
        ax.plot([0], [(g[col] == 0).mean()], marker=mk, ms=10, color=cor, ls="none")
    ax.set_xlim(-0.005, 0.22); ax.set_ylim(0, 1.02)
    ax.set_xlabel(r"Field-level recall [-]"); ax.set_ylabel(r"Cumulative proportion [-]")
    ax.legend(loc="lower right", frameon=False); limpa(ax)
    salva(fig, "figR6a_field_recall_ecdf.pdf")

    fig, ax = tela_p(0.485, 2.1)
    c = [int((g.D < 0).sum()), int((g.D == 0).sum()), int((g.D > 0).sum())]
    b = ax.bar(range(3), c, color=CINZA, width=0.6)
    for r in b:
        ax.text(r.get_x() + r.get_width() / 2, r.get_height() + 2, str(int(r.get_height())), ha="center", va="bottom")
    ax.set_xticks(range(3)); ax.set_xticklabels([r"$D_i<0$", r"$D_i=0$", r"$D_i>0$"])
    ax.set_ylabel(r"Fields [-]"); ax.set_ylim(0, 128); limpa(ax)
    salva(fig, "figR6b_paired_difference_sign.pdf")

    v = D.suporte(d); dr = v.pred_R.mean() - v.pred_S.mean(); lo, hi = D.boot_delta(g)
    fig, ax = tela_p(0.485, 2.1)
    ax.axvline(0, color="black", lw=1.6, ls="--")
    ax.plot([lo, hi], [-0.25, -0.25], color="black", lw=2.8); ax.plot([dr], [-0.25], "ks", ms=11)
    ax.text(0.02, 0.97, r"$\Delta_R=%.4f$" "\n" r"95\%% CI $[%.4f;\,%.4f]$" % (dr, lo, hi),
            transform=ax.transAxes, ha="left", va="top", linespacing=1.3)
    ax.text(0.98, 0.04, r"Permutation $p=0.816$", transform=ax.transAxes, ha="right", va="bottom", color=CINZA)
    ax.set_ylim(-1, 1); ax.set_yticks([]); ax.set_xlim(-0.012, 0.012)
    ax.set_xticks([-0.010, -0.005, 0, 0.005, 0.010])
    ax.set_xticklabels(["$-0.010$", "$-0.005$", "0", "0.005", "0.010"])
    ax.set_xlabel(r"$\Delta_R=R^{(R)}-R^{(S)}$ [-]")
    for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
    salva(fig, "figR6c_recall_difference.pdf")

    ZR, ZS = g.TP_R > 0, g.TP_S > 0
    fig, ax = tela_p(0.485, 2.1)
    p = [100 * ZR.mean(), 100 * ZS.mean()]
    b = ax.bar([0, 1], p, color=[CR, CS], width=0.55)
    for r in b:
        ax.text(r.get_x() + r.get_width() / 2, r.get_height() + 1.2, "%.1f" % r.get_height(), ha="center", va="bottom")
    ax.set_xticks([0, 1]); ax.set_xticklabels([r"ResNet50", r"Swin Transformer"])
    ax.set_ylabel(r"Fields with detection [\%]"); ax.set_ylim(0, 75); limpa(ax)
    ax.text(0.98, 0.97, r"Discordant fields: %d / %d" "\n" r"McNemar $p=0.728$" % (int((ZR & ~ZS).sum()), int((~ZR & ZS).sum())),
            transform=ax.transAxes, ha="right", va="top", linespacing=1.3)
    salva(fig, "figR6d_field_detection.pdf")


if __name__ == "__main__":
    alvo = sys.argv[1:] or ["R1", "R2", "R3", "R4", "R5", "R6"]
    d = D.instancias()
    for r in alvo:
        print(r)
        {"R5b": lambda: R5b(d), "R1": lambda: R1(d), "R2": R2, "R3": R3, "R4": lambda: R4(d), "R5": lambda: R5(d), "R6": lambda: R6(d)}[r]()
