import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom/client';
import './styles.css';

function App() {
  const [isListening, setIsListening] = useState(false);
  const [transcript, setTranscript] = useState('');
  const [error, setError] = useState('');
  const [token, setToken] = useState('');

  useEffect(() => {
    // Check backend connectivity on mount
    const checkBackend = async () => {
      try {
        const response = await fetch('/config');
        if (response.ok) {
          const config = await response.json();
          console.log('Backend config:', config);
          setTranscript('Backend connected');
        } else {
          setError('Backend not responding');
        }
      } catch (err) {
        console.error('Backend check failed:', err);
        setError('Failed to connect to backend');
      }
    };

    checkBackend();
  }, []);

  const handleStartListening = async () => {
    setIsListening(true);
    setError('');
    setTranscript('');

    try {
      console.log('Requesting token from backend...');
      const response = await fetch('/token', {
        method: 'POST',
        headers: { 
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          room: 'friday-room',
          username: 'user-' + Math.random().toString(36).substr(2, 9),
        }),
      });

      if (!response.ok) {
        throw new Error(`Token request failed: ${response.status}`);
      }

      const data = await response.json();
      console.log('Token response:', data);
      
      if (!data.token) {
        throw new Error('No token in response');
      }

      setToken(data.token);
      setTranscript(`✅ Connected to Friday!\nToken: ${data.token.substring(0, 20)}...`);
      console.log('Successfully connected with token');

    } catch (err) {
      console.error('Error during connection:', err);
      setError(`Connection error: ${err.message}`);
      setTranscript(`❌ Failed to connect: ${err.message}`);
    } finally {
      setIsListening(false);
    }
  };

  return (
    <div className="container">
      <div className="header">
        <h1>🎙️ Friday</h1>
        <p>Advanced AI Personal Assistant</p>
      </div>

      <div className="main-content">
        <div className="card">
          <h2>Start Conversation</h2>
          <div className="voice-section">
            <div className={`voice-visualizer ${isListening ? 'listening' : ''}`}>
              🎤
            </div>
            <button
              onClick={handleStartListening}
              disabled={isListening}
            >
              {isListening ? 'Connecting...' : 'Start Listening'}
            </button>
          </div>
          
          {error && (
            <div className="error-message">
              <p>{error}</p>
            </div>
          )}

          {transcript && !error && (
            <div className="transcript">
              <p>{transcript}</p>
            </div>
          )}

          {token && (
            <div className="token-info">
              <p><strong>Status:</strong> Ready for voice input</p>
            </div>
          )}
        </div>

        <div className="card">
          <h2>Features</h2>
          <ul className="features-list">
            <li>🎤 Voice Conversations</li>
            <li>💭 AI-Powered Responses</li>
            <li>⚡ Real-time Processing</li>
            <li>🔐 Secure & Private</li>
          </ul>
        </div>
      </div>
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
