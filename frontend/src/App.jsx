import { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [skills, setSkills] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return alert("Please select a file");

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      setError("");
      const res = await axios.post("http://127.0.0.1:8000/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setSkills(res.data.skills);
    } catch (err) {
      console.error(err);
      setError("Error uploading file. Make sure backend is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-r from-indigo-100 to-purple-100 flex flex-col items-center justify-start py-12">
      <h1 className="text-4xl font-bold text-gray-800 mb-8">Resume Skill Extractor</h1>

      <div className="bg-white p-8 rounded-xl shadow-lg w-full max-w-md flex flex-col items-center gap-4">
        <input
          type="file"
          onChange={handleFileChange}
          className="border border-gray-300 rounded p-2 w-full"
        />
        <button
          onClick={handleUpload}
          className="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-2 px-4 rounded w-full"
        >
          {loading ? "Extracting..." : "Extract Skills"}
        </button>
        {error && <p className="text-red-500">{error}</p>}
      </div>

      {skills.length > 0 && (
        <div className="mt-10 w-full max-w-xl bg-white p-6 rounded-xl shadow-lg">
          <h2 className="text-2xl font-semibold mb-4 text-gray-700">Extracted Skills</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            {skills.map((s, index) => (
              <div
                key={index}
                className="border border-gray-200 rounded p-3 hover:shadow-md transition-all"
              >
                <p className="font-medium text-gray-800">{s.skill}</p>
                <p className="text-sm text-gray-500">
                  {Array.isArray(s.category) ? s.category.join(", ") : s.category}
                </p>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
