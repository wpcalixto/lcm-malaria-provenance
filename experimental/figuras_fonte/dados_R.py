#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# Title:
#     Data for the Results figures
# File type:
#     Module
# Purpose:
#     Reads and checks, from preserved artifacts only, the values used in the Results figures.
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
#     - 4-redes/2.resnet/normal/kfold_epoch_results.csv
#     - 4-redes/2.resnet/resnet_optuna/logs-optuna-01042025-resnet.txt
#     - 4-redes/3.swin/swin-com-optuna/logs-optuna-01042025.txt
#     - 4-redes/3.swin/swin-sem-optuna/kfold_epoch_results.csv
#     - img_dir_annot_nii/alignment_val.csv
#     - img_dir_annot_nii/cells_val.csv
# Outputs:
#     - See docs/file_level_documentation.md
# Dependencies:
#     - numpy
#     - pandas
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
"""Dados das figuras novas R1-R6 da v18_PT, lidos SOMENTE de artefatos preservados.

Nao executa treinamento, inferencia, segmentacao, rotulagem nem XAI.
Rodar a partir da raiz do projeto:  python3 figuras_fonte/dados_R.py
Imprime cada valor ao lado do valor publicado na v17_PT e termina com erro se algum divergir.
"""
import re
import numpy as np, pandas as pd

G = "GitHub_master-2025/"
B = G + "3-Datasets/img-lcm/"
REL = B + "img_dir_annot_nii/cells_val_relabel.csv"      # caminho imposto (rotulos avaliados)
AUT = B + "img_dir_annot_nii/cells_val.csv"              # caminho automatico (exportacao)
ALN = B + "img_dir_annot_nii/alignment_val.csv"
XR  = B + "xai_resnet_fold5_nii/xai_resnet_fold5_results.csv"
XS  = B + "xai_swin_fold2_nii/xai_swin_fold2_results.csv"
KR  = G + "4-redes/2.resnet/normal/kfold_epoch_results.csv"
KS  = G + "4-redes/3.swin/swin-sem-optuna/kfold_epoch_results.csv"
LOG_R = G + "4-redes/2.resnet/resnet_optuna/logs-optuna-01042025-resnet.txt"
LOG_S = G + "4-redes/3.swin/swin-com-optuna/logs-optuna-01042025.txt"

SEMENTE_BOOT = 20260904
TAU_L, TAU_U, N_MIN = 0.08, 0.12, 30

_stem = lambda p: re.split(r"[\\/]", p)[-1]


def _xai(path):
    d = pd.read_csv(path)
    ex = d.image_path.map(_stem).str.extract(r"(?P<image>.+?)_cell_?(?P<cell_id>\d+)\.\w+$")
    return pd.DataFrame({"image": ex.image, "cell_id": ex.cell_id.astype(int), "pred": d.pred_idx.values})


def instancias():
    """3.811 instancias: omega, rotulo imposto, rotulo automatico, transformacao, predicoes."""
    rel = pd.read_csv(REL)
    aut = pd.read_csv(AUT)[["image", "cell_id", "label", "best_transform"]].rename(
        columns={"label": "label_aut", "best_transform": "tf_aut"})
    al = pd.read_csv(ALN)[["image", "transform", "nii_status"]].rename(
        columns={"transform": "tf", "nii_status": "st"})
    d = (rel.merge(aut, on=["image", "cell_id"]).merge(al, on="image")
            .merge(_xai(XR).rename(columns={"pred": "pred_R"}), on=["image", "cell_id"])
            .merge(_xai(XS).rename(columns={"pred": "pred_S"}), on=["image", "cell_id"]))
    return d.sort_values(["image", "cell_id"]).reset_index(drop=True)


def suporte(d):
    """Suporte de referencia utilizavel (mesmo filtro do R14)."""
    return d[(d.st == "ok") & (d.tf == "id") & (d.relabel == 1)]


def por_campo(v):
    g = v.groupby("image").agg(n=("relabel", "size"), TP_R=("pred_R", "sum"), TP_S=("pred_S", "sum"))
    g["R_R"], g["R_S"] = g.TP_R / g.n, g.TP_S / g.n
    g["D"] = g.R_R - g.R_S
    return g


def boot_recall(v, ycol, pcol, n_rep=2000, semente=SEMENTE_BOOT):
    """Recall com IC percentil 95% por bootstrap agrupado por campo (protocolo R-02)."""
    g = v[v[ycol] == 1].groupby("image").agg(n=(ycol, "size"), tp=(pcol, "sum"))
    n, tp = g.n.values, g.tp.values
    rng = np.random.default_rng(semente)
    rs = []
    for _ in range(n_rep):
        i = rng.integers(0, len(g), len(g))
        rs.append(tp[i].sum() / n[i].sum())
    return tp.sum() / n.sum(), np.percentile(rs, 2.5), np.percentile(rs, 97.5)


def boot_delta(g, n_rep=10_000, semente=SEMENTE_BOOT):
    n, a, b = g.n.values, g.TP_R.values, g.TP_S.values
    rng = np.random.default_rng(semente)
    out = []
    for _ in range(n_rep):
        i = rng.integers(0, len(g), len(g))
        N = n[i].sum()
        out.append(a[i].sum() / N - b[i].sum() / N)
    return np.percentile(out, 2.5), np.percentile(out, 97.5)


def trials(log):
    pat = re.compile(r"Trial (\d+) finished with value: ([\d.eE+-]+) and parameters: (\{.*?\})")
    rows = []
    for t, val, par in pat.findall(open(log, encoding="utf-8", errors="replace").read()):
        p = eval(par, {}, {})
        rows.append(dict(trial=int(t), value=float(val), lr=p["lr"], optimizer=p["optimizer"]))
    return pd.DataFrame(rows).drop_duplicates("trial").sort_values("trial").reset_index(drop=True)


def holdout(path):
    k = pd.read_csv(path)
    t = k[k.model.str.endswith("_Test")].iloc[0]
    return {c: int(t[c]) for c in ["true_positives", "false_positives", "true_negatives", "false_negatives"]}


def fold2_swin():
    s = pd.read_csv(KS)
    b1, b2 = s.iloc[:101], s.iloc[101:]
    f = lambda b: b[(b.fold == 2) & (b.epoch == 20)].iloc[0]
    m = lambda b: b[b.fold == 2].recall.mean()
    return (int(f(b1).false_negatives), int(f(b2).false_negatives),
            int(f(b1).false_positives), int(f(b2).false_positives), m(b1), m(b2))


if __name__ == "__main__":
    erros = []
    def confere(nome, obtido, publicado, tol=0):
        ok = abs(obtido - publicado) <= tol if isinstance(publicado, (int, float)) else obtido == publicado
        print(f"  {'OK ' if ok else 'XX '} {nome:48s} artefato={obtido!s:>22}  publicado={publicado}")
        if not ok: erros.append(nome)

    d = instancias()
    print("R1 — rotulos operacionais")
    w = d.frac_recalc
    confere("instancias", len(d), 3811)
    confere("instancias com omega em [tau_L, tau_U]", int(((w >= TAU_L) & (w <= TAU_U)).sum()), 0)
    confere("rotulo infectada (relabel)", int((d.relabel == 1).sum()), 3534)
    confere("rotulo nao infectada (relabel)", int((d.relabel == 0).sum()), 277)
    confere("nao infectadas com omega = 0", int(((d.relabel == 0) & (w == 0)).sum()), 277)
    confere("proporcao positiva [%]", round(100 * (d.relabel == 1).mean(), 2), 92.73)
    n_c = d.groupby("image").size()
    confere("campos", len(n_c), 221)
    confere("instancias/campo min", int(n_c.min()), 10)
    confere("instancias/campo max", int(n_c.max()), 28)
    confere("instancias/campo mediana", float(n_c.median()), 17)
    print(f"      omega positivo: min={w[d.relabel==1].min():.4f}  max={w.max():.4f}")

    print("R2 — hold-out")
    for nome, path, fp in [("ResNet50", KR, 67), ("Swin", KS, 84)]:
        h = holdout(path)
        confere(f"{nome} FN", h["false_negatives"], 86)
        confere(f"{nome} FP", h["false_positives"], fp)
        confere(f"{nome} TP+FP+TN+FN", sum(h.values()), 5512)
        confere(f"{nome} recall", round(h["true_positives"] / (h["true_positives"] + h["false_negatives"]), 4), 0.9688)

    print("R3 — busca e retreino")
    tr, ts = trials(LOG_R), trials(LOG_S)
    confere("trials ResNet50", len(tr), 30); confere("trials Swin", len(ts), 30)
    br, bs = tr.loc[tr.value.idxmax()], ts.loc[ts.value.idxmax()]
    confere("ResNet50 melhor valor", round(br.value, 4), 0.9922)
    confere("ResNet50 melhor otimizador", br.optimizer, "SGD")
    confere("Swin melhor valor", round(bs.value, 4), 0.9900)
    confere("Swin melhor lr", float(f"{bs.lr:.2e}"), 9.60e-06)
    confere("Swin melhor otimizador", bs.optimizer, "RMSprop")
    fn0, fn1, fp0, fp1, m0, m1 = fold2_swin()
    confere("Fold 2 FN ref -> retreino", (fn0, fn1), (65, 20))
    confere("Fold 2 FP ref -> retreino", (fp0, fp1), (45, 18))
    confere("Fold 2 recall medio ref", round(m0, 4), 0.9724)
    confere("Fold 2 recall medio retreino", round(m1, 4), 0.9905)

    print("R4 — composicao do suporte")
    fc = d.groupby("image").agg(st=("st", "first"), tf=("tf", "first"),
                                n=("relabel", "size"), pos=("relabel", "sum"))
    vazio = fc[fc.st != "ok"]; outra = fc[(fc.st == "ok") & (fc.tf != "id")]; util = fc[(fc.st == "ok") & (fc.tf == "id")]
    confere("anotacao vazia: campos/inst/neg", (len(vazio), int(vazio.n.sum()), int(vazio.n.sum() - vazio.pos.sum())), (4, 74, 74))
    confere("transf. != id: campos/inst/pos/neg", (len(outra), int(outra.n.sum()), int(outra.pos.sum()), int(outra.n.sum() - outra.pos.sum())), (12, 216, 13, 203))
    confere("utilizavel: campos/inst/pos", (len(util), int(util.n.sum()), int(util.pos.sum())), (205, 3521, 3521))

    print("R5 — sensibilidade geometrica")
    tfa = d.groupby("image").tf_aut.first().value_counts()
    print("      transformacoes (rotina automatica):", dict(tfa))
    tab = pd.crosstab(d.relabel, d.label_aut)
    confere("transicao imposto x automatico", tuple(tab.values.ravel()), (276, 1, 0, 3534))
    v = suporte(d)
    va = d[(d.st == "ok") & (d.label_aut == 1)]
    for nome, col, pub_i, pub_a in [("ResNet50", "pred_R", (0.0335, 0.0279, 0.0399), (0.0334, 0.0273, 0.0399)),
                                    ("Swin", "pred_S", (0.0324, 0.0266, 0.0390), (0.0322, 0.0260, 0.0384))]:
        confere(f"{nome} imposto (recall, IC)", tuple(round(x, 4) for x in boot_recall(v, "relabel", col)), pub_i)
        confere(f"{nome} automatico (recall, IC)", tuple(round(x, 4) for x in boot_recall(va, "label_aut", col)), pub_a)

    print("R6 — por campo e comparacao pareada")
    g = por_campo(v)
    confere("campos pareados", len(g), 205)
    confere("D_i < 0 / = 0 / > 0", (int((g.D < 0).sum()), int((g.D == 0).sum()), int((g.D > 0).sum())), (43, 110, 52))
    confere("Delta_R", round(v.pred_R.mean() - v.pred_S.mean(), 4), 0.0011)
    lo, hi = boot_delta(g)
    confere("IC95 Delta_R (10.000 reps)", (round(lo, 4), round(hi, 4)), (-0.0058, 0.0081))
    confere("campos com recall 0 [%] R / S", (round(100 * (g.R_R == 0).mean(), 1), round(100 * (g.R_S == 0).mean(), 1)), (57.6, 59.5))
    confere("Q3 do recall por campo R / S", (round(np.percentile(g.R_R, 75), 4), round(np.percentile(g.R_S, 75), 4)), (0.0588, 0.0588))
    confere("recall maximo por campo R / S", (round(g.R_R.max(), 2), round(g.R_S.max(), 2)), (0.19, 0.21))
    ZR, ZS = g.TP_R > 0, g.TP_S > 0
    confere(">=1 detectada [%] R / S", (round(100 * ZR.mean(), 1), round(100 * ZS.mean(), 1)), (42.4, 40.5))
    confere("discordantes n10 / n01", (int((ZR & ~ZS).sum()), int((~ZR & ZS).sum())), (39, 35))

    print("\nDIVERGENCIAS:", erros if erros else "nenhuma")
    raise SystemExit(1 if erros else 0)
