import React, { Component} from "react";
import {TextInput, StyleSheet, Text, View ,Image,Dimension, Alert, RefreshControlComponent} from "react-native";
import io from "socket.io-client";
import CountDown from 'react-native-countdown-component';
import { vw, vh, vmin, vmax } from 'react-native-expo-viewport-units';

import AsyncStorage from '@react-native-community/async-storage';

import {
  widthPercentageToDP as wp2dp,
  heightPercentageToDP as hp2dp,
} from 'react-native-responsive-screen';







export const wp = dimension => {
  return wp2dp((dimension / 360) * 100 + '%');
};



export const hp = dimension => {
  return hp2dp((dimension / 760) * 100 + '%');
};


export default class App extends Component {
  
  
  
  constructor(props) {
    super(props);
    
    
    
    this.state = {
      sayac: [0,0],
      kon_isim: "",
      resim:"",
      ip:"",
      pong:"pending",
      kayit:[],
      kayitcikti:[],
       sayi :0,
       sayi1:0,
       socketbag : 0,

       rescount : 0,
       koncount : 0,

       sayacvar: false,
       sayacvarindex : 0,

       connection:0,
    };

 
  }




  givesayacvar = async (deger) => {
    try {
      
      await AsyncStorage.setItem('kayit_sayacvar',  JSON.stringify(deger));
    } catch (e) {
    
    }
  }

  getsayacvar = async() =>{
    try {
    value = await AsyncStorage.getItem('kayit_sayacvar');
    
    if (value != null){
    value = JSON.parse(value);
    this.setState({sayacvar: value});
   
    
    }
    
    }
  
  
  
    
    catch(error){
  
    
    }
  
    }











//////////////////////////////////////


  givedata = async (deger) => {
    try {
      
      await AsyncStorage.setItem('kayit_deger',  JSON.stringify(deger));
    } catch (e) {
    
    }
  }
  
  
  getdata = async() =>{
  try {
  value = await AsyncStorage.getItem('kayit_deger');
  
  if (value != null){
  value = JSON.parse(value);
  this.setState({kayitcikti : value});
 
  
  }
  
  }



  
  catch(error){

  
  }

  }








  givekondata = async (deger) => {
    try {
      
      await AsyncStorage.setItem('kon_isim_deger',  JSON.stringify(deger));
      
    }
    
    catch (e) {
   
    }
  }
  
  
  getkondata = async() =>{
  try {
  value = await AsyncStorage.getItem('kon_isim_deger');
  
  if (value != null){
  value = JSON.parse(value);
  this.setState({kon_isim : value});
 
  
  }
  
  }

  catch(error){
   
    
    }
  
    }






    giveresdata = async (deger) => {
      try {
        
        await AsyncStorage.setItem('resim_deger',  JSON.stringify(deger));
        
      }
      
      catch (error) {
      
      }
    }
    
    
    getresdata = async() =>{
    try {
    value = await AsyncStorage.getItem('resim_deger');
    
    if (value != null){
    value = JSON.parse(value);
    this.setState({resim: value});
   
    
    }
    
    }
  
    catch(error){
     
      
      }
    
      }


connect = async ()=>{

for ( i = 0; i < 255; i++)  {
  console.log(i);
  var url = "http://192.168.1."+i+":3000";
  try{
    const response = await fetch(url);
    console.log(response.status)
    if (response.status != 200){
    
    }
    this.socket = io(url);
    this.setState({connection : 1});
    this.componentDidMount();
    break
  }
  catch(error){
    

  }

      }
  
    }


  componentDidMount() {


     

    var kayitdeger = [];
    
    
    
    
    if(this.state.socketbag == 0){

     this.connect();
      


      this.setState({ socketbag: 1 });
    }
       
   console.log(this.state.connection);
if (this.state.connection == 1){
  
    
    this.socket.on("kon_isim", msg => {
      
      this.setState({ kon_isim:  msg });
      this.givekondata(msg);
     
    });
   
  
   
    this.socket.on("sayac", msg => {

      
      this.setState({ sayac:  msg });
      this.setState({kayitcikti : [0,0,0]});
      
      

    });

    this.socket.on("resim", msg => {
       
     this.giveresdata(msg);
     this.getresdata();

    });
   
    this.socket.on("kayit_sayac", msg => {
     
      this.setState({ kayit:  msg });
       kayitdeger = this.state.kayit;
       this.givedata(kayitdeger);
       
       

        
    });


    this.socket.on("state",msg =>{


      console.log(msg);
     
    
    });


    this.socket.on("sayacvar", msg => {
      
          this.givesayacvar(msg)
          this.setState({ sayacvar:  msg });

          console.log(this.state.sayacvar);

      
    
       
      
       

        
    });


    this.socket.on("sayacdurdurma", msg => {
       
      this.givedata([0,0,0]);
      
    
 
     });
     
    }

    if(this.state.sayacvarindex == 0){

      this.getsayacvar();
      this.setState({ sayacvarindex: 1 });
    }

    if(this.state.sayi == 0){

      this.getdata();
      this.setState({ sayi: 1 });
    }
    
    if(this.state.koncount == 0){
    
      this.getkondata();
      this.setState({ koncount: 1 });
    }
    
    if(this.state.rescount == 0){
    
      this.getresdata();
      this.setState({ rescount: 1 });
    }
    
  }


  render() {
     
    let konusmasure;
    var sayacgiris=0;
    
    var saniye = 0;


    const sayac = this.state.sayac;
    saniye = (60*60*sayac[0]) + (sayac[1]*60) ;

   
    
         

     sayacgiris = ( this.state.kayitcikti[0]*3600)+( this.state.kayitcikti[1]*60)+( this.state.kayitcikti[2])


    const kon_isim = this.state.kon_isim;
    
    
    
    console.log(kon_isim);
    var resim = "";
    resim = this.state.resim;
    
    
 
    if (saniye == 0 && sayacgiris > 0) {

konusmasure = sayacgiris;

    
    }


 else if ( sayacgiris == 0  && saniye > 0 ) {

  konusmasure = saniye;
      
    
    }






  return (

    <View >

    

    { 
    
    
    resim != 0  ?
    
<View>
    
    





{ this.state.sayacvar  ? 





<View>
{ konusmasure > 0 ?

<View>

       <View>


                <CountDown
                until={konusmasure}
                //duration of countdown in seconds
                timeToShow={['H',':','M',':','S']}
                //formate to show
                onFinish= { konusmasure =0, ()=> this.givedata([0,0,0])}
              
                //on Press call
                size={vh(5)}
                style={{height:vh(20)}}
              />
              
        </View>   
  
          <View style = {styles.merkez}>
        
                 <Text style={styles.bekleme}>{kon_isim}</Text> 
    
          </View></View>:

       <View style = {styles.merkez}>
    
      <Text style={styles.bekleme2x}>{kon_isim}</Text> 
 
       </View>
      
       }
       </View>:<View>
      
              <View>
            
              </View>



              <View>   
          
                    <View style = {styles.merkez}>
                  
                            <Text style={styles.bekleme2x}>{kon_isim}</Text> 
              
                   </View>
 
            </View>

  
          
      </View>


      
      }



  <View  style = {styles.merkez}>
  <Image 
        style={{width: wp(310), height:hp(560)}}
        source={{uri: `data:image/gif;base64,${resim}`}}
      />
  </View>
  
  </View>

:<View
style={styles.kon_merkez}

>

<Text style={styles.kon_paragraph}> Programa</Text>
<Text style={styles.kon_paragraph}> Hoşgeldiniz!</Text>

</View >
    
  


  }
  

                  </View>

  );

  




  }    


}

const styles = StyleSheet.create({
  container: {
    fontSize:20,
    color : "black",
   
    backgroundColor: "#F5FCFF",
  },

  bekleme : {

     fontSize: vw(6),

  },

  bekleme2x : {

    fontSize: vw(10),

 },

  merkez:{
    flex: 0,
     flexDirection: 'row',
    alignContent:'center',
    justifyContent:'center',
  },

  kon_container: {
    flex: 1,
    alignItems: 'stretch',
    justifyContent: 'center',
  },

  kon_bekleme : {

    fontSize: 24,

 },

  kon_merkez:{
     flex:0,
     textAlign: 'center',
    alignItems: 'center',
    justifyContent: 'center',
   
  },

  kon_image: {
    flexGrow:1,
    height:null,
    width:null,
    alignItems: 'center',
    justifyContent:'center',
  },
  kon_paragraph: {
    
    fontSize:vw(12),
    
    
    
  },

});