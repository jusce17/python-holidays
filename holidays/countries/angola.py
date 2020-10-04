# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2020
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd, TU

from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, \
    NOV, DEC
from holidays.constants import WEEKEND, TUE,  THU


from holidays.holiday_base import HolidayBase


class Angola(HolidayBase):
    """
    https://en.wikipedia.org/wiki/Public_holidays_in_Angola

    http://www.siac.gv.ao/downloads/181029-Lei-Feriados.pdf
    """



    def __init__(self, **kwargs):
        self.country = 'AO'
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        self[date(year, JAN, 1)] = "Ano novo"

        self[date(year, FEB, 4)] = "Dia do Início da Luta Armada"

        self[date(year, MAR, 8)] = "Dia Internacional da Mulher"

        self[date(year, MAR, 23)] = "Dia da Libertação da África Austral"

        self[date(year, APR, 4)] = "Dia da Paz e Reconciliação"

        self[date(year, MAY, 1)] = "Dia Mundial do Trabalho"

        self[date(year, SEP, 17)] = "Dia Nacional dos Heróis"

        self[date(year, NOV, 2)] = "Dia dos Finados"

        self[date(year, NOV, 11)] = "Dia da Independência"

        # Christmas Day
        self[date(year, DEC, 25)] = "Natal"

        self[easter(year) - rd(days=2)] = "Sexta-feira Santa"

        self[easter(year)] = "Páscoa"


        quaresma = easter(year) - rd(days=46)

        self[quaresma - rd(weekday=TU(-1))] = "Carnaval"





class AO(Angola):
    pass


class AGO(Angola):
    pass
