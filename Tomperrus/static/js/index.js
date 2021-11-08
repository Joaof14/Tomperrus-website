document.addEventListener("DOMContentLoaded", function()
{
    var slide = document.getElementById("slideInicial").children;
    var forward = document.getElementById("forward");
    var back = document.getElementById("back");
    console.log(slide[1]);
    if (slide.length > 3)
    {
        for(let j = 3; j < slide.length; j++)
        {
            slide[j].style.display = "none";
        }
    }
    else{
        back.style.display= "none";
        forward.style.display = "none";
    }
})