import {Stack} from "@chakra-ui/react"

export default function Section({ref, children}) {
	return (
		<Stack ref={ref} py="20" gap="8" borderWidth="medium">{children}</Stack>
	)
}