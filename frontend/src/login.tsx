/* Login Component */
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
import { isAdmin } from './context/verify-admin';  // Check if user is admin
import { fetchKGDataById, fetchFullKGData } from './api'
import { useUserInfo } from './context/userInfo';  // Hook from userInfo context
import { useKGInfo } from './context/kgInfo';

/** Functional component for logging in. 
 * - Users can log in by entering their ID.
 * - Admins can log in with a predefined admin ID.  
*/
function App() {
  // Getting states and contexts to set
  const { setUserInfo } = useUserInfo();
  const { setKGInfo } = useKGInfo();
  const [id, setId] = useState('');
  const navigate = useNavigate();  // Hook for navigation

  // Handling the submit button action
  const handleSubmit = () => {
    console.log('Submitted ID:', id);
    // Handling admin logons, set context and redirect to admin view
    if(isAdmin(id)){
        // Admin login
        setUserInfo({ id, isAdmin: true });
        fetchFullKGData().then(data => {
            setKGInfo({ nodes: data.nodes, relationships: data.relationships, loading: true, error: null });
        }).catch(err => {
            console.error('Error fetching full KG data:', err);
        }).finally(() => {
            setKGInfo(prev => ({ ...prev, loading: false }));  // Set loading flag to false
            navigate('/admin');  // Redirect to admin view
        });
    }
    // Handling student logons, set context and redirect to student view
    else {
        setUserInfo({ id, isAdmin: false });
        fetchKGDataById(id).then(data => {
            if ('error' in data) {
                setKGInfo({ nodes: [], relationships: [], loading: true, error: data.error });
            } else {
                setKGInfo({ nodes: data.nodes, relationships: data.relationships, loading: false, error: null });
            }
        }).catch(err => {
            console.error('Error fetching KG data by ID:', err);
        }).finally(() => {
            setKGInfo(prev => ({ ...prev, loading: false }));  // Set loading flag to false
            navigate('/student');  // Redirect to student view
        });
    }
  };

  // Returning the HTML contents to display on the screen
  return (
    <>
      <h1>Enter ID</h1>
      <input 
        type="text" 
        placeholder='ID' 
        value={id} 
        onChange={(e) => setId(e.target.value)} 
      />
      <button onClick={handleSubmit}>Submit</button>
    </>
  );
}

export default App;
