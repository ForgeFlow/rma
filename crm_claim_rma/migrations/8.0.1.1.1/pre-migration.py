# -*- coding: utf-8 -*-
# © 2018 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html)
from openupgradelib import openupgrade

column_copies = {

    'crm_claim': [
                  ('claim_type', None, None),
                  ],
}


def migrate(cr, version):
    openupgrade.copy_columns(cr, column_copies)
