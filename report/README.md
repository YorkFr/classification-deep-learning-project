# LaTeX Report Notes

## Main file

- `main.tex`

## Figures folder

Put exported notebook figures into:

- `figures/alexnet_curves.png`
- `figures/dhvt_curves.png`
- `figures/comparison_curves.png`
- `figures/custom_predictions.png`
- `figures/confusion_matrices.png`
- `figures/per_class_accuracy.png`
- `figures/misclassified_examples.png`

You can rename the files, but then update the matching `\includegraphics{...}` paths in `main.tex`.

## Suggested workflow

1. Run the notebook experiments.
2. Export the training curves and prediction screenshots.
3. Place the images into `latex/figures/`.
4. Replace the placeholder figure boxes in `main.tex` with the real `\includegraphics` lines if needed.
5. Compile the report.

## Example compile command

```powershell
pdflatex main.tex
```
