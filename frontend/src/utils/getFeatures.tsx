/* Not technically context but don't care 
Holds all of the different statistics/vislauzations that we pull from the backend
Will display on the collaspible side-bar on the right of the dashboard
*/

import * as ic from "@ant-design/icons";

// Const for features available to admin dashboard. Will add as more are implemented
const ADMIN_FEATURES = [
    { key: "fullKnowledgeGraph", label: "Full Knowledge Graph", icon: <ic.BranchesOutlined style={{ fontSize: 20 }} /> },
    { key: "projectedGPA", label: "Projected GPA", icon: <ic.LineChartOutlined style={{ fontSize: 20 }} /> },
    
]

// Const for features available to student dashboard. Will add as more are implemented
const USER_FEATURES = [
    { key: "knowledgeGraph", label: "Knowledge Graph", icon: <ic.BranchesOutlined style={{ fontSize: 20 }} /> },
    { key: "courseRecommendations", label: "Course Recommendations", icon: <ic.BarsOutlined style={{ fontSize: 20 }} /> },
    { key: "degreeProgress", label: "Degree Progress", icon: <ic.CheckCircleOutlined style={{ fontSize: 20 }} /> },
    { key: "projectedGPA", label: "Projected GPA", icon: <ic.LineChartOutlined style={{ fontSize: 20 }} /> },
    
]

// Helper function to get features based on user role
export function getFeatures(isAdmin: boolean) {
    return isAdmin ? ADMIN_FEATURES : USER_FEATURES;
}
