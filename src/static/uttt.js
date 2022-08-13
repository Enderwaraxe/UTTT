var oplayer, xplayer
function play(bigpos, smallpos){
    $( "#bigboard" ).load(window.location.href + "/play?bigpos=" +bigpos + "&smallpos="+smallpos+ " #bigboard", function()
      {
        if(oplayer != "Human" || xplayer != "Human"){
          botPlay()
        }
      });
  }
function botPlay(){
  $( "#bigboard" ).load(window.location.href + "/botplay" + " #bigboard", function()
  {
    if (oplayer != "Human" && xplayer != "Human" && document.getElementById("endimage") == null){
      botPlay()
    }
  });
}
function start(){
  oplayer = document.getElementById("oplayerdropdown").value;
  xplayer = document.getElementById("xplayerdropdown").value;
  $( "#bigboard" ).load(window.location.href + "/start?xplayer=" + xplayer + "&oplayer="+ oplayer + " #bigboard", function()
  {
    if (oplayer != "Human" && xplayer != "Human"){
      botPlay()
    }
  });
}