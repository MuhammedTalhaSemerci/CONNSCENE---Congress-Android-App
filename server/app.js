const express = require("express");
const { time } = require("console");
const app = express();

app.get("/",function(req,res){

  res.send("Welcome to my server");

});

const server = require("http").createServer(app);
const io = require("socket.io").listen(server);
const port =3000;



io.on("connection", socket => {

  console.log("bir kullanıcı bağlandı:"+socket.id);
  io.emit("socket_id", socket.id); 

  socket.on('disconnect', () => {
    console.log("bir kullanıcı ayrıldı:"+socket.id);
    io.emit("socket_id_delete", socket.id); 
  });
 


socket.on("sayacdurdurma",msg =>{


  io.emit("sayac",msg);
  io.emit('sayacdurdurma',0);

});



  
socket.on("kayitlitoplusayac",msg =>{

  i = 0;
     
  for (i; i < msg.length ; i++){

   
    sayac = [msg[i][1],msg[i][2]];
    io.to(msg[i][0]).emit("sayac", sayac); 
    
  }

  i = 0;
     
  for (i; i < msg.length ; i++){
  
    io.to(msg[i][0]).emit("kon_isim", msg[i][3]); 
   
  }

});
 



socket.on("sayacvar", msg =>{

  i = 0;
  
     
  for (i; i < msg.length ; i++){
  
    io.to(msg[i][0]).emit("sayacvar", msg[i][1]); 
    console.log(msg[i][0]+"  "+ msg[i][1]);
   
  }

});
  
    

  socket.on("kayit_sayac", msg => {

    io.emit("kayit_sayac",msg);
  
  
  
    });






    socket.on("kayitlidata", msg => {
     
     

     
     
        i =0;
        for (i; i < msg.length ; i++){

          io.to(msg[i][0]).emit("resim", msg[i][1]); 


        }

        

      

  
      
      //
    
});



});


server.listen(port, () => console.log("server running on :" + port));




