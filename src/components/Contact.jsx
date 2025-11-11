import Section from "@/components/section/index.js"
import { Card, DataList, Stack, Fieldset, Field, Input, Textarea, Button } from "@chakra-ui/react"

export default function Contact() {
	const info = [
		{ label: "Email", value: "bastien.winant@gmail.com" },
		{ label: "Phone", value: "+352 691 223 827" },
		{ label: "Location", value: "Luxembourg, Luxembourg" },
	]

	return (
		<Section>
			<Section.Header>contact</Section.Header>
			<Section.Body>
				<Card.Root size="md">
					<Card.Body gap="12">
						<Stack>
							<Card.Title>Contact info</Card.Title>
							<DataList.Root variant="bold">
								{info.map((item) => (
									<DataList.Item key={item.label}>
										<DataList.ItemLabel>{item.label}</DataList.ItemLabel>
										<DataList.ItemValue>{item.value}</DataList.ItemValue>
									</DataList.Item>
								))}
							</DataList.Root>
						</Stack>
						<Stack gap="2">
							<Card.Title>Email</Card.Title>
							<Fieldset.Root size="lg">
								<Fieldset.HelperText>
									Please provide your contact details below.
								</Fieldset.HelperText>
								<Fieldset.Content>
									<Field.Root>
										<Field.Label>Email address</Field.Label>
										<Input name="email" type="email" />
									</Field.Root>
									<Field.Root>
										<Field.Label>Email address</Field.Label>
										<Textarea size="xl" resize="none" placeholder="Search the docs…" />
									</Field.Root>
									<Button type="submit" alignSelf="flex-start">
										Submit
									</Button>
								</Fieldset.Content>
							</Fieldset.Root>
						</Stack>
					</Card.Body>
				</Card.Root>
			</Section.Body>
		</Section>
	)
}