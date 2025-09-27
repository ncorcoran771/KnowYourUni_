/* Provider for the knowledge graph data */

import React, { createContext, useState, ReactNode, useContext } from 'react';

export interface KGInfo {
    nodes: string[];
    relationships: string[];
    loading: boolean;
    error: string | null;
}

export interface KGInfoContextType {
    KGInfo: KGInfo;
    setKGInfo: React.Dispatch<React.SetStateAction<KGInfo>>;
}

const KGInfoContext = createContext<KGInfoContextType | undefined>(undefined);

// Provider for KGInfo context
export const KGInfoProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
    const [KGInfo, setKGInfo] = useState<KGInfo>({ nodes: [], relationships: [], loading: false, error: null });

    return (
        <KGInfoContext.Provider value={{ KGInfo, setKGInfo }}>
            {children}
        </KGInfoContext.Provider>
    );
};

// Hook to use KGInfo context
export const useKGInfo = (): KGInfoContextType => {
    const context = useContext(KGInfoContext);
    if (!context) {
        throw new Error('useKGInfo must be used within a KGInfoProvider');
    }
    return context;
};