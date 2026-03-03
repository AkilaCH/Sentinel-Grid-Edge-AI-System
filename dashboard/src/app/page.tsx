"use client";
import { useEffect, useState } from 'react';

interface Alert {
  timestamp: string;
  status: string;
  error_score: string;
  node_id: string;
  location: string;
}

export default function Dashboard() {
  const [alerts, setAlerts] = useState<Alert[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchAlerts = async () => {
      try {
        const res = await fetch('/api/alerts');
        const data = await res.json();
        setAlerts(data.reverse());
        setLoading(false);
      } catch (err) {
        console.error("Dashboard Sync Failed", err);
      }
    };

    fetchAlerts();
    const interval = setInterval(fetchAlerts, 3000);
    return () => clearInterval(interval);
  }, []);

  const latestStatus = alerts[0]?.status || "INITIALIZING";

  return (
    <main className="min-h-screen bg-slate-950 text-slate-100 p-8 font-mono">
      <div className="flex justify-between items-center border-b border-slate-800 pb-6 mb-8">
        <div>
          <h1 className="text-3xl font-bold tracking-tighter text-blue-500">SENTINEL-GRID</h1>
          <p className="text-slate-500 text-sm">Acoustic Anomaly Detection System | Edge-Node: Active</p>
        </div>
        <div className={`px-6 py-2 rounded-full border-2 font-bold animate-pulse ${latestStatus === 'ANOMALY' ? 'border-red-600 text-red-500 bg-red-950/30' : 'border-emerald-600 text-emerald-500 bg-emerald-950/30'
          }`}>
          SYSTEM STATUS: {latestStatus}
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="md:col-span-2 bg-slate-900/50 border border-slate-800 rounded-xl p-6">
          <h2 className="text-xl mb-4 flex items-center gap-2">
            <span className="w-3 h-3 bg-blue-500 rounded-full animate-ping"></span>
            LIVE INTELLIGENCE FEED
          </h2>
          <div className="space-y-4 max-h-[500px] overflow-y-auto pr-2 custom-scrollbar">
            {loading ? <p>Scanning Network...</p> : alerts.map((alert, i) => (
              <div key={i} className={`p-4 rounded-lg border-l-4 ${alert.status === 'ANOMALY' ? 'bg-red-950/20 border-red-600' : 'bg-slate-800/40 border-slate-600'
                }`}>
                <div className="flex justify-between items-start">
                  <div>
                    <span className="text-xs text-slate-500">{alert.timestamp}</span>
                    <h3 className={`font-bold ${alert.status === 'ANOMALY' ? 'text-red-400' : 'text-slate-200'}`}>
                      {alert.status === 'ANOMALY' ? '⚠️ ACOUSTIC ANOMALY DETECTED' : '✅ BASELINE MAINTAINED'}
                    </h3>
                  </div>
                  <span className="text-xs bg-slate-700 px-2 py-1 rounded">Score: {alert.error_score}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
        <div className="space-y-6">
          <div className="bg-slate-900/50 border border-slate-800 rounded-xl p-6">
            <h2 className="text-lg mb-4 text-slate-400">NODE INFORMATION</h2>
            <div className="space-y-2 text-sm">
              <p><span className="text-slate-500">ID:</span> EDGE-NODE-01</p>
              <p><span className="text-slate-500">LOCATION:</span> SWEDEN FACTORY - FLOOR 01</p>
              <p><span className="text-slate-500">AI MODEL:</span> AUTOENCODER-V1</p>
              <p><span className="text-slate-500">THRESHOLD:</span> 0.02</p>
            </div>
          </div>
        </div>

      </div>
    </main>
  );
}