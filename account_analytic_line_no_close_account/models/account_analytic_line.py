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
        if self._check_account(vals.get("account_id")):
            msg_error = _("Analytic account is closed")
            raise UserError(msg_error)
        return result

    @api.multi
    def _check_account(self, account_id):
        res = False
        obj_analytic_account = self.env["account.analytic.account"]
        analytic_account = obj_analytic_account.browse(account_id)
        if analytic_account.state == "close":
            res = True
        return res

    @api.multi
    def write(self, vals):
        _super = super(AccountAnalyticLine, self)
        for record in self:
            # check old analytic account
            if record.account_id:
                if record.account_id.state == "close":
                    msg_error = _("Cannot Edit -> Analytic Account %s is closed") % (
                        record.account_id.name
                    )
                    raise UserError(msg_error)
            # check new analytic account
            if record._check_account(vals.get("account_id")):
                msg_error = _("Cannot Edit -> Analytic Account is closed")
                raise UserError(msg_error)
        return _super.write(vals)

    @api.multi
    def unlink(self):
        for record in self:
            if record.account_id:
                if record.account_id.state == "close":
                    msg_error = _("Cannot Delete --> Analytic account is closed")
                    raise UserError(msg_error)
        _super = super(AccountAnalyticLine, self)
        _super.unlink()
