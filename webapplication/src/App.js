import React, { Component } from 'react';
import data from '../public/data.json';


import './App.css';

class App extends Component {
  constructor(){
    super();

    /*
      This code is responsible for setting up our data store.
      We read in the data from seed.json and place it in this Map object.

      The Map is a data structure that stores key value pairs. In this instance,
      the keys are sections and the values are arrays of the articles that
      appear in each section. Note that the section is determined by the first
      letter of the article's title.

      The Map does return keys in the order they are created, by the original
      article store is not in order, so you will need to sort both the section
      headings and the titles when you display them.
      */


    console.log('hi');



  }
  render() {
    /* This is where you need to setup the view for the page */

    return(
    <div>
    </div>
  )

  }
}

export default App;
