from enum import Enum

class VariantEndpoint(Enum):
    ALL = "variants"
    ALLELE = "variants/allele/{identifier}"
    GENE = "variants/gene/{symbol}"
    RSID = "variants/rsid/{rsId}"
    RSID_IMPACT = "variants/rsid/{rsId}/impact"
    RSID_FREQUENCY = "variants/rsid/{rsId}/variant-frequency"
    SPDI = "variants/spdi/{spdi}"   
    SPDI_IMPACT = "variants/spdi/{spdi}/impact"
    SPDI_FREQUENCY = "variants/spdi/{spdi}/variant-frequency"

