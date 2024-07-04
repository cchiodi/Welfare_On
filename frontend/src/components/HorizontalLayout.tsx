import { Outlet } from 'react-router-dom';
import SwitchThemeButton from './SwitchThemeButton';
import { SignOutButton } from '@clerk/clerk-react';
//mui-material
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Fab from '@mui/material/Fab';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import { IconButton, styled } from '@mui/material';
//mui-icons
import SupportAgentRoundedIcon from '@mui/icons-material/SupportAgentRounded';
import SettingsRoundedIcon from '@mui/icons-material/SettingsRounded';
import LogoutRoundedIcon from '@mui/icons-material/LogoutRounded';
import MenuDrawerButton from './MenuDrawerButton';

function HorizontalLayout() {

	const StyledFab = styled(Fab)({
		position: 'fixed',
		zIndex: 1,
		right: 30,
		bottom: 30,
		margin: '0 auto',
		});

	return (
		<Box sx={{ flexGrow: 1 }}>
			<AppBar position="fixed" color="primary">
				<Toolbar>
					<MenuDrawerButton />
					<Typography sx={{flex: 1,}}>Welfare is on</Typography>
					<SwitchThemeButton />
					<SignOutButton>
						<IconButton color='inherit'>
							<LogoutRoundedIcon />
						</IconButton>
					</SignOutButton>
					<IconButton
						aria-label="option"
						color='inherit'
					>
						<SettingsRoundedIcon />
					</IconButton>
				</Toolbar>
			</AppBar>
			
			<Toolbar />
			<Outlet />
			<Toolbar />

			<StyledFab color="secondary" aria-label="search Welfare Coach">
				<SupportAgentRoundedIcon fontSize='large'/>
			</StyledFab>
		</Box>
	);
}

export default HorizontalLayout;