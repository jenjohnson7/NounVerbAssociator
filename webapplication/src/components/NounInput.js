import React, {Component} from 'react';
import styled from 'styled-components';

const SERVER = 'http://localhost:5042/'

//discovered how to do this on develepor.mozilla.org
const Col = styled.ul`
  -moz-column-count: 3;
  -webkit-column-count: 3;
  column-count: 3;
  list-style-type: none;
`;

const TopPadding = styled.div`
  padding-top: 20px;
`;

function VerbList(props){

  let list;
  let verbs = props.associate['assoc'];

  /*
  Sorting by frequency
  */

  if (props.sort === 'highFrequency'){
    verbs.sort(((a,b) => {return b.freq - a.freq})); //sorts from greatest freq to lowest freq
  }
  else if (props.sort === 'lowFrequency'){
    verbs.sort(((a,b) => {return a.freq - b.freq})); //sorts from lowest freq to greatest freq
  }
  else if (props.sort === 'alphabetically'){
    verbs.sort(((a,b) => { //sorts alphabetically
      if (a.verb < b.verb) {return -1;}
      if (a.verb > b.verb) {return 1;}
      return 0;}))
  }

  //within this mapping function include which items to map (I think)
  list = verbs.map((item)=> {return (<li key={item.verb}>{item.verb} {item.freq}</li>); });
  //console.log(list);

  return (
    <div>
    <Col>{list}</Col>
    </div>
  )

}

class NounInput extends Component{
  constructor(props){
    super(props);

    this.state = {
      noun: '',
      displaying: '',
      sort: 'alphabetically'
    }

  }

  getVerbArray(version, noun){

    fetch(SERVER + 'api/' + version + '/' + noun)
    .then((response)=>{
      if (response.ok){
        return response.json();
      }
    })
    .then((data)=>{
      this.setState({associated: data, displaying: noun});
    });

  }

  render () {

    let inputBar = (
      <input
        type='text'
        placeholder='noun'
        value={this.state.noun}
        onChange={(event)=>this.setState({noun: event.target.value})}>
      </input>
    );

    //change below prop with a fetch to server and a set state of verb array and queried noun
    let searchButton = (
      <button type='button' onClick={()=> this.getVerbArray(this.props.version, this.state.noun)}>Search</button>
    );

    let sortMethod = (
      <select value={this.state.sort} onChange={(event)=>this.setState({sort: event.target.value})}>
      <option value='alphabetically'>Alphabetically A-Z</option>
      <option value='highFrequency'>Frequency (high to low)</option>
      <option value='lowFrequency'>Frequency (low to high)</option>
      </select>
    );

    let verbDisplay = (<p> Please enter a singular noun.</p>);

    //displaying verbs if searchButton was clicked
    //TODO: Replace below prop with assoc array from database
    if (this.state.associated){
      verbDisplay = (
        <div>
        <span>Sort verbs {sortMethod}</span>
        <p>Associating <b>"{this.state.displaying}"</b> to:</p>
        <VerbList associate={this.state.associated} sort={this.state.sort}/>
        </div>);

    }else if (this.state.displaying !== ''){
      verbDisplay = (<p>Sorry, the word "{this.state.displaying}" has not been found in our corpus. Please make sure the noun is spelled correctly and that it is singular. </p>);
    }

    return (
      <TopPadding>
      {inputBar}{searchButton}
      {verbDisplay}
      </TopPadding>

    )
  }

}

NounInput.PropTypes = {
  version: React.PropTypes.string.isRequired,
}

VerbList.PropTypes = {
  associate: React.PropTypes.object.isRequired,
  noun: React.PropTypes.string.isRequired,
}

export default NounInput;
