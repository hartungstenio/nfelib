"""This file was generated by xsdata, v23.6, on 2023-06-28 18:36:30

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass
from nfelib.nfe_entrega.bindings.v1_0.leiaute_evento_entrega_nfe_v1_00 import TprocEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class ProcEventoNfe(TprocEvento):
    """
    Schema XML de validação do proc Comprovante de Entrega da NFe.
    """
    class Meta:
        name = "procEventoNFe"
        namespace = "http://www.portalfiscal.inf.br/nfe"
