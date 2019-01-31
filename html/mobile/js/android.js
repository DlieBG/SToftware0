async function setRelais(pin, value)
{
    SchweringApp.ping("http://huette/set?"+pin+"="+value);
    makestop();
    relais[pin]=value;
}


async function setTemp(value)
{
    SchweringApp.ping("http://huette/temp?temp="+value);
    makestop();
    solltemp=value;
}

async function setHeizung(value)
{
    SchweringApp.ping("http://huette/heizung?heizung="+value);
    makestop();
    heizung=value;
}