import React, { Component } from 'react';
import styled from 'styled-components';

//data types that will later be changed to database

import dataV1 from '../public/merged.json';
//import dataV2 from '../public/datav2.json';
//import dataV3 from '../public/datav3.json';
//import dataV4 from '../public/merged.json';
//import dataV5 from '../public/datav5.json';
//import mouse from '../public/merged.json';


//components
import NounInput from './components/NounInput.js'
import DataVersion from './components/DataVersion.js'

const SERVER = 'http://localhost:5042/'

const Title = styled.h1`
  color: blue;
  text-align: center;
`;

const Body = styled.div`
  margin: 10px 20px 10px 20px;

`;

const Box = styled.div`
  margin: 30px 30px 30px 30px
  background-color: lightblue;
  border: 2px solid blue;
  border-radius: 5px;
  opacity: 0.7;
`

const Background = styled.div`
  padding-top: 1px;
  padding-bottom: 100%;
  height: 100%;
  width: 100%;
  background-image: url("https://webdesignjustforyou.com/p/wp-content/uploads/2013/08/bg.jpg");
  background-position: left bottom;
  background-attachment: fixed;
`

class App extends Component {
  constructor(){
    super();


    //discovered how to do this from stack overflow
    //we will remove/comment out the unneeded ones in finished product so
    //that they don't slow down initial load. Or we can have it fetch the
    //correct one from the database.

    this.nounsV1 = new Map();
    Object.keys(dataV1).forEach(key => {
      this.nounsV1.set(key, dataV1[key]);
    });
    //
    // this.nounsV2 = new Map();
    // Object.keys(dataV2).forEach(key => {
    //   this.nounsV2.set(key, dataV2[key]);
    // });
    //
    // this.nounsV3 = new Map();
    // Object.keys(dataV3).forEach(key => {
    //   this.nounsV3.set(key, dataV3[key]);
    // });

    // this.nounsV4 = new Map();
    // Object.keys(dataV4).forEach(key => {
    //   this.nounsV4.set(key, dataV4[key]);
    // });

    // this.nounsV5 = new Map();
    // Object.keys(dataV5).forEach(key => {
    //   this.nounsV5.set(key, dataV5[key]);
    // });

    // this.mouse = new Map();
    // Object.keys(mouse).forEach(key => {
    //   this.mouse.set(key, mouse[key]);
    // });

    this.state = {
      dataVersion: 'version1'

    };

    fetch(SERVER + 'api/version1/cat')
    .then((response)=>{
      if (response.ok){
        return response.json();
      }
    })
    .then((data)=>{
      this.setState({test: data});
    });

  }
  render() {
    let test = (<p></p>);

    if (this.state.test){
      mytest.push(this.state.test);
      console.log(this.state.test);
      console.log(this.state.test['assoc']);
    }

    let nounVerb ; //the input bar to input a noun into

    // below can be replaced. We are instead going to be passing
    // the name 'version#' as a thing to determine which database collection to
    // look into.

    nounverb = (<NounInput version={this.state.dataVersion}/>);
    // if (this.state.dataVersion === 'version1'){
    //   nounVerb = (<NounInput associate={this.nounsV1}/>);
    // }
    //
    // else if (this.state.dataVersion === 'version2'){
    //   nounVerb = (<NounInput associate={this.nounsV2}/>);
    // }
    // else if (this.state.dataVersion === 'version3'){
    //   nounVerb = (<NounInput associate={this.nounsV3}/>);
    // }
    // else if (this.state.dataVersion === 'version4'){
    //   nounVerb = (<NounInput associate={this.nounsV4}/>);
    // }
    // else if (this.state.dataVersion === 'version5'){
    //   nounVerb = (<NounInput associate={this.nounsV5}/>);
    // }
    //
    // else if (this.state.dataVersion === 'mouse'){
    //   nounVerb = (<NounInput associate={this.mouse}/>);
    // }

    return(
      <Background>
    <Box>
      <Title>Noun Verb Associator</Title>
      <Body>
        {test}
        <DataVersion version={this.state.dataVersion} setVersion={(version)=>this.setState({dataVersion: version})} />
        {nounVerb}
      </Body>
    </Box>
    </Background>
  )

  }
}


export default App;
