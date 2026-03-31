import base64
import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_PATH = PROJECT_ROOT / "model_comparison_v3.ipynb"
OUTPUT_DIR = PROJECT_ROOT / "report" / "figures"


FIGURE_MAP = {
    (30, 0): "01_validation_curves.png",
    (36, 0): "02_confusion_matrices.png",
    (42, 0): "03_misclassified_examples.png",
    (42, 1): "04_both_models_wrong_examples.png",
    (46, 0): "05_confidence_distribution.png",
    (48, 0): "06_agreement_analysis.png",
    (38, 0): "07_per_class_accuracy.png",
    (44, 0): "08_precision_recall_f1.png",
    (50, 0): "09_dhvt_attention_visualization.png",
}


def main() -> None:
    notebook = json.loads(NOTEBOOK_PATH.read_text(encoding="utf-8"))
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    exported = []
    for (cell_index, output_index), filename in FIGURE_MAP.items():
        cell = notebook["cells"][cell_index]
        output = cell.get("outputs", [])[output_index]
        image_data = output.get("data", {}).get("image/png")
        if image_data is None:
            raise ValueError(f"Missing image/png output for cell {cell_index}, output {output_index}.")

        if isinstance(image_data, list):
            image_data = "".join(image_data)

        output_path = OUTPUT_DIR / filename
        output_path.write_bytes(base64.b64decode(image_data))
        exported.append(output_path)

    print("Exported figures:")
    for path in exported:
        print(path.relative_to(PROJECT_ROOT))


if __name__ == "__main__":
    main()
