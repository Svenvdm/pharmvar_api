import logging
import requests
import requests.packages
from typing import List, Dict, Optional
from exceptions import InvalidArgumentError
from models import Result, Variant, VariantCollection
from json import JSONDecodeError
from rest_adapter import RestAdapter
from endpoints import VariantEndpoint

class PharmVarApi:
    def __init__(self, hostname: str = "www.pharmvar.org/api-service", api_key: str = '', ver: str = '0.1', ssl_verify: bool = True, logger: logging.Logger = None):
        self._rest_adapter = RestAdapter(hostname, api_key, ver, ssl_verify, logger)

    def get_all_variants(self) -> VariantCollection:
        """
        Get all variants from the PharmVar database.
        :return: VariantCollection object containing all variants
        """

        result = self._rest_adapter._do(http_method = 'GET', endpoint = VariantEndpoint.ALL.value)
        return VariantCollection(data = result.data)


    def get_variants_by_gene(self, gene_symbol: str) -> VariantCollection:
        """
        Get all variants for a given gene symbol.
        :param gene_symbol: The gene symbol to search for
        :return: VariantCollection object containing all variants for the gene
        """
        endpoint = VariantEndpoint.GENE.value.format(symbol = gene_symbol)
        result = self._rest_adapter._do(http_method = 'GET', endpoint = endpoint)
        return VariantCollection(data = result.data)

    def get_variants_by_allele(self, identifier: str) -> VariantCollection:
        """
        Get all variants for a given identifier.
        :param identifier: can be either a PharmVar ID or an allele name.
        :return: VariantCollection object containing all variants for the identifier.
        """
        endpoint = VariantEndpoint.ALLELE.value.format(identifier = identifier)
        result = self._rest_adapter._do(http_method = 'GET', endpoint = endpoint)
        return VariantCollection(data = result.data)
    
    def get_variants_by_rsid(self, rs_id: str) -> VariantCollection:
        """
        Get all variants for a given rsID.
        :param rs_id: The rsId of the variant
        :return: VariantCollection object containing all variants for the rsID
        """
        endpoint = VariantEndpoint.RSID.value.format(rsId = rs_id)
        result = self._rest_adapter._do(http_method = 'GET', endpoint = endpoint)
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
            endpoint = VariantEndpoint.SPDI_IMPACT.value.format(spdi=spdi)
        else:
            raise InvalidArgumentError("Either rs_id or spdi must be provided.")

        result = self._rest_adapter._do(http_method = "GET", endpoint = endpoint, headers = {"Accept" : "text/plain"})

   
