import React, {Component} from 'react';
import styled from 'styled-components';


//discovered how to do this on develepor.mozilla.org
const Col = styled.ul`
  -moz-column-count: 3;
  -webkit-column-count: 3;
  column-count: 3;
  list-style-type: none;
`;

function VerbList(props){

  let list;
  const verbs = props.associate.get(props.noun);

  /*
  This is where we would put the thing to sort by frequency
  */

  list = verbs.map((item)=> {return (<li key={item.verb}>{item.verb} {item.freq}</li>); });
  console.log(list);

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
      noun: ''
    }
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

    let verbPool = (
      <button
        type='button'
        onClick={()=>{
          let verbDisplay;
          if (this.props.associate.has(this.state.noun.toLowerCase())){
            verbDisplay = (<VerbList associate={this.props.associate} noun={this.state.noun.toLowerCase()} />);
            this.setState({display: verbDisplay});
        }else{
          verbDisplay = (<p> Sorry, the word "{this.state.noun}" has not been found in our corpus </p>);
          this.setState({display: verbDisplay});
        }

      }}>Enter</button>
    );


    return (
      <div>
      {inputBar}
      {verbPool}
      {this.state.display}
      </div>

    )
  }

}

NounInput.PropTypes = {
  associate: React.PropTypes.object.isRequired,

}

VerbList.PropTypes = {
  associate: React.PropTypes.object.isRequired,
  noun: React.PropTypes.string.isRequired,
}

export default NounInput;
