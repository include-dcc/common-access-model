# Sequencing enums vs. FAIR Genomes lookups

Compares the ontology mappings in the `sequencing-assays` branch (`src/common_access_model/schema/enums/`) with the **`main` branch** of the FAIR Genomes semantic schema ([repo](https://github.com/fairgenomes/fairgenomes-semantic-model/tree/main), [lookups](https://github.com/fairgenomes/fairgenomes-semantic-model/tree/main/lookups); paper: [PMC9008059](https://pmc.ncbi.nlm.nih.gov/articles/PMC9008059/)). The repo has no releases or version tags beyond the paper's v1.1, so `main` is the latest state.

FAIR Genomes lookup files used: `SequencingMethods`, `SequencingPlatform`, `SequencingInstrumentModels`, `GenomeAccessions`, `BiospecimenTypes`, `AnalysesPerformed`. `FG:` terms are IDs minted by FAIR Genomes (`https://w3id.org/fair-genomes/resource/FG_xxxxxxx`). FAIR Genomes has no dedicated lookups for analyte type, library prep, library selection, or library strand.

Status key: **Match** = same ID in both; **Differs** = same concept, different ID or ontology; **Ours only** / **FG only** = no counterpart.

## What changed between v1.1 and `main`

Only `SequencingInstrumentModels` changed among the lookups used here: it grew from 39 to 45 rows. The six new rows are `OBI:0002750` MinION, `OBI:0002751` GridION Mk1, `OBI:0002752` PromethION, `OBI:0002632` PacBio Sequel, `OBI:0002633` PacBio Sequel II, and `OBI:0000710` Li-Cor 4300. `SequencingMethods` (35 rows), `SequencingPlatform` (7), `GenomeAccessions` (29) and the sequencing-related terms in `BiospecimenTypes` are unchanged from v1.1 in the rows I checked.

## Sequencing platform

FAIR Genomes uses GENEPIO platform terms; this model uses NCIT sequencing terms. FAIR Genomes also lists the NCIT terms in its `SequencingMethods` lookup (marked below).

| Concept | This model (`EnumSequencingPlatform`) | FAIR Genomes (`SequencingPlatform`) | Status |
|---|---|---|---|
| Illumina | NCIT:C146817 | GENEPIO:0001923 (NCIT:C146817 in `SequencingMethods`) | Differs |
| Complete Genomics | NCIT:C146815 | GENEPIO:0001924 (NCIT:C146815 in `SequencingMethods`) | Differs |
| Roche 454 | NCIT:C146809 | GENEPIO:0001926 (NCIT:C146809 in `SequencingMethods`) | Differs |
| ABI SOLiD | NCIT:C146811 | GENEPIO:0002684 (NCIT:C146811 in `SequencingMethods`) | Differs |
| PacBio / SMRT | NCIT:C146819 | GENEPIO:0001927 (NCIT:C146819 in `SequencingMethods`) | Differs |
| Ion Torrent / Ion Semiconductor | NCIT:C125894 | GENEPIO:0002683 (NCIT:C125894 in `SequencingMethods`) | Differs |
| Oxford Nanopore | NCIT:C146818 (in `SequencingMethods` too) | – | Ours only in `SequencingPlatform` |
| Helicos | – | GENEPIO:0002682 (NCIT:C146816 in `SequencingMethods`) | FG only |

## Sequencing strategy / method

This model: `EnumSequencingStrategy`. FAIR Genomes: `SequencingMethods`.

| Term | This model | FAIR Genomes | Status |
|---|---|---|---|
| Whole Genome Sequencing | NCIT:C101294 | NCIT:C101294 | Match |
| Whole Exome Sequencing | NCIT:C101295 | NCIT:C101295 | Match |
| mRNA Sequencing | NCIT:C129432 | NCIT:C129432 | Match |
| MicroRNA Sequencing | NCIT:C156057 | NCIT:C156057 | Match |
| Targeted Transcriptome Sequencing | NCIT:C158252 | NCIT:C158252 | Match |
| Targeted Genome Sequencing | NCIT:C158253 | NCIT:C158253 | Match |
| Oxford Nanopore Sequencing | NCIT:C146818 | NCIT:C146818 | Match |
| RNA Sequence Analysis | NCIT:C192768 | – | Ours only |
| Single Cell RNA Sequencing | NCIT:C171152 | – | Ours only |
| Tumor Panel Sequencing | NCIT:C165600 | – | Ours only |
| Disease Panel Gene Sequencing | NCIT:C173599 | – | Ours only |
| Multi-gene Panel Sequencing | NCIT:C198412 | – | Ours only |
| Targeted Capture Sequencing | NCIT:C204828 | – | Ours only |
| Methyl-binding Domain Sequencing | NCIT:C204820 | – | Ours only |
| Methylated DNA Immunoprecipitation Sequencing | NCIT:C204821 | – | Ours only |
| Methylation-Sensitive Restriction Enzyme Sequencing | NCIT:C204822 | – | Ours only |
| Proteomics | NCIT:C20085 | EDAM:topic_0121 (in `AnalysesPerformed`, a different field) | Differs |
| Long Read Sequencing | NCIT:C223895 | – | Ours only |
| Whole Transcriptome Sequencing | (in `EnumLibraryPrep`: NCIT:C124261) | NCIT:C124261 | Match (different field) |
| Next Generation Sequencing | – | NCIT:C101293 | FG only |
| Next Generation Targeted Sequencing | – | NCIT:C130177 | FG only |
| DNA Sequencing | – | NCIT:C153598 | FG only |
| Nucleic Acid Sequencing | – | NCIT:C18881 | FG only |
| DNA Resequencing | – | NCIT:C41254 | FG only |
| Large-Scale Sequencing | – | NCIT:C19645 | FG only |
| Population Sequencing | – | NCIT:C135457 | FG only |
| Shotgun Sequencing | – | NCIT:C19646 | FG only |
| Whole-Genome Shotgun Sequencing | – | NCIT:C19653 | FG only |
| Paired-End Sequencing | – | NCIT:C150423 | FG only (library layout) |
| Sequence-based Typing | – | NCIT:C130180 | FG only |
| Immune Repertoire Deep Sequencing | – | NCIT:C158249 | FG only |
| Dideoxy Chain Termination DNA Sequencing | – | NCIT:C19641 | FG only |
| Capillary Sequencing | – | NCIT:C146814 | FG only |
| Radioactive Sequencing | – | NCIT:C19658 | FG only |
| Pyrosequencing | – | NCIT:C99481 | FG only |
| BGISEQ-500 Sequencing | – | NCIT:C146812 | FG only (platform) |

## Library strand

This model: `EnumLibraryStrand`. FAIR Genomes carries these terms inside `SequencingMethods`.

| Term | This model | FAIR Genomes | Status |
|---|---|---|---|
| Unstranded Library Sequencing | NCIT:C150427 | NCIT:C150427 | Match |
| First-strand Library Sequencing | NCIT:C150428 | NCIT:C150428 | Match |
| Second-strand Library Sequencing | NCIT:C150426 | NCIT:C150426 | Match |

## Library prep and library selection

FAIR Genomes has no dedicated lookups for these fields, but its `BiospecimenTypes` lookup (a sample-type list) includes the NCIT genomic-library terms that this model uses for library selection. They match by ID.

| Term | This model | FAIR Genomes | Status |
|---|---|---|---|
| Hybrid Selected Genomic Library | `EnumLibrarySelection`: NCIT:C163986 | `BiospecimenTypes`: NCIT:C163986 | Match (different field) |
| Affinity Enriched Genomic Library | `EnumLibrarySelection`: NCIT:C163987 | `BiospecimenTypes`: NCIT:C163987 | Match (different field) |
| Poly-A Enriched Genomic Library | `EnumLibraryPrep` and `EnumLibrarySelection`: NCIT:C163988 | `BiospecimenTypes`: NCIT:C163988, labelled "Poly-T Enriched Genomic Library" | Match (ID); label differs |
| Randomly Selected Genomic Library | `EnumLibrarySelection`: NCIT:C163989 | `BiospecimenTypes`: NCIT:C163989 | Match (different field) |
| rRNA Depleted Genomic Library | `EnumLibrarySelection`: NCIT:C163990 | `BiospecimenTypes`: NCIT:C163990 | Match (different field) |
| miRNA Size Fractionated Genomic Library | `EnumLibrarySelection`: NCIT:C163991 | `BiospecimenTypes`: NCIT:C163991 | Match (different field) |
| Whole Transcriptome Sequencing | `EnumLibraryPrep`: NCIT:C124261 | `SequencingMethods`: NCIT:C124261 | Match (different field) |
| Polymerase Chain Reaction | `EnumLibrarySelection`: NCIT:C17003 | – | Ours only |
| polyA RNA extraction | `EnumLibraryPrep`: OBI:0000848 | – | Ours only |
| total RNA depletion | `EnumLibraryPrep`: OBI:0000855 | – | Ours only |
| Genomic Library (root of your `reachable_from`) | NCIT:C15241 | `BiospecimenTypes`: NCIT:C15241 | Match (different field) |
| DNA Library / cDNA Library / Sequencing Library | – | `BiospecimenTypes`: NCIT:C16223 / C15727 / C148073 | FG only |

## Sequencing instrument

This model: `EnumSequencingInstrument` (OBI only). FAIR Genomes: `SequencingInstrumentModels` (45 rows; OBI, GENEPIO and FG terms). Rows marked **new** were added after v1.1.

| Instrument | This model | FAIR Genomes | Status |
|---|---|---|---|
| Illumina HiSeq 1000 | OBI:0002022 | OBI:0002022 | Match |
| Illumina HiSeq 2000 | OBI:0002001 | OBI:0002001 | Match |
| Illumina HiSeq 2500 | OBI:0002002 | OBI:0002002 | Match |
| Illumina HiSeq 3000 | OBI:0002048 | OBI:0002048 | Match |
| Illumina HiSeq 4000 | OBI:0002049 | OBI:0002049 | Match |
| Illumina HiSeq X Ten | OBI:0002129 | FG:0000005 | Differs (OBI term exists) |
| Illumina HiSeq 1500 | OBI:0003386 | – | Ours only |
| Illumina HiSeq Sequencer | – | GENEPIO:0001939 | FG only |
| Illumina HiSeq X Five | – | FG:0000004 | FG only |
| MiSeq | – | OBI:0002003 | FG only |
| NextSeq 500 | – | OBI:0002021 | FG only |
| Genome Analyzer IIx | – | OBI:0002000 | FG only |
| Illumina Genome Analyzer II | – | OBI:0000703 | FG only |
| Genome Analyzer IIe | – | OBI:0002027 | FG only |
| PacBio RS II | – | OBI:0002012 | FG only |
| PacBio Sequel (**new**) | – | OBI:0002632 | FG only |
| PacBio Sequel II (**new**) | – | OBI:0002633 | FG only |
| Oxford Nanopore MinION (**new**) | – | OBI:0002750 | FG only |
| Oxford Nanopore GridION Mk1 (**new**) | – | OBI:0002751 | FG only |
| Oxford Nanopore PromethION (**new**) | – | OBI:0002752 | FG only |
| Li-Cor 4300 DNA Analysis System (**new**) | – | OBI:0000710 | FG only |
| HeliScope Single Molecule Sequencer | – | OBI:0000717 | FG only |
| 454 Genome Sequence 20 | – | OBI:0000689 | FG only |
| 454 Genome Sequencer FLX | – | OBI:0000702 | FG only |
| 454 Genome Sequencer FLX Titanium | – | GENEPIO:0001936 | FG only |
| 454 Genome Sequencer | – | GENEPIO:0001937 | FG only |
| 454 Genome Sequencer Junior | – | GENEPIO:0001938 | FG only |
| AB SOLiD System | – | OBI:0000696 | FG only |
| SOLiD 3 Plus System | – | OBI:0002007 | FG only |
| SOLiD 4 System | – | OBI:0002024 | FG only |
| SOLiD 4hq System | – | GENEPIO:0001928 | FG only |
| SOLiD 5500 | – | GENEPIO:0001929 | FG only |
| SOLiD 5500xl | – | GENEPIO:0001930 | FG only |
| SOLiD PI System | – | GENEPIO:0001931 | FG only |
| SOLiD System 2.0 | – | GENEPIO:0001932 | FG only |
| SOLiD System 3.0 | – | GENEPIO:0001933 | FG only |
| Ion Torrent PGM | – | GENEPIO:0001935 | FG only |
| Illumina MiniSeq | – | FG:0000006 | FG only |
| Illumina iSeq 100 | – | FG:0000007 | FG only |
| Illumina NextSeq 550 | – | FG:0000008 | FG only |
| Illumina NextSeq 2000 | – | FG:0000009 | FG only |
| Illumina NovaSeq 6000 | – | FG:0000010 | FG only |
| Illumina NextSeq 1000 | – | FG:0000011 | FG only |
| Illumina NextSeq 550Dx | – | FG:0000012 | FG only |
| Illumina MiSeqDx | – | FG:0000013 | FG only |
| Illumina MiSeq FGx | – | FG:0000014 | FG only |

## Reference genome

This model: `EnumReferenceGenome` (LOINC answer codes, no patch levels). FAIR Genomes: `GenomeAccessions` (NCBI assembly accessions, one term per patch release; only the unpatched builds are shown).

| Build | This model | FAIR Genomes | Status |
|---|---|---|---|
| GRCh37 | loinc:LA14029-5 | GCF_000001405.13 | Differs |
| GRCh38 | loinc:LA26806-2 | GCF_000001405.26 | Differs |
| hg19 | loinc:LA14025-3 | – | Ours only |
| GRCh37.p1 – p13, GRCh38.p1 – p13, hs38d1 | – | GCA/GCF accessions | FG only |

## Analyte type

This model: `EnumAnalyteType` (SNOMEDCT:24851008 DNA, SNOMEDCT:27888000 RNA). FAIR Genomes has no analyte-type lookup and no generic DNA/RNA terms. Its `BiospecimenTypes` lookup has only more specific nucleic-acid sample types: Blood DNA (NCIT:C158416), Total RNA (NCIT:C163995), Nucleic RNA Sample (NCIT:C174108), Formalin-Fixed Paraffin-Embedded DNA (NCIT:C156435), Formalin-Fixed Paraffin-Embedded RNA (NCIT:C156436), Nucleic Acid Aliquot (NCIT:C171176), Ancient DNA (NCIT:C95946) and Environmental DNA (NCIT:C169106). None of these match your SNOMED CT IDs.

## Not compared

- `EnumSequencingCenter` and `EnumReadGroupQualityScale` have no FAIR Genomes counterpart.
- FAIR Genomes `NGSKits` (library prep kits, all `FG:` terms) has no counterpart in this model.
- `main` also has new imaging, treatment and biomarker lookups (e.g. `AssayType`, `ImagingDevice`, `Modality`) that are unrelated to the sequencing enums.
