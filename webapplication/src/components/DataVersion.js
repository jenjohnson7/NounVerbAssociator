import React, { Component } from 'react';

/*
 * Version 1 = Method of first noun paired with all verbs following it in sentence
 * Version 2 = Method of each noun paired with immediately following verb in sentence
 *
 *
 *
 *
 *
 */


class DataVersion extends Component{
  constructor(props){
    super(props);

    this.state = {};
  }

  render(){

    /*Creates a drop down selector and sends back the currently selected stuff to App.js*/
    const versionPicker = (
      <select value={this.props.version} onChange={(event)=>this.props.setVersion(event.target.value)}>
      <option value='version1'>Version 1</option>
      <option value='version2'>Version 2</option>
      <option value='version3'>Version 3</option>
      <option value='version4'>Version 4</option>
      <option value='version5'>Version 5</option>
      <option value='mouse'>Mouse</option>
      </select>
    );

    let description ;

    if (this.props.version === 'version1'){
      description = (<span> = take first noun and all subsequent verbs.</span>);

    }else if (this.props.version === 'version2'){
      description = (<span> = take each noun followed by its immediate verb. </span>);

    }else if (this.props.version === 'version3'){
      description = (<span> = takes all nouns to all verbs in sentence. </span>);

    }else if (this.props.version === 'version4'){
      description = (<span> = takes each noun and its following verbs until next noun. </span>);

    }else if (this.props.version === 'version5'){
      description = (<span> = takes all nouns to all following verbs in sentence. </span>);

    }else if (this.props.version === 'mouse'){
      description = (<span> = version 2 test of our self-tokenized sentence of If You Give a Mouse a Cookie</span>)
    }

    return (<div>{versionPicker}{description}</div>);
  }

}

DataVersion.PropTypes = {
  version: React.PropTypes.string.isRequired,
  setVersion: React.PropTypes.func.isRequired,
}

export default DataVersion;
