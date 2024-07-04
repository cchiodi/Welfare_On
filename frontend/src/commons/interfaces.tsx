import React from "react";

export interface Props {
	children: React.ReactElement,
}

export interface ServiceObject {
	id: number,
	name: string,
	category: string,
	subcategory: string,
	dataStart : Date,
	dataEnd : Date,
	description : string,
	imgUrl : string,
	pdfUrl : string,
	color : string
}

export interface SubcategoryObject {
	id: number,
	name: string
}

export interface CategoryObject {
	id: number,
	name: string,
	color: string,
	subcategories: Array<SubcategoryObject>
}