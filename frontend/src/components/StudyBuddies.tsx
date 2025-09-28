/* Study buddy suggestions table */

import React from "react";
import { Table } from "antd";
import { fetchStudyBuddies } from "../api";
import { useUserInfo } from "../context/UserInfoProvider";

interface StudyBuddy {
    name: string;
    totalSimilarityScore: number;
    learningTypeSimilarityScore: number;
    PerformanceSimilarityScore: number;
}

export const StudyBuddies: React.FC = () => {
    // Get the study buddy data from the current user
    const { userInfo } = useUserInfo();

    const [data, setData] = React.useState<{ buddies: StudyBuddy[] }>({ buddies: [] });

    React.useEffect(() => {
        if (userInfo.id) {
            fetchStudyBuddies(userInfo.id).then((response) => {
                setData(response);
            });
        }
    }, [userInfo.id]); // Queries specific ID

    // Define columns for the table
    const columns = [
        { title: 'Name', dataIndex: 'name', key: 'name' },
        { title: 'Total Similarity Score', dataIndex: 'totalSimilarityScore', key: 'totalSimilarityScore' },
        { title: 'Learning Type Similarity Score', dataIndex: 'learningTypeSimilarityScore', key: 'learningTypeSimilarityScore' },
        { title: 'Performance Similarity Score', dataIndex: 'PerformanceSimilarityScore', key: 'PerformanceSimilarityScore' },
    ];

    return (
        <Table columns={columns} dataSource={data.buddies} rowKey="name" />
    );
};

export default StudyBuddies;