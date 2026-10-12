# Product Data Cleaning Tools

Simple, repeatable approaches for cleaning eCommerce product data before Amazon, Walmart, Shopify, eBay, and other marketplace uploads.

## Included Files
- [Product Data Audit Script](product_data_audit.py)
- [Data Quality Checklist](data_quality_checklist.md)
- [Demo Catalog](sample_catalog.csv)

## Data Quality Checks
- Trim extra whitespace
- Normalize SKUs
- Detect duplicate SKUs
- Flag missing required fields
- Standardize empty values
- Review title consistency
- Validate numeric fields
- Preserve a change log

## Run the Audit

```bash
python product_data_audit.py sample_catalog.csv
```

No third-party dependencies are required.

## Business Value
Marketplace troubleshooting becomes faster when the source catalog is consistent, auditable, and reusable across channels.

**Upwork:** https://www.upwork.com/freelancers/~0115a312ed543a19a1
