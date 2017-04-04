import React, { Component } from 'react';
import styled from 'styled-components';

//data types that will later be changed to database

import dataV1 from '../public/datav1.json';
import dataV2 from '../public/datav2.json';
//import dataV3 from '../public/datav3.json';
import dataV4 from '../public/merged.json';
//import dataV5 from '../public/datav5.json';
import mouse from '../public/mouse.json';


//components
import NounInput from './components/NounInput.js'
import DataVersion from './components/DataVersion.js'


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

    this.nounsV2 = new Map();
    Object.keys(dataV2).forEach(key => {
      this.nounsV2.set(key, dataV2[key]);
    });
    //
    // this.nounsV3 = new Map();
    // Object.keys(dataV3).forEach(key => {
    //   this.nounsV3.set(key, dataV3[key]);
    // });

    this.nounsV4 = new Map();
    Object.keys(dataV4).forEach(key => {
      this.nounsV4.set(key, dataV4[key]);
    });

    // this.nounsV5 = new Map();
    // Object.keys(dataV5).forEach(key => {
    //   this.nounsV5.set(key, dataV5[key]);
    // });

    this.mouse = new Map();
    Object.keys(mouse).forEach(key => {
      this.mouse.set(key, mouse[key]);
    });

    this.state = {
      dataVersion: 'version1'

    };

  }
  render() {

    let nounVerb ; //the input bar to input a noun into
    if (this.state.dataVersion === 'version1'){
      nounVerb = (<NounInput associate={this.nounsV1}/>);
    }

    else if (this.state.dataVersion === 'version2'){
      nounVerb = (<NounInput associate={this.nounsV2}/>);
    }
    else if (this.state.dataVersion === 'version3'){
      nounVerb = (<NounInput associate={this.nounsV3}/>);
    }
    else if (this.state.dataVersion === 'version4'){
      nounVerb = (<NounInput associate={this.nounsV4}/>);
    }
    else if (this.state.dataVersion === 'version5'){
      nounVerb = (<NounInput associate={this.nounsV5}/>);
    }

    else if (this.state.dataVersion === 'mouse'){
      nounVerb = (<NounInput associate={this.mouse}/>);
    }

    return(
    <Box>
      <Title>Noun Verb Associator</Title>
      <Body>
        <DataVersion version={this.state.dataVersion} setVersion={(version)=>this.setState({dataVersion: version})} />
        {nounVerb}
      </Body>
    </Box>
  )

  }
}


export default App;
