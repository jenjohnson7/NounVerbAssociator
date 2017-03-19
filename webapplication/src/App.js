import React, { Component } from 'react';
import data from '../public/newdata_filtered.json';
import styled from 'styled-components';

import NounInput from './components/NounInput.js'

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
    this.nouns = new Map();
    Object.keys(data).forEach(key => {
      this.nouns.set(key, data[key]);
    })


  }
  render() {

    return(
    <div>
      <Title>Noun Verb Associator</Title>
      <Body>
        <NounInput associate={this.nouns}/>
      </Body>
    </div>
  )

  }
}


export default App;
