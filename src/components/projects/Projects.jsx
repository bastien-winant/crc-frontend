import Section from "@/components/section/index.js"
import { Stack } from "@chakra-ui/react"
import ProjectCard from "@/components/projects/ProjectCard.jsx";


export default function Projects() {
	return (
		<Section>
			<Section.Header>featured projects</Section.Header>
			<Section.Body>
				<Stack gap="4">
					<ProjectCard
						title="Subscriber Cancellations Data Pipeline"
						description="This sofa is perfect for modern tropical spaces, baroque inspired spaces."
						techStack={['Python', 'Apache Spark', 'PostgreSQL']}
						githubUrl="https://espn.com"
					/>
					<ProjectCard
						title="Bike Rental Data Management"
						description="This sofa is perfect for modern tropical spaces, baroque inspired spaces. thavnaskljdvnadjksvnaksjdnvkasj"
						techStack={['Python', 'SQLMesh', 'PostgreSQL']}
						githubUrl="https://espn.com"
					/>
					<ProjectCard
						title="Bike Rental Data Management"
						description="This sofa is perfect for modern tropical spaces, baroque inspired spaces."
						techStack={['Python', 'SQLMesh', 'PostgreSQL']}
						githubUrl="https://espn.com"
					/>
				</Stack>
			</Section.Body>
		</Section>
	)
}