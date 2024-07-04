import React, { useState, FormEvent } from 'react';
import './Register.css';
import { POST } from '../commons/httpRequests';
import { registerEndpoint } from '../commons/endpoints';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import InputAdornment from '@mui/material/InputAdornment';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import VisibilityRounded from '@mui/icons-material/VisibilityRounded';
import VisibilityOffRounded from '@mui/icons-material/VisibilityOffRounded';
import KeyboardArrowLeftRounded from '@mui/icons-material/KeyboardArrowLeftRounded';
import { Divider, FormControlLabel, MenuItem, Switch } from '@mui/material';
import { Link } from 'react-router-dom';
import { genders, maritalStatuses, workplaces } from '../commons/constants';

const Register: React.FC = () =>
{
	const [emailError, setEmailError] = useState<boolean>(false);
	const [passwordError, setPasswordError] = useState<boolean>(false);
	const [confirmPasswordError, setConfirmPasswordError] = useState<boolean>(false);
	const [showPassword, setShowPassword] = useState<boolean>(false);
	const [showConfirmPassword, setConfirmShowPassword] = useState<boolean>(false);
	const [hasChildren, setHasChildren] = useState<boolean>(false);
	const [hasElders, setHasElders] = useState<boolean>(false);

	const [params, setParams] = useState<{[key: string]: any}>(
		{
			email: '',
			password: '',
			name : '',
			lastName : '',
			gender: '',
			birthdate : null,
			workplace : '',
			phoneNumber : '',
			maritalStatus : '',
			hasChildren : false,
			hasElders : false,
		}
	);
	const [currentSection, setCurrentSection] = useState<number>(0);

	const handleShowPassword = () =>
	{
		setShowPassword(!showPassword);
	}

	const handleShowConfirmPassword = () =>
	{
		setConfirmShowPassword(!showConfirmPassword);
	}

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

	const checkData = (e: FormEvent<HTMLFormElement>) =>
	{
		e.preventDefault();
		const form = e.target as HTMLFormElement;
		const emailInput = (form.elements.namedItem('emailInput') as HTMLInputElement).value;
		const passwordInput = (form.elements.namedItem('passwordInput') as HTMLInputElement).value;
		const confirmPasswordInput = (form.elements.namedItem('confirmPasswordInput') as HTMLInputElement).value;

		//Email
		if (checkEmail(emailInput))
		{
			setEmailError(false);
		}
		else
		{
			setEmailError(true);
			return;
		}

		//Password
		if (checkPassword(passwordInput))
			setPasswordError(false);
		else
		{
			setPasswordError(true);
			return;
		}

		//Confirm Password
		if (confirmPasswordInput === passwordInput)
		{
			setConfirmPasswordError(false);
		}
		else
		{
			setConfirmPasswordError(true);
			return;
		}

		setParams({
			...params,
			'email': emailInput,
			'password': passwordInput,
		});
		gotoNextSection();
	}

	const handleInput = (e: FormEvent<HTMLFormElement>) => {
		e.preventDefault();
		const form = e.target as HTMLFormElement;

		Array.from(form.elements).forEach((element) => {
			const input = element as HTMLInputElement;
			if (input.name) {
				params[input.name] = input.value;
			}
		});

		console.log(params);
		gotoNextSection();
	}

	const handleRegister = (e: FormEvent<HTMLFormElement>) => {
		e.preventDefault();
		POST(registerEndpoint, params);
	};

	const gotoNextSection = () => {
		if (currentSection < 2) {
			 setCurrentSection(currentSection + 1);
		}
	};

	// const gotoPreviousSection = () => {
	//	 if (currentSection > 0) {
	//			setCurrentSection(currentSection - 1);
	//	 }
	// };

	return (
		<Box className='registrationPage'>
			<Link to='/' className='returnButton'>
				<Button
					startIcon={<KeyboardArrowLeftRounded />}
				>
					Torna al login
				</Button>
			</Link>
			<Typography
				variant='h3'
				gutterBottom
				textAlign={'center'}
				margin={'20px'}
			>
				Crea il tuo account Welfare
			</Typography>

			<Box className='scrollContainer'>
				<Box className='scrollContent'
					style={{ transform: `translateX(-${currentSection * (100 / 3)}%)` }}
				>
					<Box id='loginDataInputBox'
						className='dataInputBox'
					>
						<Typography
							variant='h4'
							margin={'20px'}
							textAlign={'right'}
						>
							Inserisci<br/>Email e Password
						</Typography>

						<Divider orientation='vertical' />

						<Box
							component='form'
							onSubmit={checkData}
							className='maxFourInputsGroup'
						>
							<TextField id='emailInput'
								name='email'
								type='email'
								className='standardInput'
								label='E-mail'
								variant='outlined'
								error = {emailError}
								helperText={emailError ? 'Email non valida.' : null}
								required
								fullWidth
							/>

							<Box
								width={'100%'}
							>
								<TextField id='passwordInput'
									name='password'
									type={showPassword ? 'text' : 'password'}
									className='standardInput'
									label='Password'
									variant='outlined'
									error = {passwordError}
									helperText={passwordError ? 'Password non valida.' : null}
									required
									fullWidth
									InputProps={{
										endAdornment:
											<InputAdornment position='end'>
												<IconButton
													aria-label='toggle password visibility'
													onClick={handleShowPassword}
													edge='end'
												>
													{showPassword ? <VisibilityOffRounded /> : <VisibilityRounded />}
												</IconButton>
											</InputAdornment>,
									}}
								/>

								{passwordError ?
									<Typography
										color={'error'}
										fontSize={'small'}
									>
										- Minimo 8 caratteri;<br/>
										- Almeno una minuscola;<br/>
										- Almeno una maiuscola;<br/>
										- Almeno un numero;<br/>
										- Almeno un carattere speciale:<br />
										! # $ % & ' * + - / = ? ^ _ &#123; | &#125; ~
									</Typography>
									: null
								}
							</Box>

							<TextField id='confirmPasswordInput'
								name='confirmPassword'
								type={showConfirmPassword ? 'text' : 'password'}
								className='standardInput'
								label='Conferma Password'
								variant='outlined'
								error={confirmPasswordError}
								helperText={confirmPasswordError ? 'Le password non coincidono.' : null}
								required
								fullWidth
								InputProps={{
									endAdornment:
										<InputAdornment position='end'>
											<IconButton
												aria-label='toggle password visibility'
												onClick={handleShowConfirmPassword}
												edge='end'
											>
												{showConfirmPassword ? <VisibilityOffRounded /> : <VisibilityRounded />}
											</IconButton>
										</InputAdornment>,
								}}
							/>

							<Button
								type='submit'
								className='submitButton'
								variant='outlined'
								size='large'
								sx={{ height: 56}}
								fullWidth
							>
								Continua
							</Button>
						</Box>
					</Box>

					<Box id="nameInputBox"
						className="dataInputBox"
					>
						<Typography
							variant='h4'
							margin={'20px'}
							textAlign={'right'}
						>
							Inserisci<br/>Nome e Cognome
						</Typography>

						<Divider orientation='vertical' />

						<Box
							component='form'
							onSubmit={handleInput}
							className='maxFourInputsGroup'
						>
							<TextField id='nameInput'
								name='name'
								type='text'
								className='standardInput'
								label='Nome'
								variant='outlined'
								required
								fullWidth
							/>

							<TextField id='lastnameInput'
								name='lastName'
								type='text'
								className='standardInput'
								label='Cognome'
								variant='outlined'
								required
								fullWidth
							/>

							<Button
								type='submit'
								className='submitButton'
								variant='outlined'
								size='large'
								sx={{ height: 56}}
								fullWidth
							>
								Continua
							</Button>
						</Box>
					</Box>

					<Box id="additionalInputBox"
						className="dataInputBox"
						component='form'
						onSubmit={handleInput}
					>
						<Typography
							variant='h4'
							margin={'20px'}
							textAlign={'right'}
						>
							Inserisci<br/>dati aggiuntivi
						</Typography>

						<Divider orientation='vertical' />

						<Box className="maxFourInputsGroup">
							<TextField id='genderInput'
								name='gender'
								type='text'
								className='standardInput'
								label='Sesso'
								variant='outlined'
								fullWidth
								select
							>
								{genders.map((gender) => (
									<MenuItem key={gender} value={gender}>
										{gender}
									</MenuItem>
								))}
							</TextField>

							<TextField id='birthdateInput'
								name='birthdate'
								type='text'
								className='standardInput'
								label='Data di nascita'
								variant='outlined'
								fullWidth
							/>

							<TextField id='phoneNumberInput'
								name='phoneNumber'
								type='phone'
								className='standardInput'
								label='Telefono'
								variant='outlined'
								fullWidth
							/>

							<TextField id='maritalStatusInput'
								name='maritalStatus'
								type='text'
								className='standardInput'
								label='Stato sociale'
								variant='outlined'
								fullWidth
								select
							>
								{maritalStatuses.map((maritalStatus) => (
									<MenuItem key={maritalStatus} value={maritalStatus}>
										{maritalStatus}
									</MenuItem>
								))}
							</TextField>
						</Box>

						<Box className="maxFourInputsGroup">

							<TextField id='workplaceInput'
								name='workplace'
								type='text'
								className='standardInput'
								label='Zona di lavoro'
								variant='outlined'
								fullWidth
								select
							>
								{workplaces.map((workplace) => (
									<MenuItem key={workplace} value={workplace}>
										{workplace}
									</MenuItem>
								))}
							</TextField>

							<FormControlLabel
								control={
									<Switch
										checked={hasChildren}
										onChange={() => {
											setHasChildren(!hasChildren);
											params.hasChildren = !params.hasChildren;
										}}
									/>
								}
								sx={{ height: 56}}
								label='Hai figli?'
							/>

							<FormControlLabel
								control={
									<Switch
										checked={hasElders}
										onChange={() => {
											setHasElders(!hasElders);
											params.hasElders = !params.hasElders;
										}}
									/>
								}
								sx={{ height: 56}}
								label='Hai parenti?'
							/>

							<Button
								type='submit'
								className='submitButton'
								variant='outlined'
								size='large'
								sx={{ height: 56}}
								fullWidth
							>
								Continua
							</Button>
						</Box>
					</Box>
				</Box>
			</Box>
		</Box>
	)
}

export default Register;
