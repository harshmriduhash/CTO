# AI CTO Frontend

This is the frontend application for the AI CTO project, built with Next.js and TypeScript.

## Technologies Used

- Next.js 14
- React 18
- TypeScript
- Tailwind CSS
- Supabase Client

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   npm install
   ```
3. Set up environment variables in a `.env.local` file:
   ```
   NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
   NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```

## Running the Frontend

To start the development server:

```
npm run dev
```

The application will be available at `http://localhost:3000`.

## Project Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── Questionnaire.tsx
│   │   ├── ProjectPlan.tsx
│   │   └── ReviewAnswers.tsx
│   ├── types/
│   │   └── index.ts
│   ├── services/
│   │   └── api.ts
│   ├── lib/
│   │   └── questionnaire.ts
│   └── pages/
│       └── index.tsx
├── public/
├── styles/
├── package.json
├── tsconfig.json
└── .env.local
```

## Questionnaire Component

The main Questionnaire component (`src/components/Questionnaire.tsx`) handles the display and submission of the project questionnaire.

### Question Generation

Questions are defined in `src/lib/questionnaire.ts` as an array of question objects. Each question includes:
- The question text
- Answer options
- A tooltip for additional information

### Submitting Responses

When a user completes the questionnaire:
1. The `handleSubmit` function in `Questionnaire.tsx` is called.
2. It creates a `QuestionnaireResponse` object with the questions and user answers.
3. The `submitQuestionnaire` function from `src/services/api.ts` is called to send the data to the backend.
4. The backend processes the questionnaire and returns a project plan.
5. The frontend displays the generated project plan using the `ProjectPlan` component.

## Project Plan Generation

The project plan is generated on the backend using the OpenAI Assistant API. The frontend receives the plan as an `AIProjectDetails` object, which includes:
- Project title and description
- Recommended tech stack
- Key features
- Project timeline
- Budget estimate
- Product requirements
- Job description
- Required skills

This information is then displayed to the user using the `ProjectPlan` component (`src/components/ProjectPlan.tsx`).

## Supabase Integration

The frontend uses the Supabase client to interact with the database for operations such as fetching questionnaires. The Supabase client is initialized in `src/services/api.ts`.

## API Service

The `api.ts` file in the `services` folder contains functions for interacting with the backend API:

- `submitQuestionnaire`: Sends the completed questionnaire to the backend
- `getQuestionnaire`: Fetches a questionnaire from Supabase
- `createJobPosting`: Creates a new job posting based on the project plan

## Type Definitions

The `types/index.ts` file contains TypeScript interfaces for various data structures used in the application, including:

- `QuestionOption`
- `Question`
- `Answer`
- `Questionnaire`
- `UserResponse`
- `ProjectPlan`
- `QuestionnaireResponse`
- `AIProjectDetails`
- `JobPosting`

## Styling

The project uses Tailwind CSS for styling. Custom styles can be added in the `styles` directory.

## Building for Production

To create a production build:

```
npm run build
```

Then, to start the production server:

```
npm start
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.