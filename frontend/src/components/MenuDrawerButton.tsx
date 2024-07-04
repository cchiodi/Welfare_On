import { Button, Drawer } from "@mui/material";
import MenuDrawer from "./MenuDrawer";
import React from "react";
import { drawerWidth } from '../commons/constants';
import MenuRoundedIcon from '@mui/icons-material/MenuRounded';

interface MenuDrawerButtonProps {
  width?: string;
  height?: string;
  borderRadius?: string;
}

function MenuDrawerButton({ width, height, borderRadius }: MenuDrawerButtonProps) {
	const [openDrawer, setOpenDrawer] = React.useState(false);
	const [isClosing, setIsClosing] = React.useState(false);

  const handleDrawerToggle = () => {
    if (!isClosing) {
      setOpenDrawer(!openDrawer);
			console.log(openDrawer)
    }
  };

  const handleDrawerClose = () => {
    setIsClosing(true);
    setOpenDrawer(false);
  };

  const handleDrawerTransitionEnd = () => {
    setIsClosing(false);
  };
	
	return (
		<>
			<Drawer
				variant="temporary"
				open={openDrawer}
				onTransitionEnd={handleDrawerTransitionEnd}
				onClose={handleDrawerClose}
				ModalProps={{
					keepMounted: true,
				}}
				sx={{
					display: { xs: 'block' },
					'& .MuiDrawer-paper': { boxSizing: 'border-box', width: drawerWidth },
				}}
			>
				<MenuDrawer onClose={handleDrawerClose}/>
			</Drawer>
			<Button
				aria-label="open drawer"
				color='inherit'
				onClick={handleDrawerToggle}
				sx={{
					width: width || 'auto',
					height: height || 'auto',
					borderRadius: borderRadius || 'auto',
				}}
			>
				<MenuRoundedIcon />
			</Button>
		</>
	);
}

export default MenuDrawerButton;