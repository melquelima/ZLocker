(self.webpackChunkargon_dashboard_pro_angular=self.webpackChunkargon_dashboard_pro_angular||[]).push([[246],{1246:function(e,t,n){"use strict";n.r(t),n.d(t,{ProceduresModule:function(){return b}});var i=n(6728),a=n(146),o=n(1116),r=n(4762),c=n(9847),s=n(4455),l=n(529),d=n(483),u=n(2693),p=n(6691),h=function(){function e(e,t,n,i,a,o){this.http=e,this.route=t,this.route2=n,this.alertService=i,this.snackBar=a,this.authService=o,this.baseUrl=l.N.base_url}return e.prototype.getDays=function(){var e=this.http.get(this.baseUrl+"/api/skip_days",this.authService.httpOptions());return this.authService.onRequest(e)},e.prototype.newDay=function(e){var t=this.http.post(this.baseUrl+"/api/skip_days",{day:e},this.authService.httpOptions());return this.authService.onRequest(t)},e.prototype.deleteDay=function(e){var t=this.http.delete(this.baseUrl+"/api/skip_days/"+e,this.authService.httpOptions());return this.authService.onRequest(t)},e.\u0275fac=function(t){return new(t||e)(d.LFG(u.eN),d.LFG(a.F0),d.LFG(a.gz),d.LFG(s.c),d.LFG(p.c),d.LFG(c.e))},e.\u0275prov=d.Yz7({token:e,factory:e.\u0275fac,providedIn:"root"}),e}(),g=n(7647);function Z(e,t){if(1&e){var n=d.EpF();d.TgZ(0,"span"),d.TgZ(1,"button",42),d.NdJ("click",function(){var e=d.CHM(n).row;return d.oxw().deleteDay(e)}),d.TgZ(2,"span",22),d._UZ(3,"i",43),d.qZA(),d.TgZ(4,"span",24),d._uU(5," Remove "),d.qZA(),d.qZA(),d.qZA()}}var f=function(){function e(e,t){this.skipDayService=e,this.alerService=t,this.entries=10,this.temp=[],this.selected=[],this.dayRows=[]}return e.prototype.ngOnInit=function(){var e=this;this.alerService.loading("Loading Emails....."),this.skipDayService.getDays().subscribe(function(t){e.dayRows=t,e.loadData(e.dayRows),e.alerService.closeLoading()})},e.prototype.loadData=function(e){this.temp=e.map(function(e,t){return(0,r.pi)({},e)})},e.prototype.deleteDay=function(e){var t=this;this.alerService.confirm("Wait!","Do you really need to delete this day?").then(function(n){n.isConfirmed&&(t.alerService.loading("Deleting Day..."),t.skipDayService.deleteDay(e.id).subscribe(function(e){t.alerService.closeLoading(),t.dayRows=t.dayRows.filter(function(t){if(t.day!=e.day)return t}),t.loadData(t.dayRows)}),console.log(e))})},e.prototype.newDay=function(){var e=this;this.alerService.customNewDay().then(function(t){t.isConfirmed&&(e.alerService.loading("Adding new Day..."),e.skipDayService.newDay(t.value.day).subscribe(function(t){e.alerService.closeLoading(),e.dayRows.push(t),e.loadData(e.dayRows)}))})},e.prototype.exportDays=function(){var e="Day\n";e+=this.dayRows.map(function(e){return e.day}).join("\n"),this.saveData(e,"emails.csv")},e.prototype.saveData=function(e,t){var n=document.createElement("a");document.body.appendChild(n),n.setAttribute("style","display: none");var i=new Blob([e],{type:"octet/stream"}),a=window.URL.createObjectURL(i);n.href=a,n.download=t,n.click(),window.URL.revokeObjectURL(a)},e.prototype.entriesChange=function(e){this.entries=e.target.value},e.prototype.filterTable=function(e){var t=e.target.value;this.temp=this.dayRows.filter(function(e){for(var n in e)if(-1!==("number"==typeof e[n]?e[n].toString():e[n]).toLowerCase().indexOf(t.toLowerCase()))return!0;return!1})},e.prototype.onSelect=function(e){var t,n=e.selected;this.selected.splice(0,this.selected.length),(t=this.selected).push.apply(t,n)},e.prototype.onActivate=function(e){this.activeRow=e.row},e.\u0275fac=function(t){return new(t||e)(d.Y36(h),d.Y36(s.c))},e.\u0275cmp=d.Xpm({type:e,selectors:[["app-skip-days"]],decls:58,vars:10,consts:[[1,"header","bg-danger","pb-6"],[1,"container-fluid"],[1,"header-body"],[1,"row","align-items-center","py-4"],[1,"col-lg-6","col-7"],[1,"h2","text-white","d-inline-block","mb-0"],["aria-label","breadcrumb",1,"d-none","d-md-inline-block","ml-md-4"],[1,"breadcrumb","breadcrumb-links","breadcrumb-dark"],[1,"breadcrumb-item"],["href","javascript:void(0)"],[1,"fas","fa-home"],[1,"col-lg-6","col-5","text-right"],[1,"container-fluid","mt--6"],[1,"row"],[1,"col"],[1,"card"],[1,"card-header"],[1,"col-md-9"],[1,"mb-0"],[1,"text-sm","mb-0"],[1,"col-md-2"],["type","button",1,"btn","btn-icon","btn-success","btn-block",3,"click"],[1,"btn-inner--icon"],[1,"ni","ni-fat-add"],[1,"btn-inner--text"],[1,"col-md-1"],["type","button",1,"btn","btn-icon","btn-success","btn-download",3,"click"],[1,"ni","ni-cloud-download-95"],[1,"dataTables_wrapper","py-4"],[1,"col-sm-12","col-md-6"],["id","datatable_length",1,"dataTables_length"],["name","datatable_length","aria-controls","datatable",1,"form-control","form-control-sm",3,"change"],["value","10",3,"selected"],["value","25",3,"selected"],["value","50",3,"selected"],["value","-1",3,"selected"],["id","datatable_filter",1,"dataTables_filter"],["type","search","placeholder","Search records","aria-controls","datatable",1,"form-control","form-control-sm",3,"keyup"],[1,"bootstrap","selection-cell",3,"columnMode","headerHeight","footerHeight","rowHeight","limit","rows","activate"],["name","Day"],["name","Actions"],["ngx-datatable-cell-template",""],["type","button",1,"btn","btn-icon","btn-danger",3,"click"],[1,"ni","ni-scissors"]],template:function(e,t){1&e&&(d.TgZ(0,"div",0),d.TgZ(1,"div",1),d.TgZ(2,"div",2),d.TgZ(3,"div",3),d.TgZ(4,"div",4),d.TgZ(5,"h6",5),d._uU(6,"Operational Report - Skipping days"),d.qZA(),d.TgZ(7,"nav",6),d.TgZ(8,"ol",7),d.TgZ(9,"li",8),d.TgZ(10,"a",9),d._UZ(11,"i",10),d.qZA(),d.qZA(),d.qZA(),d.qZA(),d.qZA(),d._UZ(12,"div",11),d.qZA(),d.qZA(),d.qZA(),d.qZA(),d.TgZ(13,"div",12),d.TgZ(14,"div",13),d.TgZ(15,"div",14),d.TgZ(16,"div",15),d.TgZ(17,"div",16),d.TgZ(18,"div",13),d.TgZ(19,"div",17),d.TgZ(20,"h3",18),d._uU(21,"Day List"),d.qZA(),d.TgZ(22,"p",19),d._uU(23," This is a day list wich operational report bots will skip! "),d.qZA(),d.qZA(),d.TgZ(24,"div",20),d.TgZ(25,"button",21),d.NdJ("click",function(){return t.newDay()}),d.TgZ(26,"span",22),d._UZ(27,"i",23),d.qZA(),d.TgZ(28,"span",24),d._uU(29," New "),d.qZA(),d.qZA(),d.qZA(),d.TgZ(30,"div",25),d.TgZ(31,"button",26),d.NdJ("click",function(){return t.exportDays()}),d.TgZ(32,"span",22),d._UZ(33,"i",27),d.qZA(),d.qZA(),d.qZA(),d.qZA(),d.qZA(),d.TgZ(34,"div",28),d.TgZ(35,"div",13),d.TgZ(36,"div",29),d.TgZ(37,"div",30),d.TgZ(38,"label"),d._uU(39," Show "),d.TgZ(40,"select",31),d.NdJ("change",function(e){return t.entriesChange(e)}),d.TgZ(41,"option",32),d._uU(42,"10"),d.qZA(),d.TgZ(43,"option",33),d._uU(44,"25"),d.qZA(),d.TgZ(45,"option",34),d._uU(46,"50"),d.qZA(),d.TgZ(47,"option",35),d._uU(48,"All"),d.qZA(),d.qZA(),d._uU(49," entries "),d.qZA(),d.qZA(),d.qZA(),d.TgZ(50,"div",29),d.TgZ(51,"div",36),d.TgZ(52,"label"),d.TgZ(53,"input",37),d.NdJ("keyup",function(e){return t.filterTable(e)}),d.qZA(),d.qZA(),d.qZA(),d.qZA(),d.qZA(),d.TgZ(54,"ngx-datatable",38),d.NdJ("activate",function(e){return t.onActivate(e)}),d._UZ(55,"ngx-datatable-column",39),d.TgZ(56,"ngx-datatable-column",40),d.YNc(57,Z,6,0,"ng-template",41),d.qZA(),d.qZA(),d.qZA(),d.qZA(),d.qZA(),d.qZA(),d.qZA()),2&e&&(d.xp6(41),d.Q6J("selected",10==t.entries),d.xp6(2),d.Q6J("selected",25==t.entries),d.xp6(2),d.Q6J("selected",50==t.entries),d.xp6(2),d.Q6J("selected",-1==t.entries),d.xp6(7),d.Q6J("columnMode","force")("headerHeight",50)("footerHeight",50)("rowHeight","auto")("limit",-1!=t.entries?t.entries:void 0)("rows",t.temp))},directives:[i.YN,i.Kr,g.nE,g.UC,g.vq],styles:[".bg-danger[_ngcontent-%COMP%]{background-color:#f5a036!important}.btn-download[_ngcontent-%COMP%]{background-color:#0f034e;border-color:#0f034e}"]}),e}(),v=[{path:"",redirectTo:"procedures",pathMatch:"full"},{path:"",children:[{path:"next_gen",component:function(){function e(){}return e.prototype.ngOnInit=function(){},e.\u0275fac=function(t){return new(t||e)},e.\u0275cmp=d.Xpm({type:e,selectors:[["app-next-gen"]],decls:2,vars:0,template:function(e,t){1&e&&(d.TgZ(0,"p"),d._uU(1,"next-gen works!"),d.qZA())},styles:[""]}),e}()},{path:"skip_days",component:f}]}],b=function(){function e(){}return e.\u0275fac=function(t){return new(t||e)},e.\u0275mod=d.oAB({type:e}),e.\u0275inj=d.cJS({imports:[[o.ez,a.Bz.forChild(v),i.u5,g.xD]]}),e}()}}]);