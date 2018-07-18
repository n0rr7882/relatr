import React, { Component } from 'react'
import PropTypes from 'prop-types'

import ClipWithThumb from '../../../lib/ClipWithThumb';
import Button from '../../../lib/Button';

import './Chain.css';

export default class Chain extends Component {

    static propTypes = {
        chain: PropTypes.object.isRequired,
    }

    render() {
        return (
            <div className='chain'>
                
            </div>
        );
    }
}
