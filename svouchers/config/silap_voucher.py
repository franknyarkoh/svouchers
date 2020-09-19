from __future__ import unicode_literals
from frappe import _

def get_data():

    return [
        {
            "label": _("SILAP Vouchers"),
            "icon": "octicon octicon-briefcase",
            "items": [
                {
                    "type": "doctype",
                    "name": "Request Voucher",
                    "label": _("Request Voucher"),
                }
                }
            ]
        }
    ]
