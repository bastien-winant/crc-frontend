import Section from "@/components/section/index.js"
import { Card, DataList, Fieldset, Field, Input, Textarea, Button } from "@chakra-ui/react"

export default function Contact() {
	const info = [
		{ label: "Email", value: "bastien.winant@gmail.com" },
		{ label: "Phone", value: "+352 691 223 827" },
		{ label: "Location", value: "Luxembourg, Luxembourg" },
	]

	return (
		<Section>
			<Section.Header>get in touch</Section.Header>
			<Section.Body>
				<Card.Root
					flexDirection={{ base: "column", md: "row" }}
					overflow="hidden"
					size="md"
				>
					<Card.Body gap="4" borderWidth="thin">
						<Card.Title>Email me</Card.Title>
						<Fieldset.Root size="md">
							<Fieldset.Content>
								<Field.Root>
									<Input name="email" type="email" placeholder="Email address" />
								</Field.Root>
								<Field.Root>
									<Textarea h="36" size="md" resize="none" placeholder="Search the docs…" />
								</Field.Root>
								<Button type="submit" alignSelf="flex-start" size="sm">
									Send email
								</Button>
							</Fieldset.Content>
						</Fieldset.Root>
					</Card.Body>
					<Card.Body gap="4" borderWidth="thin">
						<Card.Title>Contact info</Card.Title>
						<DataList.Root variant="bold">
							{info.map((item) => (
								<DataList.Item key={item.label}>
									<DataList.ItemLabel>{item.label}</DataList.ItemLabel>
									<DataList.ItemValue>{item.value}</DataList.ItemValue>
								</DataList.Item>
							))}
						</DataList.Root>
					</Card.Body>
				</Card.Root>
			</Section.Body>
		</Section>
	)
}