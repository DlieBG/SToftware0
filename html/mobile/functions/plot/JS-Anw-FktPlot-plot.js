"use strict";

var SW = window.SW || {};

// Math.log10 wird noch nicht von allen Browsern unterstützt
if(!Math.log10) Math.log10 = function(x) { return Math.log(x)/Math.LN10; };

// Das Plotobjekt
// feld ist das Objekt bzw. dessen Id, in dem das Diagramm erstellt werden soll
// xstr und ystr geben die Bezeichner der Objektelemente mit den x- und y-Werten im Datenarray an.
// Defaultwerte sind x und y. Das Datenarray sieht dan so aus: [{x:xwert,y:ywert}{...},...]
SW.plot = function(feld,xstr,ystr) {
	// Defaultwerte
	this.ticwidth = 1;
	this.linewidth = 1;
	this.borderwidth = 2;
	this.framecol = "black";
	this.gridcol = "gray";
	this.labelcol = "black";
	this.fillopac = 0.1;
	
	// Plotbereich anlegen
	if(typeof feld == "string") feld = document.getElementById(feld);
	feld.innerHTML = "";

	// Einige Variablen
	var xobj = xstr?xstr:"x";
	var yobj = ystr?ystr:"y";
	var xmin=0,xmax=0,ymin=0,ymax=0;
	var xfak=0,yfak=0;
	var dx,dy,fx,fy;
	var gr = null;

	// Zu den Werten in daten xmin, xmax, ymin und ymax ermitteln
	this.scale = function(daten) {
		if(xmin==xmax) { // Startwerte beim ersten Datensatz
			xmax = xmin = daten[0][xobj];
			ymax = ymin = daten[0][yobj];
		}
		for(var i=1;i<daten.length;i++) {
			var t = daten[i];
			if(t[xobj]<xmin) xmin = t[xobj];
			if(t[xobj]>xmax) xmax = t[xobj];
			if(t[yobj]<ymin) ymin = t[yobj];
			if(t[yobj]>ymax) ymax = t[yobj];
		}
	} // scale
	
	// Plotbereich leeren
	this.clear = function() {
		feld.innerHTML = "";
		xmax = xmin = ymax = ymin = xfak = yfak = 0;
	} // clear

	// Achsenkreuz, Tics und Beschriftung, linke untere Ecke bei (x0,y0)
	// xtext und ytext sind die Beschriftungen der Achsen
	this.frame = function(x0,y0,xtext,ytext) {
		this.x0 = x0;
		this.y0 = y0;
		// Den Bereich für das Diagramm anlegen
		feld.innerHTML = "";
		gr = new SW.grafik(feld);
		this.method = gr.method;
		// Achsenbeschriftungen
		if(xtext.length) gr.text((gr.w-x0)/2+x0,0,".9em",this.labelcol,xtext,"mu","h"); 
		if(ytext.length) gr.text(10,(gr.h-y0)/2+y0,".9em",this.labelcol,ytext,"mm","v");
		// xmin und xmax auf die nächst kleinere bzw. größere "glatte" Zahl runden und den 
		// Abstand der Tics auf glatte Zahlen (1 2 5 0) für x-Achse legen
		if(xmax==xmin) { xmin -= 0.5; xmax += 0.5; }
		dx = (xmax - xmin)/100;		
		xmin -= dx; xmax += dx;
		dx = xmax - xmin;
		fx = Math.pow(10,Math.floor(Math.log10(dx))-1); // Die Größenordnung ermitteln
		xmin = Math.floor(xmin/fx)*fx;
		xmax = Math.ceil(xmax/fx)*fx;
		xfak = (gr.w-x0)/(xmax-xmin);
		var tx = ticdist(100*dx/gr.w);
		var mxmin = Math.ceil(xmin/tx)*tx;
		// Tics und Zahlen an der x-Achse
		gr.setwidth(this.ticwidth);
		for(var x=mxmin;x<=xmax;x+=tx) {
			var xx = (x-xmin)*xfak + x0;
			gr.line(xx,y0,xx,gr.h,this.gridcol);
			if(xtext.length && xx<(gr.w-5) && xx>5) gr.text(xx,y0-2,".8em",this.labelcol,myround(x,tx),"mo","h");
		}
		// ymin und ymax auf die nächst kleinere bzw. größere "glatte" Zahl runden und den 
		// Abstand der Tics auf glatte Zahlen (1 2 5 0) für x-Achse legen
		if(ymax==ymin) { ymin -= 0.5; ymax += 0.5; }
		dy = (ymax - ymin)/100; 
		ymin -= dy; ymax += dy;
		dy = ymax - ymin;
		fy = Math.pow(10,Math.floor(Math.log10(dy))-1); // Die Größenordnung ermitteln
		ymin = Math.floor(ymin/fy)*fy;
		ymax = Math.ceil(ymax/fy)*fy;
		yfak = (gr.h-y0)/(ymax-ymin);
		var ty = ticdist(gr.h<250 ?  50*dy/gr.h : 100*dy/gr.h);
		var mymin = Math.ceil(ymin/ty)*ty;
		// Tics und Zahlen an der y-Achse
		for(var y=mymin;y<=ymax;y+=ty) {
			var yy = (y-ymin)*yfak + y0;
			gr.line(x0,yy,gr.w,yy,this.gridcol);
			if(ytext.length && yy<(gr.h-5) && yy>5) gr.text(x0-2,yy,".8em",this.labelcol,myround(y,ty),"rm","h");
		}
		gr.setwidth(this.borderwidth);
		gr.polyline([
			{x:x0, y: y0},
			{x:gr.w-this.borderwidth, y:y0},
			{x:gr.w-this.borderwidth, y:gr.h-this.borderwidth},
			{x:x0, y:gr.h-this.borderwidth},
			{x:x0, y:y0}],
			this.framecol);
	} // frame

	// Daten Plotten
	// daten: Datenarray mit Objekten mit den x- und y-Werten
	// color Diagrammfarbe
	this.plot = function(daten,color) {
		var arr=[];
		for(var i=0,l=daten.length;i<l;i++)
			arr.push({x:(daten[i][xobj]-xmin)*xfak+this.x0, y:(daten[i][yobj]-ymin)*yfak+this.y0});
		if(this.fillopac>0) {
			var fillline;
			if(ymax*ymin<=0) fillline = -ymin*yfak+this.y0 ; 
			else if(ymin>0) fillline = 1+this.y0;
			else fillline = gr.h-1;
			arr.push({x:(daten[l-1][xobj]-xmin)*xfak+this.x0,y:fillline});
			arr.push({x:(daten[0][xobj]-xmin)*xfak+this.x0,y:fillline});
			arr.push({x:(daten[0][xobj]-xmin)*xfak+this.x0,y:(daten[0][yobj]-ymin)*yfak+this.y0});
			gr.polyfill(arr,color,this.fillopac);
			arr.length -= 3;
		}
		gr.setwidth(this.linewidth);
		gr.polyline(arr,color);
	} // plot
	
	// Hilfsfunktionen zum Runden
	var myround = function(z,d) { 
		var l10 = Math.floor(Math.log10(d));
		var f = Math.pow(10,l10); 
		var zz = Math.round(z/f)*f;
		var zzz = Number(zz.toPrecision(15)).toString(10);
		return zzz; 
	}
	
	// Hilfsfunktion zum berechnen des Abstands der Achsen-Tics, Abstände auf 1 2 5 0 gerundet
	var ticdist = function(td) { 
		var td10 = Math.pow(10,Math.floor(Math.log10(td)));
		td = Math.round(td/td10);
		td = Number(String(td).replace(/3/,"2").replace(/[4567]/,"5").replace(/[89]/,"10"));
		td *= td10;
		return td;
	} // ticdist
} // plot