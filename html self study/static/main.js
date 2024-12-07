let canvas = document.getElementById("canvas")
let ctx = canvas.getContext("2d");
canvas.height =1020;
canvas.width = 1200;

let data = {};
let command = ""
let background = new Image()
let player1 = new Image()
let player2 = new Image()
let cubeBlue = new Image()
let cubeYellow = new Image()
let cubeRed = new Image()
let cubeViolet = new Image()
let infectionMark = new Image()
let outBreakMark = new Image()
let vaccineMark = new Image()
let treatAvailable = new Image()
let buildAvailable = new Image()
let cureAvailable = new Image()
let researchCenter = new  Image()
let doctor1 = new Image()
let moveList = []

doctor1.src = "../static/img/doctor1.png"
researchCenter.src = "../static/img/RC.png"
cubeBlue.src = "../static/img/blue.png"
cubeYellow.src = "../static/img/yellow.png"
cubeRed.src = "../static/img/red.png"
cubeViolet.src = "../static/img/violet.png"
background.src = "../static/img/background.png"
player1.src = "../static/img/pawnRed.png"
player2.src = "../static/img/pawnYellow.png"
infectionMark.src = "../static/img/infectionMark.png"
outBreakMark.src = "../static/img/outBreakMark.png"
vaccineMark.src = "../static/img/vaccineMark.png"
treatAvailable.src = "../static/img/treatAvailable.png"
buildAvailable.src = "../static/img/buildAvailable.png"
cureAvailable.src = "../static/img/cureAvailable.png"

background.onload = function(){
  ctx.drawImage(background,0,0);
}

function circle(X, Y) {
  ctx.beginPath();
  ctx.arc(X+5, Y+5, 10, 0, 2 * Math.PI);
  ctx.fillStyle = "rgba(111,227,58,0.3)";
  ctx.fill();
  ctx.stroke()
}

function print_card(X,Y,text1,text2,textColor,backgroundColor) {
  ctx.font =  "15px Arial";
  Y += 720
  ctx.textAlign = "center";
  ctx.fillStyle = backgroundColor;
  ctx.fillRect(X, Y, 120 , 45);
  ctx.fillStyle = textColor;
  ctx.textAlign = "center"
  ctx.fillText(text1, X+60, Y+20);
  ctx.fillText(text2, X+60, Y+35);
}

function print_cube(x,y,cube) {
  let l_i = 0
  let cube_xy = [[0,-2],[-8,4],[+8,4],[-16,9],[0,9],[16,9]]
  for (let i = 0; i < cube[0]; i++){
    ctx.drawImage(cubeBlue,x + cube_xy[l_i][0], y + cube_xy[l_i][1])
    l_i += 1
  }
  for (let i = 0; i < cube[1]; i++){
    ctx.drawImage(cubeViolet,x + cube_xy[l_i][0], y + cube_xy[l_i][1])
    l_i += 1
  }
  for (let i = 0; i < cube[2]; i++){
    ctx.drawImage(cubeRed,x + cube_xy[l_i][0], y + cube_xy[l_i][1])
    l_i += 1
  }
  for (let i = 0; i < cube[3]; i++){
    ctx.drawImage(cubeYellow,x + cube_xy[l_i][0], y + cube_xy[l_i][1])
    l_i += 1
  }
}

function drawGraphic(data){
  drawBackground(data)
  drawPlayerCard(data)
  drawVirusCube(data)
  drawMoveIndicator(data)
  drawGameInfo(data)
  drawPlayerPawn(data)
  drawStory(data)
}

function drawBackground(data){
  ctx.drawImage(background,0,0);
}

function drawPlayerPawn(data){
  if (data['player'][0]['latitude'] === data['player'][1]['latitude']){
    ctx.drawImage(player1, data['player'][0]['latitude']-10, data['player'][0]['longitude']- 20);
    ctx.drawImage(player2, data['player'][1]['latitude'], data['player'][1]['longitude']- 20);
  }
  else{
    ctx.drawImage(player1, data['player'][0]['latitude'], data['player'][0]['longitude']-20);
    ctx.drawImage(player2, data['player'][1]['latitude'], data['player'][1]['longitude']-20);
  }
}

function drawPlayerCard(data){
  if (data['own']){
    let order = 0
    data['own'].forEach((item) =>{
      let textColor = 'rgb(0,67,106)';
      let backgroundColor = 'rgb(150,222,255)';
      switch (item['color']){
        case 'blue':{
          textColor = 'rgb(0,67,106)'
          backgroundColor = 'rgb(109,207,246)'
          break
        }
        case 'violet':{
          textColor = 'rgb(58,0,106)'
          backgroundColor = 'rgb(161,134,190)'
          break
        }
        case 'yellow':{
          textColor = 'rgb(106,97,0)'
          backgroundColor = 'rgb(255,247,153)'
          break
        }
        case 'red':{
          textColor = 'rgb(106,0,0)'
          backgroundColor = 'rgb(245,152,157)'
          break
        }
      }
      print_card(order%4*130+60,Math.floor(order/4)*50+60,item['name'],"("+item['color']+")",textColor,backgroundColor)
      order += 1
    })
  }
}

function drawVirusCube(data){
  data['city'].forEach((city) => {
    if(city['blue']+city['red']+city['violet']+city['yellow'] > 0){
      print_cube(city['latitude'],city['longitude'],[city['blue'],city['violet'],city['red'],city['yellow']])
    }
    if(city['research_center'] > 0){
      ctx.drawImage(researchCenter,city['latitude']-5,city['longitude']-30)
    }
  })
}

function drawMoveIndicator(data) {
  moveList = []
  if (data['action']['move']['jet']) {
    data['city'].forEach((item) => {
      circle(item['latitude'], item['longitude'])
      moveList.push({
        "id": item["id"],
        "latitude": item['latitude'],
        "longitude": item['longitude']
      })
    })
  }
  else {
    if (data['action']['move']['drive']) {
      data['action']['move']['drive'].forEach((item) => {
        circle(item['location'][0], item['location'][1])
        moveList.push({
          "id": item["id"],
          "latitude": item['location'][0],
          "longitude": item['location'][1]
        })
      })
    }
    if (data['action']['move']['fly']) {
      data['action']['move']['fly'].forEach((item) => {
        circle(item['location'][0], item['location'][1])
        moveList.push({
          "id": item["id"],
          "latitude": item['location'][0],
          "longitude": item['location'][1]
        })
      })
    }
    if (data['action']['move']['rc']) {
      data['action']['move']['fly'].forEach((item) => {
        circle(item['location'][0], item['location'][1])
        moveList.push({
          "id": item["id"],
          "latitude": item['location'][0],
          "longitude": item['location'][1]
        })
      })
    }
  }
}

function drawGameInfo(data){
  if (data['game']['player_turn'] === 1)
    ctx.drawImage(player1, 110, 730);
  else
    ctx.drawImage(player2, 110, 730);
  ctx.font =  "17px Arial";
  ctx.textAlign = "left";
  ctx.fillStyle = "rgba(10,10,10,1)";
  ctx.fillText("Player " + data['game']['player_turn'] + " turn. "
      + data['game']['action_point'] + " Action point left. player hand:", 135, 753)

  ctx.drawImage(infectionMark, 34+24*data['game']['infection_track'],538)

  for (let i = 0; i < data['game']['outbreak_track']; i++)
    ctx.drawImage(outBreakMark,48 + 23 * i-14, 468)
  if (data['game']['blue'] === 1)
    ctx.drawImage(vaccineMark,45, 660)
  if (data['game']['violet'] === 1)
    ctx.drawImage(vaccineMark,85, 660)
  if (data['game']['red'] === 1)
    ctx.drawImage(vaccineMark,125, 660)
  if (data['game']['yellow'] === 1)
    ctx.drawImage(vaccineMark,165, 660)
  if ((data['action']['build']))
    ctx.drawImage(buildAvailable,602,844)
  if ((data['action']['treat'][0]+data['action']['treat'][1]+data['action']['treat'][2]+data['action']['treat'][3])>0)
    ctx.drawImage(treatAvailable,602,785)
  if ((data['action']['cure']))
    ctx.drawImage(cureAvailable,602,897)
}

function drawStory(data){
  ctx.drawImage(doctor1, 900,900)
  ctx.font =  "17px Arial";
  ctx.textAlign = "left";
  ctx.fillStyle = "rgba(10,10,10,1)";
  ctx.fillText(data['computerInfo'][0], 700, 753)
  data['computerInfo'].shift()
}

function checkLegitMove(data,x,y){
  command = false
  //click on map
  moveList.forEach((item)=>{
    let distance = (x-7 - item['latitude'])**2 + (y-7 - item['longitude'])**2
    if (distance < 250){
      command = 'move '+item["id"]
    }
  })
  //treat button
  if (((x-655)**2 + (y-791)**2) <1000){
    for (let i  = 0; i < data['action']['treat'].length; i++)
      if (data['action']['treat'][i] > 0)
        command = 'treat ' + i
  }
  //build button
  if (((x-655)**2 + (y-856)**2) <1000){
    if (data['action']['build']){
      command = 'build rc'
    }
  }
  //cure button
  if (((x-655)**2 + (y-912)**2) <1000){
    if (data['action']['cure']){
      command = 'cure '+ data['action']['cure']['cure']
    }
  }
  //new game button
  if (((x-236)**2 + (y-975)**2) <1000)
    command = "gameInit new"

  //new game button
  if (((x-378)**2 + (y-975)**2) <1000)
    command = "gameTutorial new"

  console.log(data['computerInfo'])
  return command
}

canvas.addEventListener('click', async function(event){
  event.preventDefault()
  let canvasBoundary = canvas.getBoundingClientRect()
  const x = event.clientX - canvasBoundary.left
  const y = event.clientY - canvasBoundary.top - 0.8125
  command = checkLegitMove(data,x,y)
  if (command){
    let data_obj = await fetch(`/test2?data=${command}`)
    data = await data_obj.json()
  }
  drawGraphic(data)
})
