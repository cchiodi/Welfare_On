import React, { useEffect, useState } from "react";
import { CategoryObject } from "../commons/interfaces";
import axios from "axios";
import { categoriesEndpoint, jsonServerHost } from "../commons/endpoints";
import { Collapse, Divider, IconButton, List, ListItem, ListItemButton, ListItemText, Toolbar, Typography } from "@mui/material";
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft';
import ExpandLess from '@mui/icons-material/ExpandLess';
import ExpandMore from '@mui/icons-material/ExpandMore';
import { TinyColor } from "@ctrl/tinycolor";
import { useNavigate } from "react-router-dom";

interface Props {
	onClose: () => void;
}

function MenuDrawer({onClose}: Props){
	const [categories, setCategories] = useState<Array<CategoryObject>>([]);
	const [openCategories, setOpenCategories] = useState<{ [key: string]: boolean }>({});
	const navigate = useNavigate();

	useEffect(() => {
		const fetchCategories = async () => {
			try {
				const url = `${jsonServerHost}${categoriesEndpoint}`;
				console.log("fetchCategories: ", url);
				const res = await axios.get(url);
				console.log('Get:', res);
				if (res.status === 200) {
					setCategories(res.data);
				}
			} catch (error) {
				console.error('Error fetching services:', error);
			}
		};

		fetchCategories();
	}, []);

	const handleOpen = (categoryId: number) => {
		setOpenCategories(prevState => ({
			...prevState,
			[categoryId]: !prevState[categoryId]
		}));
	};

	const filter = (endpoint: string) => {
		console.log("filter ", endpoint);
		navigate("/homepage/" + endpoint);
	}

	return (
		<div>
			<Toolbar>
				<Typography sx={{flex:1, fontWeight: 600}}>CATEGORIE</Typography>
				<IconButton onClick={onClose}>
					<ChevronLeftIcon />
				</IconButton>
			</Toolbar>
			<Divider />
			<List disablePadding>
				{categories.map((category) => {
					const isOpen = openCategories[category.id] || false;
					const catColor = new TinyColor(category.color).lighten();
					const textColor = catColor.isLight() ? "black": "white";

					return (
						<React.Fragment key={category.id}>
							<ListItem component='div' key={category.id} disablePadding sx={{width: '240px'}}>
								<ListItemButton
									component="button"
									onClick={() => filter(category.id as unknown as string)}
									sx={{ width: 210, overflow: 'auto' }}
								>
									<ListItemText primary={category.name} primaryTypographyProps={{fontWeight: 600}}/>
								</ListItemButton>

								{/* <Divider variant="middle" orientation="vertical" flexItem /> */}
								
								<ListItemButton
									onClick={() => handleOpen(category.id)}
									sx={{ height: 48, width: 30, paddingLeft: "3px", paddingRight: "3px",
										background: catColor.toHexString(),
										"&:hover": {background: catColor.lighten().toHexString()}
									}}	
								>
									{isOpen ? <ExpandLess sx={{color: textColor}} />
										: <ExpandMore sx={{color: textColor}} />}
								</ListItemButton>
							</ListItem>

							<Collapse key={category.id + '-sublist'} in={isOpen} timeout="auto" unmountOnExit>
							<List>
								{category.subcategories.map((subcategory) => {
									const endpoint = category.id as unknown as string + "/" + subcategory.id as unknown as string
									return (
										<ListItemButton
											key={subcategory.id}
											component="button"
											onClick={() => filter(endpoint)}
											sx={{pl:4, height: 24}}
										>
											<ListItemText primary={subcategory.name} />
										</ListItemButton>
									)
								})}
							</List>
							</Collapse>
						</React.Fragment>
					);
				})}
			</List>
		</div>
	);
};

export default MenuDrawer;
