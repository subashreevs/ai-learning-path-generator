import { useState } from "react";
import TopicInput from "./components/TopicInput";
import FileUpload from "./components/FileUpload";
import Roadmap from "./components/Roadmap";

export default function App() {
  const [roadmap, setRoadmap] = useState("");

  return (
    <div className="min-h-screen bg-gray-900 text-white p-6">
      <h1 className="text-4xl font-bold text-center mb-8">AI Learning Path Generator</h1>

      <div className="max-w-3xl mx-auto space-y-8">
        <TopicInput setRoadmap={setRoadmap} />
        <FileUpload setRoadmap={setRoadmap} />
        <Roadmap roadmap={roadmap} />
      </div>
    </div>
  );
}