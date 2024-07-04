import axios from "axios";
import { useEffect, useState } from "react";
import { jsonServerHost, servicesEndpoint } from "../commons/endpoints";
import { Box, Button, Card, CardActionArea, CardActions, CardContent, CardHeader, CardMedia, Link, Typography } from "@mui/material";
import Grid from '@mui/material/Unstable_Grid2/Grid2';
import FileDownloadRoundedIcon from '@mui/icons-material/FileDownloadRounded';
import { ServiceObject } from "../commons/interfaces";
import { useLoaderData } from "react-router-dom";
import { TinyColor } from '@ctrl/tinycolor';

function Homepage() {
	const [services, setServices] = useState<Array<ServiceObject>>([]);
	const categoryId = useLoaderData() as string;

	useEffect(() => {
    const fetchServices = async () => {
      try {
        const url = `${jsonServerHost}${servicesEndpoint}${categoryId}`;
        console.log(url);
        const res = await axios.get(url);
        console.log('Get:', res);
        if (res.status === 200) {
          setServices(res.data);
        }
      } catch (error) {
        console.error('Error fetching services:', error);
      }
    };

    fetchServices();
  }, [categoryId]);

	// function isLight(color: string) {
	// 	const hex = color.replace('#', '');
	// 	const c_r = parseInt(hex.substring(0, 0 + 2), 16);
	// 	const c_g = parseInt(hex.substring(2, 2 + 2), 16);
	// 	const c_b = parseInt(hex.substring(4, 4 + 2), 16);
	// 	const brightness = ((c_r * 299) + (c_g * 587) + (c_b * 114)) / 1000;
	// 	return brightness > 155;
	// }

	return (	
		<Box sx={{ flexGrow: 1 }} padding={{ xs: 2, md: 3 }}>
			<Grid container spacing={{ xs: 2, md: 3 }} columns={{ xs: 4, sm: 8, md: 12 }}>
				{services.map(service => {
					const catColor = new TinyColor(service.color);
					const textColor = catColor.isLight() ? 'black': 'white';
					return(
						<Grid xs={4} key={service.id}>
							<Card sx={{borderRadius: '20px'}}>
								<CardHeader
									title={service.category}
									sx={{
										backgroundImage: `linear-gradient(to right, ${catColor.darken(10).toString()}, ${catColor}, ${catColor.brighten(10).toString()})`,
										padding: 0,
										paddingLeft: '20px',
										height: '25px',
									}}
									titleTypographyProps={{
										color: textColor,
										fontSize: 20,
										fontWeight: 500,
									}}
								/>
								<CardActionArea
									sx={{
										borderRadius: 0,
									}}
								>
									<CardMedia
										component="img"
										image={service.imgUrl !== "" ? service.imgUrl : '/servicePlaceholder.jpg'}
										sx={{
											height: '220px',
										}}
									/>
									<CardContent>
										<Typography gutterBottom variant="h5" component="div" sx={{maxHeight: '32px'}}>
											{service.name}
										</Typography>
										<Box
											sx={{
												flex: 1,
												height: '70px',
												overflow: 'auto',
											}}
										>
											<Typography variant="body2" color="text.secondary">
												{service.description}
											</Typography>
										</Box>
									</CardContent>
								</CardActionArea>
								<CardActions
									sx={{
										height:'48px',
										justifyContent: 'right',
									}}
								>
									<Link href={service.pdfUrl} color="inherit" underline='none'>
										<Button size="small" color="primary">
											<FileDownloadRoundedIcon/>
										</Button>
									</Link>
								</CardActions>
							</Card>
						</Grid>
					)
				})}
			</Grid>
		</Box>
	);
}

export default Homepage;