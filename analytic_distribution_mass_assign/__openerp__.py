# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Mass Changing Journal Item Analytic Distribution",
    "version": "9.0.1.0.0",
    "category": "Accounting",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": False,
    "application": False,
    "depends": [
        "account_analytic_plans",
        "analytic_account_mass_assign",
    ],
    "data": [
        "views/account_distribution_mass_assign_view.xml"
    ],
}
