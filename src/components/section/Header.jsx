import { Container, Heading } from "@chakra-ui/react"

export default function Header({children}) {
	return (
		<Container maxW="4xl">
			<Heading as="h2" size={{ base: "2xl", md: "3xl" }} textTransform="capitalize">{ children }</Heading>
		</Container>
	)
}