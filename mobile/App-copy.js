import React, { Component } from "react";
import { TextInput, StyleSheet, Text, View } from "react-native";
import io from "socket.io-client";
import CountDown from 'react-native-countdown-component';



export default class App extends Component {
  
  constructor(props) {
    super(props);
    this.state = {
      chatMessage:"" ,
      chatMessages: 0
      
      
      
    };

 
  }

  componentDidMount() {
    this.socket = io("http://192.168.1.42:3000");
    
    this.socket.on("my message", msg => {
      
      this.setState({ chatMessages:  msg });
     
    });
   
  

  }




  render() {

    const chatMessages = this.state.chatMessages;
   

    return (
      <View style={styles.container}>
       
      <Text>{parseInt(chatMessages)}</Text>
      

      <CountDown
        size={30}
        until={60* 60 * parseInt(chatMessages)}
        onFinish={() => alert('Finished')}
        digitStyle={{backgroundColor: '#FFF', borderWidth: 2, borderColor: '#1CC625'}}
        digitTxtStyle={{color: '#1CC625'}}
        timeLabelStyle={{color: 'red', fontWeight: 'bold'}}
        separatorStyle={{color: '#1CC625'}}
        timeToShow={['H', 'M', 'S']}
        timeLabels={{m: null, s: null}}
        showSeparator
      />

                    </View>

       
         
     
     

    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#F5FCFF"
  }
});