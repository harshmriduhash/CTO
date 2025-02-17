"use client";

import React, { useState, useEffect } from 'react'
import { motion, AnimatePresence } from "framer-motion"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Progress } from "@/components/ui/progress"
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"
import { useToast } from "@/hooks/use-toast"
import { AlertCircle, ArrowLeft, ArrowRight } from 'lucide-react'
import { TooltipProvider } from "@/components/ui/tooltip"
import QuestionCard from './QuestionCard'
import ReviewAnswers from './ReviewAnswers'
import ProjectPlan from './ProjectPlan'
import { ProjectPlan as ProjectPlanType, Question, QuestionnaireResponse } from '@/types'
import { submitQuestionnaire } from '@/services/api'
import { questionnaire } from '@/lib/questionnaire'

export default function Questionnaire() {
  const [currentStep, setCurrentStep] = useState(0)
  const [answers, setAnswers] = useState<string[]>(new Array(questionnaire.length).fill(''))
  const [submitted, setSubmitted] = useState(false)
  const [isReviewing, setIsReviewing] = useState(false)
  const [editingQuestion, setEditingQuestion] = useState<number | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [projectPlan, setProjectPlan] = useState<ProjectPlanType | null>(null)
  const [isLoading, setIsLoading] = useState(false)
  const { toast } = useToast()

  const progressPercentage = ((currentStep + 1) / questionnaire.length) * 100

  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      if (event.key === 'ArrowRight') {
        handleNext()
      } else if (event.key === 'ArrowLeft') {
        handlePrevious()
      }
    }

    window.addEventListener('keydown', handleKeyDown)
    return () => window.removeEventListener('keydown', handleKeyDown)
  }, [currentStep])

  const handleNext = () => {
    if (answers[currentStep] === '') {
      setError('Please select an answer before proceeding.')
      return
    }
    setError(null)
    if (currentStep < questionnaire.length - 1) {
      setCurrentStep(currentStep + 1)
    } else {
      setIsReviewing(true)
    }
  }

  const handlePrevious = () => {
    if (currentStep > 0) {
      setCurrentStep(currentStep - 1)
    }
    setError(null)
  }

  const handleSubmit = async () => {
    setIsLoading(true)
    try {
      const response: QuestionnaireResponse = {
        questions: questionnaire,
        answers: answers,
      }
      const plan = await submitQuestionnaire(response)
      setProjectPlan(plan)
      setSubmitted(true)
      toast({
        title: "Project Plan Generated",
        description: "Your AI CTO has analyzed your responses and generated a project plan!",
        duration: 5000,
      })
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to generate project plan. Please try again.",
        variant: "destructive",
        duration: 5000,
      })
    } finally {
      setIsLoading(false)
    }
  }

  const handleAnswerChange = (value: string) => {
    setAnswers(prev => {
      const newAnswers = [...prev]
      newAnswers[currentStep] = value
      return newAnswers
    })
    setError(null)
  }

  const handleEditAnswer = (index: number) => {
    setCurrentStep(index)
    setEditingQuestion(index)
    setIsReviewing(false)
  }

  const handleFinishEditing = () => {
    setIsReviewing(true)
    setEditingQuestion(null)
  }

  if (submitted && projectPlan) {
    return <ProjectPlan plan={projectPlan} />
  }

  if (isReviewing) {
    return (
      <ReviewAnswers
        questionnaire={questionnaire}
        answers={answers}
        onEditAnswer={handleEditAnswer}
        onSubmit={handleSubmit}
        isLoading={isLoading}
      />
    )
  }

  return (
    <TooltipProvider>
      <div className="min-h-screen bg-gradient-to-br from-primary/20 to-secondary/20 flex items-center justify-center p-4">
        <Card className="w-full max-w-3xl mx-auto">
          <CardHeader>
            <CardTitle className="text-2xl font-bold text-center">Project Questionnaire</CardTitle>
          </CardHeader>
          <CardContent>
            <Progress value={progressPercentage} className="mb-4" />
            <AnimatePresence mode="wait">
              <motion.div
                key={currentStep}
                initial={{ opacity: 0, x: 50 }}
                animate={{ opacity: 1, x: 0 }}
                exit={{ opacity: 0, x: -50 }}
                transition={{ duration: 0.3 }}
                className="space-y-4"
              >
                <QuestionCard
                  question={questionnaire[currentStep].question}
                  options={questionnaire[currentStep].options}
                  tooltip={questionnaire[currentStep].tooltip}
                  answer={answers[currentStep]}
                  onAnswerChange={handleAnswerChange}
                />
                {error && (
                  <Alert variant="destructive">
                    <AlertCircle className="h-4 w-4" />
                    <AlertTitle>Error</AlertTitle>
                    <AlertDescription>{error}</AlertDescription>
                  </Alert>
                )}
              </motion.div>
            </AnimatePresence>
          </CardContent>
          <CardFooter className="flex justify-between">
            {editingQuestion !== null ? (
              <Button onClick={handleFinishEditing}>
                <ArrowLeft className="w-4 h-4 mr-2" />
                Back to Review
              </Button>
            ) : (
              <Button onClick={handlePrevious} disabled={currentStep === 0}>
                <ArrowLeft className="w-4 h-4 mr-2" />
                Previous
              </Button>
            )}
            <Button onClick={editingQuestion !== null ? handleFinishEditing : handleNext}>
              {editingQuestion !== null ? (
                <>Finish Editing</>
              ) : currentStep === questionnaire.length - 1 ? (
                <>Review</>
              ) : (
                <>
                  Next
                  <ArrowRight className="w-4 h-4 ml-2" />
                </>
              )}
            </Button>
          </CardFooter>
        </Card>
      </div>
    </TooltipProvider>
  )
}