from enum import Enum

class BaseEnum(Enum):
    @classmethod
    def get_valid_values(cls):
        return [member.value for member in cls]

class ExcludeSubAlleles(BaseEnum):
    TRUE = True
    FALSE = False
    DEFAULT = False

class IncludeReferenceVariants(BaseEnum):
    TRUE = True
    FALSE = False
    DEFAULT = False

class IncludeRetiredAlleles(BaseEnum):
    TRUE = True
    FALSE = False
    DEFAULT = False

class IncludeRetiredReferenceSequences(BaseEnum):
    TRUE = True
    FALSE = False
    DEFAULT = False

class Function(BaseEnum):
    DECREASED = "decreased function"
    NOT_ASSIGNED = "function not assigned"
    INCREASED = "increased function"
    NORMAL = "normal function"  
    POSSIBLY_DECREASED = "possibly decreased"
    SEVERELY_DECREASED = "severely decreased"
    UNCERTAIN = "uncertain function"
    UNKNOWN = "unknown function"
    DEFAULT = None

class EvidenceLevel(BaseEnum):
    DEFINITIVE = "Definitive"
    LIMITED = "Limited"
    MODERATE = "Moderate"
    DEFAULT = None

class Position(BaseEnum):
    DEFAULT = None

class ReferenceBaseSequence(BaseEnum):
    A = "A"
    C = "C"
    G = "G"
    T = "T"
    DEFAULT = None

class ReferenceCollection(BaseEnum):
    GRCH37 = "GRCh37"
    GRCH38 = "GRCh38"
    REFSEQ_GENE = "RefSeqGene"
    REFSEQ_TRANSCRIPT = "RefSeqTranscript"
    DEFAULT = "GRCh38"

class ReferenceLocationType(BaseEnum):
    ATG_START = "ATG Start"
    SEQUENCE_START = "Sequence Start"
    DEFAULT = None

class VariantBaseSequence(BaseEnum):
    A = "A"
    C = "C"
    G = "G"
    T = "T"
    DEFAULT = None

class ReferenceSequence(BaseEnum):
    DEFAULT = None

class FilterError(BaseEnum):
    INVALID_ATTRS = "Invalid attribute(s): {}"
    TYPE_MISMATCH = "Type mismatch for {}: expected {}, got {}"

class QueryParameters(BaseEnum):
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

class ValidationRule(BaseEnum):
    EXCLUDE_SUB_ALLELES = {
        "parameter": QueryParameters.EXCLUDE_SUB_ALLELES.value,
        "valid_values": ExcludeSubAlleles.get_valid_values(),
        "error_message": f"Invalid value for exclude-sub-alleles parameter. Valid values are: {ExcludeSubAlleles.get_valid_values()}."
    }
    REFERENCE_COLLECTION = {
        "parameter": QueryParameters.REFERENCE_COLLECTION.value,
        "valid_values": ReferenceCollection.get_valid_values(),
        "error_message": f"Invalid value for reference-collection parameter. Valid values are: {ReferenceCollection.get_valid_values()}."
    }
    REFERENCE_BASE_SEQUENCE = {
        "parameter": QueryParameters.REFERENCE_BASE_SEQUENCE.value,
        "valid_values": ReferenceBaseSequence.get_valid_values(),
        "error_message": f"Invalid value for reference-base-sequence parameter. Valid values are: {ReferenceBaseSequence.get_valid_values()}."
    }
    REFERENCE_LOCATION_TYPE = {
        "parameter": QueryParameters.REFERENCE_LOCATION_TYPE.value,
        "valid_values": ReferenceLocationType.get_valid_values(),
        "error_message": f"Invalid value for reference-location-type parameter. Valid values are: {ReferenceLocationType.get_valid_values()}."
    }
    FUNCTION = {
        "parameter": QueryParameters.FUNCTION.value,
        "valid_values": Function.get_valid_values(),
        "error_message": f"Invalid value for function parameter. Valid values are: {Function.get_valid_values()}."
    }
    INCLUDE_REFERENCE_VARIANTS = {
        "parameter": QueryParameters.INCLUDE_REFERENCE_VARIANTS.value,
        "valid_values": IncludeReferenceVariants.get_valid_values(),
        "error_message": f"Invalid value for include-reference-variants parameter. Valid values are: {IncludeReferenceVariants.get_valid_values()}."
    }
    INCLUDE_RETIRED_ALLELES = {
        "parameter": QueryParameters.INCLUDE_RETIRED_ALLELES.value,
        "valid_values": IncludeRetiredAlleles.get_valid_values(),
        "error_message": f"Invalid value for include-retired-alleles parameter. Valid values are: {IncludeRetiredAlleles.get_valid_values()}."
    }
    INCLUDE_RETIRED_REFERENCE_SEQUENCES = {
        "parameter": QueryParameters.INCLUDE_RETIRED_REFERENCE_SEQUENCES.value,
        "valid_values": IncludeRetiredReferenceSequences.get_valid_values(),
        "error_message": f"Invalid value for include-retired-reference-sequences parameter. Valid values are: {IncludeRetiredReferenceSequences.get_valid_values()}."
    }
    MIN_EVIDENCE_LEVEL = {
        "parameter": QueryParameters.MIN_EVIDENCE_LEVEL.value,
        "valid_values": EvidenceLevel.get_valid_values(),
        "error_message": f"Invalid value for min-evidence-level parameter. Valid values are: {EvidenceLevel.get_valid_values()}."
    }
    POSITION = {
        "parameter": QueryParameters.POSITION.value,
        "error_message": f"position parameter must be a positive integer or None.",
        "validator": lambda x: isinstance(x, int) and x > 0 if x is not None else True
    }
    # has no values, but needs to be a string or None
    REFERENCE_SEQUENCE = {
        "parameter": QueryParameters.REFERENCE_SEQUENCE.value,
        "error_message": f"Invalid value for reference-sequence parameter. Valid values are: {ReferenceSequence.get_valid_values()}.",
        "validator": lambda x: isinstance(x, str) or x is None
    }

    @classmethod
    def get_rule_parameters(cls):
        return [rule.value["parameter"] for rule in cls]
    @classmethod
    def get_rule(cls, parameter):
        for rule in cls:
            if rule.value["parameter"] == parameter:
                return rule.value
        return None
