# Copyright 2017 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Mass Changing Journal Item Analytic Distribution",
    "version": "8.0.1.0.0",
    "category": "Accounting",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "application": False,
    "depends": [
        "account_analytic_plans",
        "analytic_account_mass_assign",
    ],
    "data": ["views/account_distribution_mass_assign_view.xml"],
    "images": [
        "static/description/banner.png",
    ],
}
