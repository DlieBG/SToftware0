"use strict";

//window.addEventListener("DOMContentLoaded",function() {
window.addEventListener("load",function() {
	// Zahlen einlesen und bei Bedarf korrigieren
	var get_num = function(e) {
		var num = e.value;
		if (isNaN(num)) { num = num.replace(/,/g,"."); }
		if (isNaN(num) || num.length==0 ) { num = 0.0; e.value = num; }
		return parseFloat(num);
	}
	// Der Funktionsplotter
	var fkt_plotter = function() {
		var funktionen = [];
		// Funktionen lesen
		for(var i=0;i<e_fkt.length;i++ ) funktionen[i] = e_fkt[i].value;
		// xmin und xmax lesen, prüfen und bei Bedarf korrigieren
		var xmin = get_num(e_xmin);
		var xmax = get_num(e_xmax);
		if (xmax==xmin) {
			xmin -= 0.5; xmax += 0.5;
			e_xmin.value = xmin;
			e_xmax.value = xmax;
		}
		else if (xmax<xmin) {
			var t = xmax;
			xmax = xmin;
			xmin = t;
			e_xmin.value = xmin;
			e_xmax.value = xmax;
		}
		var dx = (xmax - xmin)/npt;
		// Werte für Diagramm berechnen ...
		var daten = [];
		for(var i=0;i<funktionen.length;i++) {
			try { 
				if(funktionen[i].length && funktionen[i].search(/\S/)!=-1) {
					var fun = new Function("x","with(Math){return("+funktionen[i]+")}");
					var ar = [];
					for(var x=xmin;x<=xmax;x+=dx) ar.push( { x: x, y: fun(x) } );
					daten.push(ar);
				}
			}
			catch(e) { 
				alert("Fehler in der Formel Nr "+(i+1)+":\n\n"+funktionen[i]+"\n\n"+e); 
			}
		}
		// ... und plotten
		plt.clear();
		plt.fillopac = .3;
		for(var i=0;i<daten.length;i++) if(!isNaN(daten[i][0].y)) plt.scale(daten[i]);
		plt.frame(50,35,"x","y");
		for(var i=0;i<daten.length;i++) if(!isNaN(daten[i][0].y)) plt.plot(daten[i],cols[i]);
		// ... und Ausgabe in versteckter Tabelle für Screenreader
		var tabelle = "";
		for(var j=0;j<daten.length;j++) {
			tabelle += "<table>";
			tabelle += "<caption>Wertetabelle für Funktion "+(j+1)+"</caption>";
			tabelle += "<thead><tr><th colspan='2'>"+funktionen[j]+"</th></tr>";
			tabelle += "<tr><th>x</th><th>y"+(j+1)+"</th></tr></thead>";
			tabelle += "<tbody>";
			for(var i=0;i<daten[j].length;i+=npt/20 ) tabelle += "<tr><td>"+daten[j][i].x.toFixed(3)+"</td><td>"+daten[j][i].y.toFixed(3)+"</td></tr>";
			tabelle += "</tbody>"
			tabelle += "</table>";
		}
		e_wertetabelle.innerHTML = tabelle;
	} // fkt_plotter

	var i,j,e_plotarea,e_wertetabelle,e_fkt=[],e_xmin,e_xmax,plt,e_jsfkt,e_vdeffkt;
	var npt = 1000;
	var current = 0;
	var cols = ["#ff0000","#008000","#0000ff"];
	var vdef_fkt = { 
		AM: "(1-0.3*sin(x/4))*sin(3*x)",
		PM: "sin(3*x-2*sin(x/3))",
		"sin(x)/x": "sin(x)/x",
		sinh: "(exp(x)-exp(-x))/2",
		cosh: "(exp(x)+exp(-x))/2",
		tanh: "(exp(x)-exp(-x))/(exp(x)+exp(-x))",
		Puls: "(function(){var y=0;for(var ii=10;ii<30;ii++) y+=sin(ii*x);return y})(x)"
	};
	var js_fkt = {
		abs: "abs(x)",
		acos: "acos(x)",
		asin: "asin(x)",
		atan: "atan(x)",
		cos: "cos(x)",
		exp: "exp(x)",
		log: "log(x)",
		pow: "pow(x,2)",
		sin: "sin(x)",
		sqrt: "sqrt(x)",
		tan: "tan(x)",
	};

	// Referenzen
	e_plotarea = document.getElementById("plotarea");
	e_wertetabelle = document.getElementById("wertetabelle");
	e_xmin = document.getElementById("idxmin");
	e_xmax = document.getElementById("idxmax");
	e_jsfkt = document.querySelectorAll("#jsfkt button"); 
	e_vdeffkt = document.querySelectorAll("#vdeffkt button"); 
	for(i=0;i<3;i++) {
		e_fkt[i] = document.getElementById("fkt"+(i+1));
		document.getElementById("f"+(i+1)).style.color = cols[i];
	}
	// Die Eventhandler
	document.getElementById("plotbutton").addEventListener("click",fkt_plotter);
	document.getElementById("fkt1").addEventListener("click",function(){ current = 0 });
	document.getElementById("fkt2").addEventListener("click",function(){ current = 1 });
	document.getElementById("fkt3").addEventListener("click",function(){ current = 2 });
	for(i=0;i<e_vdeffkt.length;i++) e_vdeffkt[i].addEventListener("click",function() { 
		e_fkt[current].value = vdef_fkt[this.innerHTML] });
	for(i=0;i<e_jsfkt.length;i++) e_jsfkt[i].addEventListener("click",function() { 
		e_fkt[current].value += "+"+ js_fkt[this.innerHTML] });
	// Plottbereich anlegen und Startwerte plotten
	plt = new SW.plot(e_plotarea);
	fkt_plotter();
	// SVG kann sich an Größenänderungen anpassen, bei Canvas muss der Plot neu erstellt werden
	if(plt.method=="canvas")
		window.addEventListener("resize",function() {
			plt = new SW.plot(e_plotarea);
			fkt_plotter();
		});
});