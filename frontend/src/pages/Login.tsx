import React from "react";
import './Login.css';
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import { Navigate } from "react-router-dom";
import { SignInButton, SignUpButton, SignedIn } from "@clerk/clerk-react";

const Login: React.FC = () =>
{
	return (
		<Box className="loginPage">
			<SignedIn>
				<Navigate to='/homepage' />
			</SignedIn>
			<Typography
				variant="h1"
				gutterBottom
				textAlign={'center'}
				margin={'20px'}
			>
				Welfy
			</Typography>
			<Box className="loginButtons">
				<SignInButton mode="modal">
					<Button
						variant='outlined'
						size='large'
						fullWidth
					>
						Accedi
					</Button>
				</SignInButton>
				<Typography
					variant="caption"
					width='100%'
					textAlign='center'
				>
					oppure
				</Typography>
				<SignUpButton mode="modal">
					<Button
						variant='outlined'
						size='large'
						fullWidth
					>
						Registrati
					</Button>
				</SignUpButton>
			</Box>
		</Box>
	)
}

export default Login;
