"""This file was generated by xsdata, v23.6, on 2023-06-28 18:36:32

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass
from nfelib.cte.bindings.v4_0.evento_cte_tipos_basico_v4_00 import Tevento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class EventoCte(Tevento):
    """
    Schema XML de validação do Pedido de Registro de Evento do CT-e.
    """
    class Meta:
        name = "eventoCTe"
        namespace = "http://www.portalfiscal.inf.br/cte"
