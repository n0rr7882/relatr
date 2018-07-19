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
                    "thumbnail": "http://localhost:8000/public/users/1/thumbnails/14a709a4-f4cc-4d23-b683-6219f8757233.jpeg",
                    "banner": "http://localhost:8000/public/users/1/banners/fe6adcbb-f2fd-45e1-83b9-ba48e34d15bd.jpeg",
                    "username": "norr",
                    "first_name": "Dongho",
                    "last_name": "Yu",
                    "email": "n0rr7882@gmail.com",
                    "date_joined": "2018-06-29T05:35:02.753770Z"
                },
                "thumbnail": "http://localhost:8000/public/users/1/thumbnails/14a709a4-f4cc-4d23-b683-6219f8757233.jpeg",
                "banner": "http://localhost:8000/public/users/1/banners/fe6adcbb-f2fd-45e1-83b9-ba48e34d15bd.jpeg",
                "created_at": "2018-06-29T05:40:10.930443Z"
            },
            "text": "#asdf #asdfffff\n ㅁㄴㅇㄹㅁㄴㅇㄹ\n #안녕",
            "image": null,
            "tags": [
                "안녕",
                "asdfffff",
                "asdf"
            ],
            "mentions": [
                {
                    "id": 2,
                    "user": {
                        "id": 2,
                        "thumbnail": null,
                        "banner": null,
                        "username": "test1",
                        "first_name": "FN",
                        "last_name": "LN",
                        "email": "test1@gmail.com",
                        "date_joined": "2018-06-29T05:39:18.993960Z"
                    },
                    "thumbnail": null,
                    "banner": null,
                    "created_at": "2018-06-29T05:39:19.123021Z"
                },
                {
                    "id": 4,
                    "user": {
                        "id": 4,
                        "thumbnail": null,
                        "banner": null,
                        "username": "test3",
                        "first_name": "F3",
                        "last_name": "L3",
                        "email": "test3@gmail.com",
                        "date_joined": "2018-06-29T05:39:42.312320Z"
                    },
                    "thumbnail": null,
                    "banner": null,
                    "created_at": "2018-06-29T05:39:42.450048Z"
                }
            ],
            "likes": [
                {
                    "id": 2,
                    "user": {
                        "id": 2,
                        "thumbnail": null,
                        "banner": null,
                        "username": "test1",
                        "first_name": "FN",
                        "last_name": "LN",
                        "email": "test1@gmail.com",
                        "date_joined": "2018-06-29T05:39:18.993960Z"
                    },
                    "thumbnail": null,
                    "banner": null,
                    "created_at": "2018-06-29T05:39:19.123021Z"
                }
            ],
            "parent_chain": null,
            "child_chains": [
                15
            ],
            "created_at": "2018-06-29T05:51:21.500437Z"
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
