// drive.js
// Tristan Van Cise
// 11/29/2018
// Snobot
//
// Frontend interface to backend drive endpoints

import React, { Component } from 'react';
import axios from 'axios';

/***  RASPBERRY PI RUNNING FLASK BACKEND IP ***/
const url = 'http://192.168.1.143:5000';

export class DriveControl extends Component {
    constructor(props) {
        super(props)

        this.state = {
            speed: '0',
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.drive_forward = this.drive_forward.bind(this);
        this.drive_backward = this.drive_backward.bind(this);
        this.spin_left = this.spin_left(this);
        this.spin_right = this.spin_right(this);
        this.onKeyPressed = this.onKeyPressed.bind(this);
    }

    handleChange(event) {
        if(event.target.value >= 0 && event.target.value <= 100) {
            this.setState({speed: event.target.value});
            // console.log('Speed set to ' + this.state.speed);
        }
    }

    handleSubmit(event) {
        event.preventDefault();
    }

    drive_forward() {
        const endpoint = url + '/forward/' + this.state.speed;
        axios.get(endpoint)
            .then(console.log('Drive forward succeeded on: ' + endpoint));
    }

    drive_backward() {
        const endpoint = url + '/backward/' + this.state.speed;
        axios.get(endpoint)
            .then(console.log('Drive backward succeeded on: ' + endpoint));
    }

    spin_left() {
        const endpoint = url + '/spinLeft/' + this.state.speed;
        axios.get(endpoint)
            .then(console.log('Drive forward succeeded on: ' + endpoint));
    }

    spin_right() {
        const endpoint = url + '/spinRight/' + this.state.speed;        
        axios.get(endpoint)
            .then(console.log('Drive forward succeeded on: ' + endpoint));
    }

    onKeyPressed(e) {
        const W = 87;
        const A = 65;
        const S = 83;
        const D = 68;

        if(e.keyCode === W) {
            this.drive_forward();
        }
        if(e.keyCode === A) {
            this.spin_left();
        }
        if(e.keyCode === S) {
            this.drive_backward();
        }
        if(e.keyCode === D) {
            this.spin_right();
        }
    }

    render() {
        return (
            <div 
                className="control"
                style={{color: "coral"}}
                onKeyDown={this.onKeyPressed}
                tabIndex="0"
            >
                <span>
                    <button onClick={this.drive_forward}>
                        Forward
                    </button>
                    <button onClick={this.drive_backward}>
                        Backward
                    </button>
                </span>

                <form onSubmit={this.handleSubmit}>
                    <label> 
                        <br />
                        Speed <br /> 
                        <input type="text" onChange={this.handleChange} value={this.state.speed} />
                    </label>
                </form>      
            </div>
        );
    }
}