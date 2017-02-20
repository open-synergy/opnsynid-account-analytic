# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class AccountDistributionMassAssign(models.TransientModel):
    _inherit = "account.analytic_mass_assign"
    _description = "Account Distribution Mass Assign"

    analytic_account_id = fields.Many2one(
        string="Analytic Account",
        comodel_name="account.analytic.plan.instance",
        required=True
    )

    @api.multi
    def button_change_analytic(self):
        obj_acc_move_line = self.env['account.move.line']
        active_ids = self.env.context['active_ids']

        for record in obj_acc_move_line.browse(active_ids):
            record.analytics_id = self.analytic_account_id.id
            record.create_analytic_lines()

        return True
