<!DOCTYPE html>
<?php
$format = "txt"; //Moeglichkeiten: csv und txt
 
$datum_zeit = date("d.m.Y H:i:s");
$ip = $_SERVER["REMOTE_ADDR"];
$site = $_SERVER['REQUEST_URI'];
$browser = $_SERVER["HTTP_USER_AGENT"];
 
$monate = array(1=>"Januar", 2=>"Februar", 3=>"Maerz", 4=>"April", 5=>"Mai", 6=>"Juni", 7=>"Juli", 8=>"August", 9=>"September", 10=>"Oktober", 11=>"November", 12=>"Dezember");
$monat = date("n");
$jahr = date("y");
 
$dateiname="logs/log_".$monate[$monat]."_$jahr.$format";
 
$header = array("Datum", "IP", "Seite", "Browser");
$infos = array($datum_zeit, $ip, $site, $browser);
 
if($format == "csv") {
 $eintrag= '"'.implode('", "', $infos).'"';
} else { 
 $eintrag = implode("\t", $infos);
}
 
$write_header = !file_exists($dateiname);
 
$datei=fopen($dateiname,"a");
 
if($write_header) {
 if($format == "csv") {
 $header_line = '"'.implode('", "', $header).'"';
 } else {
 $header_line = implode("\t", $header);
 }
 
 fputs($datei, $header_line."\n");
}
 
fputs($datei,$eintrag."\n");
fclose($datei);
?>
  <html>
    <head>
      <!--Import Google Icon Font-->
      <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
      <!--Import materialize.css-->
      <link type="text/css" rel="stylesheet" href="css/materialize.min.css"  media="screen,projection"/>

      <!--Let browser know website is optimized for mobile-->
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
      <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">

      <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
      <script>
        (adsbygoogle = window.adsbygoogle || []).push({
          google_ad_client: "ca-pub-3292679658415729",
          enable_page_level_ads: true
        });
      </script>
    </head>

    <body>
      <!--Import jQuery before materialize.js-->
      <script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
      
  <div id="header">    
      <nav>
          <div class="nav-wrapper">
            <a href="" class="brand-logo center">SToftware0</a>
            <ul class="right">
              <li><a href="https://www.paypal.me/DlieBG/5"><i class="material-icons">euro_symbol</i></a></li>
              <li><a onclick="document.getElementById('input').value='bewertung';document.getElementById('form').submit()"><i class="material-icons">star</i></a></li>              
              <li><a onclick="document.getElementById('input').value='hilfe';document.getElementById('form').submit()"><i class="material-icons">book</i></a></li>
            </ul>
          </div>
        </nav>
        <p>
          <div class="row">
            <div class="input-field col s12">
              <form id="form" method="POST" action="http://benedikt-schwering.de:443/call/" autocomplete="off" target="iframe">
                  <!--<input value="" id="input" type="text" autocomplete="false" name="ST0q">-->
                  <input id="input" class="materialize-textarea" name="ST0q" rows="1"></input>
                  <label class="active" for="input">Eingabe</label>
              </form>
            </div>
          </div>
        </p>
  </div>
  <div id="body">
        <iframe id="iframe" name="iframe" style="width:100vw; height:calc(100vh - 186px); border: none;" src="http://benedikt-schwering.de:443/call/?ST0q="></iframe>
  </div>
  <div id="footer" style="position:absolute;bottom:0;width:100%;height:64px;background:#ee6e73;" hidden>
        <nav style="position:absolute;bottom:0;width:100%;height:64px;background:#ee6e73;">
          <div class="nav-wrapper" style="position:absolute;bottom:0;width:100%;height:64px;background:#ee6e73;">
            <a href="" style="height: 64px;" class="brand-logo center">SToftware0 by Benedikt Schwering & Florian T&uuml;nte</a>
          </div>
        </nav>
  </div>
        <footer class="page-footer" style=" position:absolute;bottom:0;width:100%;height:300px;" hidden>
            <div class="container">
              <div class="row">
                <div class="col l6 s12">
                  <h5 class="white-text">&Uuml;ber...</h5>
                  <p class="grey-text text-lighten-4">SToftware0 by Benedikt Schwering & Florian T&uuml;nte</p>
                  <p>
                    <form method="POST" action="http://localhost:8000/call/" autocomplete="off" target="iframe">
                      <!--<input value="" id="input" type="text" autocomplete="false" name="ST0q">-->
                      <input id="input2" class="materialize-textarea" name="ST0q" rows="1"></input>
                      <label class="active" for="input2">localhost</label>
                  </form>
                  </p>
                </div>
                <div class="col l4 offset-l2 s12">
                  <h5 class="white-text">Links</h5>
                  <ul>
                    <li><a class="grey-text text-lighten-3" onclick="document.getElementById('input').value='hilfe';document.getElementById('form').submit()">Funktionen</a></li>
                    <li><a class="grey-text text-lighten-3" href="impressum.html">Impressum</a></li>
                  </ul>
                </div>
              </div>
            </div>
            <div class="footer-copyright">
              <div class="container">
               &copy; 2019 Copyright by Schwering Software
              <a class="grey-text text-lighten-4 right" href="#!"></a>
              </div>
            </div>
          </footer>
        



        <script type="text/javascript" src="js/materialize.js"></script>
      <script type="text/javascript" src="js/materialize.min.js"></script>
      <script>

        
      </script>
    </body>
  </html>
