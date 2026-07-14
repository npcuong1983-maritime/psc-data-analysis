# PSC Detention Data Cleaning

This project demonstrates how publicly available PSC detention data can be transformed into an analyzable dataset.

## Background

Public PSC data is often fragmented and distributed across multiple sources and formats.

This project uses publicly available Tokyo MOU detention data as an example of how raw detention lists can be transformed into a structured dataset for further analysis.

## Challenges

- Multiple rows belonging to a single ship detention case.
- Merged cells exported from Excel files.
- Inconsistent data structures.
- Deficiency descriptions mixed with deficiency codes.

## Techniques

- Forward filling (`ffill`)
- Groupby aggregation
- Deficiency code extraction
- Data reshaping using pandas

## Example outputs

- Number of detained ships by flag state
- Ranking of detention-related deficiency codes
- Detention grounds by ship type
- Aggregated detention statistics

## Tools

- Python
- Pandas
- Matplotlib

## Data source

- Tokyo MOU Detention List
- Publicly available PSC information