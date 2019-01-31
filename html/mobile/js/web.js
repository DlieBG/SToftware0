async function setRelais(pin, value)
{
    this.img = new Image();
    this.img.src = "http://huette/set?"+pin+"="+value;
    makestop();
    relais[pin]=value;
}

async function setTemp(value)
{
    this.img = new Image();
    this.img.src = "http://huette/temp?temp="+value;
    makestop();
    solltemp=value;
}

async function setHeizung(value)
{
    this.img = new Image();
    this.img.src = "http://huette/heizung?heizung="+value;
    makestop();
    heizung=value;
}
