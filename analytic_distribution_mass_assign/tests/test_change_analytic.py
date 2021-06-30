# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from datetime import datetime

from openerp.tests.common import TransactionCase


class TestChangeAnalytic(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(TestChangeAnalytic, self).setUp(*args, **kwargs)
        # Objects
        self.obj_period = self.env["account.period"]
        self.obj_move = self.env["account.move"]
        self.obj_move_line = self.env["account.move.line"]
        self.analytic_plan = self.env["account.analytic.plan"]
        self.analytic_plan_line = self.env["account.analytic.plan.line"]
        self.analytic_instance = self.env["account.analytic.plan.instance"]
        self.analytic_instance_line = self.env["account.analytic.plan.instance.line"]
        self.wiz = self.env["account.analytic_mass_assign"]

        # Data
        self.journal = self.env.ref("account.sales_journal")
        self.acc_sale = self.env.ref("account.a_sale")
        self.acc_recv = self.env.ref("account.a_recv")
        self.analytic_acc_id = self.env.ref("account.analytic_in_house")
        self.analytic_root_id = self.env.ref("account.analytic_root")

    def _create_move(self):
        date = datetime.now()
        period_id = self.obj_period.find(
            date, context={"account_period_prefer_normal": True}
        )

        move_vals = {
            "journal_id": self.journal.id,
            "period_id": period_id.id,
            "date": date,
        }

        move_id = self.obj_move.create(move_vals)

        self.obj_move_line.create(
            {
                "move_id": move_id.id,
                "name": "/",
                "debit": 0,
                "credit": 875000,
                "account_id": self.acc_sale.id,
                "analytic_account_id": False,
            }
        )

        self.obj_move_line.create(
            {
                "move_id": move_id.id,
                "name": "/",
                "debit": 875000,
                "credit": 0,
                "account_id": self.acc_recv.id,
                "analytic_account_id": False,
            }
        )
        return move_id

    def _create_plan(self):
        plan_vals = {"name": "Test Plan"}

        plan_id = self.analytic_plan.create(plan_vals)

        self.analytic_plan_line.create(
            {
                "plan_id": plan_id.id,
                "name": "/",
                "sequence": 1,
                "root_analytic_id": self.analytic_root_id.id,
            }
        )

        instance_vals = {
            "name": "Test Plan",
            "code": "001",
            "journal_id": self.journal.id,
            "plan_id": plan_id.id,
        }

        intance_id = self.analytic_instance.create(instance_vals)

        self.analytic_instance_line.create(
            {"plan_id": intance_id.id, "analytic_account_id": self.analytic_acc_id.id}
        )
        return intance_id

    def test_change_analytic(self):
        # Create Journal Entries
        # Condition: No Analytic Account
        move = self._create_move()
        check_line = self.obj_move_line.search_count(
            [("move_id", "=", move.id), ("analytics_id", "=", False)]
        )
        self.assertEqual(check_line, 2)

        intance_id = self._create_plan()

        # Create Wizard
        data_wzd = {"analytic_account_id": intance_id.id}
        wiz = self.wiz.with_context(active_ids=move.line_id.ids).create(data_wzd)
        wiz.button_change_analytic()

        check_line = self.obj_move_line.search_count(
            [("move_id", "=", move.id), ("analytics_id", "=", intance_id.id)]
        )
        self.assertEqual(check_line, 2)
