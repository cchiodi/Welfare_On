import Typography from "@mui/material/Typography";
import React, { useEffect, useState } from "react";
import { GET } from "../commons/httpRequests";
import { Box, Container } from "@mui/material";

const GridOfInterests: React.FC = () =>
{
	const [interests, setInterests] = useState([
		{
			'id': 0,
			'name': 'zero',
		},
		{
			'id': 1,
			'name': 'uno',
		},
		{
			'id': 2,
			'name': 'due',
		},
		{
			'id': 3,
			'name': 'tre',
		},
		{
			'id': 4,
			'name': 'quattro',
		},
		{
			'id': 5,
			'name': 'cinque',
		},
	])

	return (
		<Container>
			<Typography>Seleziona i tuoi interessi</Typography>
			{interests.map(interest => {
				return (
					<Typography>{interest.name}</Typography>
				)
			})}
		</Container>
	)
}

export default GridOfInterests;
