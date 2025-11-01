import { Card, Wrap, Badge, Button, For, LinkBox, LinkOverlay } from "@chakra-ui/react"
import { LuGithub } from "react-icons/lu"

export default function ProjectCard() {
	const title = "Live room Sofa"
	const description = "This sofa is perfect for modern tropical spaces, baroque inspired spaces."
	const techStack = ['Python', 'SQLMesh', 'PostgreSQL']
	const githubUrl = "https://espn.com"

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
				{/*<Button variant="solid" size="sm">Buy now</Button>*/}
				{/*<Button variant="ghost" size="sm">Add to cart</Button>*/}
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