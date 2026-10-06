import { useEffect, useMemo, useState } from "react";
import {
  Activity, AlertTriangle, ArrowUpRight, BarChart3, BrainCircuit, ChevronRight,
  CircleDot, Database, Globe2, Layers3, LockKeyhole, Radar, Search, Shield, Siren,
  TerminalSquare, X
} from "lucide-react";

type Alert = { id:string; severity:string; title:string; source:string; status:string; score:number };
type Incident = { id:string; title:string; severity:string; status:string; score:number; technique_ids:string[]; indicator_ids:string[] };

const API = import.meta.env.VITE_API_URL || "http://localhost:8000";

const nav = [
  ["Command Center", TerminalSquare],
  ["Investigations", Search],
  ["Threat Intelligence", Radar],
  ["Entity Graph", Globe2],
  ["Incident Response", Siren],
  ["AI Analyst", BrainCircuit],
  ["Data Explorer", Database],
] as const;

function App() {
  const [section, setSection] = useState("Command Center");
  const [overview, setOverview] = useState<any>(null);
  const [alerts, setAlerts] = useState<Alert[]>([]);
  const [incidents, setIncidents] = useState<Incident[]>([]);
  const [query, setQuery] = useState("");
  const [searchResults, setSearchResults] = useState<any>(null);
  const [selectedIncident, setSelectedIncident] = useState<any>(null);
  const [apiOnline, setApiOnline] = useState(false);

  useEffect(() => {
    Promise.all([
      fetch(API + "/api/v1/system/overview").then(r => r.json()),
      fetch(API + "/api/v1/alerts").then(r => r.json()),
      fetch(API + "/api/v1/incidents").then(r => r.json()),
    ]).then(([o,a,i]) => {
      setOverview(o); setAlerts(a); setIncidents(i); setApiOnline(true);
    }).catch(() => setApiOnline(false));
  }, []);

  const runSearch = async () => {
    if (query.trim().length < 2) return;
    const data = await fetch(API + "/api/v1/search?q=" + encodeURIComponent(query)).then(r => r.json());
    setSearchResults(data);
    setSection("Data Explorer");
  };

  const posture = overview?.threat_posture ?? 72;
  const metrics = [
    ["ACTIVE CASES", overview?.active_cases ?? 24, "+4.8%", Activity],
    ["CORRELATED EVENTS", overview?.correlated_events ?? 1842, "+12.3%", Layers3],
    ["HIGH-RISK IOCs", overview?.high_risk_iocs ?? 2, "+7.1%", Radar],
    ["ANALYST QUEUE", overview?.analyst_queue ?? 3, "-3.2%", BarChart3],
  ] as const;

  const currentTitle = section === "Command Center" ? "Threat Operations" : section;
  const currentSubtitle = section === "Command Center"
    ? "Unified defensive intelligence operations"
    : "SENTINEL-X analyst workspace";

  return (
    <div className="shell">
      <aside className="sidebar">
        <div className="brand">
          <div className="brand-mark"><Shield size={21} /></div>
          <div><strong>SENTINEL-X</strong><span>CYBER INTELLIGENCE</span></div>
        </div>
        <div className="classification">PUBLIC RESEARCH BUILD <span>v0.2</span></div>
        <nav>
          {nav.map(([label, Icon]) => (
            <button className={section === label ? "nav-item active" : "nav-item"} key={label}
              onClick={() => setSection(label)}>
              <Icon size={17}/><span>{label}</span>{section === label && <ChevronRight size={14} className="nav-arrow"/>}
            </button>
          ))}
        </nav>
        <div className="sidebar-bottom">
          <div className="system-card">
            <div><CircleDot size={12}/> SYSTEM STATUS</div>
            <strong>{apiOnline ? "OPERATIONAL" : "OFFLINE / DEMO"}</strong>
            <span>{apiOnline ? "API and intelligence services reachable" : "Start Docker Compose to connect API"}</span>
          </div>
          <div className="user-chip"><div className="avatar">AN</div><div><strong>ANALYST-01</strong><span>Tier 2 Analyst</span></div></div>
        </div>
      </aside>

      <main>
        <header className="topbar">
          <div><div className="eyebrow">OPERATIONS / {currentSubtitle.toUpperCase()}</div><h1>{currentTitle}</h1></div>
          <div className="top-actions">
            <form className="global-search" onSubmit={e => {e.preventDefault(); runSearch();}}>
              <Search size={14}/><input value={query} onChange={e=>setQuery(e.target.value)} placeholder="Search intelligence..." />
            </form>
            <div className="live"><span/> {apiOnline ? "LIVE DATA" : "DEMO MODE"}</div>
            <button className="icon-button"><LockKeyhole size={17}/></button>
            <button className="profile">AN</button>
          </div>
        </header>

        {section === "Command Center" && (
          <>
            <section className="hero">
              <div><div className="hero-kicker"><Radar size={15}/> INTELLIGENCE FUSION ENGINE</div>
                <h2>Unified threat visibility.</h2>
                <p>Correlate defensive security observations into prioritized incidents, investigations, and analyst-ready intelligence.</p>
              </div>
              <div className="hero-status"><span>THREAT POSTURE</span><strong>{posture >= 80 ? "ELEVATED" : "GUARDED"}</strong><small>Score {posture}/100</small></div>
            </section>
            <section className="metrics">{metrics.map(([label,value,change,Icon]) =>
              <article className="metric" key={label}><div className="metric-top"><span>{label}</span><Icon size={16}/></div><strong>{value.toLocaleString()}</strong><small>{change} <span>vs previous window</span></small></article>
            )}</section>
            <section className="grid">
              <article className="panel alerts">
                <div className="panel-heading"><div><span className="section-label">PRIORITY QUEUE</span><h3>Active intelligence alerts</h3></div>
                  <button className="text-button" onClick={()=>setSection("Incident Response")}>View queue <ArrowUpRight size={14}/></button></div>
                <div className="alert-list">{alerts.map(a =>
                  <div className="alert-row" key={a.id} onClick={()=>setSelectedIncident(a)}>
                    <div className={`severity ${a.severity.toLowerCase()}`}><AlertTriangle size={16}/></div>
                    <div className="alert-main"><strong>{a.title}</strong><span>{a.id} · {a.source} · {a.status}</span></div>
                    <div className="alert-time">{a.score}/100</div><ChevronRight size={16}/>
                  </div>
                )}</div>
              </article>
              <article className="panel posture"><div className="panel-heading"><div><span className="section-label">RISK ENGINE</span><h3>Current posture</h3></div></div>
                <div className="score-ring" style={{background:`conic-gradient(#738e9e 0 ${posture}%, #1b252c ${posture}% )`}}><div><strong>{posture}</strong><span>/100</span></div></div>
                <div className="posture-copy"><strong>{posture >= 80 ? "Elevated" : "Guarded"}</strong><span>Risk score derived from active synthetic alerts.</span></div>
                <div className="bar"><i style={{width:`${posture}%`}}/></div>
                <div className="mini-stats"><span>Incidents <b>{incidents.length}</b></span><span>Open alerts <b>{overview?.open_alerts ?? 0}</b></span></div>
              </article>
              <article className="panel activity-panel"><div className="panel-heading"><div><span className="section-label">EVENT STREAM</span><h3>Correlation activity</h3></div><span className="live-tag">● STREAMING</span></div>
                <div className="activity-chart">{[38,51,45,68,56,74,61,83,70,91,76,87,72,95,82,90,78,88,93,81].map((h,i)=><i key={i} style={{height:`${h}%`}}/>)}</div>
                <div className="chart-labels"><span>-60m</span><span>-45m</span><span>-30m</span><span>-15m</span><span>NOW</span></div>
              </article>
              <article className="panel quick"><div className="panel-heading"><div><span className="section-label">ANALYST TOOLS</span><h3>Investigation shortcuts</h3></div></div>
                <button onClick={()=>setSection("Investigations")}><Search/><span><b>New investigation</b><small>Start an analyst case</small></span><ChevronRight/></button>
                <button onClick={()=>setSection("Threat Intelligence")}><Radar/><span><b>Explore intelligence</b><small>Search indicators and entities</small></span><ChevronRight/></button>
                <button onClick={()=>setSection("AI Analyst")}><BrainCircuit/><span><b>Ask AI analyst</b><small>Analyze authorized evidence</small></span><ChevronRight/></button>
              </article>
            </section>
          </>
        )}

        {section !== "Command Center" && (
          <section className="workspace">
            <div className="workspace-banner"><div><span className="section-label">ANALYST MODULE</span><h2>{section}</h2><p>Operational module connected to the SENTINEL-X defensive intelligence API.</p></div><div className="module-status">{apiOnline ? "API CONNECTED" : "DEMO MODE"}</div></div>
            {section === "Investigations" && <div className="module-grid">{incidents.map(i=><button className="module-card" key={i.id} onClick={()=>setSelectedIncident(i)}><span>{i.id}</span><strong>{i.title}</strong><small>{i.severity} · {i.status} · SCORE {i.score}</small><ChevronRight/></button>)}</div>}
            {section === "Incident Response" && <div className="module-grid">{alerts.map(a=><button className="module-card" key={a.id} onClick={()=>setSelectedIncident(a)}><span>{a.id}</span><strong>{a.title}</strong><small>{a.severity} · {a.status} · {a.source}</small><ChevronRight/></button>)}</div>}
            {section === "Threat Intelligence" && <div className="intel-table"><div className="table-head"><span>ID</span><span>TYPE</span><span>VALUE</span><span>CONFIDENCE</span><span>SEVERITY</span></div>{["IOC-0001","IOC-0002","IOC-0003","IOC-0004"].map((id,i)=><div className="table-row" key={id}><span>{id}</span><span>{["IPv4","Domain","SHA-256","URL"][i]}</span><span>{["198.51.100.42","telemetry-lab.example","000000…000000","demo.invalid/resource"][i]}</span><span>{[94,81,73,66][i]}%</span><span>{["CRITICAL","HIGH","MEDIUM","MEDIUM"][i]}</span></div>)}</div>}
            {section === "Entity Graph" && <div className="graph-stage"><div className="graph-node center">INC-2026-0042</div><div className="graph-node n1">IOC-0001</div><div className="graph-node n2">T1110</div><div className="graph-node n3">T1078</div><div className="graph-node n4">AUTH-GATEWAY</div><div className="graph-line l1"/><div className="graph-line l2"/><div className="graph-line l3"/><div className="graph-line l4"/><p>Relationship visualization uses synthetic entities. Production graph analytics will be added in the next release.</p></div>}
            {section === "AI Analyst" && <div className="ai-panel"><BrainCircuit size={32}/><h3>Analyst Copilot</h3><p>Advisory analysis layer. Future responses will be grounded in case evidence, source provenance, confidence, and ATT&CK mappings.</p><div className="ai-prompt">Ask: “Summarize the evidence in INC-2026-0042.”</div><div className="ai-disclaimer">AI OUTPUT IS ADVISORY · VERIFY AGAINST SOURCE EVIDENCE</div></div>}
            {section === "Data Explorer" && <div>{searchResults ? <div className="module-grid">{[...searchResults.alerts,...searchResults.incidents,...searchResults.indicators].map((x:any,i)=><div className="module-card static" key={i}><span>{x.id}</span><strong>{x.title || x.value}</strong><small>{x.severity || x.indicator_type} · confidence {x.confidence ?? x.score ?? "n/a"}</small></div>)}</div> : <div className="empty-state"><Search size={30}/><h3>Search intelligence</h3><p>Use the search field above to query synthetic indicators, alerts, and incidents.</p></div>}</div>}
          </section>
        )}

        <footer><span>SENTINEL-X / DEFENSIVE RESEARCH PLATFORM</span><span>DATA MODE: SYNTHETIC · BUILD 0.2.0</span></footer>
      </main>

      {selectedIncident && <div className="modal-backdrop" onClick={()=>setSelectedIncident(null)}><div className="modal" onClick={e=>e.stopPropagation()}>
        <button className="modal-close" onClick={()=>setSelectedIncident(null)}><X/></button>
        <span className="section-label">CASE DETAIL</span><h2>{selectedIncident.id}</h2><h3>{selectedIncident.title}</h3>
        <div className="modal-grid"><div><span>SEVERITY</span><b>{selectedIncident.severity}</b></div><div><span>STATUS</span><b>{selectedIncident.status}</b></div><div><span>SCORE</span><b>{selectedIncident.score}/100</b></div><div><span>SOURCE</span><b>{selectedIncident.source || "CORRELATION ENGINE"}</b></div></div>
        <p>This case is part of the synthetic defensive dataset. Detailed evidence, timeline, ATT&CK mappings, analyst notes, and audit history will be attached as the case-management layer expands.</p>
      </div></div>}
    </div>
  );
}
export default App;
