import { NavContext } from "@/contexts/navContext/NavContext.jsx"
import { useRef } from "react"

export const NavContextProvider = ({children}) => {
	const homeRef = useRef(null)
	const contactRef = useRef(null)
	const projectsRef = useRef(null)

	const scrollToRef = (ref) => {
		ref.current.scrollIntoView({
			behavior: "smooth",
			block: "start"
		})
	}

	return (
		<NavContext.Provider value={{ homeRef, contactRef, projectsRef, scrollToRef }}>{children}</NavContext.Provider>
	)
}