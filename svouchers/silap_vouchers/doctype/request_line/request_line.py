# -*- coding: utf-8 -*-
# Copyright (c) 2020, SILAP Company Limited and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

#class RequestLine(Document):
#	pass
frappe.ui.form.on("Request Line", {
	rqty: function(frm,cdt, cdn){
		calculate_total(frm, cdt, cdn);
	},
	rprice: function(frm, cdt, cdn){
		calculate_total(frm, cdt, cdn);
	}
});
var calculate_total = function(frm, cdt, cdn) {
	var child = locals[cdt][cdn];
	frappe.model.set_value(cdt, cdn, "row.ramount", child.rqty * child.rprice);
cur_frm.refresh_field('ramount');
};

