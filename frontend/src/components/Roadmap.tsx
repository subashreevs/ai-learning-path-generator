interface Props {
  roadmap: string;
}

export default function Roadmap({ roadmap }: Props) {
  if (!roadmap) return null;

  return (
    <div className="bg-gray-800 p-6 rounded-lg whitespace-pre-wrap">
      <h2 className="text-2xl font-bold mb-4">Generated Learning Path</h2>
      <p>{roadmap}</p>
    </div>
  );
}