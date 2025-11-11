import { ScrollArea } from "@chakra-ui/react"

export default function Layout({children}) {
	return (
		<ScrollArea.Root size="xs" height="100vh" variant="hover">
			<ScrollArea.Viewport border="2px solid red">
				<ScrollArea.Content>
					{children}
				</ScrollArea.Content>
			</ScrollArea.Viewport>
			<ScrollArea.Scrollbar />
		</ScrollArea.Root>
	)
}