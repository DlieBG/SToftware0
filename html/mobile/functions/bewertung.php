<?php
$datum = date('d').'.'.date('m').'.'.date('Y');
$zeit = date('H').':'.date('i');

mkdir('/var/www/html/SToftware0/python/SToftware0/html/bewertungen/'.$datum);
$file = '/var/www/html/SToftware0/python/SToftware0/html/bewertungen/'.$datum.'/'.$zeit;
if($_POST['bewertung']!='')
  file_put_contents($file, $_POST['bewertung']);
?>

<!DOCTYPE html>
  <html>
    <head>
      <!--Import Google Icon Font-->
      <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
      <!--Import materialize.css-->
      <link type="text/css" rel="stylesheet" href="../css/materialize.min.css"  media="screen,projection"/>

      <style>
       body {
          display: flex;
          min-height: 100vh;
          flex-direction: column;
        }

        main {
          flex: 1 0 auto;
        }
      </style>

      <!--Let browser know website is optimized for mobile-->
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
      <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    </head>

    <body>
      <!--Import jQuery before materialize.js-->
      <script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>


      <div class="row">
          <div class="col s12 m12">
            <div class="card">
              <div class="card-content">
                <span class="card-title">Bewertung</span>
                  <p>
                    Bitte schreib uns was dir nicht gefällt, damit wir es verbessern können!
                    <br>
                    <div class="row">
                      <form class="col s12">
                        <div class="row">
                          <div class="input-field col s12">
                            <textarea id="bewertung" class="materialize-textarea"></textarea>
                            <label for="textarea1">Bewertung</label>
                          </div>
                        </div>
                      </form>
                    </div>
                  </p>
              </div>
              <div class="card-action">
                <a href="#" id="sendbtn">Senden!</a>
              </div>
            </div>
          </div>
        </div>

    <script>
      document.getElementById("sendbtn").onclick= 
        function()
        {
          if(document.getElementById("bewertung").value!="")
          {
            Materialize.toast('Danke!', 4000)
            post("bewertung.php", {bewertung: document.getElementById("bewertung").value });
          }
          else
          Materialize.toast('Bitte etwas eingeben!', 4000)
        }

      function post(path, params, method) {
          method = method || "post"; // Set method to post by default if not specified.

          // The rest of this code assumes you are not using a library.
          // It can be made less wordy if you use one.
          var form = document.createElement("form");
          form.setAttribute("method", method);
          form.setAttribute("action", path);

          for(var key in params) {
              if(params.hasOwnProperty(key)) {
                  var hiddenField = document.createElement("input");
                  hiddenField.setAttribute("type", "hidden");
                  hiddenField.setAttribute("name", key);
                  hiddenField.setAttribute("value", params[key]);

                  form.appendChild(hiddenField);
              }
          }

          document.body.appendChild(form);
          form.submit();
      }
    </script>
    
    <script type="text/javascript" src="../js/materialize.js"></script>
    <script type="text/javascript" src="../js/materialize.min.js"></script>
    </body>
  </html>
