"""This file was generated by xsdata, v23.6, on 2023-06-27 01:20:37

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass
from nfelib.cte.bindings.v4_0.cte_tipos_basico_v4_00 import Tgtve

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class Gtve(Tgtve):
    """
    Guia de Trasnsporte Eletrônica.
    """
    class Meta:
        name = "GTVe"
        namespace = "http://www.portalfiscal.inf.br/cte"