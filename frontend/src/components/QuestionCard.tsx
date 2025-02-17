import React from 'react'
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Label } from "@/components/ui/label"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip"
import { Button } from "@/components/ui/button"
import { HelpCircle } from 'lucide-react'

interface QuestionCardProps {
  question: string
  options: string[]
  tooltip: string
  answer: string
  onAnswerChange: (value: string) => void
}

const QuestionCard: React.FC<QuestionCardProps> = ({
  question,
  options,
  tooltip,
  answer,
  onAnswerChange
}) => (
  <Card className="w-full">
    <CardHeader>
      <div className="flex items-center justify-between">
        <CardTitle className="text-xl font-semibold">{question}</CardTitle>
        <Tooltip>
          <TooltipTrigger asChild>
            <Button variant="ghost" size="sm">
              <HelpCircle className="w-4 h-4" />
              <span className="sr-only">Help</span>
            </Button>
          </TooltipTrigger>
          <TooltipContent>
            <p>{tooltip}</p>
          </TooltipContent>
        </Tooltip>
      </div>
    </CardHeader>
    <CardContent>
      <RadioGroup value={answer} onValueChange={onAnswerChange}>
        {options.map((option, index) => (
          <div key={index} className="flex items-center space-x-2 p-2 hover:bg-secondary rounded-md transition-colors">
            <RadioGroupItem value={option} id={`option-${index}`} />
            <Label htmlFor={`option-${index}`} className="flex-grow cursor-pointer">{option}</Label>
          </div>
        ))}
      </RadioGroup>
    </CardContent>
  </Card>
)

export default React.memo(QuestionCard)