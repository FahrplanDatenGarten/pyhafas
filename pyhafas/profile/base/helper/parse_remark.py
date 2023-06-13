from pyhafas.profile import ProfileInterface
from pyhafas.profile.interfaces.helper.parse_remark import ParseRemarkHelperInterface
from pyhafas.types.fptf import Remark


class BaseParseRemarkHelper(ParseRemarkHelperInterface):
    def parse_remark(self: ProfileInterface, remark: dict, common: dict) -> Remark:
        """
        Parses Remark HaFAS returns into Remark object

        :param remark: Remark object given back by HaFAS
        :param common: Common object given back by HaFAS
        :return: Parsed Remark object
        """

        rem = Remark(
            remark_type=remark.get('type'),
            code=remark.get('code') if remark.get('code') != "" else None,
            subject=remark.get('txtS') if remark.get('txtS') != "" else None,
            text=remark.get('txtN') if remark.get('txtN') != "" else None,
            priority=remark.get('prio'),
            trip_id=remark.get('jid'),
        )
        # print(rem, remark)
        return rem
