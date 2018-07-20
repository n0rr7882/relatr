import React, { Component } from 'react'
import Button from '../lib/Button';
import IconButton from '../lib/IconButton';
import Thumb from '../lib/Thumb';
import Input from '../lib/Input';
import Textarea from '../lib/Textarea';
import ClipWithThumb from '../lib/ClipWithThumb';
import Chain from './templates/Chain/Chain';

export default class App extends Component {

    state = {
        value: 'asdf',
        chain: {
            "id": 1,
            "account": {
                "id": 1,
                "user": {
                    "id": 1,
                    "thumbnail": null,
                    "banner": null,
                    "username": "norr",
                    "first_name": "Dongho",
                    "last_name": "Yu",
                    "email": "n0rr7882@gmail.com",
                    "date_joined": "2018-07-19T06:00:31.103179Z"
                },
                "thumbnail": null,
                "banner": null,
                "created_at": "2018-07-19T06:00:31.224239Z"
            },
            "text": "#이것은 #태그\r\n입**니**다. @test",
            "image": null,
            "tags": [
                {
                    "id": 1,
                    "name": "이것은"
                },
                {
                    "id": 6,
                    "name": "태그"
                }
            ],
            "mentions": [
                {
                    "id": 2,
                    "user": {
                        "id": 2,
                        "thumbnail": null,
                        "banner": null,
                        "username": "test",
                        "first_name": "Harry",
                        "last_name": "Lee",
                        "email": "test1@gmail.com",
                        "date_joined": "2018-07-20T03:16:03.788796Z"
                    },
                    "thumbnail": null,
                    "banner": null,
                    "created_at": "2018-07-20T03:16:03.920303Z"
                }
            ],
            "likes": [],
            "parent_chain": null,
            "child_chains": [],
            "created_at": "2018-07-19T06:01:04.765431Z"
        }
    };

    render() {
        return (
            <div>
                <Button href='#' />
                <IconButton href='#' name='heart' />
                <Thumb href='#' imgPath="https://avatars1.githubusercontent.com/u/20741222?s=40&v=4" />
                <Input value={this.state.value} onChange={(e) => this.setState({ value: e.target.value })} />
                <Textarea value={this.state.value} onChange={(e) => this.setState({ value: e.target.value })} />
                <ClipWithThumb href='#' imgPath="https://avatars1.githubusercontent.com/u/20741222?s=40&v=4" title='유동호' description='n0rr7882@gmail.com' />
                <Chain chain={this.state.chain} />
            </div>
        )
    }
}
