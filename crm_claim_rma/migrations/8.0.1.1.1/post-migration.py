# -*- coding: utf-8 -*-
# © 2018 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html)
from openupgradelib import openupgrade


def set_type(cr):
    cr.execute("""
        update crm_claim set claim_type = 1
        where %s = 'customer' 
    """ % openupgrade.get_legacy_name('claim_type'))
    cr.execute("""
        update crm_claim set claim_type = 2
        where %s = 'supplier' 
    """ % openupgrade.get_legacy_name('claim_type'))
    cr.execute("""
        update crm_claim set claim_type = 3
        where %s = 'other' 
    """ % openupgrade.get_legacy_name('claim_type'))


@openupgrade.migrate(use_env=False)
def migrate(cr, version):
    set_type(cr)
