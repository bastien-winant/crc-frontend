import { Card, Wrap, Badge, Button, For, LinkBox, LinkOverlay } from "@chakra-ui/react"
import { LuGithub } from "react-icons/lu"

export default function ProjectCard({title, description, techStack, githubUrl}) {
	return (
		<Card.Root size="md">
			<Card.Header>
				<Card.Title>{title}</Card.Title>
			</Card.Header>
			<Card.Body>
				<Card.Description>{description}</Card.Description>
				<Wrap mt="4">
					<For each={techStack}>
						{(item, index) => <Badge key={index}>{item}</Badge>}
					</For>
				</Wrap>
			</Card.Body>
			<Card.Footer>
				<LinkBox>
					<Button variant="outline" size="sm">
						<LuGithub />
						Code
					</Button>
					<LinkOverlay href={githubUrl} target="_blank" />
				</LinkBox>
			</Card.Footer>
		</Card.Root>
	)
}