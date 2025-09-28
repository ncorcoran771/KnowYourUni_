/* Student Dashboard */
import React from 'react';
import { Layout } from 'antd';
import { Shell } from './components/Shell';

export const StudentDashboard: React.FC = () => {

    return (
        <Layout style={{ minHeight: '100vh' }}>
            <div style={{ margin: '16px', padding: '16px' }}>
                <Shell />
            </div>
            <Layout.Footer style={{ textAlign: 'center' }}>HackUMBC '25 - KnowYourUni</Layout.Footer>
        </Layout>
    );
};

export default StudentDashboard;