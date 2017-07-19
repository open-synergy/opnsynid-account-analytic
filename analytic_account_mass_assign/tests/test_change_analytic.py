# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase
from datetime import datetime


class TestChangeAnalytic(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(TestChangeAnalytic, self).setUp(*args, **kwargs)
        # Objects
        self.obj_move = self.env['account.move']
        self.obj_move_line = self.env['account.move.line']
        self.wiz = self.env['account.analytic_mass_assign']
        self.obj_journal = self.env['account.journal']
        self.obj_account = self.env['account.account']

        # Data
        self.journal = self.obj_journal.search(
            [('type', '=', 'sale')]
        )[0]
        self.acc_sale = self.obj_account.search(
            [('internal_type', '=', 'payable')]
        )[0]
        self.acc_recv = self.obj_account.search(
            [('internal_type', '=', 'receivable')]
        )[0]
        self.analytic_acc_id =\
            self.env.ref('analytic.analytic_internal')

    def _create_move(self):
        move_vals = {
            'name': '/',
            'journal_id': self.journal.id,
            'line_ids': [(0, 0, {
                'name': '/',
                'debit': 875000,
                'account_id': self.acc_sale.id,
                'analytic_account_id': False
            }), (0, 0, {
                'name': '/',
                'credit': 875000,
                'account_id': self.acc_recv.id,
                'analytic_account_id': False
            })]
        }

        move_id = self.obj_move.create(move_vals)

        return move_id

    def test_change_analytic(self):
        # Create Journal Entries
        # Condition: No Analytic Account
        move = self._create_move()
        check_line = self.obj_move_line.search_count([
            ('move_id', '=', move.id),
            ('analytic_account_id', '=', False)
        ])
        self.assertEqual(check_line, 2)

        # Create Wizard
        data_wzd = {
            'analytic_account_id': self.analytic_acc_id.id
        }
        wiz = self.wiz.with_context(
            active_ids=move.line_ids.ids
        ).create(data_wzd)
        wiz.button_change_analytic()

        check_line = self.obj_move_line.search_count([
            ('move_id', '=', move.id),
            ('analytic_account_id', '=', self.analytic_acc_id.id)
        ])
        self.assertEqual(check_line, 2)
