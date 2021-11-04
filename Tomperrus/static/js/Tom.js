var flavours;
var aside;
var rotulo;
var color;
console.log("funcionou");
document.addEventListener("DOMContentLoaded", function()
{
    aside = document.querySelector('aside');
    flavours = document.querySelector('select');
    rotulo = document.querySelector('.rotulo').children;
    console.log(rotulo);
    for (var i = 0; i < flavours.length; i++)
    {
        if(i !== flavours.selectedIndex)
        {
            rotulo[i].style.display = "none";
        }
    }
    flavours.addEventListener("change", function()
    {
        console.log(flavours[flavours.selectedIndex].value);
        for (var i = 0; i < flavours.length; i++)
        {
            if(i !== flavours.selectedIndex)
            {
                rotulo[i].style.display = "none";
            }
            else
            {
                rotulo[i].style.display = "flex";
                aside.style.backgroundColor = flavours[flavours.selectedIndex].value;
            }
        }
    })
})