import React, { Component } from 'react'
import PropTypes from 'prop-types'

import TimeAgo from 'react-timeago';

import ClipWithThumb from '../../../lib/ClipWithThumb';
import Button from '../../../lib/Button';
import IconButton from '../../../lib/IconButton';

import { render } from '../../../utils/chain-render';

import './Chain.css';

export default class Chain extends Component {

    static propTypes = {
        chain: PropTypes.object.isRequired,
    }

    state = {
        chain: this.props.chain
    };

    componentDidMount() {
        render(this.props.chain).then(chain => this.setState({ chain }));
    }

    render() {
        const chain = this.state.chain;
        return (
            <div className='chain'>
                {chain.parent_chain ? (
                    <div className='chain-extend'>
                        <IconButton color='text-blue' iconType='s' iconName='ellipsis-h' />
                    </div>
                ) : null}
                <div className='chain-header'>
                    <ClipWithThumb
                        href='#'
                        imgPath={chain.account.thumbnail || null}
                        title={`${chain.account.user.first_name} ${chain.account.user.last_name}`}
                        description={`@${chain.account.user.username} (${chain.account.user.email})`}
                    />
                    <Button color='blue' text='Follow' />
                </div>
                <div className='chain-content'>
                    <p dangerouslySetInnerHTML={{ __html: chain.text }} />
                </div>
                <div className='chain-date'>
                    <TimeAgo date={chain.created_at} />
                </div>
                <div className='chain-footer'>
                    <div className='chain-footer-left'>
                        <IconButton
                            color='text-blue'
                            iconType='s'
                            iconName='reply'
                        />
                        <IconButton
                            color='text-blue'
                            iconType='s'
                            iconName='edit'
                        />
                    </div>
                    <div className='chain-footer-right'>
                        <IconButton
                            color='text-blue'
                            iconType='s'
                            iconName='heart'
                            text={chain.likes.length.toString()}
                        />
                        <IconButton
                            color='text-gray'
                            iconType='s'
                            iconName='retweet'
                            text={chain.child_chains.length.toString()}
                        />
                    </div>
                </div>
            </div>
        );
    }
}
