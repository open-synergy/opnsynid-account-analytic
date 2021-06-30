# Copyright 2017 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Mass Changing Journal Item Analytic Account",
    "version": "8.0.1.0.1",
    "category": "Accounting",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "application": False,
    "depends": [
        "account",
    ],
    "data": ["views/account_analytic_mass_assign_view.xml"],
    "images": [
        "static/description/banner.png",
    ],
}
