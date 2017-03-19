import React, { Component } from 'react';
<<<<<<< HEAD
import data from '../public/newdata_filtered.json';
=======
>>>>>>> 1cee6cd34b935d719673665a997e07e6dec089bc
import styled from 'styled-components';

//data types that will later be changed to database
import dataV1 from '../public/datav1.json';
import dataV2 from '../public/datav2.json';
import mouse from '../public/mouse.json';


//components
import NounInput from './components/NounInput.js'
import DataVersion from './components/DataVersion.js'


const Title = styled.h1`
  text-align: center;
`;

const Body = styled.div`
  margin: 10px 20px 10px 20px;

`;

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

    else if (this.state.dataVersion === 'mouse'){
      nounVerb = (<NounInput associate={this.mouse}/>);
    }

    return(
    <div>
      <Title>Noun Verb Associator</Title>
      <Body>
        <DataVersion version={this.state.dataVersion} setVersion={(version)=>this.setState({dataVersion: version})} />
        {nounVerb}
      </Body>
    </div>
  )

  }
}


export default App;
