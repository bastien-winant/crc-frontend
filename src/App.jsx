import { ScrollArea } from "@chakra-ui/react"
import Landing from "@/components/Landing.jsx"
import About from "@/components/About.jsx"
import Projects from "@/components/projects/Projects.jsx"
import './App.css'

function App() {
  return (
		<ScrollArea.Root size="xs" height="100vh" variant="hover">
			<ScrollArea.Viewport>
				<ScrollArea.Content>
					<Landing />
					<About />
					<Projects />
				</ScrollArea.Content>
			</ScrollArea.Viewport>
			<ScrollArea.Scrollbar>
				<ScrollArea.Thumb />
			</ScrollArea.Scrollbar>
			<ScrollArea.Corner />
		</ScrollArea.Root>
  )
}

export default App
