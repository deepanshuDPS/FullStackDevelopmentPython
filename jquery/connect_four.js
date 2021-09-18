
$(document).ready(function() {
var firstTurn = prompt('Enter the first player name')
var secondTurn = prompt('Enter the second player name')
//
var hd3 = $('h3')
hd3.text('Lets start the game with '+firstTurn)
var tds = $('td')
var tabRows = $('table tr')
var winner =0;


//
var flag = true

function changeColor(currentCol){

  if(flag){
    currentCol.bgColor = "blue"
    hd3.text('Turn = '+secondTurn)
  }
  else {
    currentCol.bgColor = "red"
    hd3.text('Turn = '+firstTurn)
  }
    flag = !flag;
}

function blink_text() {
    $('h2').fadeOut(500);
    $('h2').fadeIn(500);
}
function alertForWinner(){
  hd3.fadeOut(2000);
  hd3.text('Play Again')
  hd3.fadeIn(1000);
  if(winner==1)
    $('h2').text("Winner is "+firstTurn);
  else
    $('h2').text("Winner is "+secondTurn);
  setInterval(blink_text,1000);
}

function checkForWinner(){

  var rows = tabRows.length
  for(var i=0;i<rows;i++){
    var currentRow = tabRows.eq(i);
    for(var j=0;j<4;j++){
      console.log("color: "+currentRow.find('td')[j].bgColor);
      if(currentRow.find('td')[j].bgColor !=="#bbb" &&
      currentRow.find('td')[j].bgColor===currentRow.find('td')[j+1].bgColor  &&
      currentRow.find('td')[j+1].bgColor===currentRow.find('td')[j+2].bgColor &&
      currentRow.find('td')[j+2].bgColor===currentRow.find('td')[j+3].bgColor){
          console.log('winner');
          if(currentRow.find('td')[j].bgColor ==="blue")
              return 1;
          else
              return 2;
      }
    }
  }

  return 0;
}
//
for(var i=0;i<tds.length;i++){
  tds.eq(i).click(function checkForIndex(){

    if(winner==0){
      var whichColumn = tds.index(this)%7;
      var rows = tabRows.length
      for(j=rows - 1 ;j>=0;j--){
        var currentCol = tabRows.eq(j).find('td')[whichColumn]
        var bgColor = currentCol.bgColor;
        if(bgColor==="#bbb"){
              changeColor(currentCol)
              break
          }
      }
      winner = checkForWinner();
      if(winner!=0){
        alertForWinner()
      }
    }
    else{
      alertForWinner()
    }
  });
}
});
