import { React, useState } from 'react';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import { Avatar, Button } from '@material-ui/core';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import axios from 'axios';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import validator from 'validator';
import PasswordChecklist from "react-password-checklist";
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import InputLabel from '@mui/material/InputLabel';


const Signup = () => {

    const [fullName, setFullName] = useState('');
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [submitted, setSubmitted] = useState(false);
    const [error, setError] = useState('');
    const [passwordShown, setPasswordShown] = useState(false);
    //State to check if user already exists
    const [userExists, setUserExists] = useState(false);
    const [role, setRole] = useState('');

    const handleFullName = (e) => {
        setFullName(e.target.value);
        setSubmitted(false);
    };

    const handleUsername = (e) => {
        setUsername(e.target.value);
        setSubmitted(false);
    };

    const handleEmail = (e) => {
        setEmail(e.target.value);
        setSubmitted(false);
    };

    const handlePassword = (e) => {
        setPassword(e.target.value);
        setSubmitted(false);
    };

    const handleConfirmPassword = (e) => {
        setConfirmPassword(e.target.value);
        setSubmitted(false);
    };

    const handleSubmit = async (e) => {
        const registered = {
            fullName: fullName,
            username: username,
            email: email,
            password: password,
            role: role
        }
        axios.post("http://localhost:4000/signup", registered)
            .then(response =>
                console.log('User has been added to the database successfully'),
                setSubmitted(true),
                setError(''))
        setFullName("");
        setUsername("");
        setEmail("");
        setPassword("");
        setConfirmPassword("");
        
    };

    const togglePassword = () => {
        setPasswordShown(!passwordShown);
    };

    const handleRole = (event) => {
        setRole(event.target.value);
    };

    function validateEmail(email) {
        const regexp = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return regexp.test(email);
    }

    async function checkExistingUser(username, email) {
        const user = {
            username: username,
            email: email
        }
        return axios.post("http://localhost:4000/checkExistingUser", user).then(response => {
            return response.data.userExists
        })
    }

    const paperStyle = {
        padding: 20,
        height: '90%',
        maxHeight: '675px',
        width: 280,
        margin: "20px auto"
    }

    const avatarStyle = {
        backgroundColor: '#1bbd7e'
    }

    const buttonStyle = { margin: '30px 0' }

    const backGroundImage = {
        display: 'flex',
        minHeight: '100vh',
        backgroundImage: "url(/assets/landing_page_background.jpeg)",
        backgroundSize: 'cover',
        justifyContent: 'center'
    }

    const errorMessage = {
        color: 'red',
        display: 'flex',
        justifyContent: 'center',
        fontWeight: 'bold'
    }

    const passwordShow = {
        display: 'flex',
    }

    const pStyle = {
        position: 'relative',
        left: '-15px'
    }

    const roleSelectStyle = {
        marginTop: '30px',
        height: '35px',
    }

    const roleSelectLabelStyle = {
        marginTop: '20px'
    }

    return (
        <div style={backGroundImage}>
            <Grid>
                <Paper elevation={10} style={paperStyle}>
                    <Grid align='center'>
                        <Avatar style={avatarStyle}>
                            <LockOutlinedIcon />
                        </Avatar>
                        <h2>
                            Sign Up
                        </h2>
                    </Grid>
                    <TextField label='Full Name' placeholder='Enter full name' onChange={handleFullName} value={fullName} variant="standard" fullWidth required />
                    <TextField label='Username' placeholder='Enter username' onChange={handleUsername} value={username} variant="standard" fullWidth required />
                    <TextField label='Email' placeholder='Enter email' onChange={handleEmail} value={email} variant="standard" fullWidth required />
                    
                    <TextField label='Password' placeholder='Enter password' onChange={handlePassword} value={password} variant="standard" type={passwordShown ? "text" : "password"} fullWidth required />
                    <TextField label='Confirm Password' placeholder='Enter password' onChange={handleConfirmPassword} value={confirmPassword} variant="standard" type={passwordShown ? "text" : "password"} fullWidth required />
                    <FormControl variant="standard" fullWidth>
                        <InputLabel style={roleSelectLabelStyle}>Select Role *</InputLabel>
                            <Select
                                value={role}
                                label="Role"
                                onChange={handleRole}
                                style={roleSelectStyle}
                            >
                                <MenuItem value={'Teacher'}>Teacher</MenuItem>
                                <MenuItem value={'Student'}>Student</MenuItem>
                        </Select>
                    </FormControl>
                    
                    <div style={passwordShow}>
                        <FormControlLabel
                            control={
                                <Checkbox
                                    name="checkedB"
                                    color="primary"
                                />
                            }
                            onClick={togglePassword}
                        />
                        <p style={pStyle}>Show Password</p>
                    </div>
                    <PasswordChecklist
                        rules={["minLength", "specialChar", "number", "capital", "match", "lowercase"]}
                        minLength={8}
                        value={password}
                        valueAgain={confirmPassword}
                    />
                    <Button type='submit' color='primary' variant='contained' style={buttonStyle}  onClick={handleSubmit} fullWidth>
                        Sign Up
                    </Button>
                    {error && (<p className="error" style={errorMessage}> {error} </p>)}
                </Paper>
            </Grid>
        </div>
    )
}

export default Signup
