# Product Data Cleaning Tools

Simple, repeatable approaches for cleaning eCommerce product data before Amazon, Walmart, Shopify, eBay, and other marketplace uploads.

## Data Quality Checks
- Trim extra whitespace
- Normalize SKUs
- Detect duplicate SKUs
- Flag missing required fields
- Standardize empty values
- Review title consistency
- Validate numeric fields
- Preserve a change log

## Example

```python
def normalize_sku(value):
    return (value or "").strip().upper()

def missing_fields(row, required):
    return [field for field in required if not str(row.get(field, "")).strip()]
```

## Business Value
Marketplace troubleshooting becomes faster when the source catalog is consistent, auditable, and reusable across channels.

**Upwork:** https://www.upwork.com/freelancers/~0115a312ed543a19a1
