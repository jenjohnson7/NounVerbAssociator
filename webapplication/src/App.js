import React, { Component } from 'react';
import styled from 'styled-components';

//data types that will later be changed to database


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
  background-color: dodgerblue;
  background-position: left bottom;
  background-attachment: fixed;
`

class App extends Component {
  constructor(){
    super();

    this.state = {
      dataVersion: 'version1'

    };

    // fetch(SERVER + 'api/version1/cat')
    // .then((response)=>{
    //   if (response.ok){
    //     return response.json();
    //   }
    // })
    // .then((data)=>{
    //   this.setState({test: data});
    // });

  }
  render() {
    // if (this.state.test){
    //   let mytest = this.state.test;
    //   console.log(this.state.test);
    //   console.log(this.state.test['assoc']);
    //   console.log(this.state.test['assoc'].length);
    // }

    //the input bar to input a noun into
    let nounverb = (<NounInput version={this.state.dataVersion}/>);

    return(
      <Background>
    <Box>
      <Title>Noun Verb Associator</Title>
      <Body>
        <DataVersion version={this.state.dataVersion} setVersion={(version)=>this.setState({dataVersion: version})} />
        {nounverb}
      </Body>
    </Box>
    </Background>
  )

  }
}


export default App;
