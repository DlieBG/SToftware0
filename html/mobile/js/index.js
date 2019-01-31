var stop = false;
var heizung = false;
var isttemp = 20;
var isthygro = 50;
var solltemp = 20;

function getRelais()
{
    var head = document.getElementById('relais');
      var script= document.createElement('script');
      script.src= 'http://huette/get';
      head.innerHTML = "";
      head.appendChild(script);
}

async function updateSchalter()
{
    getRelais();  
    if(!stop)
    {
        $('#D1').prop('checked', relais[0]);
        $('#D2').prop('checked', relais[1]);
        if($('#D1').is(":checked")||$('#D2').is(":checked"))
            $('#D').prop('checked', true);
        else
            $('#D').prop('checked', false);


        $('#W1').prop('checked', relais[2]);
        $('#W2').prop('checked', relais[3]);
        $('#W3').prop('checked', relais[4]);
        $('#W4').prop('checked', relais[5]);
        if($('#W1').is(":checked")||$('#W2').is(":checked")||$('#W3').is(":checked")||$('#W4').is(":checked"))
            $('#W').prop('checked', true);
        else
            $('#W').prop('checked', false);

        
        $('#A1').prop('checked', relais[6]);
        $('#A2').prop('checked', relais[7]);
        $('#A3').prop('checked', relais[8]);
        if($('#A1').is(":checked")||$('#A2').is(":checked")||$('#A3').is(":checked"))
            $('#A').prop('checked', true);
        else
            $('#A').prop('checked', false);


        $('#S1').prop('checked', relais[9]);
        $('#S2').prop('checked', relais[10]);
        if($('#S1').is(":checked")||$('#S2').is(":checked"))
            $('#S').prop('checked', true);
        else
            $('#S').prop('checked', false);


        $('#SD1').prop('checked', relais[11]);
        $('#SD2').prop('checked', relais[12]);
        $('#SD3').prop('checked', relais[13]);
        $('#SD4').prop('checked', relais[14]);
    }

    document.getElementById("D").onchange = function(){
        setRelais(0, $('#D').is(":checked"));
        setRelais(1, $('#D').is(":checked"));
    };
    document.getElementById("D1").onchange = function(){setRelais(0, !relais[0]);};
    document.getElementById("D2").onchange = function(){setRelais(1, !relais[1]);};


    document.getElementById("W").onchange = function(){
        setRelais(2, $('#W').is(":checked"));
        setRelais(3, $('#W').is(":checked"));        
        setRelais(4, $('#W').is(":checked"));  
        setRelais(5, $('#W').is(":checked"));   
    };
    document.getElementById("W1").onchange = function(){setRelais(2, !relais[2]);};
    document.getElementById("W2").onchange = function(){setRelais(3, !relais[3]);};
    document.getElementById("W3").onchange = function(){setRelais(4, !relais[4]);};
    document.getElementById("W4").onchange = function(){setRelais(5, !relais[5]);};


    document.getElementById("A").onchange = function(){
        setRelais(6, $('#A').is(":checked"));
        setRelais(7, $('#A').is(":checked"));        
        setRelais(8, $('#A').is(":checked"));   
    };
    document.getElementById("A1").onchange = function(){setRelais(6, !relais[6]);};
    document.getElementById("A2").onchange = function(){setRelais(7, !relais[7]);};
    document.getElementById("A3").onchange = function(){setRelais(8, !relais[8]);};


    document.getElementById("S").onchange = function(){
        setRelais(9, $('#S').is(":checked"));
        setRelais(10, $('#S').is(":checked"));  
    };
    document.getElementById("S1").onchange = function(){setRelais(9, !relais[9]);};
    document.getElementById("S2").onchange = function(){setRelais(10, !relais[10]);};


    document.getElementById("SD1").onchange = function(){setRelais(11, !relais[11]);};
    document.getElementById("SD2").onchange = function(){setRelais(12, !relais[12]);};
    document.getElementById("SD3").onchange = function(){setRelais(13, !relais[13]);};
    document.getElementById("SD4").onchange = function(){setRelais(14, !relais[14]);};


    await new Promise((resolve, reject) => setTimeout(resolve, 500));    
        updateSchalter();
}

var off = [
    false,    //Deckenlampe links
    false,    //Deckenlampe rechts
    false,    //Wandlampe links vorne
    false,    //Wandlampe links hinten
    false,    //Wandlampe rechts hinten
    false,    //Wandlampe rechts vorne
    false,    //Strahler links
    false,    //Strahler mitte
    false,    //Strahler rechts
    false,    //Seitenbeleuchtung links
    false,    //Seitenbeleuchtung rechts
    false,    //Steckdosen vorne links 
    false,    //Steckdosen vorne links 
    false,    //Steckdosen hinten rechts
    false,    //Steckdosen vorne rechts
    ];

var on = [
    true,    //Deckenlampe links
    true,    //Deckenlampe rechts
    true,    //Wandlampe links vorne
    true,    //Wandlampe links hinten
    true,    //Wandlampe rechts hinten
    true,    //Wandlampe rechts vorne
    true,    //Strahler links
    true,    //Strahler mitte
    true,    //Strahler rechts
    true,    //Seitenbeleuchtung links
    true,    //Seitenbeleuchtung rechts
    true,    //Steckdosen vorne links 
    true,    //Steckdosen vorne links 
    true,    //Steckdosen hinten rechts
    true,    //Steckdosen vorne rechts
    ];

var szene1 = [ //wenig Licht
    false,    //Deckenlampe links
    false,    //Deckenlampe rechts
    true,    //Wandlampe links vorne
    true,    //Wandlampe links hinten
    true,    //Wandlampe rechts hinten
    true,    //Wandlampe rechts vorne
    false,    //Strahler links
    true,    //Strahler mitte
    false,    //Strahler rechts
    false,    //Seitenbeleuchtung links
    false,    //Seitenbeleuchtung rechts
    ];

var szene2 = [ //viel Licht
    true,    //Deckenlampe links
    true,    //Deckenlampe rechts
    true,    //Wandlampe links vorne
    true,    //Wandlampe links hinten
    true,    //Wandlampe rechts hinten
    true,    //Wandlampe rechts vorne
    true,    //Strahler links
    true,    //Strahler mitte
    true,    //Strahler rechts
    true,    //Seitenbeleuchtung links
    true,    //Seitenbeleuchtung rechts
    ];

var szene3 = [ //Nacht
    false,    //Deckenlampe links
    false,    //Deckenlampe rechts
    true,    //Wandlampe links vorne
    true,    //Wandlampe links hinten
    true,    //Wandlampe rechts hinten
    true,    //Wandlampe rechts vorne
    true,    //Strahler links
    true,    //Strahler mitte
    true,    //Strahler rechts
    true,    //Seitenbeleuchtung links
    true,    //Seitenbeleuchtung rechts
    ];

async function updateSzenen()
{
    if(!stop)
    {
        $('#off').prop('checked', relais.slice(0,15).equals(off)&&!heizung);
        $('#on').prop('checked', relais.slice(0,15).equals(on)&&heizung);
        $('#szene1').prop('checked', relais.slice(0,11).equals(szene1));
        $('#szene2').prop('checked', relais.slice(0,11).equals(szene2));
        $('#szene3').prop('checked', relais.slice(0,11).equals(szene3));
    }


    document.getElementById("off").onchange = function(){
        for(var i=0; i<15; i++)
            setRelais(i, off[i]);
        setHeizung(false);
    };

    document.getElementById("on").onchange = function(){
        for(var i=0; i<15; i++)
            setRelais(i, on[i]);
        setHeizung(true);
    };

    document.getElementById("szene1").onchange = function(){
        for(var i=0; i<11; i++)
            setRelais(i, szene1[i]);
    };

    document.getElementById("szene2").onchange = function(){
        for(var i=0; i<11; i++)
            setRelais(i, szene2[i]);
    };

    document.getElementById("szene3").onchange = function(){
        for(var i=0; i<11; i++)
            setRelais(i, szene3[i]);
    };


    await new Promise((resolve, reject) => setTimeout(resolve, 500));    
        updateSzenen();
}

async function updateHeizung()
{
    if(!stop)
    {
        if(heizung)
        {
            if(relais[15])
            {
                $('#heizungstate').text( "whatshot");
                $('#hzstate').text( "Heizung ein - aktiv");
                $('#hzstia2').text( "whatshot");
            }
            else
            {
                $('#heizungstate').text( "done");
                $('#hzstate').text( "Heizung ein - nicht aktiv");
                $('#hzstia2').text( "");
            }
            $('#hzstia').text( "check_circle");
        }
        else
        {
            $('#heizungstate').text( "power_settings_new");
            $('#hzstate').text( "Heizung aus");
            $('#hzstia').text( "cancel");
            $('#hzstia2').text( "");
        }

        $('#tempsoll').html(solltemp+"&deg;C");
        $('#tempist').html(isttemp+"&deg;C");
        $('#hygroist').html(isthygro+"%");
        
        document.getElementById("hzbtn").onclick = function(){
            setHeizung(!heizung);
        };

        document.getElementById("hzp").onclick = function(){
            setTemp(solltemp+1);
        };
        document.getElementById("hzm").onclick = function(){
            setTemp(solltemp-1);
        };
    }


    await new Promise((resolve, reject) => setTimeout(resolve, 500));
        updateHeizung();
}

async function makestop()
{
    stop = true;
    await new Promise((resolve, reject) => setTimeout(resolve, 500));
    stop = false;
}

updateSchalter();
updateSzenen();
updateHeizung();
