# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class AccountAnalyticPlanInstance(models.Model):
    _inherit = "account.analytic.plan.instance"

    active = fields.Boolean(
        string="Active",
        default=True
    )
