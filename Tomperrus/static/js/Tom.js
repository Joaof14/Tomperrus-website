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
    var slide = document.querySelectorAll(".ProductImg");
    var forward = document.getElementById("forward");
    var back = document.getElementById("back");
    console.log(slide[0]);
    if (slide.length > 1)
    {
        for(let j = 1; j < slide.length; j++)
        {
            slide[j].style.display = "none";
        }
        var counter = 0;
        back.addEventListener("click", function()
        {
            slide[counter].style.display = "none";
            counter--;
            if(counter<0)
            {
                counter = slide.length - 1;
            }
            slide[counter].style.display = "flex";
        })
        forward.addEventListener("click", function()
        {
            slide[counter].style.display = "none";
            counter++;
            if(counter == slide.length)
            {
                counter = 0;
            }
            slide[counter].style.display = "flex";
        })
    }
    else
    {
        back.style.display= "none";
        forward.style.display = "none";
    }
})