import React from 'react'
import { motion } from "framer-motion"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { ScrollArea } from "@/components/ui/scroll-area"
import { Edit2, Send } from 'lucide-react'

interface ReviewAnswersProps {
  questionnaire: Array<{ question: string }>
  answers: string[]
  onEditAnswer: (index: number) => void
  onSubmit: () => void
  isLoading: boolean
}

const ReviewAnswers: React.FC<ReviewAnswersProps> = ({
  questionnaire,
  answers,
  onEditAnswer,
  onSubmit,
  isLoading
}) => {
  return (
    <Card className="w-full max-w-3xl mx-auto mt-10">
      <CardHeader>
        <CardTitle className="text-2xl font-bold text-center">Review Your Answers</CardTitle>
      </CardHeader>
      <CardContent>
        <ScrollArea className="h-[60vh]">
          {questionnaire.map((q, index) => (
            <motion.div 
              key={index}
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ duration: 0.5 }}
              className="flex justify-between items-start bg-secondary p-4 rounded-lg mb-2"
            >
              <div>
                <h3 className="font-semibold">{q.question}</h3>
                <p className="mt-2">{answers[index] || 'Not answered'}</p>
              </div>
              <Button onClick={() => onEditAnswer(index)} variant="outline" size="sm">
                <Edit2 className="w-4 h-4 mr-2" />
                Edit
              </Button>
            </motion.div>
          ))}
        </ScrollArea>
      </CardContent>
      <CardFooter className="flex justify-end">
        <Button onClick={onSubmit} size="lg" disabled={isLoading}>
          {isLoading ? (
            <>Generating Plan...</>
          ) : (
            <>
              Generate Project Plan
              <Send className="w-4 h-4 ml-2" />
            </>
          )}
        </Button>
      </CardFooter>
    </Card>
  )
}

export default ReviewAnswers