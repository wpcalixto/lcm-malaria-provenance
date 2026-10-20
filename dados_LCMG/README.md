# Low-Cost Microscope Germany (LCMG) dataset

Part of the record *Low-Cost Microscope dataset, code, and model checkpoints for Computational provenance in external evaluation of deep learning for malaria microscopy*, version v1.0.0, DOI [10.5281/zenodo.23505452](https://doi.org/10.5281/zenodo.23505452). License: CC BY 4.0.

## Description

Grayscale field-of-view images acquired with a low-cost microscopy system developed at Technische Hochschule Mannheim, from malaria laboratory cultures maintained at Heidelberg University, without Giemsa staining. Each field contains multiple cells; no cell is provided as a pre-segmented unit.

## Contents

| Directory | Content |
|---|---|
| `img_dir/train`, `img_dir/val` | 221 + 221 fields of view, 8-bit grayscale BMP, 2048 x 1088 pixels |
| `ann_dir/train`, `ann_dir/val` | 221 + 221 annotation masks, palette-indexed PNG (filled bounding boxes), same name and size as the image |
| `splits/` | `train.txt`, `val.txt`: field identifiers of each list |
| `cell_labels/` | cell-level tables produced by the annotation notebook (`experimental/4-redes/1.annotations/creating_annot_v2.ipynb`) and the alignment audit (`audit_masks.csv`) |
| `metadata/` | dataset metadata, file manifest, data dictionary, acquisition and annotation notes, quality-control report |
| `documentation/` | ethical and legal statement, limitations |
| `checksums/` | SHA-256 of every file of this directory |

File names are the original identifiers (pattern `YYYY_MM_DD_hh_mm_ss_xx`) and are kept because the partition files, the cell-level tables and the code refer to them. Image and mask are linked by identical names.

In the article, quantitative evaluation used the 221 fields of the `val` list (`cell_labels/cells_val_relabel.csv`), and the integrated execution used fields of the `train` list.

## Limitations

- The samples originate from laboratory cultures maintained at Heidelberg University and do not correspond to clinical infection cases.
- The criterion that allocated fields of view to the two lists (`train`, `val`) is not recorded in the available artifacts; the list names are nominal.
- The PNG masks in `ann_dir/` are palette-indexed filled bounding boxes. Index 4 (black) is the background. The correspondence between the other indices and the parasite developmental stages is not documented in the available artifacts.
- The NIfTI pixel-level masks used in the article as the operational reference for cell labeling are not part of the available files and are not included. The cell-level labels derived from them are included in `cell_labels/`.
- The cell crops referenced in the `path` column of the cell-level tables are not included; that column preserves absolute paths of the original machine.
- As stated in the article, the evaluated labels do not provide a valid reference for the negative class in the target domain; external evaluation is restricted to the sensitivity of the infected class.
- Some scripts preserve machine-specific absolute paths of the original repository; the executable code was not modified.

## Citation

Premebida, S. M., Pereira, G. Q., Wiedemann, P., Martins, M. S. R., & Calixto, W. P. (2026). Low-Cost Microscope dataset, code, and model checkpoints for Computational provenance in external evaluation of deep learning for malaria microscopy (Version 1.0.0) [Data set and software]. Zenodo. https://doi.org/10.5281/zenodo.23505452
