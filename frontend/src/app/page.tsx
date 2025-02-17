import Link from "next/link";

export default function Home() {
  return (
    <div className="container mx-auto py-10">
      <h1 className="text-3xl font-bold mb-6">Welcome to our Questionnaire App</h1>
      <Link href="/questionnaire" className="text-blue-500 hover:underline">
        Start Questionnaire
      </Link>
    </div>
  );
}
