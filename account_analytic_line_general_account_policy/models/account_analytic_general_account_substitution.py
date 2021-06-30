# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class AccountAnalyticGeneralAccountSubstitution(models.Model):
    _name = "account.analytic_general_account_substitution"
    _description = "General Account Substitution"

    analytic_account_id = fields.Many2one(
        string="Analytic Account",
        comodel_name="account.analytic.account",
    )
    product_id = fields.Many2one(
        string="Product",
        comodel_name="product.product",
        required=True,
    )
    expense_general_account_id = fields.Many2one(
        string="Expense General Account",
        comodel_name="account.account",
    )
    income_general_account_id = fields.Many2one(
        string="Income General Account",
        comodel_name="account.account",
    )
