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
    Official Holidays in Angola in their current form
    Source1: https://en.wikipedia.org/wiki/Public_holidays_in_Angola
    Source2: http://www.siac.gv.ao/downloads/181029-Lei-Feriados.pdf
    """



    def __init__(self, **kwargs):
        self.country = 'AO'
        HolidayBase.__init__(self, **kwargs)

    def _long_weekends(self, description, full_date):
        """
        According to the most recently low in Angola:
        If the holidays happens to be on a Tuesday, the Monday before that is a holiday as well,
        If it happens to be on a Thursday, the Friday before it is a Holiday as well
        """

        if date(*full_date).weekday() in WEEKEND:
            pass
        elif date(*full_date).weekday() == TUE:
            self[date(*full_date)] = description
            self[date(*full_date) - rd(days=1)] = description + " (Ponte antes do feriado)"

        elif date(*full_date).weekday() == THU:
            self[date(*full_date)] = description
            self[date(*full_date) + rd(days=1)] = description + " (Ponte depois do feriado)"
        else:
            self[date(*full_date)] = description





    def _populate(self, year):
        # New Year's Day
        self._long_weekends("Ano novo", [year, JAN, 1])

        self._long_weekends("Dia do Início da Luta Armada", [year, FEB, 4])

        self._long_weekends("Dia Internacional da Mulher",[year, MAR, 8])

        self._long_weekends("Dia da Libertação da África Austral",[year, MAR, 23])

        self._long_weekends("Dia da Paz e Reconciliação",[year, APR, 4 ])

        self._long_weekends("Dia Mundial do Trabalho",[year, MAY, 1])

        self._long_weekends("Dia do Herói Nacional",[ year, SEP, 17 ])

        self._long_weekends("Dia dos Finados",[year, NOV, 2])

        self._long_weekends("Dia da Independência",[ year, NOV, 11 ])

        # Christmas Day
        self._long_weekends("Dia de Natal e da Família",[year, DEC, 25 ])

        self[easter(year) - rd(days=2)] = "Sexta-feira Santa"
        self[easter(year)] = "Páscoa"
        quaresma = easter(year) - rd(days=46)
        self[quaresma - rd(weekday=TU(-1))] = "Carnaval"





class AO(Angola):
    pass


class AGO(Angola):
    pass
