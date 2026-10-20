# Annotation notes

As described in the article, two annotation sources exist for the LCMG fields:

1. Bounding boxes marked by a participant in the microscopy project, originally distinguished by color according to parasite developmental stage and unified into a single infected category for the binary problem. The PNG masks in `ann_dir/` contain filled rectangles with palette indices; index 4 (black) is the background. The mapping between the other indices and the developmental stages is not documented in the available artifacts.
2. NIfTI masks with pixel-level delineation, produced by a biomedical scientist from Hospital Israelita Albert Einstein, adopted in the article as the operational reference. These masks are not part of the available files and are not included.

No documentary record of reciprocal blinding between the two sources is available.

Cell-level labels (`cell_labels/`): cells segmented with Cellpose were matched to the NIfTI reference after geometric alignment (slice and transformation per field). `label` follows the export routine (`frac_on_cell >= frac_thresh`); `relabel` is the label effectively evaluated in the article, recalculated with a fixed transformation, mask dilation and a minimum intersection (`frac_recalc`, `inter_px`). Parameters are recorded in the notebook `experimental/4-redes/1.annotations/creating_annot_v2.ipynb`.
