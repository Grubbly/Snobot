// drive.js
// Tristan Van Cise
// 11/29/2018
// Snobot
//
// Frontend interface to backend drive endpoints

import React, { Component } from 'react'
import axios from 'axios'

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
    }

    handleChange(event) {
        this.setState({speed: event.target.value});
        console.log('Speed set to ' + this.state.speed);
    }

    handleSubmit(event) {
        event.preventDefault();
    }

    drive_forward() {
        axios.get('http://192.168.1.143:5000/forward/' + this.state.speed)
            .then(console.log('Drive forward succeeded on: http://192.168.1.143:5000/forward/'));
    }

    drive_backward() {
        axios.get('http://192.168.1.143:5000/backward'.concat(this.state.speed))
            .then(console.log('Drive backward succeeded on: http://192.168.1.143:5000/backward'));
    }

    render() {
        return (
            <div>
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
                        Speed:
                        <input type="text" onChange={this.handleChange} value={this.state.speed} />
                    </label>
                    {/* <input type="submit" value="Submit" /> */}
                </form>
                
            </div>
        );
    }
}