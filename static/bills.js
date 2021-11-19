function getLine(line)
{
    let t = document.getElementById("table");
    let trs = t.getElementsByTagName("tr")[line];
    let tds = trs.getElementsByTagName("td");
    let list = [];
    for(let i=1;i<tds.length;i++)
    {
        list.push(tds[i].innerHTML)
    }
    document.getElementById("Szamlaszam").setAttribute('value',list[0]);
    document.getElementById("Megrendeloneve").setAttribute('value',list[1]);
    document.getElementById("Osszeg").setAttribute('value',parseInt(list[2]));
    document.getElementById("Kiallitas").value=list[3];
    document.getElementById("Hatarido").value=list[4];
    if(list[5]==" 1 ")
    {
        document.getElementById("Teljesitve").checked=true;
    }
    else
    {
        document.getElementById("Teljesitve").checked=false;
    }
}