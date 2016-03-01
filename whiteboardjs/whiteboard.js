$(document).ready(function(){
  var canvas = document.getElementById("whiteboard");
  var ctx = canvas.getContext("2d");
  console.log(ctx);
  ctx.fillStyle = "#FF0000";
  ctx.fillRect(0,0,150,75);

});
