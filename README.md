# Low-Cost Microscope dataset, code, and model checkpoints for Computational provenance in external evaluation of deep learning for malaria microscopy

> **GitHub repository:** code and documentation only. The LCMG images (`dados_LCMG/img_dir/`), masks (`dados_LCMG/ann_dir/`) and model checkpoints (`software_MUM-XAI/models/*.pth`) are distributed only through Zenodo: https://doi.org/10.5281/zenodo.23505452. `SHA256SUMS` lists the complete Zenodo package.

## 1. Identification

- Title: Low-Cost Microscope dataset, code, and model checkpoints for Computational provenance in external evaluation of deep learning for malaria microscopy
- Version: v1.0.0
- Resource type: Dataset (with software and model checkpoints)
- DOI: [10.5281/zenodo.23505452](https://doi.org/10.5281/zenodo.23505452)
- Authors:
- Sthefanie Monica Premebida; ORCID 0000-0002-8964-2119; Federal University of Technology - Parana, Brazil
- Gabrielly Queiroz Pereira; ORCID 0000-0003-2663-0783; State University of Ponta Grossa, Brazil
- Philipp Wiedemann; ORCID not available; Department of Biotechnology, Mannheim University of Applied Sciences, Germany
- Marcella Scoczynski R. Martins; ORCID 0000-0002-5716-4968; Federal University of Technology - Parana, Brazil
- Wesley Pacheco Calixto; ORCID 0000-0002-1928-4432; Institute of Systems and Robotics, University of Coimbra, Portugal
- Corresponding author: Wesley Pacheco Calixto, wesley.pacheco@isr.uc.pt, Institute of Systems and Robotics, University of Coimbra
- Licenses: LCMG data under CC BY 4.0; experimental code under the MIT License; MUM-XAI code under the Apache License 2.0
- Date: 2026-10-20
- Language: English
- Source repository (code only): https://github.com/wpcalixto/lcm-malaria-provenance

## 2. General description

This record contains the materials associated with the article *Computational provenance in external evaluation of deep learning for malaria microscopy*: the Low-Cost Microscope Germany (LCMG) dataset, the experimental materials, the MUM-XAI application code, and the ResNet50 and Swin Transformer model checkpoints. The LCMG dataset was produced in collaboration between Technische Hochschule Mannheim and Heidelberg University. The materials are organized for auditing, reuse and partial reproduction of the procedures described in the article.

## 3. Contents

- `dados_LCMG/`: 442 grayscale field-of-view microscopy images (`.bmp`) in two lists of 221 fields, 442 annotation masks (`.png`), cell-level labels and partition files. See `dados_LCMG/README.md`.
- `experimental/`: notebooks, experimental partitions, CSV files and figure-generation scripts. Files are identical to commit `880f1a4` of https://github.com/sthemonica/master-2025, except for the comment headers added to Python scripts. Third-party articles, competition files (Lacuna/Zindi) and exploratory scripts not used in the article were excluded. See `experimental/docs/`.
- `software_MUM-XAI/`: MUM-XAI application code (version 1.0, https://doi.org/10.5281/zenodo.17689404) with the reference checkpoints `models/resnet_fold5.pth` (ResNet50, fold 5) and `models/swin_fold2.pth` (Swin Transformer, fold 2), which replace the Git LFS pointer files of the previous record.
- `LICENSES/`, `CITATION.cff`, `CHANGELOG.md`, `SHA256SUMS`.

## 4. Directory structure

```text
lcm_malaria_provenance_v1.0.0/
  README.md  CITATION.cff  CHANGELOG.md  SHA256SUMS
  LICENSES/            CC-BY-4.0.txt, MIT.txt, Apache-2.0.txt
  dados_LCMG/          LCMG dataset (CC BY 4.0)
    img_dir/{train,val}/      221 + 221 grayscale fields of view (.bmp)
    ann_dir/{train,val}/      221 + 221 annotation masks (.png)
    splits/                   train.txt, val.txt
    cell_labels/              cell-level labels, alignment tables, audit_masks.csv
    metadata/  documentation/  checksums/
  experimental/        notebooks, partitions, CSV files and figure scripts (MIT)
    3-Datasets/  4-redes/  6-métricas-artigos/  8-streamlit/  malaria-classifier-LC/  figuras_fonte/  docs/
  software_MUM-XAI/    MUM-XAI application code (Apache-2.0) and checkpoints in models/
```

On Zenodo, `dados_LCMG/`, `experimental/` and `software_MUM-XAI/` are distributed as ZIP archives that preserve this tree.

## 5. Usage

- Verify integrity: `sha256sum -c SHA256SUMS` from the package root.
- MUM-XAI: create the environment from `software_MUM-XAI/environment.yml` and run `streamlit run app/app.py` from `software_MUM-XAI/`.
- Experimental notebooks and scripts: environment in `experimental/requirements.txt`. The notebooks preserve their executed outputs.
- External datasets are not included: NIH Malaria Dataset (U.S. National Library of Medicine) and Lacuna Malaria Detection Challenge Dataset (Zindi).

## 6. Limitations

- The samples originate from laboratory cultures maintained at Heidelberg University and do not correspond to clinical infection cases.
- The criterion that allocated fields of view to the two lists (`train`, `val`) is not recorded in the available artifacts; the list names are nominal.
- The PNG masks in `ann_dir/` are palette-indexed filled bounding boxes. Index 4 (black) is the background. The correspondence between the other indices and the parasite developmental stages is not documented in the available artifacts.
- The NIfTI pixel-level masks used in the article as the operational reference for cell labeling are not part of the available files and are not included. The cell-level labels derived from them are included in `cell_labels/`.
- The cell crops referenced in the `path` column of the cell-level tables are not included; that column preserves absolute paths of the original machine.
- As stated in the article, the evaluated labels do not provide a valid reference for the negative class in the target domain; external evaluation is restricted to the sensitivity of the infected class.
- Some scripts preserve machine-specific absolute paths of the original repository; the executable code was not modified.

## 7. Citation

Premebida, S. M., Pereira, G. Q., Wiedemann, P., Martins, M. S. R., & Calixto, W. P. (2026). Low-Cost Microscope dataset, code, and model checkpoints for Computational provenance in external evaluation of deep learning for malaria microscopy (Version 1.0.0) [Data set and software]. Zenodo. https://doi.org/10.5281/zenodo.23505452

## 8. Funding

FCT - Fundacao para a Ciencia e a Tecnologia, I.P., project UIDB/00048/2020 (DOI 10.54499/UIDB/00048/2020); CNPq, Brazil (Processes 301644/2022-5, 303909/2025-0 and 174987/2023-4); Fundacao Araucaria (Process 56/2026 FAUEPG).
