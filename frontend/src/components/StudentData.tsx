import React, { useState, useMemo } from 'react';

// structure for a single student object
interface Student {
  id: number;
  name: string;
  gpa: number;
  gradYear: number;
}

// This is EXAMPLE DATA!!! This should come from a fastAPI call in the following format:
// GET /api/students
// Response: [{ id: number, name: string, gpa: number, gradYear: number }, ...]
const studentData: Student[] = [
  { id: 101, name: 'Alice Johnson', gpa: 3.8, gradYear: 2025 },
  { id: 102, name: 'Bob Smith', gpa: 3.2, gradYear: 2026 },
];

// StudentDetailModal Component: Displays a pop-up with student details
const StudentDetailModal: React.FC<{ student: Student | null; onClose: () => void }> = ({ student, onClose }) => {
  if (!student) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
      <div className="bg-white rounded-lg shadow-2xl p-8 m-4 max-w-sm w-full transform transition-all duration-300 ease-in-out scale-95 hover:scale-100">
        <h2 className="text-2xl font-bold mb-4 text-gray-800 border-b pb-2">Student Details</h2>
        <div className="space-y-3 text-gray-700">
          <p><strong>ID:</strong> {student.id}</p>
          <p><strong>Name:</strong> {student.name}</p>
          <p><strong>GPA:</strong> {student.gpa.toFixed(1)}</p>
          <p><strong>Graduation Year:</strong> {student.gradYear}</p>
        </div>
        <div className="mt-6 text-right">
          <button
            onClick={onClose}
            className="px-6 py-2 bg-indigo-600 text-white rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-colors duration-200"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
};


// --- MAIN APP COMPONENT ---
const App: React.FC = () => {
  // State for the search query
  const [searchTerm, setSearchTerm] = useState('');
  // State to manage which student is being viewed in the modal
  const [selectedStudent, setSelectedStudent] = useState<Student | null>(null);

  // Filter students based on the search term.
  // useMemo ensures this only recalculates when the data or search term changes.
  const filteredStudents = useMemo(() => {
    if (!searchTerm) {
      return studentData;
    }
    return studentData.filter(student =>
      student.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
  }, [searchTerm]);

  // Handler to open the modal
  const handleViewClick = (student: Student) => {
    setSelectedStudent(student);
  };

  // Handler to close the modal
  const handleCloseModal = () => {
    setSelectedStudent(null);
  };

  return (
    <div className="bg-gray-100 min-h-screen font-sans text-gray-800 p-4 sm:p-6 md:p-8">
      <div className="max-w-4xl mx-auto bg-white rounded-xl shadow-lg overflow-hidden">
        {/* Header Section */}
        <div className="p-6 bg-gray-50 border-b">
          <h1 className="text-3xl font-bold text-gray-900">Student Directory</h1>
          <p className="text-gray-600 mt-1">Search and view student information.</p>
        </div>

        {/* Search Bar */}
        <div className="p-6">
          <input
            type="text"
            placeholder="Search by name..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 transition-shadow duration-200"
          />
        </div>

        {/* Students Table */}
        <div className="overflow-x-auto">
          <table className="w-full text-left">
            <thead className="bg-gray-100">
              <tr>
                <th className="px-6 py-3 text-sm font-semibold uppercase tracking-wider text-gray-600">Name</th>
                <th className="px-6 py-3 text-sm font-semibold uppercase tracking-wider text-gray-600">ID</th>
                <th className="px-6 py-3 text-sm font-semibold uppercase tracking-wider text-gray-600">GPA</th>
                <th className="px-6 py-3 text-sm font-semibold uppercase tracking-wider text-gray-600 hidden sm:table-cell">Grad Year</th>
                <th className="px-6 py-3 text-sm font-semibold uppercase tracking-wider text-gray-600">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200">
              {filteredStudents.length > 0 ? (
                filteredStudents.map((student) => (
                  <tr key={student.id} className="hover:bg-gray-50 transition-colors duration-150">
                    <td className="px-6 py-4 whitespace-nowrap font-medium">{student.name}</td>
                    <td className="px-6 py-4 whitespace-nowrap">{student.id}</td>
                    <td className="px-6 py-4 whitespace-nowrap">{student.gpa.toFixed(1)}</td>
                    <td className="px-6 py-4 whitespace-nowrap hidden sm:table-cell">{student.gradYear}</td>
                    <td className="px-6 py-4 whitespace-nowrap">
                      <button
                        onClick={() => handleViewClick(student)}
                        className="px-4 py-1.5 text-sm font-medium text-white bg-indigo-600 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-transform duration-150 active:scale-95"
                      >
                        View
                      </button>
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan={5} className="text-center py-10 text-gray-500">
                    No students found matching your search.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Modal for viewing student details */}
      <StudentDetailModal student={selectedStudent} onClose={handleCloseModal} />
    </div>
  );
};

export default App;
