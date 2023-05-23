import abc

from pyhafas.types.fptf import Remark


class ParseRemarkHelperInterface(abc.ABC):
    @abc.abstractmethod
    def parse_remark(
            self,
            remark: dict,
            common: dict) -> Remark:
        """
        Parses Remark HaFAS returns into Remark object

        :param remark: Remark object given back by HaFAS
        :param common:  Common object given back by HaFAS
        :return: Parsed Remark object
        """
        pass
