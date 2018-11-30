// drive.js
// Tristan Van Cise
// 11/29/2018
// Snobot
//
// Frontend interface to backend drive endpoints

import React, { Component } from 'react';
import axios from 'axios';

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
        axios.get('http://192.168.1.143:5000/forward/' + this.state.speed)
            .then(console.log('Drive forward succeeded on: http://192.168.1.143:5000/forward/'));
    }

    drive_backward() {
        axios.get('http://192.168.1.143:5000/backward/' + this.state.speed)
            .then(console.log('Drive backward succeeded on: http://192.168.1.143:5000/backward'));
    }

    onKeyPressed(e) {
        if(e.keyCode === 87) {
            this.drive_forward();
        }
        if(e.keyCode === 83) {
            this.drive_backward();
        }
        console.log(e.keyCode);
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