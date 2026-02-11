import React, { useState } from 'react'

const API_URL = import.meta?.env?.VITE_API_URL || 'http://localhost:8000'

export default function App() {
  const [input, setInput] = useState('')
  const [messages, setMessages] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  async function sendMessage(e) {
    e?.preventDefault()
    const question = input.trim()
    if (!question) return

    const userMsg = { role: 'user', text: question }
    setMessages(prev => [...prev, userMsg])
    setInput('')
    setLoading(true)
    setError(null)

    try {
      const res = await fetch(`${API_URL}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question })
      })

      if (!res.ok) {
        const text = await res.text()
        throw new Error(`Server error: ${res.status} ${text}`)
      }

      const data = await res.json()
      const assistantMsg = { role: 'assistant', text: data.answer, sources: data.sources || [] }
      setMessages(prev => [...prev, assistantMsg])
    } catch (err) {
      setError(err.message)
      setMessages(prev => [...prev, { role: 'assistant', text: 'Error: ' + err.message }])
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <h1>RAG Chatbot</h1>

      <div className="chat">
        {messages.length === 0 && <div className="empty">Ask me something about the corpus.</div>}

        {messages.map((m, i) => (
          <div key={i} className={`message ${m.role}`}>
            <div className="role">{m.role === 'user' ? 'You' : 'Assistant'}</div>
            <div className="text">{m.text}</div>
            {m.sources && m.sources.length > 0 && (
              <details className="sources">
                <summary>Sources ({m.sources.length})</summary>
                <ul>
                  {m.sources.map((s, idx) => (
                    <li key={idx}><pre>{typeof s === 'string' ? s : JSON.stringify(s)}</pre></li>
                  ))}
                </ul>
              </details>
            )}
          </div>
        ))}
      </div>

      <form onSubmit={sendMessage} className="composer">
        <input
          value={input}
          onChange={e => setInput(e.target.value)}
          placeholder="Type a question and press Enter"
          disabled={loading}
        />
        <button type="submit" disabled={loading}>Send</button>
      </form>

      {loading && <div className="loading">Thinking…</div>}
      {error && <div className="error">{error}</div>}
    </div>
  )
}
