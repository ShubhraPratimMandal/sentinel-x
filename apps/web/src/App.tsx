import {
  Activity,
  AlertTriangle,
  ArrowUpRight,
  BarChart3,
  BrainCircuit,
  ChevronRight,
  CircleDot,
  Database,
  Globe2,
  Layers3,
  LockKeyhole,
  Radar,
  Search,
  Shield,
  Siren,
  TerminalSquare,
} from "lucide-react";

const alerts = [
  { id: "SX-0421", severity: "CRITICAL", title: "Synthetic credential anomaly cluster", source: "AUTH-GATEWAY", time: "08:42 UTC" },
  { id: "SX-0418", severity: "HIGH", title: "Suspicious DNS observation group", source: "DNS-SENSOR", time: "08:31 UTC" },
  { id: "SX-0415", severity: "MEDIUM", title: "Repeated failed authentication pattern", source: "IDENTITY", time: "08:14 UTC" },
];

const metrics = [
  ["ACTIVE CASES", "24", "+4.8%", Activity],
  ["CORRELATED EVENTS", "1,842", "+12.3%", Layers3],
  ["HIGH-RISK IOCs", "137", "+7.1%", Radar],
  ["ANALYST QUEUE", "18", "-3.2%", BarChart3],
] as const;

function App() {
  return (
    <div className="shell">
      <aside className="sidebar">
        <div className="brand">
          <div className="brand-mark"><Shield size={21} /></div>
          <div>
            <strong>SENTINEL-X</strong>
            <span>CYBER INTELLIGENCE</span>
          </div>
        </div>

        <div className="classification">PUBLIC RESEARCH BUILD <span>v0.1</span></div>

        <nav>
          {[
            ["Command Center", TerminalSquare],
            ["Investigations", Search],
            ["Threat Intelligence", Radar],
            ["Entity Graph", Globe2],
            ["Incident Response", Siren],
            ["AI Analyst", BrainCircuit],
            ["Data Explorer", Database],
          ].map(([label, Icon], index) => (
            <button className={index === 0 ? "nav-item active" : "nav-item"} key={String(label)}>
              <Icon size={17} />
              <span>{String(label)}</span>
              {index === 0 && <ChevronRight size={14} className="nav-arrow" />}
            </button>
          ))}
        </nav>

        <div className="sidebar-bottom">
          <div className="system-card">
            <div><CircleDot size={12} /> SYSTEM STATUS</div>
            <strong>OPERATIONAL</strong>
            <span>All local services nominal</span>
          </div>
          <div className="user-chip">
            <div className="avatar">AN</div>
            <div><strong>ANALYST-01</strong><span>Tier 2 Analyst</span></div>
          </div>
        </div>
      </aside>

      <main>
        <header className="topbar">
          <div>
            <div className="eyebrow">OPERATIONS / COMMAND CENTER</div>
            <h1>Threat Operations</h1>
          </div>
          <div className="top-actions">
            <div className="live"><span /> LIVE DATA</div>
            <button className="icon-button"><LockKeyhole size={17} /></button>
            <button className="profile">AN</button>
          </div>
        </header>

        <section className="hero">
          <div>
            <div className="hero-kicker"><Radar size={15} /> INTELLIGENCE FUSION ENGINE</div>
            <h2>Unified threat visibility.</h2>
            <p>Correlate synthetic security observations into prioritized incidents, investigations, and analyst-ready intelligence.</p>
          </div>
          <div className="hero-status">
            <span>THREAT POSTURE</span>
            <strong>GUARDED</strong>
            <small>Updated 09:14:32 UTC</small>
          </div>
        </section>

        <section className="metrics">
          {metrics.map(([label, value, change, Icon]) => (
            <article className="metric" key={label}>
              <div className="metric-top"><span>{label}</span><Icon size={16} /></div>
              <strong>{value}</strong>
              <small>{change} <span>vs previous window</span></small>
            </article>
          ))}
        </section>

        <section className="grid">
          <article className="panel alerts">
            <div className="panel-heading">
              <div><span className="section-label">PRIORITY QUEUE</span><h3>Active intelligence alerts</h3></div>
              <button className="text-button">View queue <ArrowUpRight size={14} /></button>
            </div>
            <div className="alert-list">
              {alerts.map((alert) => (
                <div className="alert-row" key={alert.id}>
                  <div className={`severity ${alert.severity.toLowerCase()}`}><AlertTriangle size={16} /></div>
                  <div className="alert-main">
                    <strong>{alert.title}</strong>
                    <span>{alert.id} · {alert.source}</span>
                  </div>
                  <div className="alert-time">{alert.time}</div>
                  <ChevronRight size={16} />
                </div>
              ))}
            </div>
          </article>

          <article className="panel posture">
            <div className="panel-heading"><div><span className="section-label">RISK ENGINE</span><h3>Current posture</h3></div></div>
            <div className="score-ring"><div><strong>72</strong><span>/100</span></div></div>
            <div className="posture-copy"><strong>Guarded</strong><span>Elevated activity requires analyst review.</span></div>
            <div className="bar"><i /></div>
            <div className="mini-stats"><span>Baseline <b>64</b></span><span>Peak <b>81</b></span></div>
          </article>

          <article className="panel activity-panel">
            <div className="panel-heading"><div><span className="section-label">EVENT STREAM</span><h3>Correlation activity</h3></div><span className="live-tag">● STREAMING</span></div>
            <div className="activity-chart">
              {[38, 51, 45, 68, 56, 74, 61, 83, 70, 91, 76, 87, 72, 95, 82, 90, 78, 88, 93, 81].map((height, i) => <i key={i} style={{ height: `${height}%` }} />)}
            </div>
            <div className="chart-labels"><span>-60m</span><span>-45m</span><span>-30m</span><span>-15m</span><span>NOW</span></div>
          </article>

          <article className="panel quick">
            <div className="panel-heading"><div><span className="section-label">ANALYST TOOLS</span><h3>Investigation shortcuts</h3></div></div>
            <button><Search /><span><b>New investigation</b><small>Start an analyst case</small></span><ChevronRight /></button>
            <button><Radar /><span><b>Explore intelligence</b><small>Search indicators and entities</small></span><ChevronRight /></button>
            <button><BrainCircuit /><span><b>Ask AI analyst</b><small>Analyze authorized evidence</small></span><ChevronRight /></button>
          </article>
        </section>

        <footer>
          <span>SENTINEL-X / DEFENSIVE RESEARCH PLATFORM</span>
          <span>DATA MODE: SYNTHETIC · BUILD 0.1.0</span>
        </footer>
      </main>
    </div>
  );
}

export default App;
