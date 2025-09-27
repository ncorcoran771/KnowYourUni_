import React from 'react';
import { Button, Layout } from 'antd';

const { Header, Content, Footer } = Layout;

export const AdminDashboard: React.FC = () => {
    const handleBack = () => {
        console.log('Back button clicked');
        // Add navigation logic here
    };

    return (
        <Layout style={{ minHeight: '100vh' }}>
            <Header style={{ display: 'flex', alignItems: 'center', backgroundColor: '#001529' }}>
                <Button type="primary" onClick={handleBack} style={{ marginRight: 'auto' }}>
                    Back
                </Button>
                <h1 style={{ color: 'white', margin: 0 }}>Admin Dashboard</h1>
            </Header>
            <Content style={{ margin: '16px', padding: '16px', backgroundColor: 'white' }}>
                <p>Welcome to the Admin Dashboard!</p>
                {/* Add dashboard content here */}
            </Content>
            <Footer style={{ textAlign: 'center' }}>© 2025 KnowYourUni</Footer>
        </Layout>
    );
};

export default AdminDashboard;