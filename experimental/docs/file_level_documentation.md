# File-level documentation (experimental)

| File | Type | Size [bytes] | Purpose |
|---|---|---|---|
| `3-Datasets/img-lcm/auditoria/audit_masks.csv` | .csv | 12471 | LCMG partitions, cell-level tables, alignment tables, audit table and XAI result tables |
| `3-Datasets/img-lcm/images_separation.md` | .md | 927 | LCMG partitions, cell-level tables, alignment tables, audit table and XAI result tables |
| `3-Datasets/img-lcm/img_dir_annot_jpg/alignment_train.csv` | .csv | 10009 | LCMG partitions, cell-level tables, alignment tables, audit table and XAI result tables |
| `3-Datasets/img-lcm/img_dir_annot_jpg/alignment_val.csv` | .csv | 10000 | LCMG partitions, cell-level tables, alignment tables, audit table and XAI result tables |
| `3-Datasets/img-lcm/img_dir_annot_jpg/cells_train.csv` | .csv | 889058 | LCMG partitions, cell-level tables, alignment tables, audit table and XAI result tables |
| `3-Datasets/img-lcm/img_dir_annot_jpg/cells_val.csv` | .csv | 838133 | LCMG partitions, cell-level tables, alignment tables, audit table and XAI result tables |
| `3-Datasets/img-lcm/img_dir_annot_nii/alignment_train.csv` | .csv | 9886 | LCMG partitions, cell-level tables, alignment tables, audit table and XAI result tables |
| `3-Datasets/img-lcm/img_dir_annot_nii/alignment_val.csv` | .csv | 8725 | LCMG partitions, cell-level tables, alignment tables, audit table and XAI result tables |
| `3-Datasets/img-lcm/img_dir_annot_nii/cells_train.csv` | .csv | 907030 | LCMG partitions, cell-level tables, alignment tables, audit table and XAI result tables |
| `3-Datasets/img-lcm/img_dir_annot_nii/cells_train_relabel.csv` | .csv | 941557 | LCMG partitions, cell-level tables, alignment tables, audit table and XAI result tables |
| `3-Datasets/img-lcm/img_dir_annot_nii/cells_val.csv` | .csv | 822652 | LCMG partitions, cell-level tables, alignment tables, audit table and XAI result tables |
| `3-Datasets/img-lcm/img_dir_annot_nii/cells_val_relabel.csv` | .csv | 856086 | LCMG partitions, cell-level tables, alignment tables, audit table and XAI result tables |
| `3-Datasets/img-lcm/splits/train.txt` | .txt | 5083 | LCMG partitions, cell-level tables, alignment tables, audit table and XAI result tables |
| `3-Datasets/img-lcm/splits/val.txt` | .txt | 5083 | LCMG partitions, cell-level tables, alignment tables, audit table and XAI result tables |
| `3-Datasets/img-lcm/xai_resnet_fold5_jpg/xai_resnet_fold5_results.csv` | .csv | 2497932 | LCMG partitions, cell-level tables, alignment tables, audit table and XAI result tables |
| `3-Datasets/img-lcm/xai_resnet_fold5_nii/xai_resnet_fold5_results.csv` | .csv | 2480467 | LCMG partitions, cell-level tables, alignment tables, audit table and XAI result tables |
| `3-Datasets/img-lcm/xai_swin_fold2_jpg/xai_swin_fold2_results.csv` | .csv | 2471492 | LCMG partitions, cell-level tables, alignment tables, audit table and XAI result tables |
| `3-Datasets/img-lcm/xai_swin_fold2_nii/xai_swin_fold2_results.csv` | .csv | 2457852 | LCMG partitions, cell-level tables, alignment tables, audit table and XAI result tables |
| `4-redes/0.mask-generator/cellpose/cellpose.ipynb` | .ipynb | 994226 | Cellpose segmentation and mask generation |
| `4-redes/0.mask-generator/mask_generator.py` | .py | 4834 | Generates filled binary masks from annotation images of the LCMG fields of view. |
| `4-redes/0.mask-generator/masks_with_ai/gerar_mascaras.py` | .py | 6564 | Generates masks from segmentation coordinates stored in a CSV file (exploratory step). |
| `4-redes/0.mask-generator/masks_with_ai/resultados_segmentacao_v2.csv` | .csv | 666422 | Cellpose segmentation and mask generation |
| `4-redes/0.mask-generator/trial-segmentation/anotacoes-testes.ipynb` | .ipynb | 3781682 | Cellpose segmentation and mask generation |
| `4-redes/0.mask-generator/trial-segmentation/giemsa-art.ipynb` | .ipynb | 1181609 | Cellpose segmentation and mask generation |
| `4-redes/0.mask-generator/trial-segmentation/image-segmentator.ipynb` | .ipynb | 539621 | Cellpose segmentation and mask generation |
| `4-redes/1.annotations/audit_viewer.py` | .py | 11288 | Interactive visual audit of the geometric alignment between annotation masks and fields of view; records decisions in audit_masks.csv. |
| `4-redes/1.annotations/creating_annot_dani.ipynb` | .ipynb | 19993 | Annotation export, relabeling (creating_annot_v2.ipynb) and alignment audit |
| `4-redes/1.annotations/creating_annot_v1.ipynb` | .ipynb | 787291 | Annotation export, relabeling (creating_annot_v2.ipynb) and alignment audit |
| `4-redes/1.annotations/creating_annot_v2.ipynb` | .ipynb | 803886 | Annotation export, relabeling (creating_annot_v2.ipynb) and alignment audit |
| `4-redes/1.annotations/creating_annot_v3.ipynb` | .ipynb | 17157 | Annotation export, relabeling (creating_annot_v2.ipynb) and alignment audit |
| `4-redes/2.resnet/normal/kfold_epoch_results.csv` | .csv | 14038 | ResNet50 training, k-fold results and hyperparameter optimization logs |
| `4-redes/2.resnet/normal/resnet50_tl_imagenet_kfold_exec_modificado.ipynb` | .ipynb | 39179 | ResNet50 training, k-fold results and hyperparameter optimization logs |
| `4-redes/2.resnet/resnet_optuna/logs-optuna-01042025-resnet.txt` | .txt | 38209 | ResNet50 training, k-fold results and hyperparameter optimization logs |
| `4-redes/2.resnet/resnet_optuna/resnet50_optuna_exec.ipynb` | .ipynb | 52137 | ResNet50 training, k-fold results and hyperparameter optimization logs |
| `4-redes/3.swin/swin-com-optuna/logs-optuna-01042025.txt` | .txt | 38377 | Swin Transformer training, k-fold results and hyperparameter optimization logs |
| `4-redes/3.swin/swin-com-optuna/logs/optuna_trials_results.csv` | .csv | 4167 | Swin Transformer training, k-fold results and hyperparameter optimization logs |
| `4-redes/3.swin/swin-com-optuna/pth.txt` | .txt | 6723 | Swin Transformer training, k-fold results and hyperparameter optimization logs |
| `4-redes/3.swin/swin-com-optuna/swin_optuna_exec.ipynb` | .ipynb | 53301 | Swin Transformer training, k-fold results and hyperparameter optimization logs |
| `4-redes/3.swin/swin-sem-optuna/kfold_epoch_results.csv` | .csv | 29596 | Swin Transformer training, k-fold results and hyperparameter optimization logs |
| `4-redes/3.swin/swin-sem-optuna/swin_tl_imagenet_kfold_exec.ipynb` | .ipynb | 59230 | Swin Transformer training, k-fold results and hyperparameter optimization logs |
| `4-redes/4.xai/resnet/xai_resnet_fold5.ipynb` | .ipynb | 929769 | Grad-CAM, Integrated Gradients and Occlusion inspection |
| `4-redes/4.xai/resnet/xai_resnet_fold5.py` | .py | 11757 | Computes Grad-CAM, Integrated Gradients and Occlusion maps for the ResNet50 fold 5 checkpoint on LCMG cell crops. |
| `4-redes/4.xai/swin/xai_swin_fold2.ipynb` | .ipynb | 1030793 | Grad-CAM, Integrated Gradients and Occlusion inspection |
| `4-redes/4.xai/swin/xai_swin_fold2.py` | .py | 10556 | Computes Grad-CAM, Integrated Gradients and Occlusion maps for the Swin Transformer fold 2 checkpoint on LCMG cell crops. |
| `6-métricas-artigos/metricas-defesa/images.ipynb` | .ipynb | 681477 | Metric notebooks of earlier reports |
| `6-métricas-artigos/metricas-defesa/tabelas.ipynb` | .ipynb | 0 | Metric notebooks of earlier reports |
| `6-métricas-artigos/metricas-gecco/Transformer vs CNN Malaria.pdf` | .pdf | 895201 | Metric notebooks of earlier reports |
| `6-métricas-artigos/metricas-gecco/metricas.ipynb` | .ipynb | 3878418 | Metric notebooks of earlier reports |
| `6-métricas-artigos/metricas-qualificação/metricas.ipynb` | .ipynb | 4755166 | Metric notebooks of earlier reports |
| `8-streamlit/aplicativo/appui.py` | .py | 31336 | Interface version of the Streamlit application for segmentation, classification and explainability. |
| `8-streamlit/aplicativo/requirements.txt` | .txt | 251 | Development versions of the application |
| `8-streamlit/app.py` | .py | 25581 | Development version of the Streamlit application for segmentation, classification and explainability. |
| `8-streamlit/app10.py` | .py | 24585 | Development version of the Streamlit application with batch processing of multiple images. |
| `LICENSE` | - | 1068 | Repository file |
| `README.md` | .md | 129 | Repository file |
| `docs/modified_files.csv` | .csv | 9775 | Documentation of this component |
| `docs/provenance_commit_880f1a4.csv` | .csv | 6114 | Documentation of this component |
| `figuras_fonte/dados_R.py` | .py | 12361 | Reads and checks, from preserved artifacts only, the values used in the Results figures. |
| `figuras_fonte/estilo_fluxograma.py` | .py | 4610 | Defines the graphical identity shared by the flowchart figures. |
| `figuras_fonte/gera_R7_fluxo_integrado.py` | .py | 4505 | Generates the panels with the preserved visual outputs of the integrated MUM-XAI execution. |
| `figuras_fonte/gera_R8_auditoria.py` | .py | 5861 | Generates the provenance audit map figure. |
| `figuras_fonte/gera_R_resultados.py` | .py | 19612 | Generates the Results figures (support composition, hold-out confusion matrices, optimization and recall panels). |
| `figuras_fonte/gera_fig1_fluxo_global.py` | .py | 5720 | Generates a draft of the global methodology workflow diagram. |
| `figuras_fonte/gera_fig2_microprocessos.py` | .py | 4876 | Generates a draft of the microprocess workflow of the integrated pipeline. |
| `figuras_fonte/gera_fig3_dominio_origem.py` | .py | 6949 | Generates the source-domain (NIH) sample panels. |
| `figuras_fonte/gera_fig4_dominio_alvo.py` | .py | 4406 | Generates the target-domain (LCMG) field-of-view and annotation panels. |
| `figuras_fonte/gera_fig4_fig5_recall_loss.py` | .py | 5049 | Generates the validation recall and training loss curves per fold in the source domain. |
| `figuras_fonte/gera_fig6_matrizes.py` | .py | 4581 | Generates the target-domain confusion matrices from the preserved XAI result tables. |
| `figuras_fonte/gera_fig6_matrizes_dados.py` | .py | 2904 | Reads the counts of the target-domain confusion matrices without generating figures. |
| `figuras_fonte/gera_fig7_matrizes_fonte130.py` | .py | 3479 | Generates the target-domain confusion matrices with enlarged fonts and fixed physical size. |
| `figuras_fonte/gera_fig8_xai.py` | .py | 5414 | Reassembles the preserved XAI composites without re-running explainability methods. |
| `figuras_fonte/norma_figuras.py` | .py | 7920 | Implements the figure construction rules (fonts, sizes, palette and export) used by the figure scripts. |
| `malaria-classifier-LC/__init__.py` | .py | 2409 | Empty initializer of the malaria-classifier-LC package. |
| `malaria-classifier-LC/main.py` | .py | 3439 | Entry point that configures and launches k-fold training of the classifier package. |
| `malaria-classifier-LC/models/efficientnetb0_model.py` | .py | 2422 | Empty file preserved from the original repository; no executable content. |
| `malaria-classifier-LC/models/resnet_model.py` | .py | 2862 | Defines the ResNet50 classifier wrapper (ResNet50Model) used for binary classification of cell crops. |
| `malaria-classifier-LC/models/swin_model.py` | .py | 2949 | Defines the Swin Transformer classifier wrapper (SwinModel) used for binary classification of cell crops. |
| `malaria-classifier-LC/pre-processing.py` | .py | 2420 | Empty file preserved from the original repository; no executable content. |
| `malaria-classifier-LC/train.py` | .py | 4952 | Implements the training epoch, the validation step and the k-fold cross-validation loop. |
| `malaria-classifier-LC/transforms.py` | .py | 3472 | Builds the image transforms and the data loaders used in training and validation. |
| `requirements.txt` | .txt | 2518 | Repository file |
