from pathlib import Path
from PIL import Image
import numpy as np


def load_image(path: str | Path) -> Image.Image:
    path = Path(path)

    if not path.is_file():
        raise FileNotFoundError(f"Image not found: {path}")

    with Image.open(path) as image:
        return image.convert("RGB")

def to_numpy(image: Image.Image) -> np.ndarray:
    return np.array(image)
