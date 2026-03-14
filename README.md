# Classification Deep Learning Project

This repository is organized around a homework-style notebook that compares `AlexNet` and `DHVT` on the same image classification dataset.

## Main files

- `model_comparison.ipynb`: current comparison notebook
- `model_comparison_v2.ipynb`: alternate notebook snapshot
- `report/main.tex`: LaTeX report
- `slides/main.tex`: LaTeX beamer presentation

## Notebook workflow

The main notebook keeps both models in one file so the comparison stays on the same dataset and under the same experiment structure.

The notebook supports:

- selecting local or Colab runtime
- selecting `CIFAR-10`, `CIFAR-100`, or `custom_folder`
- training `AlexNet` and `DHVT`
- saving and reloading checkpoints
- running inference on images stored in `test_images/`
- exporting figures used in the report

## Data and outputs

- `models/`: saved checkpoints
- `predictions/`: saved prediction outputs
- `test_images/`: custom images for inference
- `documents/`: reference papers and supporting material
- `report/figures/`: extracted notebook figures used in the report and slides

If you use `custom_folder`, keep the dataset in this structure:

```text
custom_folder/
  train/
    class_name/
  val/
    class_name/
```

## Environment

The local environment uses the project virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

CUDA-enabled PyTorch is installed in that environment.

## Colab workflow

When the notebook runs in Colab, the saved models and inference inputs should be stored in Google Drive under your project folder.

Use these folders in Drive:

- `models/` for checkpoints
- `test_images/` for custom inference images
- `predictions/` for exported predictions

## Report

The report is in `report/main.tex`. It uses the exported figures in `report/figures/`.

To compile:

```powershell
cd report
pdflatex main.tex
pdflatex main.tex
```

## Slides

The presentation is in `slides/main.tex`. It reuses the figures from `report/figures/`.

To compile:

```powershell
cd slides
pdflatex main.tex
pdflatex main.tex
```
