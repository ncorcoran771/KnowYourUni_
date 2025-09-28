/* Not technically context but don't care 
Holds all of the different statistics/vislauzations that we pull from the backend
Will display on the collaspible side-bar on the right of the dashboard
*/

import * as ic from "@ant-design/icons";

// Const for features available to admin dashboard. Will add as more are implemented
const ADMIN_FEATURES = [
    { key: "studentData", label: "Overview", icon: <ic.BranchesOutlined style={{ fontSize: 20 }} /> },
    { key: "gpaForecast", label: "Projected GPA", icon: <ic.LineChartOutlined style={{ fontSize: 20 }} /> },
    { key: "unibud", label: "Unibud Chat", icon: <ic.MessageOutlined style={{ fontSize: 20 }} /> },
]

// Const for features available to student dashboard. Will add as more are implemented
const USER_FEATURES = [
    { key: "studentData", label: "Overview", icon: <ic.BranchesOutlined style={{ fontSize: 20 }} /> },
    { key: "courseSuggestion", label: "Course Recommendations", icon: <ic.BarsOutlined style={{ fontSize: 20 }} /> },
    { key: "gpaForecast", label: "GPA Forecast", icon: <ic.LineChartOutlined style={{ fontSize: 20 }} /> },
    { key: "studyBuddies", label: "Suggested Study Buddies", icon: <ic.LineChartOutlined style={{ fontSize: 20 }} /> },
    { key: "unibud", label: "Unibud Chat", icon: <ic.MessageOutlined style={{ fontSize: 20 }} /> },
]

// Helper function to get features based on user role
export function getFeatures(isAdmin: boolean) {
    return isAdmin ? ADMIN_FEATURES : USER_FEATURES;
}
