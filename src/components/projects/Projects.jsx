import Section from "@/components/section/index.js"
import { Stack } from "@chakra-ui/react"
import ProjectCard from "@/components/projects/ProjectCard.jsx";


export default function Projects() {
	return (
		<Section>
			<Section.Header>featured projects</Section.Header>
			<Section.Body>
				<Stack gap="4">
					<ProjectCard />
					<ProjectCard />
					<ProjectCard />
				</Stack>
			</Section.Body>
		</Section>
	)
}