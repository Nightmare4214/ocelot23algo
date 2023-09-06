from pathlib import Path

# Grand Challenge folders were input files can be found
GC_CELL_FPATH = Path("/home/icml007/Nightmare4214/datasets/ocelot2023_v1.0.1/images/test/cell")
GC_TISSUE_FPATH = Path("/home/icml007/Nightmare4214/datasets/ocelot2023_v1.0.1/images/test/tissue")

GC_METADATA_FPATH = Path("/home/icml007/Nightmare4214/datasets/ocelot2023_v1.0.1/metadata.json")

# Grand Challenge output file
GC_DETECTION_OUTPUT_PATH = Path("test/output/cell_classification.json")

# Sample dimensions
SAMPLE_SHAPE = (1024, 1024, 3)
