import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'
import { RouterProvider, createBrowserRouter } from 'react-router-dom'
import App from './App.tsx'
import ErrorPage from './pages/ErrorPage.tsx'
import Login from './pages/Login.tsx'
import Homepage from './pages/Homepage.tsx'
import { ClerkProvider } from '@clerk/clerk-react'
import { ColorModeContext } from './commons/contexts.tsx'
import { ThemeProvider } from '@mui/material/styles'
import { CssBaseline, PaletteMode, createTheme } from '@mui/material'

const PUBLISHABLE_KEY = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

if (!PUBLISHABLE_KEY) {
  throw new Error("Missing Publishable Key")
}

const router = createBrowserRouter([
	{
		path: '/',
		element: <App />,
		errorElement: <ErrorPage />,
		children: [
			{
				path: 'homepage/',
				element: <Homepage />,
				loader: async() => {return ("")},
			},
			{
				path: 'homepage/:categoryId',
				element: <Homepage />,
				loader: async ({ params }) => {
					return `?categoryId=${params.categoryId}`;
				}
			},
			{
				path: 'homepage/:categoryId/:subcategoryId',
				element: <Homepage />,
				loader: async ({ params }) => {
					return `?subcategoryId=${params.subcategoryId}`;
				}
			},
		]
	},
	{
		path: '/login',
		element: <Login />,
	},
])

const getPalette = (mode: PaletteMode) => ({
	palette: {
		mode,
		...(mode === 'light'
			? {
				primary: {
				main: '#37424A',
				},
				secondary: {
				main: '#E27249',
				},
				background: {
					default: '#cccccc',
				},
			} : {
				primary: {
					main: '#b1bac1',
				},
				secondary: {
					main: '#E27249',
				},
				background: {
					default: '#000000',
				},
			}),
	},
	typography: {
		fontFamily: 'QuickSand'
	},
});

const RootComponent = () => {
  const [mode, setMode] = React.useState<PaletteMode>('light');
  const colorMode = React.useMemo(() => ({
    toggleColorMode: () => {
      setMode((prevMode: PaletteMode) =>
        prevMode === 'light' ? 'dark' : 'light',
      );
    },
  }), []);

  const theme = React.useMemo(() => createTheme(getPalette(mode)), [mode]);

  return (
    <ClerkProvider publishableKey={PUBLISHABLE_KEY}>
      <ColorModeContext.Provider value={colorMode}>
        <ThemeProvider theme={theme}>
          <CssBaseline />
          <RouterProvider router={router} />
        </ThemeProvider>
      </ColorModeContext.Provider>
    </ClerkProvider>
  );
};

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <RootComponent />
  </React.StrictMode>
);
