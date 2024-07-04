import { useEffect, useState } from 'react';
import HorizontalLayout from './components/HorizontalLayout';
import VerticalLayout from './components/VerticalLayout';
//mui-material
import { SignedIn, SignedOut } from '@clerk/clerk-react';
import { Navigate } from 'react-router-dom';

function App() {
	const [isVertical, setIsVertical] = useState<boolean>(false);

	const handleResize = () => {
			setIsVertical(window.innerWidth <= 451);
	};

	useEffect(() => {
	handleResize();
	window.addEventListener('resize', handleResize);
	return () => {
			window.removeEventListener('resize', handleResize);
	};
	}, []);

	return (
		<>
			<SignedIn>
				<Navigate to='/homepage' />
				{isVertical ? <VerticalLayout /> : <HorizontalLayout />}
			</SignedIn>
			<SignedOut>
				<Navigate to='/login' />
			</SignedOut>
		</>
	)
}

export default App;
