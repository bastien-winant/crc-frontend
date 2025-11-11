import { Container } from "@chakra-ui/react"

export default function Body({children}) {
	return (
		<Container maxW="4xl">{children}</Container>
	)
}