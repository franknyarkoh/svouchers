frappe.ui.form.on("Request Line", {
      rqty: function(frm, cdt, cdn) {
        var d = locals[cdt][cdn];
                frappe.model.set_value(d.doctype, d.name, 'ramount', (d.rqty * d.rprice));  
                     }
 });  
 
 frappe.ui.form.on("Request Line", {
      rprice: function(frm, cdt, cdn) {
        var d = locals[cdt][cdn];
                frappe.model.set_value(d.doctype, d.name, 'ramount', (d.rqty * d.rprice));
    }
});

frappe.ui.form.on("Request Line", {
   ramount:function(frm, cdt, cdn){
   var d = locals[cdt][cdn];
   var total = 0;
   frm.doc.request_line.forEach(function(d) { total += d.ramount; });
   frm.set_value("rtotal", total);
   refresh_field("rtotal");
 },
   request_line_remove:function(frm, cdt, cdn){
   var d = locals[cdt][cdn];
   var total = 0;
   frm.doc.request_line.forEach(function(d) { total += d.ramount; });
   frm.set_value("rtotal", total);
   refresh_field("rtotal");
   	}
   });