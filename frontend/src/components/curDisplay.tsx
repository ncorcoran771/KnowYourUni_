/** Basic helper function to return the currently selected element from the dashboard */

// Import for FC
import React from "react";
// Imports for different displays/elements
import UnibudChat from "./Unibud";
import StudyBuddies from "./StudyBuddies";
import ForecastData from "./ForecastData";
import StudentData from "./StudentData";
import CourseSuggestion from "./CourseSuggestion";

type Props = { selection: string };

const CurDisplay: React.FC<Props> = ({ selection }) => {
  const views: Record<string, React.ReactNode> = {
    studentData: <StudentData />,
    courseSuggestion: <CourseSuggestion />,
    studyBuddies: <StudyBuddies />,
    unibud: <UnibudChat />,
    gpaForecast: <ForecastData />
    // Add more mappings as needed
};

  return <>{views[selection] ?? <div>Select a panel</div>}</>;
};

export default CurDisplay;