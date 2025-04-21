# ScEMLA
ScEMLA: Ensemble Machine Learning-Based Pre-Trained annotation Approach for scRNA-seq data using Gradient Boosting with Genetic Optimizer
 
This repository contains code for our BMC Bioinformatics paper on scRNA-seq annotation using an ensemble learning approach with genetic optimization for feature selection.

We selected four sequencing datasets from human pancreatic tissue for experiments: Baron human (inDrop sequencing) (Klein and Macosko, 2017) https://
pubmed.ncbi.nlm.nih.gov/28721415/, Enge (Smart-seq2) (Picelli et al., 2013) https:
//www.nature.com/articles/nmeth.2639, Muraro (CEL-seq2) (Hashimshony et al.,
2012) https://www.sciencedirect.com/science/article/pii/S2211124712002288, and
Segerstolpe (Smart-seq2) https://bioconductor.org/books/3.20/OSCA.workflows/
segerstolpe-human-pancreas-smart-seq2.html.

## Structure
- `src/`: Core pipeline modules
- `run_pipeline.py`: Main script to run the full annotation workflow


## Setup

```bash
pip install -r requirements.txt
python run_pipeline.py

