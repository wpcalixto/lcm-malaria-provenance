# Limitations

- The samples originate from laboratory cultures maintained at Heidelberg University and do not correspond to clinical infection cases.
- The criterion that allocated fields of view to the two lists (`train`, `val`) is not recorded in the available artifacts; the list names are nominal.
- The PNG masks in `ann_dir/` are palette-indexed filled bounding boxes. Index 4 (black) is the background. The correspondence between the other indices and the parasite developmental stages is not documented in the available artifacts.
- The NIfTI pixel-level masks used in the article as the operational reference for cell labeling are not part of the available files and are not included. The cell-level labels derived from them are included in `cell_labels/`.
- The cell crops referenced in the `path` column of the cell-level tables are not included; that column preserves absolute paths of the original machine.
- As stated in the article, the evaluated labels do not provide a valid reference for the negative class in the target domain; external evaluation is restricted to the sensitivity of the infected class.
- Some scripts preserve machine-specific absolute paths of the original repository; the executable code was not modified.
