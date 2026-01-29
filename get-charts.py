import json
import pandas as pd
from tqdm import tqdm

INPUT_PATH = "data/hci-alt-text-dataset-20220915.jsonl"
OUTPUT_CSV = "is_plot_images.csv"

rows = []

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    for line in tqdm(f):
        record = json.loads(line)

        if record.get("is_plot") is True:
            alt_text = record.get("alt_text")

            for uri in record.get("local_uri", []):
                rows.append({
                    "local_uri": f"images/{uri}",
                    "alt_text": alt_text
                })

df = pd.DataFrame(rows)
df.to_csv(OUTPUT_CSV, index=False)

print(f"Saved {len(df)} images with is_plot=true to {OUTPUT_CSV}")
