


function get_Temperature (p1){

}

function get_Humidity (p1){

}

function downTemp(temp){
    // var temp = 26;
    var temp = getElementById
    temp--;
    return temp
}

$(document).ready(function (){
   $('#adjustdown').on("click",
       (
           function (){
              var temp = $(this).val();
              temp--;

           }
       )
                        )
});




$(document).ready(function (){
   $('#adjustup').on("click",
       (
           function (){
              var temp = $(this).val();
              temp--;

           }
       )
                        )
});



$(document).ready(function (){
   $('#acswitch').on("click",
       (
           function (){
               if ($(this).attr("class")=='far fa-toggle-on fa-3x')
               {
                         $(this).attr(
                  {
                      "class" : "far fa-toggle-off fa-3x",
                      "id" : "acswitch",
                      "onclick" : " ",
                         }
                                     );
               }
               else {
                        $(this).attr(
                  {
                      "class" : "far fa-toggle-on fa-3x",
                      "id" : "acswitch",
                      "onclick" : " ",
                         }
                                     );

               }


           }
       )
                        )
});






