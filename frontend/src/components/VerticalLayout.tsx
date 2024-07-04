import { Outlet } from 'react-router-dom';
import { Props } from '../commons/interfaces';
import SwitchThemeButton from './SwitchThemeButton';
import { SignOutButton } from '@clerk/clerk-react';
import MenuDrawerButton from './MenuDrawerButton';
//mui-material
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Divider from '@mui/material/Divider';
import Fab from '@mui/material/Fab';
import Button from '@mui/material/Button';
import Slide from '@mui/material/Slide';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import { IconButton, styled } from '@mui/material';
import useScrollTrigger from '@mui/material/useScrollTrigger';
//mui-icons
import SupportAgentRoundedIcon from '@mui/icons-material/SupportAgentRounded';
import SettingsRoundedIcon from '@mui/icons-material/SettingsRounded';
import LogoutRoundedIcon from '@mui/icons-material/LogoutRounded';

function VerticalLayout() {

	const StyledFab = styled(Fab)({
		position: 'absolute',
		zIndex: 1,
		top: -30,
		left: 0,
		right: 0,
		margin: '0 auto',
		});

	const HideOnScroll = (props: Props) => {
		const trigger = useScrollTrigger();
		
		return (
			<Slide appear={false} direction="down" in={!trigger}>
				{props.children}
			</Slide>
		);
	}

	return (
		<Box sx={{ flexGrow: 1 }}>
			<HideOnScroll> 
				<AppBar position="fixed" color="primary">
					<Toolbar>
						<Typography sx={{flex: 1}}>Welfare is on</Typography>
						<SwitchThemeButton />
						<SignOutButton>
							<IconButton color='inherit'>
								<LogoutRoundedIcon />
							</IconButton>
						</SignOutButton>
					</Toolbar>
				</AppBar>
			</HideOnScroll>
			
			<Toolbar />
			<Outlet />
			<Toolbar />

			<AppBar
				component={'footer'}
				position="fixed"
				color="primary"
				sx={{
					borderRadius: '20px 20px 0 0',
					top: 'auto', bottom: 0,
					width: '100%', height: '56px',
				}}
			>
				<Toolbar
					sx={{ padding: 0, }}
				>
					<MenuDrawerButton width="50%" height="56px" borderRadius="20px 0 0 0" />
					<StyledFab color="secondary" aria-label="search Welfare Coach">
						<SupportAgentRoundedIcon fontSize='large'/>
					</StyledFab>
					<Divider orientation='vertical' flexItem/>
					<Button
						aria-label="option"
						color='inherit'
						sx={{
							width: '50%', height: '56px',
							borderRadius: '0 20px 0 0',
						}}
					>
						<SettingsRoundedIcon />
					</Button>
				</Toolbar>
			</AppBar>
		</Box>
	);
}

export default VerticalLayout;