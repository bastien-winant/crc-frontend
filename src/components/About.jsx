import Section from "@/components/section/index.js"
import { Stack, Text } from "@chakra-ui/react"

export default function About() {
	return (
		<Section>
			<Section.Header>about me</Section.Header>
			<Section.Body>
				<Stack gap="8">
					<Text>
						I'm a third-year Computer Science student at State University with a strong focus on data engineering and analytics.
						My journey into data began when I discovered the power of transforming messy datasets into meaningful insights that drive real-world decisions.
					</Text>
					<Text>
						Currently, I'm deepening my expertise in distributed systems, data warehousing, and ETL pipeline development.
						I work with technologies like Python, SQL, Apache Spark, and cloud platforms to build robust data infrastructure.
					</Text>
					<Text>
						When I'm not coding, you'll find me exploring new datasets on Kaggle,
						contributing to open-source data tools, or reading about the latest developments in data architecture and machine learning operations.
					</Text>
				</Stack>
			</Section.Body>
		</Section>
	)
}