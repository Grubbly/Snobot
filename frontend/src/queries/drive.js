// drive.js
// Tristan Van Cise
// 11/29/2018
// Snobot
//
// Frontend interface to backend drive endpoints

import React, { Component } from 'react';
import axios from 'axios';

/***  RASPBERRY PI RUNNING FLASK BACKEND IP ***/
const url_raw = 'http://192.168.137.205';
const url = url_raw + ':5000';

export class DriveControl extends Component {
    constructor(props) {
        super(props)

        this.state = {
            speed: '0',
            top_position: '1',
            bottom_position: '1',
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.drive_forward = this.drive_forward.bind(this);
        this.drive_backward = this.drive_backward.bind(this);
        this.spin_left = this.spin_left.bind(this);
        this.spin_right = this.spin_right.bind(this);
        this.onKeyPressed = this.onKeyPressed.bind(this);
        this.stop = this.stop.bind(this);
    }

    handleChange(event) {
        if(event.target.value >= 0 && event.target.value <= 100) {
            this.setState({speed: event.target.value});
            // console.log('Speed set to ' + this.state.speed);
        }
    }

    handleTopServo(event) {
        if(event.target.value >= 0 && event.target.value <= 100) {
            this.setState({top_position: event.target.value});
            // console.log('Speed set to ' + this.state.speed);
        }
    }

    handleSubmit(event) {
        event.preventDefault();
    }

    spin_left() {
        console.log("Inside spin left");
        const endpoint = url + '/spinLeft/' + this.state.speed;
        axios.get(endpoint)
            .then(console.log('Drive forward succeeded on: ' + endpoint));
    }

    spin_right() {
        const endpoint = url + '/spinRight/' + this.state.speed;        
        axios.get(endpoint)
            .then(console.log('Drive forward succeeded on: ' + endpoint));
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

    turn_top_camera_servo(position) {
        const endpoint = url + '/turnTopServoCamera/' + position;
        axios.get(endpoint)
            .then(console.log('Turn top camera servo succeeded on: ' + endpoint));
    }

    stop() {
        const endpoint = url + '/forward/0';
        axios.get(endpoint)
            .then(console.log('Stop succeeded on: ' + endpoint));
        this.setState({speed: 0});
    }

    onKeyPressed(e) {
        const W = 87;
        const A = 65;
        const S = 83;
        const D = 68;
        const SPACE = 32;
        const Q = 81;
        const LEFT = 37;
        const RIGHT = 39;
        const UP = 38;
        const DOWN = 40;
        const SHIFT = 16;

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
        if(e.keyCode >= 96 && e.keyCode <= 105) {
            this.setState({speed: (e.keyCode-96)*11});
        }
        if(e.keyCode === RIGHT) {
            let position = parseInt(this.state.top_position);
            if(this.state.top_position < 98 && this.state.top_position > 0) {
                position += 2;
            }
            this.turn_top_camera_servo(position);
            this.setState({top_position: position});
        }
        if(e.keyCode === LEFT) {
            let position = parseInt(this.state.top_position);
            if(this.state.top_position < 100 && this.state.top_position > 2) {
                position -= 2;
            }
            this.turn_top_camera_servo(position);
            this.setState({top_position: position});
        }
        if(e.keyCode === UP) {
            let position = parseInt(this.state.bottom_position);
            if(this.state.bottom_position < 98 && this.state.bottom_position > 0) {
                position += 2;
            }
            this.turn_bottom_camera_servo(position);
            this.setState({bottom_position: position});
        }
        if(e.keyCode === DOWN) {
            let position = parseInt(this.state.bottom_position);
            if(this.state.bottom_position < 100 && this.state.bottom_position > 2) {
                position -= 2;
            }
            this.turn_bottom_camera_servo(position);
            this.setState({bottom_position: position});
        }
        if(e.keyCode === SPACE || e.keyCode === Q) {
            this.stop();
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
                <article>
                    <iframe src={url_raw + ":8080/?action=stream"} title="NoIR Camera View" width="700" height="1000" scrolling="no" style={{border: "none"}}>
                        <p> Uh oh, browser does not support iframes.</p>
                    </iframe>
                </article>

                <article style={{position: "absolute", 
                                // background: "seagreen", 
                                top: "700px",
                                right: "0%",
                                width: "100%",
                                height: "100%"
                                }}>
                    <span>
                        <button onClick={this.drive_forward}>
                            Forward
                        </button>
                        <button onClick={this.drive_backward}>
                            Backward
                        </button>
                        <button onClick={this.spin_left}>
                            Spin Left
                        </button>
                        <button onClick={this.spin_right}>
                            Spin Right
                        </button>
                    </span>

                    <form onSubmit={this.handleSubmit}>
                        <label> 
                            <br />
                            Speed <br /> 
                            <input type="text" onChange={this.handleChange} value={this.state.speed} />
                            <br />
                            Top Servo <br /> 
                            <input type="text" onChange={this.handleTopServo} value={this.state.top_position} />
                        </label>
                    </form>      
                </article>
                
            </div>
        );
    }
}