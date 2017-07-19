# -*- coding: utf-8 -*-
# © 2017 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html)

from openerp import api, fields, models


class RmaOrder(models.Model):
    _inherit = "rma.order"

    @api.onchange('partner_id')
    def _testing(self):
        pass


class RmaOrderLine(models.Model):
    _inherit = "rma.order.line"

    qc_issue_id = fields.Many2one(
        comodel_name="qc.issue", string="Quality Control Issue")

    @api.onchange('product_id')
    def _testing(self):
        pass
