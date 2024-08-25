from typing import List, Dict
   

class Result:
    def __init__(self, status_code: int, message: str = "", data: List[Dict] = None):
        """
        Result returned from low-level RestAdapter
        :param status_code: Standard HTTP Status code
        :param message: Human readable result
        :param data: Python List of Dictionaries (or maybe just a single Dictionary on error)
        """
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data if data else []


class Variant:
    def __init__(self, hgvs: str, impact: str, position: str, referenceCollections: List[str], referenceLocation: str, referenceSequence: str, rsId: str, url: str, variantFrequency: List[Dict], variantId: str):
        """
        Represents a variant
        :param hgvs: The HGVS syntax for the variant
        :param impact: The amino acid impact for the variant
        :param position: The Position String for the variant as it is stored in the PharmVar database
        :param reference_collections: List of reference collections
        :param reference_location: The reference location type defining the start position for counting
        :param reference_sequence: The reference sequence for the variant
        :param rs_id: The RS ID Number for the variant
        :param url: The PharmVar URL for the variant
        :param variant_frequency: List of variant frequencies
        :param variant_id: The transient variant ID used for identifying corresponding positions across multiple reference sequences
        """
        self.hgvs = hgvs
        self.impact = impact
        self.position = position
        self.reference_collections = referenceCollections
        self.reference_location = referenceLocation
        self.reference_sequence = referenceSequence
        self.rs_id = rsId
        self.url = url
        self.variant_frequency = variantFrequency
        self.variant_id = variantId

    def __repr__(self) -> str:
        return f"Variant(hgvs={self.hgvs}, impact={self.impact}, position={self.position}, reference_collections={self.reference_collections}, reference_location={self.reference_location}, reference_sequence={self.reference_sequence}, rs_id={self.rs_id}, url={self.url}, variant_frequency={self.variant_frequency}, variant_id={self.variant_id})"

class VariantCollection:
    def __init__(self, data: List[Dict]):
        """
        Represents a list of variants
        :param variants: List of Variant objects
        """
        self.variants = [Variant(**variant) for variant in data]

    ## create method that gets all the variants with an impact.
    

    def __len__(self) -> int:
        return len(self.variants)

    def __getitem__(self, index: int) -> Variant:
        return self.variants[index]

    def __iter__(self):
        return iter(self.variants)

    def __repr__(self) -> str:
        return f"VariantList(variants={self.variants})"