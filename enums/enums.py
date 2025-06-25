from enum import Enum

class ExcludeSubAlleles(Enum):
    TRUE = True
    FALSE = False
    DEFAULT = False

class IncludeReferenceVariants(Enum):
    TRUE = True
    FALSE = False
    DEFAULT = False

class IncludeRetiredAlleles(Enum):
    TRUE = True
    FALSE = False
    DEFAULT = False

class IncludeRetiredReferenceSequences(Enum):
    TRUE = True
    FALSE = False
    DEFAULT = False

class Function(Enum):
    DECREASED = "decreased function"
    NOT_ASSIGNED = "function not assigned"
    INCREASED = "increased function"
    NORMAL = "normal function"  
    POSSIBLY_DECREASED = "possibly decreased"
    SEVERELY_DECREASED = "severely decreased"
    UNCERTAIN = "uncertain function"
    UNKNOWN = "unknown function"
    DEFAULT = None

class EvidenceLevel(Enum):
    DEFINITIVE = "Definitive"
    LIMITED = "Limited"
    MODERATE = "Moderate"
    DEFAULT = None

class Position(Enum):
    DEFAULT = None

class ReferenceBaseSequence(Enum):
    A = "A"
    C = "C"
    G = "G"
    T = "T"
    DEFAULT = None

class ReferenceCollection(Enum):
    GRCH37 = "GRCh37"
    GRCH38 = "GRCh38"
    REFSEQ_GENE = "RefSeqGene"
    REFSEQ_TRANSCRIPT = "RefSeqTranscript"
    DEFAULT = "GRCh38"

class ReferenceLocationType(Enum):
    ATG_START = "ATG Start"
    SEQUENCE_START = "Sequence Start"
    DEFAULT = None

class VariantBaseSequence(Enum):
    A = "A"
    C = "C"
    G = "G"
    T = "T"
    DEFAULT = None

class ReferenceSequence(Enum):
    DEFAULT = None

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