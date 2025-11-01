import Section from "@/components/section/index.js"
import { Button, ButtonGroup, Heading, Stack, Text } from "@chakra-ui/react"


export default function Landing() {
	return (
		<Section>
			<Section.Body>
				<Stack gap="4">
					<Heading
						as="h1"
						size={{ base: "4xl", md: "6xl" }}
						letterSpacing="tight"
						fontWeight="bold"
					>
						Bastien Winant
					</Heading>
					<Text fontSize="xl" color="fg.muted">
						Computer Science Student & Aspiring Data Engineer
					</Text>
					<Text fontsize="md">
						Building scalable data pipelines and analytics solutions.
						Passionate about transforming raw data into actionable insights using modern data engineering tools and practices.
					</Text>
					<ButtonGroup mt="6">
						<Button variant="solid">Get in touch</Button>
						<Button variant="outline">View projects</Button>
					</ButtonGroup>
				</Stack>
			</Section.Body>
		</Section>
	)
}