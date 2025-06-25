from typing import Optional, Dict
import logging
from exceptions.exceptions import InvalidArgumentError
from api import RestAdapter, VariantEndpoint, AlleleEndPoint
from models import Variant, VariantCollection, AlleleCollection
from config import APIConfig
from enums.enums import QueryParameters, IncludeReferenceVariants, IncludeRetiredAlleles, IncludeRetiredReferenceSequences, Function, EvidenceLevel, ReferenceBaseSequence, ReferenceCollection, ReferenceLocationType, VariantBaseSequence, Position, ReferenceSequence, ExcludeSubAlleles
class PharmVarApi:
    """
    PharmVarApi is a class that provides methods to interact with the PharmVar API.
    It uses a RestAdapter object to make HTTP requests to the API server.
    The class provides methods to get variants, alleles and genes from the PharmVar database.
    """    
    # Initialize the PharmVarApi object with a RestAdapter object
    def __init__(self, hostname: str = APIConfig.DEFAULT_HOST, api_key: str = '', ver: str = APIConfig.DEFAULT_VERSION, logger: logging.Logger = APIConfig.DEFAULT_LOGGER):
        self._rest_adapter = RestAdapter(hostname, api_key, ver, logger)
    
    # Variant methods

    def get_all_variants(self) -> VariantCollection:

        ### TODO: add parameters
        """
        Get all variants from the PharmVar database.
        return: VariantCollection object containing all variants
        """

        result = self._rest_adapter._do(http_method = 'GET', endpoint = VariantEndpoint.ALL.value)
        return VariantCollection(data = result.data)


    def get_variants_by_gene(self,
                            gene_symbol: str,
                            include_reference_variants: bool = IncludeReferenceVariants.DEFAULT.value,
                            include_retired_reference_sequences: bool = IncludeRetiredReferenceSequences.DEFAULT.value,
                            position: int | None = Position.DEFAULT.value,
                            reference_base_sequence: str | None = ReferenceBaseSequence.DEFAULT.value,
                            reference_collection: str | None = ReferenceCollection.DEFAULT.value,
                            reference_location_type: str | None = ReferenceLocationType.DEFAULT.value,
                            reference_sequence: str | None = ReferenceSequence.DEFAULT.value,
                            variant_base_sequence: str | None = VariantBaseSequence.DEFAULT.value
                            ) -> VariantCollection:
        """
        Get all variants for a given gene symbol.
        :param gene_symbol: The gene symbol to search for
        :param include_reference_variants: Include reference variants like A>A or C>C. Default is False.
        :param include_retired_reference_sequences: Include variants from retired reference sequences. Default is False.
        :param position: Filter results by variant position.
        :param reference_base_sequence: Filter by reference base sequence (A, C, G, T).
        :param reference_collection: Filter by reference collection (GRCh37, GRCh38, etc.).
        :param reference_location_type: Filter by reference starting location.
        :param reference_sequence: Filter by reference sequence (e.g., "NG_008376.4").
        :param variant_base_sequence: Filter by observed variant base sequence (A, C, G, T).
        :return: VariantCollection object containing all variants for the gene
        """

        params = {
            QueryParameters.INCLUDE_REFERENCE_VARIANTS: include_reference_variants,
            QueryParameters.INCLUDE_RETIRED_REFERENCE_SEQUENCES: include_retired_reference_sequences,
            QueryParameters.POSITION: position,
            QueryParameters.REFERENCE_BASE_SEQUENCE: reference_base_sequence,
            QueryParameters.REFERENCE_COLLECTION: reference_collection,
            QueryParameters.REFERENCE_LOCATION_TYPE: reference_location_type,
            QueryParameters.REFERENCE_SEQUENCE: reference_sequence,
            QueryParameters.VARIANT_BASE_SEQUENCE: variant_base_sequence
        }


        endpoint = VariantEndpoint.GENE.value.format(symbol = gene_symbol)
        result = self._rest_adapter._do(http_method = 'GET', endpoint = endpoint, params = params)
        return VariantCollection(data = result.data)

    def get_variants_by_allele(self, identifier: str,
                                include_reference_variants: bool = IncludeReferenceVariants.DEFAULT.value,
                                include_retired_alleles: bool = IncludeRetiredAlleles.DEFAULT.value,
                                include_retired_reference_sequences: bool = IncludeRetiredReferenceSequences.DEFAULT.value,
                                position: int | None = Position.DEFAULT.value,
                                reference_base_sequence: str | None = ReferenceBaseSequence.DEFAULT.value,
                                reference_collection: str | None = ReferenceCollection.DEFAULT.value,
                                reference_location_type: str | None = ReferenceLocationType.DEFAULT.value,
                                reference_sequence: str | None = ReferenceSequence.DEFAULT.value,
                                variant_base_sequence: str | None = VariantBaseSequence.DEFAULT.value
                               ) -> VariantCollection:
        """
        Get all variants for a given identifier.
        :param identifier: can be either a PharmVar ID or an allele name. Required
        :param include_reference_variants: Include reference variants like A>A or C>C. Default is False.
        :param include_retired_alleles: Include retired allele definitions from previous versions. Default is False.
        :param include_retired_reference_sequences: Include variants from retired reference sequences. Default is False.
        :param position: Filter results by variant position.
        :param reference_base_sequence: Filter by reference base sequence (A, C, G, T).
        :param reference_collection: Filter by reference collection (GRCh37, GRCh38, etc.).
        :param reference_location_type: Filter by reference starting location.
        :param reference_sequence: Filter by reference sequence (e.g., "NG_008376.4").
        :param variant_base_sequence: Filter by observed variant base sequence (A, C, G, T).
        :return: VariantCollection object containing all variants for the identifier.
        """
        params = {
            QueryParameters.INCLUDE_REFERENCE_VARIANTS.value: include_reference_variants,
            QueryParameters.INCLUDE_RETIRED_ALLELES.value: include_retired_alleles,
            QueryParameters.INCLUDE_RETIRED_REFERENCE_SEQUENCES.value: include_retired_reference_sequences,
            QueryParameters.POSITION.value: position,
            QueryParameters.REFERENCE_BASE_SEQUENCE.value: reference_base_sequence,
            QueryParameters.REFERENCE_COLLECTION.value: reference_collection,
            QueryParameters.REFERENCE_LOCATION_TYPE.value: reference_location_type,
            QueryParameters.REFERENCE_SEQUENCE.value: reference_sequence,
            QueryParameters.VARIANT_BASE_SEQUENCE.value: variant_base_sequence
        }

        endpoint = VariantEndpoint.ALLELE.value.format(identifier = identifier)
        result = self._rest_adapter._do(http_method = 'GET', endpoint = endpoint, params = params)
        return VariantCollection(data = result.data)
    
    def get_variants_by_rsid(self, rs_id: str,
                            include_reference_variants: bool = IncludeReferenceVariants.DEFAULT.value,
                            include_retired_reference_sequences: bool = IncludeRetiredReferenceSequences.DEFAULT.value,
                            position: int | None = Position.DEFAULT.value,
                            reference_base_sequence: str | None = ReferenceBaseSequence.DEFAULT.value,
                            reference_collection: str | None = ReferenceCollection.DEFAULT.value,
                            reference_location_type: str | None = ReferenceLocationType.DEFAULT.value,
                            reference_sequence: str | None = ReferenceSequence.DEFAULT.value,
                            variant_base_sequence: str | None = VariantBaseSequence.DEFAULT.value
                            ) -> VariantCollection:
        """
        Get all variants for a given rsID.
        :param rs_id: The rsId of the variant
        :param include_reference_variants: Include reference variants like A>A or C>C. Default is False.
        :param include_retired_reference_sequences: Include variants from retired reference sequences. Default is False.
        :param position: Filter results by variant position.
        :param reference_base_sequence: Filter by reference base sequence (A, C, G, T).
        :param reference_collection: Filter by reference collection (GRCh37, GRCh38, etc.). Default is GRCh38.
        :param reference_location_type: Filter by reference starting location.
        :param reference_sequence: Filter by reference sequence (e.g., "NG_008376.4").
        :param variant_base_sequence: Filter by observed variant base sequence (A, C, G, T).
        :return: VariantCollection object containing all variants for the rsID
        """
        params = {
            QueryParameters.INCLUDE_REFERENCE_VARIANTS.value: include_reference_variants,
            QueryParameters.INCLUDE_RETIRED_REFERENCE_SEQUENCES.value: include_retired_reference_sequences,
            QueryParameters.POSITION.value: position,
            QueryParameters.REFERENCE_BASE_SEQUENCE.value: reference_base_sequence,
            QueryParameters.REFERENCE_COLLECTION.value: reference_collection,
            QueryParameters.REFERENCE_LOCATION_TYPE.value: reference_location_type,
            QueryParameters.REFERENCE_SEQUENCE.value: reference_sequence,
            QueryParameters.VARIANT_BASE_SEQUENCE.value: variant_base_sequence
        }

        endpoint = VariantEndpoint.RSID.value.format(rsId = rs_id)
        result = self._rest_adapter._do(http_method = 'GET', endpoint = endpoint, params = params)
        return VariantCollection(data = result.data)
    
    def get_variants_by_spdi(self, spdi: str) -> VariantCollection:
        """
        Get all variants for a given SPDI.
        :param spdi: the SPDI designation of a variant: Reference Sequence:Position:Deletion:Insertion
        :return: VariantCollection object containing all variants for the SPDI
        """
        endpoint = VariantEndpoint.SPDI.value.format(spdi = spdi)
        result = self._rest_adapter._do(http_method = 'GET', endpoint = endpoint)
        return VariantCollection(data = result.data)
    
    def get_variant_impact(self, *, rs_id: str = None, spdi: str = None) -> str:
        """
        Get the impact of a variant for a given rsID or SPDI.
        :param rs_id: The rsId of the variant
        :param spdi: the SPDI designation of a variant: Reference Sequence:Position:Deletion:Insertion
        :return: VariantCollection object containing the impact of the variant for the rsID
        """
        if rs_id is not None and spdi is not None:
            raise InvalidArgumentError("Only one of rs_id or spdi can be provided, not both")

        if rs_id is not None:
            endpoint = VariantEndpoint.RSID_IMPACT.value.format(rsId=rs_id)
        elif spdi is not None:
            endpoint = VariantEndpoint.SPDI_IMPACT.value.format(spdi= spdi)
        else:
            raise InvalidArgumentError("Either rs_id or spdi must be provided.")

        result = self._rest_adapter._do(http_method = "GET", endpoint = endpoint, headers={"Accept": "*/*"})
        # Save in Variant instance with rs_id or spdi and impact
        variant = Variant(impact = result.data, rsId = rs_id,
                        referenceSequence = spdi.split(":")[0] if spdi else None,
                        position = spdi.split(":")[1] if spdi else None
                        )
        return variant.impact
    
        # Allele methods

    def get_all_alleles(
            self,
            exclude_sub_alleles: bool = ExcludeSubAlleles.DEFAULT.value,
            function: str | None = Function.DEFAULT.value,
            include_reference_variants: bool = IncludeReferenceVariants.DEFAULT.value,
            include_retired_alleles: bool = IncludeRetiredAlleles.DEFAULT.value,
            include_retired_reference_sequences: bool = IncludeRetiredReferenceSequences.DEFAULT.value,
            min_evidence_level: str | None = EvidenceLevel.DEFAULT.value,
            position: int | None = Position.DEFAULT.value,
            reference_base_sequence: str | None = ReferenceBaseSequence.DEFAULT.value,
            reference_collection: str | None = ReferenceCollection.DEFAULT.value,
            reference_location_type: str | None = ReferenceLocationType.DEFAULT.value,
            reference_sequence: str | None = ReferenceSequence.DEFAULT.value,
            variant_base_sequence: str | None = VariantBaseSequence.DEFAULT.value
        ) -> AlleleCollection:
            """
            Get all alleles from the PharmVar database with optional filtering parameters.

            Parameters:
                exclude_sub_alleles (bool): Exclude sub-allele definitions from results. Default is False.
                function (Function): Filter results by function (decreased function, function not assigned, increased function, normal function, possibly decreased, severely decreased, uncertain function, unknown function).
                include_reference_variants (bool): Include reference variants like A>A or C>C. Default is False.
                include_retired_alleles (bool): Include retired allele definitions from previous versions. Default is False.
                include_retired_reference_sequences (bool): Include variants from retired reference sequences. Default is False.
                min_evidence_level (EvidenceLevel): Filter by minimum evidence level (Definitive, Limited, Moderate).
                position (int): Filter results by variant position.
                reference_base_sequence (ReferenceBase): Filter by reference base sequence (A, C, G, T).
                reference_collection (ReferenceCollection): Filter by reference collection (GRCh37, GRCh38, etc.).
                reference_location_type (ReferenceLocationType): Filter by reference starting location.
                reference_sequence (str): Filter by reference sequence (e.g., "NG_008376.4").
                variant_base_sequence (ReferenceBase): Filter by observed variant base sequence (A, C, G, T).

            Returns:
                AlleleCollection: Collection of alleles matching the specified criteria
            """
            params = {
                QueryParameters.EXCLUDE_SUB_ALLELES.value: exclude_sub_alleles,
                QueryParameters.INCLUDE_REFERENCE_VARIANTS.value: include_reference_variants,
                QueryParameters.INCLUDE_RETIRED_ALLELES.value: include_retired_alleles,
                QueryParameters.INCLUDE_RETIRED_REFERENCE_SEQUENCES.value: include_retired_reference_sequences
            }

            # Add optional parameters if they are provided
            if function:
                params[QueryParameters.FUNCTION.value] = function
            if min_evidence_level:
                params[QueryParameters.MIN_EVIDENCE_LEVEL.value] = min_evidence_level
            if position:
                params[QueryParameters.POSITION.value] = position
            if reference_base_sequence:
                params[QueryParameters.REFERENCE_BASE_SEQUENCE.value] = reference_base_sequence
            if reference_collection:
                params[QueryParameters.REFERENCE_COLLECTION.value] = reference_collection
            if reference_location_type:
                params[QueryParameters.REFERENCE_LOCATION_TYPE.value] = reference_location_type
            if reference_sequence:
                params[QueryParameters.REFERENCE_SEQUENCE.value] = reference_sequence
            if variant_base_sequence:
                params[QueryParameters.VARIANT_BASE_SEQUENCE.value] = variant_base_sequence

            result = self._rest_adapter._do(
                http_method='GET', 
                endpoint=AlleleEndPoint.ALL.value,
                params=params
            )
            
            return AlleleCollection(data=result.data)
    
    # Gene methods

    # other methods
    # def _validate_parameters(self, **kwargs):
    #     """
    #     Validate the parameters passed to the method.
    #     :param kwargs: A dictionary of keyword arguments
    #     :return: None
    #     """
    #     valid_attrs = self._get_items()[0].__dict__.keys()
    #     invalid_attrs = [k for k in kwargs if k not in valid_attrs]
    #     if invalid_attrs:
    #         raise ValidationError(f"Invalid attribute {invalid_attrs} for {self._validate_parameters.__name__}")



    def _validate_parameters(self, params: Dict):
        """
        # Validate API parameters before making requests
        
        # Args:
        #     params: Dictionary of parameters to validate
            
        # Raises:
        #     ParameterValidationError if any parameter is invalid
        # """
    # Map from API parameter names (with hyphens) to their validation rules
        validation_rules = {
            "reference-collection": {
                "valid_values": ["GRCh37", "GRCh38"],
                "error_msg": "Invalid reference collection. Valid options are: GRCh37, GRCh38"
            },
            "reference-base-sequence": {
                "valid_values": ["A", "C", "G", "T"],
                "error_msg": "Invalid reference base sequence. Valid options are: A, C, G, T"
            },
            "variant-base-sequence": {
                "valid_values": ["A", "C", "G", "T"],
                "error_msg": "Invalid variant base sequence. Valid options are: A, C, G, T"
            },
            "position": {
                "validator": lambda x: isinstance(x, int) and x > 0 if x is not None else True,
                "error_msg": "Position must be a positive integer"
            }
        }
        
        # Clean params by removing None values
        clean_params = {k: v for k, v in params.items() if v is not None}
        
        for param_name, param_value in clean_params.items():
            # Skip validation for parameters not in our validation rules
            if param_name not in validation_rules:
                continue
                
            rule = validation_rules[param_name]
            
            # Check against valid values list if provided
            if "valid_values" in rule and param_value is not None:
                if param_value not in rule["valid_values"]:
                    raise ValueError(rule["error_msg"])
            
            # Run custom validator function if provided
            if "validator" in rule and param_value is not None:
                if not rule["validator"](param_value):
                    raise ValueError(rule["error_msg"])