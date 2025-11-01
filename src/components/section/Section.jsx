import { Stack } from "@chakra-ui/react"

export default function Section({children}) {
	return (
		<Stack py="24" gap="8" borderWidth="thin">{children}</Stack>
	)
}