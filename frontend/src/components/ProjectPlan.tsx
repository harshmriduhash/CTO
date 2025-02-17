import React from 'react'
import { motion } from "framer-motion"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { ScrollArea } from "@/components/ui/scroll-area"
import { AIProjectDetails } from '@/types'

interface ProjectPlanProps {
  plan: ProjectPlan;
}

const ProjectPlan: React.FC<ProjectPlanProps> = ({ plan }) => (
  <Card className="w-full max-w-3xl mx-auto mt-10">
    <CardHeader>
      <CardTitle className="text-2xl font-bold text-center">Your AI CTO Project Plan</CardTitle>
    </CardHeader>
    <CardContent>
      <ScrollArea className="h-[60vh]">
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="space-y-4"
        >
          <section>
            <h3 className="font-semibold text-lg">Project Title</h3>
            <p>{plan.title}</p>
          </section>
          <section>
            <h3 className="font-semibold text-lg">Project Description</h3>
            <p>{plan.description}</p>
          </section>
          <section>
            <h3 className="font-semibold text-lg">Recommended Tech Stack</h3>
            <ul className="list-disc pl-5 mt-2">
              {plan.tech_stack.map((tech, index) => (
                <li key={index}>{tech}</li>
              ))}
            </ul>
          </section>
          <section>
            <h3 className="font-semibold text-lg">Key Features</h3>
            <ul className="list-disc pl-5 mt-2">
              {plan.features.map((feature, index) => (
                <li key={index}>{feature}</li>
              ))}
            </ul>
          </section>
          <section>
            <h3 className="font-semibold text-lg">Product Requirements Document (PRD)</h3>
            <p className="mt-2 whitespace-pre-wrap">{plan.product_requirements}</p>
          </section>
          <section>
            <h3 className="font-semibold text-lg">Job Description</h3>
            <p className="mt-2 whitespace-pre-wrap">{plan.job_description}</p>
          </section>
          <section>
            <h3 className="font-semibold text-lg">Required Skills</h3>
            <ul className="list-disc pl-5 mt-2">
              {plan.required_skills.map((skill, index) => (
                <li key={index}>{skill}</li>
              ))}
            </ul>
          </section>
          <section>
            <h3 className="font-semibold text-lg">Project Timeline</h3>
            <ul className="list-disc pl-5 mt-2">
              {Object.entries(plan.timeline).map(([phase, duration]) => (
                <li key={phase}>{phase}: {duration}</li>
              ))}
            </ul>
          </section>
          <section>
            <h3 className="font-semibold text-lg">Budget Estimate</h3>
            <p className="mt-2">${plan.budget_estimate.toLocaleString()}</p>
          </section>
        </motion.div>
      </ScrollArea>
    </CardContent>
    <CardFooter>
      <Button onClick={() => console.log('Create job posting')}>Create Job Posting</Button>
    </CardFooter>
  </Card>
)

export default ProjectPlan