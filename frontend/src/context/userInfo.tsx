/* Provider for user information context */

import React, { createContext, useState, ReactNode } from 'react';

export interface UserInfo {
    id?: string;
    isAdmin?: boolean;
}

export interface UserInfoContextType {
    userInfo: UserInfo;
    setUserInfo: React.Dispatch<React.SetStateAction<UserInfo>>;
}

const UserInfoContext = createContext<UserInfoContextType | undefined>(undefined);

// Provider for user information context
export const UserInfoProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
    const [userInfo, setUserInfo] = useState<UserInfo>({});

    return (
        <UserInfoContext.Provider value={{ userInfo, setUserInfo }}>
            {children}
        </UserInfoContext.Provider>
    );
};

// Hook to use user information context
export const useUserInfo = (): UserInfoContextType => {
    const context = React.useContext(UserInfoContext);
    if (!context) {
        throw new Error('useUserInfo must be used within a UserInfoProvider');
    }
    return context;
};