# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class AccountAnalyticAccount(models.Model):
    _name = "account.analytic.account"
    _inherit = "account.analytic.account"

    general_account_substitution_ids = fields.One2many(
        string="General Account Substitutions",
        comodel_name="account.analytic_general_account_substitution",
        inverse_name="analytic_account_id",
    )
