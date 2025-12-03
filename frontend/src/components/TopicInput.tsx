import { useState } from "react";
import axios from "axios";

interface Props {
  setRoadmap: (value: string) => void;
}

export default function TopicInput({ setRoadmap }: Props) {
  const [topic, setTopic] = useState("");

  async function generate() {
    if (!topic.trim()) return;

    const res = await axios.post("http://127.0.0.1:8000/generate", {
      topic: topic, // MUST MATCH BACKEND
    });

    setRoadmap(res.data.roadmap);
  }

  return (
    <div className="bg-gray-800 p-6 rounded-lg space-y-4">
      <h2 className="text-xl font-semibold">Generate from Topic</h2>

      <input
        type="text"
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
        className="w-full p-3 rounded bg-gray-700 text-white"
        placeholder="Ex: Machine Learning Engineer"
      />

      <button
        onClick={generate}
        className="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded"
      >
        Generate
      </button>
    </div>
  );
}