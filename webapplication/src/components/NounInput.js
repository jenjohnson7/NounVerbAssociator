import React, {Component} from 'react';
import styled from 'styled-components';

const SERVER = 'http://localhost:5042/'

const Col = styled.ul`
  list-style-type: none;
`
const InnerCol = styled.li`
  float: left;
  width: 25%;
`

const TopPadding = styled.div`
  padding-top: 20px;
  overflow:auto;
`;


function VerbList(props){

  let list;
  let verbs = props.associate['assoc'];

  /*
  Sorting by frequency
  */

  if (props.sort === 'highFrequency'){ //sorts high to low
    verbs.sort(((a,b) => {
      if (b.freq - a.freq !== 0) {
        return b.freq - a.freq
      }else{ //if same, go by alpha-order
        if (a.verb < b.verb) {return -1;}
        if (a.verb > b.verb) {return 1;}
        return 0;
      }}));
  }

  else if (props.sort === 'lowFrequency'){ //sorts low to high
    verbs.sort(((a,b) => {
      if (a.freq - b.freq !== 0) {
        return a.freq - b.freq
      }else{ //if same, go by alpha-order
        if (a.verb < b.verb) {return -1;}
        if (a.verb > b.verb) {return 1;}
        return 0;
      }}));
  }

  else if (props.sort === 'alphabetically'){
    verbs.sort(((a,b) => { //sorts alphabetically
      if (a.verb < b.verb) {return -1;}
      if (a.verb > b.verb) {return 1;}
      return 0;}))
  }

  //within this mapping function include which items to map (I think)
  if (props.showfreq){
    list = verbs.map((item)=> {return (<InnerCol key={item.verb}>{item.verb} {item.freq}</InnerCol>); });
  }else{
    list = verbs.map((item)=> {return (<InnerCol key={item.verb}>{item.verb}</InnerCol>); });
  }

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
      sort: 'highFrequency',
      associated: null,
      showfreq: true
    }

  }

  filterFreq(assoc){ //where assoc is object['assoc'] (aka: array of verb objects)
    if (assoc.length <= 44){

      //--
      console.log(" <= 44: length", assoc.length);
      let totalfreq = 0;
      assoc.forEach(verb => {totalfreq += verb['freq']});
      console.log("Mean = ", totalfreq / (assoc.length));
      //--

      return assoc;

    }else{
      let totalfreq = 0;
      assoc.forEach(verb => {totalfreq += verb['freq']});

      console.log("totalfreq =", totalfreq);

      const mean = totalfreq / (assoc.length)
      const upper = Math.floor(mean * 5);
      const lower = Math.floor(mean * .3);

      let filtered = assoc.filter(verb => {
        return ((verb['freq'] < upper) && (verb['freq'] > lower))});

      if (filtered.length >= 88){
        const bolster = Math.floor(filtered.length / 200);
        filtered = filtered.filter(verb => {
          if (lower <= 2){
            return verb['freq'] > 1 + bolster;

          }else{
            return verb['freq'] > (lower + (lower * .3) + bolster);
          }}
        );
      }

      console.log("Objects before cutoff ", assoc.length);
      console.log("Objects after cutoff ", filtered.length);
      console.log("Mean = ", mean);
      console.log("Upper = ", upper);
      console.log("Lower = ", lower);

      return filtered;
    }

  }

  getVerbArray(version, noun){
    noun = noun.toLowerCase();

    fetch(SERVER + 'api/' + version + '/' + noun)
    .then((response)=>{
      if (response.ok){
        return response.json();
      }
    })
    .then((data)=>{
      console.log(data['noun']);
      data['assoc'] = this.filterFreq(data['assoc']);
      this.setState({associated: data, displaying: noun});
    });

  }

  render () {

    let inputBar = (
      <input
        type='text'
        placeholder='noun'
        value={this.state.noun}
        onChange={(event)=>this.setState({associated: null, noun: event.target.value})}>
      </input>
    );

    let showFreqBox = (
      <input
        type='checkbox'
        onClick={()=> this.state.showfreq ? this.setState({showfreq: false}) : this.setState({showfreq: true})}>
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
    if (this.state.associated){
      verbDisplay = (
        <div>
         <span>Hide Frequencies? Yes{showFreqBox}</span>
         <br></br>
         <span>Sort verbs {sortMethod}</span>
         <p>Associating <b>"{this.state.displaying}"</b> with:</p>
         <VerbList associate={this.state.associated} sort={this.state.sort} showfreq={this.state.showfreq}/>
        </div>);

      }
    // }else if (this.state.displaying !== ''){
    //   verbDisplay = (<p>Sorry, the word "{this.state.displaying}" has not been found in our corpus. Please make sure the noun is spelled correctly and that it is singular. </p>);
    // }

    return (
      <TopPadding>
      {inputBar}{searchButton}
      {verbDisplay}
      </TopPadding>

    )
  }

}

NounInput.PropTypes = {
  version: React.PropTypes.string.isRequired
}

VerbList.PropTypes = {
  associate: React.PropTypes.object.isRequired,
  noun: React.PropTypes.string.isRequired,
  showfreq: React.PropTypes.bool.isRequired
}

export default NounInput;
