
"""
>>> self
res.users(1,)
>>> self._name
'res.users'
>>> self.name
'OdooBot'
>>> self.login
'__system__'

>>> self.env
<odoo.api.Environment object at 0x7f9fb92e0fa0>

>>> self.env["res.partner"].search([("display_name", "like", "Azure")])
res.partner(14, 26, 33, 27)

>>> self.env.context
{'lang': 'en_US', 'tz': 'Europe/Brussels'}

>>> self.env.ref('base.user_root')
res.users(1,)

>>> self.env['res.partner'].search([('display_name', 'like', 'Lumber')])
res.partner(15, 34)

>>> self.env['res.partner'].browse([15, 34])
res.partner(15, 34)
"""

>>> self.env["res.partner"].read_group([("display_name", "like", "Azure")], fields=["state_id:count_distinct",], groupby=["country_id"], lazy=False)
[{'__count': 4, 'state_id': 1, 'country_id': (233, <odoo.tools.func.lazy object at 0x7f38ac66fa80>), '__domain': ['&', ('country_id', '=', 233), ('display_name', 'like', 'Azure')]}]
>>> self.env["res.country"].browse(233).name
'United States'

>>> print(self.name)
OdooBot

>>> for rec in self: print(rec.name)
...
OdooBot

>>> self.company_id
res.company(1,)
>>> self.company_id.name
'YourCompany'
>>> self.company_id.currency_id
res.currency(1,)
>>> self.company_id.currency_id.name
'EUR'

>>> self.company_id.parent_id
res.company()
>>> self.company_id.parent_id.name
False

>>> self.browse(2).login_date
datetime.datetime(2022, 5, 6, 3, 26, 21, 714562)

>>> root = self.env["res.users"].browse(1)
>>> print(root.name)
OdooBot
>>> root.name = "Superuser"
>>> print(root.name)
Superuser

>>> from datetime import date
>>> self.date = date(2020, 12, 1)
>>> self.date
datetime.date(2020, 12, 1)
>>> self.date = "2020-12-02"
>>> self.date
datetime.date(2020, 12, 2)

>>> import base64
>>> blackdot_binary = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x04\x00\x00\x00\xb5\x1c\x0c\x02\x00\x00\x00\x0bIDATx\xdacd\xf8\x0f\x00\x01\x05\x01\x01'\x18\xe3f\x00\x00\x00\x00IEND\xaeB'\x82"
>>> self.image_1920 = base64.b64encode(blackdot_binary).decode("utf-8")

>>> self.child_ids = None
>>> self.child_ids
res.partner()

>>> mycompany_partner = self.company_id.partner_id
>>> myaddress = self.partner_id
>>> mycompany_partner.child_ids = mycompany_partner.child_ids | myaddress

>>> Partner = self.env["res.partner"]
>>> recs = Partner.search([("name", "ilike", "Azure")])
>>> recs.write({"comment": "Hello!"})
True

>>> self.write({ 'child_ids': address1 | address2})

>>> Partner = self.env['res.partner']
>>> new = Partner.create({'name': 'ACME', 'is_company': True})
>>> print(new)
res.partner(56,)

>>> rec = Partner.search([('name', '=', 'ACME')])
>>> rec.unlink()
2022-06-05 01:53:09,906 43 INFO odoo-dev odoo.models.unlink: User #1 deleted mail.message records with IDs: [22]
2022-06-05 01:53:09,952 43 INFO odoo-dev odoo.models.unlink: User #1 deleted res.partner records with IDs: [56]
2022-06-05 01:53:09,961 43 INFO odoo-dev odoo.models.unlink: User #1 deleted mail.followers records with IDs: [6]
True

>>> demo = self.env.ref("base.user_demo")
>>> new = demo.copy({"name": "John", "login": "john@example.com"})

>>> from datetime import date
>>> date.today()
datetime.date(2022, 6, 5)
>>> from datetime import timedelta
>>> date(2022, 6, 5) + timedelta(days=7)
datetime.date(2022, 6, 12)

>>> from dateutil.relativedelta import relativedelta
>>> date(2022, 6, 5) + relativedelta(years=1, months=1)
datetime.date(2023, 7, 5)

>>> from odoo.tools import date_utils
>>> from datetime import datetime
>>> now = datetime(2022, 6, 5, 0, 0, 0)
>>> date_utils.start_of(now, 'week')
datetime.datetime(2022, 5, 30, 0, 0)
>>> date_utils.end_of(now, 'week')
datetime.datetime(2022, 6, 5, 23, 59, 59, 999999)
>>> today = date(2022, 6, 5)
>>> date_utils.add(today, months=2)
datetime.date(2022, 8, 5)
>>> date_utils.subtract(today, months=2)
datetime.date(2022, 4, 5)

>>> date(2022, 6, 5).strftime("%d/%m/%Y")
'05/06/2022'

>>> from odoo import fields
>>> fields.Datetime.to_datetime("2020-11-21 23:11:55")
datetime.datetime(2020, 11, 21, 23, 11, 55)

>>> from datetime import datetime
>>> datetime.strptime("03/11/2020", "%d/%m/%Y")
datetime.datetime(2020, 11, 3, 0, 0)

>>> from datetime import datetime
>>> import pytz
>>> naive_date = datetime(2020, 12, 1, 0, 30, 0)
>>> client_tz = self.env.context["tz"]
>>> client_date = pytz.timezone(client_tz).localize(naive_date)
>>> utc_date = client_date.astimezone(pytz.utc)
>>> print(utc_date)
2020-11-30 23:30:00+00:00


>>> rs0 = self.env["res.partner"].search([("display_name", "like", "Azure")])
>>> len(rs0)
4
>>> rs0.filtered(lambda r: r.name.startswith("Nicole"))
res.partner(27,)
>>> rs0.filtered("is_company")
res.partner(14,)
>>> rs0.mapped("name")
['Azure Interior', 'Brandon Freeman', 'Colleen Diaz', 'Nicole Ford']
>>> rs0.sorted("name", reverse=True).mapped("name")
['Nicole Ford', 'Colleen Diaz', 'Brandon Freeman', 'Azure Interior']
>>> rs0.mapped(lambda r: (r.id, r.name))
[(14, 'Azure Interior'), (26, 'Brandon Freeman'), (33, 'Colleen Diaz'), (27, 'Nicole Ford')]

>>> Partner = self.env['res.partner']
>>> recs = self.env['res.partner']>>> for i in range(3):...     rec = Partner.create({"name": "Partner %s" % i})
...     recs |= rec
...
>>> print(recs)res.partner(58, 59, 60)


>>> self.env.cr.execute("SELECT id, login FROM res_users WHERE login=%s OR id=%s", ("demo", 1))
>>> self.env.cr.execute("SELECT id, login FROM res_users WHERE login=%(login)s OR id=%(id)s", {"login": "demo", "id": 1})

>>> self.env.cr.fetchall()
[(1, '__system__'), (6, 'demo')]

>>> self.env.cr.dictfetchall()
[{'id': 1, 'login': '__system__'}, {'id': 6, 'login': 'demo'}]


