import { Container, Heading } from "@chakra-ui/react"

export default function Header({children}) {
	return (
		<Container maxW="4xl">
			<Heading as="h2" textTransform="capitalize">{children}</Heading>
		</Container>
	)
}