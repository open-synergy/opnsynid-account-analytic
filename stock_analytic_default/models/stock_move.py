# Copyright 2018 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    @api.model
    def _default_analytic_account_id(self):
        analytic_default = self._get_analytic_default(user_id=self.env.user.id)
        return analytic_default and analytic_default.analytic_id

    analytic_account_id = fields.Many2one(
        default=lambda self: self._default_analytic_account_id(),
    )

    @api.model
    def _get_analytic_default(
        self,
        product_id=False,
        partner_id=False,
        user_id=False,
        date=False,
        company_id=False,
    ):
        obj_default = self.env["account.analytic.default"]
        analytic_default = obj_default.account_get(
            product_id=product_id,
            partner_id=partner_id,
            user_id=user_id,
            date=date,
            company_id=company_id,
        )
        return analytic_default
