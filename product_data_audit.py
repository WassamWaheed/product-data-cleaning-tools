import csv
import sys
from collections import Counter

if len(sys.argv) != 2:
    print("Usage: python product_data_audit.py catalog.csv")
    raise SystemExit(1)

with open(sys.argv[1], newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

skus = [(row.get("sku") or "").strip().upper() for row in rows]
counts = Counter(skus)

print(f"Rows: {len(rows)}")
print(f"Unique SKUs: {len([sku for sku in counts if sku])}")

for sku, count in counts.items():
    if sku and count > 1:
        print(f"DUPLICATE SKU: {sku} ({count} rows)")

for index, row in enumerate(rows, start=2):
    missing = [field for field in ("sku", "title", "brand") if not (row.get(field) or "").strip()]
    if missing:
        print(f"ROW {index}: missing {', '.join(missing)}")
