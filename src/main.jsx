import { StrictMode } from 'react'
import { Provider as ChakraProvider } from "@/components/ui/provider.jsx"
import { NavContextProvider } from "@/contexts/navContext/NavContextProvider.jsx"
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
		<ChakraProvider>
			<NavContextProvider>
				<App />
			</NavContextProvider>
		</ChakraProvider>
  </StrictMode>,
)
