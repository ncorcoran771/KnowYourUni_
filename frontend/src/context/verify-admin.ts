/** PROOF-OF-CONCEPT ONLY
 * In a real-world application, these would be protected under an actual auth system.
 * However, given the timeline, they will be predefined as context here.
 */

// POC list of predetermined admin IDs
export const adminIDs = ['admin123', 'admin456', 'admin789'];

// Function to check if a given ID is an admin ID
// Note: In a real application, this would be handled via authentication and not client-side logic
export function isAdmin(id: string | undefined): boolean {
    return id !== undefined && adminIDs.includes(id);
}