# Copyright 2020 PT. Simetri Sinergi Indonesia
# Copyright 2020 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models, tools


class AccountAnalyticLineAnalysis(models.Model):
    _name = "account.analytic_line_analysis"
    _description = "Account Analytic Line Analysis"
    _auto = False

    unit_amount = fields.Float(
        string="Quantity",
    )
    amount = fields.Float(
        string="Amount",
    )
    account_id = fields.Many2one(
        string="Analytic Account",
        comodel_name="account.analytic.account",
    )
    journal_id = fields.Many2one(
        string="Analytic Journal",
        comodel_name="account.analytic.journal",
    )
    user_id = fields.Many2one(
        string="User",
        comodel_name="res.users",
    )
    date = fields.Date(
        string="Date",
    )
    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
    )
    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
    )
    product_id = fields.Many2one(
        string="Product",
        comodel_name="product.product",
    )
    general_account_id = fields.Many2one(
        string="General Account",
        comodel_name="account.account",
    )
    move_id = fields.Many2one(
        string="Move Line",
        comodel_name="account.move.line",
    )
    general_journal_id = fields.Many2one(
        string="General Journal",
        comodel_name="account.journal",
    )
    period_id = fields.Many2one(
        string="Period",
        comodel_name="account.period",
    )

    def _select(self):
        select_str = """
        SELECT
            a.id AS id,
            a.unit_amount AS unit_amount,
            a.amount AS amount,
            a.account_id AS account_id,
            a.journal_id AS journal_id,
            a.user_id AS user_id,
            a.date AS date,
            a.company_id AS company_id,
            a.product_id AS product_id,
            a.general_account_id AS general_account_id,
            b.id AS move_id,
            b.partner_id AS partner_id,
            b.journal_id AS general_journal_id,
            b.period_id AS period_id
        """
        return select_str

    def _from(self):
        from_str = """
        account_analytic_line AS a
        """
        return from_str

    def _where(self):
        where_str = """
        WHERE 1 = 1
        """
        return where_str

    def _join(self):
        join_str = """
        JOIN account_move_line AS b ON a.move_id = b.id
        """
        return join_str

    def _group_by(self):
        group_str = """
        """
        return group_str

    def init(self, cr):
        tools.drop_view_if_exists(cr, self._table)
        # pylint: disable=locally-disabled, sql-injection
        cr.execute(
            """CREATE or REPLACE VIEW %s as (
            %s
            FROM %s
            %s
            %s
            %s
        )"""
            % (
                self._table,
                self._select(),
                self._from(),
                self._join(),
                self._where(),
                self._group_by(),
            )
        )
