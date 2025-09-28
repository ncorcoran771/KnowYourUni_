/* All api endpoints, which will be redirected to fastapi */

/** Example endpoint to get the current health status of the backend 
 * Expecting a response like { status: "ok" }
*/
export async function getHealth(){
    const res = await fetch('/api/health');
    if (!res.ok) {
        throw new Error('Failed to fetch health status');
    }
    return res.json() as Promise<{ status: string }>;
}

/** Fetch knowledge graph data by ID 
 * Params: id - The student ID to fetch the knowledge graph for
 * Returns: An object containing nodes and relationships or an error message
*/
export async function fetchKGDataById(id: string){
    // Ensure that the student id actuallty exists
    const validRes = await fetch(`/api/validate/${id}`);
    if (!validRes.ok || validRes.status === 404) {
        // Return with error if student could be not validated
        return { error: 'Invalid ID' };  
    }

    // Get the full knowledge graph data for the given ID
    const res = await fetch(`/api/kg/${id}`);
    if (!res.ok) {
        throw new Error('Failed to fetch knowledge graph data');
    }
    return res.json() as Promise<{ nodes: string[], relationships: string[] }>;
}

/** Fetch the full knowledge graph for admins 
 * Returns: An object containing nodes and relationships or an error message
*/
export async function fetchFullKGData(){
    const res = await fetch('/api/kg/');
    if (!res.ok) {
        throw new Error('Failed to fetch full knowledge graph data');
    }
    return res.json() as Promise<{ nodes: string[], relationships: string[] }>;
}

/** Fetches the study buddy data */
export async function fetchStudyBuddies(id: string) {
    const res = await fetch(`/api/get_study_buddies/${id}`);
    if (!res.ok) {
        throw new Error('Failed to fetch study buddies data');
    }
    return res.json() as Promise<{ buddies: any[] }>;
}