import React, { useState, useRef, useEffect } from 'react'

const API_URL = import.meta?.env?.VITE_API_URL || 'http://localhost:8000'

function Header() {
  return (
    <header className="header">
      <div className="brand">
        <div className="logo">R</div>
        <div className="title">RAG Chat</div>
      </div>
      <div className="subtitle">Retrieve-and-Generate assistant</div>
    </header>
  )
}

function Avatar({ role }) {
  if (role === 'user') return <div className="avatar user">U</div>
  return <div className="avatar bot">A</div>
}

export default function App() {
  const [input, setInput] = useState('')
  const [messages, setMessages] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const listRef = useRef(null)

  useEffect(() => {
    const el = listRef.current
    if (el) el.scrollTop = el.scrollHeight
  }, [messages, loading])

  async function sendMessage(e) {
    e?.preventDefault()
    const question = input.trim()
    if (!question) return

    const userMsg = {
      id: Date.now() + Math.random(),
      role: 'user',
      text: question,
      time: new Date().toISOString()
    }
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
      const assistantMsg = {
        id: Date.now() + Math.random(),
        role: 'assistant',
        text: data.answer || data?.text || JSON.stringify(data),
        sources: data.sources || [],
        time: new Date().toISOString()
      }
      setMessages(prev => [...prev, assistantMsg])
    } catch (err) {
      setError(err.message)
      setMessages(prev => [...prev, { id: Date.now() + Math.random(), role: 'assistant', text: 'Error: ' + err.message, time: new Date().toISOString() }])
    } finally {
      setLoading(false)
    }
  }

  function handleKeyDown(e) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      sendMessage()
    }
  }

  function clearChat() {
    setMessages([])
    setError(null)
  }

  return (
    <div className="app">
      <div className="card">
        <Header />

        <main className="chat" ref={listRef} aria-live="polite">
          {messages.length === 0 && (
            <div className="empty">Welcome — ask a question about the corpus.</div>
          )}

          {messages.map(m => (
            <div key={m.id} className={`message-row ${m.role}`}>
              <Avatar role={m.role} />
              <div className={`message ${m.role}`}>
                <div className="meta">
                  <span className="who">{m.role === 'user' ? 'You' : 'Assistant'}</span>
                  <span className="time">{new Date(m.time).toLocaleTimeString()}</span>
                </div>
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
            </div>
          ))}
        </main>

        <form onSubmit={sendMessage} className="composer">
          <textarea
            value={input}
            onChange={e => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Type your message and press Enter to send"
            rows={1}
          />
          <div className="controls">
            <button type="button" className="btn clear" onClick={clearChat} title="Clear chat">Clear</button>
            <button type="submit" className="btn send" disabled={loading} aria-busy={loading}>{loading ? 'Sending…' : 'Send'}</button>
          </div>
        </form>

        {error && <div className="error">{error}</div>}
      </div>
    </div>
  )
}
