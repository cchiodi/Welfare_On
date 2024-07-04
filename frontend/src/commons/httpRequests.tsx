import axios from "axios";
import { mainHost } from "./endpoints";
import { useAuth } from "@clerk/clerk-react";

const retrieveToken = async() => {
	const { getToken } = useAuth();
	const token = await getToken();

	console.log('retrieveToken: ', token)

	return token;
}

export const POST =	async(endpoint: string, params: object) =>
{
	const token = await retrieveToken();

	axios.post(mainHost + endpoint, params,
		{
			headers: {
				'content-type': 'application/json',
				'authorization': `bearer ${token}`,
			}
		}
	).then((r) => {
		console.log(r);
	}).catch((error) => {
		console.log(error);
	})
}

export const GET =	async(endpoint: string, params: object) =>
{
	const token = await retrieveToken();

	axios.get(mainHost + endpoint,
		{
			headers: {
				'content-type': 'application/json',
				'authorization': `bearer ${token}`,
			},
			params: params,
		}
	).then((r) => {
		console.log(r);
		return r;
	}).catch((error) => {
		console.log(error);
	})
}
