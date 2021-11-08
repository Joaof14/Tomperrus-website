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
        var counter0 = 0;
        var counter1 = 1;
        var counter2 = 2;
        back.addEventListener("click", function()
        {
            slide[counter0].style.display = "none";
            slide[counter1].style.display = "none";
            slide[counter2].style.display = "none";
            counter0--;
            counter1--;
            counter2--;
            if(counter0<0)
            {
                counter0 = slide.length - 1;
            }
            if(counter1<0)
            {
                counter1 = slide.length - 1;
            }
            if(counter2<0)
            {
                counter2 = slide.length - 1;
            }
            slide[counter0].style.display = "flex";
            slide[counter1].style.display = "flex";
            slide[counter2].style.display = "flex";
            slide[counter0].style.order = "1";
            slide[counter1].style.order = "2";
            slide[counter2].style.order = "3";
        })
        forward.addEventListener("click", function()
        {
            slide[counter0].style.display = "none";
            slide[counter1].style.display = "none";
            slide[counter2].style.display = "none";
            counter0++;
            counter1++;
            counter2++;
            if(counter0 == slide.length)
            {
                counter0 = 0;
            }
            if(counter1 == slide.length)
            {
                counter1 = 0;
            }
            if(counter2 == slide.length)
            {
                counter2 = 0;
            }
            slide[counter0].style.display = "flex";
            slide[counter1].style.display = "flex";
            slide[counter2].style.display = "flex";
            slide[counter0].style.order = "1";
            slide[counter1].style.order = "2";
            slide[counter2].style.order = "3";
        })
    }
    else{
        back.style.display= "none";
        forward.style.display = "none";
    }
})