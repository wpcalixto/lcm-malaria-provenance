# Quality-control report

Automatic checks performed when the package was assembled (2026-10-20):

| Check | train | val |
|---|---|---|
| Images (.bmp) | 221 | 221 |
| Masks (.png) | 221 | 221 |
| Identifiers in splits/*.txt | 221 | 221 |
| Every image has a mask with the same name | True | True |
| Split list equals the image set | True | True |
| Image size (width, height, bits) | [(2048, 1088, 8)] | [(2048, 1088, 8)] |
| Mask size (width, height, bit depth) | [(2048, 1088, 4)] | [(2048, 1088, 4)] |

- Fields shared between train and val: 0.
- Byte-identical duplicate images: 0.
- Hidden, temporary and system files: removed.
- Cell-level tables: copied unchanged from commit 880f1a4 of sthemonica/master-2025.
