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
    let bill_id = document.getElementById("Szamlaszam");
    bill_id.innerHTML=list[0];
    document.getElementById("Szamlaszam").setAttribute('value',list[0]);
    document.getElementById("Megrendeloneve").setAttribute('value',list[1]);
    document.getElementById("Osszeg").setAttribute('value',parseInt(list[2]));

    let begining ="";
    for(let i=1;i<list[3].length-1;i++)
    {
        begining+=list[3][i];
    }
    let end = "";
    for(let i=1;i<list[4].length-1;i++)
    {
        end+=list[4][i];
    }
    document.getElementById("Kiallitas").value=begining;
    document.getElementById("Hatarido").value=end;
    if(list[5]==" 1 ")
    {
        document.getElementById("Teljesitve").checked=true;
    }
    else
    {
        document.getElementById("Teljesitve").checked=false;
    }
}