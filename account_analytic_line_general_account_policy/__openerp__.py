# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Set Alternate General Account On Analytic Line",
    "version": "8.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "application": False,
    "depends": [
        "account_analytic_line_onchange",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/account_analytic_account_views.xml",
    ],
}
