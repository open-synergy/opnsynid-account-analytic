# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import _, api, models
from openerp.exceptions import Warning as UserError


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    @api.model
    def create(self, vals):
        _super = super(AccountAnalyticLine, self)
        result = _super.create(vals)

        if vals.get("account_id"):
            obj_analytic_account = self.env["account.analytic.account"]
            analytic_account = obj_analytic_account.browse(vals["account_id"])
            if analytic_account.state == "close":
                msg_error = _("Analytic account is closed")
                raise UserError(msg_error)
        return result
