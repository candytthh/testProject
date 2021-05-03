// function WebSocketTest(){
//     alert(1)
//         if ("WebSocket" in window) {
//             alert("您的浏览器支持 WebSocket!");
//             // 打开一个 web socket
//             ws = new WebSocket("ws://127.0.0.1:8000/path/");
//             ws.onopen = function () {
//                 // Web Socket 已连接上，使用 send() 方法发送数据
//                 ws.send("发送数据");
//                 alert("数据发送中...");
//             };
//             ws.onmessage = function (evt) {
//                 var received_msg = evt.data;
//                 alert("数据已接收...");
//                 alert("数据:" + received_msg)
//             };
//             ws.onclose = function () {
//                 // 关闭 websocket
//                 alert("连接已关闭...");
//             };
//         }
//         else {
//             // 浏览器不支持 WebSocket
//             alert("您的浏览器不支持 WebSocket!");
//         }
//
// }

// need a refresh function to refresh the page in few seconds

var ws = new WebSocket(
    "ws://" + window.location.host
);

ws.onopen = function()
               {
                  // Web Socket 已连接上，使用 send() 方法发送数据
                  ws.send("发送数据");
                  alert("数据发送中...");
               };

ws.onmessage =function (msg){
    let datapoint = JSON.parse(msg.data);
    console.log(datapoint);
}












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
               if ($(this).attr("class")=='far fa-toggle-on fa-4x')
               {
                         $(this).attr(
                  {
                      "class" : "far fa-toggle-off fa-4x",
                      "id" : "acswitch",
                      "onclick" : " ",
                         }
                                     );
               }
               else {
                        $(this).attr(
                  {
                      "class" : "far fa-toggle-on fa-4x",
                      "id" : "acswitch",
                      "onclick" : " ",
                         }
                                     );

               }


           }
       )
                        )
});






