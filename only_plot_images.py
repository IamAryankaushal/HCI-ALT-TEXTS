import os
import shutil
import pandas as pd
from tqdm import tqdm

CSV_PATH = "is_plot_images.csv"
DEST_DIR = "plot_images_only"

# create destination directory if it doesn't exist
os.makedirs(DEST_DIR, exist_ok=True)

df = pd.read_csv(CSV_PATH)

for img_path in tqdm(df["local_uri"]):
    if os.path.exists(img_path):
        shutil.copy(img_path, DEST_DIR)
    else:
        print(f"Missing file: {img_path}")

print(f"Copied {len(df)} plot images to '{DEST_DIR}/'")
