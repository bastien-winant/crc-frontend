import { NavContext } from "@/contexts/navContext/NavContext.jsx"
import { useRef } from "react"

export const NavContextProvider = ({children}) => {
	const homeRef = useRef(null)
	const aboutRef = useRef(null)
	const projectsRef = useRef(null)

	return (
		<NavContext.Provider value={{ homeRef, aboutRef, projectsRef }}>{children}</NavContext.Provider>
	)
}