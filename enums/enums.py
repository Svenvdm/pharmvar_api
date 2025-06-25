from enum import Enum

class Function(str, Enum):
    DECREASED = "decreased function"
    NOT_ASSIGNED = "function not assigned"
    INCREASED = "increased function"
    NORMAL = "normal function"  
    POSSIBLY_DECREASED = "possibly decreased"
    SEVERELY_DECREASED = "severely decreased"
    UNCERTAIN = "uncertain function"
    UNKNOWN = "unknown function"

class EvidenceLevel(str, Enum):
    DEFINITIVE = "Definitive"
    LIMITED = "Limited"
    MODERATE = "Moderate"

class ReferenceBaseSequence(str, Enum):
    A = "A"
    C = "C"
    G = "G"
    T = "T"

class ReferenceCollection(str, Enum):
    GRCH37 = "GRCh37"
    GRCH38 = "GRCh38"
    REFSEQ_GENE = "RefSeqGene"
    REFSEQ_TRANSCRIPT = "RefSeqTranscript"

class ReferenceLocationType(str, Enum):
    ATG_START = "ATG Start"
    SEQUENCE_START = "Sequence Start"

class VariantBaseSequence(str, Enum):
    A = "A"
    C = "C"
    G = "G"
    T = "T"

class ReferenceSequence(str, Enum):
    # too many possibilities
    pass

class FilterError(Enum):
    INVALID_ATTRS = "Invalid attribute(s): {}"
    TYPE_MISMATCH = "Type mismatch for {}: expected {}, got {}"

class QueryParameters(Enum):
    GENE_SYMBOL = "gene-symbol"
    IDENTIFIER = "identifier"
    EXCLUDE_SUB_ALLELES = "exclude-sub-alleles"
    FUNCTION = "function"
    INCLUDE_REFERENCE_VARIANTS = "include-reference-variants"
    INCLUDE_RETIRED_ALLELES = "include-retired-alleles"
    INCLUDE_RETIRED_REFERENCE_SEQUENCES = "include-retired-reference-sequences"
    MIN_EVIDENCE_LEVEL = "min-evidence-level"
    POSITION = "position"
    REFERENCE_BASE_SEQUENCE = "reference-base-sequence"
    REFERENCE_COLLECTION = "reference-collection"
    REFERENCE_LOCATION_TYPE = "reference-location-type"
    REFERENCE_SEQUENCE = "reference-sequence"
    VARIANT_BASE_SEQUENCE = "variant-base-sequence"