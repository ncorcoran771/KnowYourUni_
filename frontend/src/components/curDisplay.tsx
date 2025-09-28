/** Basic helper function to return the currently selected element from the dashboard */

// Import for FC
import React from "react";
// Imports for different displays/elements
import UnibudChat from "./unibud";
import StudyBuddies from "./StudyBuddies";

type Props = { selection: string };

const CurDisplay: React.FC<Props> = ({ selection }) => {
  const views: Record<string, React.ReactNode> = {
    overview: <div>📊 Overview content here</div>,
    studyBuddies: <StudyBuddies />,
    unibud: <UnibudChat />
    // Add more mappings as needed
};

  return <>{views[selection] ?? <div>Select a panel</div>}</>;
};

export default CurDisplay;