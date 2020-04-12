# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models, api


class AccountAnalyticLine(models.Model):
    _name = "account.analytic.line"
    _inherit = "account.analytic.line"

    pricelist_id = fields.Many2one(
        string="Pricelist",
        comodel_name="product.pricelist",
    )

    @api.onchange(
        "product_id",
        "unit_amount",
        "journal_id",
        "product_uom_id",
        "pricelist_id",
        "date",
    )
    def onchange_amount(self):
        _super = super(AccountAnalyticLine, self)
        _super.onchange_amount()

        is_sale_line = False
        obj_uom = self.env["product.uom"]
        obj_precision = self.env["decimal.precision"]

        if self.journal_id:
            if self.journal_id.type == "sale":
                is_sale_line = True

        if self.pricelist_id:
            pricelist = self.pricelist_id
            ctx1 = {}
            if self.date:
                ctx1.update({"date": self.date})
            amount_unit = pricelist.with_context(ctx1).price_get(
                prod_id=self.product_id.id,
                qty=self.unit_amount)[pricelist.id]
            amount = obj_uom._compute_price(
                self.product_id.uom_id.id,
                amount_unit,
                self.product_uom_id.id) * self.unit_amount
            prec = obj_precision.precision_get("Account")
            result = round(amount, prec)
            if not is_sale_line:
                result *= -1.0

            self.amount = result
