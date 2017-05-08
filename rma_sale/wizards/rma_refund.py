# -*- coding: utf-8 -*-
# © 2017 Eficent Business and IT Consulting Services S.L.
# © 2015 Eezee-It, MONK Software, Vauxoo
# © 2013 Camptocamp
# © 2009-2013 Akretion,
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html)
from openerp import models, fields, exceptions, api, _
import openerp.addons.decimal_precision as dp
from openerp.exceptions import UserError


class RmaRefund(models.TransientModel):
    _inherit = "rma.refund"

    @api.returns('rma.order.line')
    def _prepare_item(self, line):
        res = super(RmaRefund, self)._prepare_item(line)
        res['sale_line_id'] = line.sale_line_id.id
        return res

    @api.model
    def _get_invoice(self, line):
        if line.sale_line_id and line.sale_line_id.id:
            invoice_ids = line.sale_line_id.order_id.invoices_ids
            return invoice_ids.mapped('invoice_ids')
        return super(RmaRefund, self)._get_invoice(line)


class RmaRefundItem(models.TransientModel):
    _inherit = "rma.refund.item"

    sale_line_id = fields.Many2one('sale.order.line',
                                    string='Sale Line')
