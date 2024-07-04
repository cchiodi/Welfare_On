import React, { useState, FormEvent } from "react";
import './Login.css';
import { loginEndpoint, mainHost } from "../commons/endpoints";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Typography from "@mui/material/Typography";
import axios from "axios";
import { Link } from "react-router-dom";

const Login: React.FC = () =>
{
	const [emailError, setEmailError] = useState<boolean>(false)
	const [passwordError, setPasswordError] = useState<boolean>(false)
	const [params, setParams] = useState<object>(
		{
			"email": "",
			"password": "",
		}
	)

	const checkPassword = (password: string) =>
		{
			const passwordRegex = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!#$%&'*+-/=?^_`{|}~])[A-Za-z\d!#$%&'*+-/=?^_`{|}~]{8,}$/
			return passwordRegex.test(password);
		}

	const checkEmail = (email: string) =>
	{
		const emailRegex = /^[a-zA-Z\d!#$%&'*+-/=?^_`{|}~]+@[a-zA-Z\d.-]+\.[a-zA-Z]{2,}$/;
		return emailRegex.test(email);
	}

	const handleLogin = (e: FormEvent<HTMLFormElement>) =>
	{
		e.preventDefault();
		const form = e.target as HTMLFormElement;
		const email = (form.elements.namedItem('emailInput') as HTMLInputElement).value;
		const password = (form.elements.namedItem('passwordInput') as HTMLInputElement).value;

		//Email
		console.log("Email: ", email, " -valid: ",checkEmail(email));
		if (checkEmail(email))
			setEmailError(false);
		else
		{
			setEmailError(true);
			return;
		}

		//Password
		console.log("Password: ", password, " -valid: ", checkPassword(password));
		if (checkPassword(password))
			setPasswordError(false);
		else
		{
			setPasswordError(true);
			return;
		}

		//Getting token
		console.log("GET - email: ", email, " password: ", password);
		setParams(
			{
				"email": {email},
				"password": {password},
			}
		)
		axios.get(mainHost + loginEndpoint,
			{
				headers: {
					'content-type': 'application/json',
				},
				params: params,
			}
		).then((r) => {
			console.log(r);
			localStorage.setItem('token', r.data.token);
		}).catch((error) => {
			console.log(error);
		})
	}

	return (
		<Box className="loginPage">
			<Typography
				variant="h3"
				gutterBottom
				textAlign={'center'}
				margin={'20px'}
			>
				Login
			</Typography>
			<Box component="form" onSubmit={handleLogin} className="loginForm">
				<TextField
					type="email"
					className="standardInput"
					id="emailInput"
					label="Email"
					variant="outlined"
					error = {emailError}
					helperText={emailError ? "Email non valida." : null}
				/>
				<TextField
					type="password"
					className="standardInput"
					id="passwordInput"
					label="Password"
					variant="outlined"
					error = {passwordError}
					helperText={passwordError ?	`Password non valida.` : null}
				/>
				<Button
					type='submit'
					className='submitButton'
					variant='outlined'
					size='large'
					fullWidth
				>
					Login
				</Button>
			</Box>
			<Link to='/register'>
				<Button
					className="gotoButton"
				>
					Registrati
				</Button>
			</Link>
		</Box>
	)
}

export default Login;
