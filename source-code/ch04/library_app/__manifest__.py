# -*- coding: utf-8 -*-

{
    "name": "Library Management",
    "summary": "Manage library catalog and book lending.",
    "author": "Alan Hou",
    "license": "AGPL-3",
    "category": "Services/Library",
    "website": "https://alanhou.org",
    "version": "15.0.1.0.0",
    "depends": ["base"],
    "data": [
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/library_menu.xml",
        "views/book_list_template.xml",
    ],
    "application": True,
}
