import { useState } from "react";
import axios from "axios";

interface Props {
  setRoadmap: (value: string) => void;
}

export default function FileUpload({ setRoadmap }: Props) {
  const [file, setFile] = useState<File | null>(null);

  async function upload() {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    const res = await axios.post(
      "http://127.0.0.1:8000/generate-from-pdf",
      formData,
      { headers: { "Content-Type": "multipart/form-data" } }
    );

    setRoadmap(res.data.roadmap);
  }

  return (
    <div className="bg-gray-800 p-6 rounded-lg space-y-4">
      <h2 className="text-xl font-semibold">Upload Resume (PDF)</h2>

      <input
        type="file"
        className="text-white"
        accept="application/pdf"
        onChange={(e) => setFile(e.target.files?.[0] ?? null)}
      />

      <button
        onClick={upload}
        className="bg-green-600 hover:bg-green-700 px-4 py-2 rounded"
      >
        Upload & Generate
      </button>
    </div>
  );
}