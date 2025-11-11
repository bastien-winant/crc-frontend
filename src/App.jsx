import Layout from "@/components/Layout.jsx"
import About from "@/components/About.jsx"
import Projects from "@/components/projects/Projects.jsx"
import Contact from "@/components/Contact.jsx"
import './App.css'

function App() {
  return (
    <Layout>
			<About />
			<Projects />
			<Contact />
    </Layout>
  )
}

export default App
