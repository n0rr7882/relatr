import React, { Component } from 'react'
import Button from '../lib/Button';
import IconButton from '../lib/IconButton';
import Thumb from '../lib/Thumb';
import Input from '../lib/Input';
import Textarea from '../lib/Textarea';
import ClipWithThumb from '../lib/ClipWithThumb';

export default class App extends Component {

  state = {
    value: 'asdf'
  };

  render() {
    return (
      <div>
        <Button href='#' />
        <IconButton href='#' name='heart'/>
        <Thumb href='#' imgPath="https://avatars1.githubusercontent.com/u/20741222?s=40&v=4" />
        <Input value={this.state.value} onChange={(e) => this.setState({ value: e.target.value })}/>
        <Textarea value={this.state.value} onChange={(e) => this.setState({ value: e.target.value })}/>
        <ClipWithThumb href='#' imgPath="https://avatars1.githubusercontent.com/u/20741222?s=40&v=4" title='유동호' description='n0rr7882@gmail.com'/>
      </div>
    )
  }
}
