import http.server
import socketserver
import json
import os
import sys
from datetime import datetime

# Add root folder to path to allow importing erp modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from erp.core.auth import auth_service
from erp.core.db import db_instance
from erp.core.logger import audit_log
from erp.modules.financial_reporting.category_reporting import CategoryReporter

PORT = 8000

HTML_DASHBOARD = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AuraLedger BI & Category Analytics Dashboard</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Chart.js CDN -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        .custom-scrollbar::-webkit-scrollbar { width: 6px; height: 6px; }
        .custom-scrollbar::-webkit-scrollbar-track { background: #f1f1f1; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
    </style>
</head>
<body class="bg-slate-50 text-slate-800 font-sans min-h-screen flex flex-col">

    <!-- Header Banner -->
    <header class="bg-gradient-to-r from-blue-900 via-indigo-900 to-slate-900 text-white shadow-md">
        <div class="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8 flex justify-between items-center">
            <div class="flex items-center space-x-3">
                <div class="bg-blue-600 p-2 rounded-lg text-white font-bold text-xl tracking-wider">AL</div>
                <div>
                    <h1 class="text-xl font-bold tracking-tight">AuraLedger BI Suite</h1>
                    <p class="text-xs text-blue-300 font-medium">Enterprise Category & Subcategory Reporting</p>
                </div>
            </div>
            <div class="flex items-center space-x-4">
                <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500 text-white shadow-sm">
                    SYSTEM READY (66K LOC)
                </span>
                <span class="text-slate-400 text-xs hidden sm:inline">User: admin (Controller)</span>
            </div>
        </div>
    </header>

    <!-- Main Container -->
    <main class="flex-grow max-w-7xl mx-auto w-full px-4 sm:px-6 lg:px-8 py-6 space-y-6">

        <!-- Top Metrics Row -->
        <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
            <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm flex flex-col justify-between">
                <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Total Assets</span>
                <h3 class="text-2xl font-bold text-slate-800 mt-2" id="kpi-assets">$0.00</h3>
                <span class="text-xs text-emerald-600 mt-1 font-medium">Real-time GL Rollup</span>
            </div>
            <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm flex flex-col justify-between">
                <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Total Liabilities</span>
                <h3 class="text-2xl font-bold text-slate-800 mt-2" id="kpi-liabilities">$0.00</h3>
                <span class="text-xs text-rose-500 mt-1 font-medium">Outstanding Balances</span>
            </div>
            <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm flex flex-col justify-between">
                <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Net Worth (Equity)</span>
                <h3 class="text-2xl font-bold text-slate-800 mt-2" id="kpi-networth">$0.00</h3>
                <span class="text-xs text-indigo-600 mt-1 font-medium">Assets minus Liabilities</span>
            </div>
            <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm flex flex-col justify-between">
                <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Audit logs count</span>
                <h3 class="text-2xl font-bold text-slate-800 mt-2" id="kpi-logs-count">0</h3>
                <span class="text-xs text-slate-500 mt-1 font-medium">Compliance entries recorded</span>
            </div>
        </div>

        <!-- Dashboard Layout Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">

            <!-- Left Panel: Transaction Simulator & Audit Logs -->
            <div class="space-y-6 lg:col-span-1">
                
                <!-- Transaction Simulator -->
                <div class="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
                    <div class="bg-slate-50 px-4 py-3 border-b border-slate-200 flex justify-between items-center">
                        <h2 class="font-bold text-slate-700 text-sm uppercase tracking-wider">Transaction Simulator</h2>
                        <span class="text-xs text-blue-600 font-semibold">ACID Sandbox</span>
                    </div>
                    <div class="p-4 space-y-3">
                        <p class="text-xs text-slate-500">Inject transactions to immediately see category-based aggregations update.</p>
                        <div class="space-y-2">
                            <button onclick="postSimulatedTx('aws')" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-3 rounded-lg text-xs transition duration-150 flex justify-between">
                                <span>Inject AWS Hosting Invoice</span>
                                <span class="font-mono bg-blue-800 px-1.5 rounded">$18,200.00</span>
                            </button>
                            <button onclick="postSimulatedTx('saas_rev')" class="w-full bg-emerald-600 hover:bg-emerald-700 text-white font-semibold py-2 px-3 rounded-lg text-xs transition duration-150 flex justify-between">
                                <span>Receive SaaS Subscriptions</span>
                                <span class="font-mono bg-emerald-800 px-1.5 rounded">$45,000.00</span>
                            </button>
                            <button onclick="postSimulatedTx('machinery')" class="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-2 px-3 rounded-lg text-xs transition duration-150 flex justify-between">
                                <span>Purchase Equipment (CAPEX)</span>
                                <span class="font-mono bg-indigo-800 px-1.5 rounded">$15,000.00</span>
                            </button>
                            <button onclick="postSimulatedTx('salaries')" class="w-full bg-slate-700 hover:bg-slate-800 text-white font-semibold py-2 px-3 rounded-lg text-xs transition duration-150 flex justify-between">
                                <span>Post Engineering Salaries</span>
                                <span class="font-mono bg-slate-900 px-1.5 rounded">$145,000.00</span>
                            </button>
                        </div>
                        <div id="tx-success-alert" class="hidden mt-3 p-2 bg-emerald-50 border border-emerald-200 text-emerald-800 text-xs rounded-lg flex items-center space-x-2">
                            <span class="font-bold">✔</span>
                            <span id="tx-success-msg">Transaction posted successfully.</span>
                        </div>
                    </div>
                </div>

                <!-- Recent Compliance Audit Logs -->
                <div class="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden flex flex-col h-[340px]">
                    <div class="bg-slate-50 px-4 py-3 border-b border-slate-200 flex justify-between items-center">
                        <h2 class="font-bold text-slate-700 text-sm uppercase tracking-wider">Compliance Audit Trail</h2>
                        <button onclick="loadLogs()" class="text-xs text-blue-600 font-semibold hover:underline">Refresh</button>
                    </div>
                    <div class="p-3 bg-slate-900 text-slate-300 font-mono text-[10px] flex-grow overflow-y-auto custom-scrollbar" id="logs-view">
                        Loading logs...
                    </div>
                </div>
            </div>

            <!-- Right Panel: BI Category Reporting Engine -->
            <div class="lg:col-span-2 space-y-6">

                <!-- Navigation Tabs -->
                <div class="bg-white p-2 rounded-xl border border-slate-200 shadow-sm flex space-x-2">
                    <button id="tab-gl" onclick="switchTab('gl')" class="flex-1 py-2 px-4 text-xs font-bold rounded-lg transition duration-150 bg-blue-600 text-white shadow-sm">
                        General Ledger Categories
                    </button>
                    <button id="tab-assets" onclick="switchTab('assets')" class="flex-1 py-2 px-4 text-xs font-bold rounded-lg transition duration-150 text-slate-600 hover:bg-slate-100">
                        Fixed Asset Depreciation
                    </button>
                    <button id="tab-vendors" onclick="switchTab('vendors')" class="flex-1 py-2 px-4 text-xs font-bold rounded-lg transition duration-150 text-slate-600 hover:bg-slate-100">
                        Vendor Spend Analysis
                    </button>
                </div>

                <!-- Tab 1: General Ledger Categories -->
                <div id="panel-gl" class="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
                    <div class="p-4 border-b border-slate-200 flex flex-col sm:flex-row justify-between items-start sm:items-center space-y-2 sm:space-y-0">
                        <div>
                            <h2 class="font-bold text-slate-800 text-base">Hierarchical Balance Sheet Aggregates</h2>
                            <p class="text-xs text-slate-500">Rollups structured by Account Category -> Subcategory -> Accounts.</p>
                        </div>
                        <div class="flex space-x-2">
                            <button onclick="downloadReport('gl', 'json')" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold py-1.5 px-3 rounded-lg text-xs border border-slate-200">
                                JSON
                            </button>
                            <button onclick="downloadReport('gl', 'csv')" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold py-1.5 px-3 rounded-lg text-xs border border-slate-200">
                                CSV
                            </button>
                        </div>
                    </div>
                    <div class="p-4 overflow-x-auto custom-scrollbar">
                        <div id="gl-tree-container" class="space-y-4 text-sm">
                            <!-- Populated dynamically -->
                        </div>
                    </div>
                </div>

                <!-- Tab 2: Fixed Assets Depreciation -->
                <div id="panel-assets" class="hidden bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
                    <div class="p-4 border-b border-slate-200 flex justify-between items-center">
                        <div>
                            <h2 class="font-bold text-slate-800 text-base">Capital Assets Grouping & Depreciation Ledger</h2>
                            <p class="text-xs text-slate-500">Fixed assets grouped by asset categories and subcategories.</p>
                        </div>
                        <div class="flex space-x-2">
                            <button onclick="downloadReport('fixed_assets', 'json')" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold py-1.5 px-3 rounded-lg text-xs border border-slate-200">
                                JSON
                            </button>
                            <button onclick="downloadReport('fixed_assets', 'csv')" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold py-1.5 px-3 rounded-lg text-xs border border-slate-200">
                                CSV
                            </button>
                        </div>
                    </div>
                    <div class="p-4 overflow-x-auto custom-scrollbar">
                        <div id="assets-container" class="space-y-6">
                            <!-- Populated dynamically -->
                        </div>
                    </div>
                </div>

                <!-- Tab 3: Vendor Spend -->
                <div id="panel-vendors" class="hidden bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
                    <div class="p-4 border-b border-slate-200 flex justify-between items-center">
                        <div>
                            <h2 class="font-bold text-slate-800 text-base">Vendor Spend Classification</h2>
                            <p class="text-xs text-slate-500">Historical purchasing patterns categorized by trade classifications.</p>
                        </div>
                        <div class="flex space-x-2">
                            <button onclick="downloadReport('vendors', 'json')" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold py-1.5 px-3 rounded-lg text-xs border border-slate-200">
                                JSON
                            </button>
                            <button onclick="downloadReport('vendors', 'csv')" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold py-1.5 px-3 rounded-lg text-xs border border-slate-200">
                                CSV
                            </button>
                        </div>
                    </div>
                    <div class="p-4 grid grid-cols-1 md:grid-cols-5 gap-6">
                        <!-- Chart container -->
                        <div class="md:col-span-2 flex flex-col items-center justify-center border-r border-slate-200 pr-0 md:pr-4">
                            <h4 class="text-xs font-bold text-slate-500 mb-2 uppercase tracking-wide">Category Distribution</h4>
                            <div class="w-full max-w-[200px] h-[200px]">
                                <canvas id="vendorSpendChart"></canvas>
                            </div>
                        </div>
                        <!-- List container -->
                        <div class="md:col-span-3 space-y-4" id="vendors-container">
                            <!-- Populated dynamically -->
                        </div>
                    </div>
                </div>

            </div>
        </div>

    </main>

    <!-- Footer -->
    <footer class="bg-slate-950 text-slate-500 py-6 border-t border-slate-900 mt-12">
        <div class="max-w-7xl mx-auto px-4 text-center text-xs space-y-2">
            <p>AuraLedger Double-Entry Simulation Suite is completely compliant with Python 3.12 specifications.</p>
            <p>&copy; 2026 AuraLedger Corp. All rights reserved.</p>
        </div>
    </footer>

    <!-- Interactive Scripting -->
    <script>
        let vendorChartInstance = null;

        // Init loads
        document.addEventListener('DOMContentLoaded', () => {
            loadLogs();
            loadAllReports();
            setInterval(loadLogs, 8000);
        });

        function switchTab(tabName) {
            const tabs = ['gl', 'assets', 'vendors'];
            tabs.forEach(t => {
                const btn = document.getElementById(`tab-${t}`);
                const panel = document.getElementById(`panel-${t}`);
                if (t === tabName) {
                    btn.className = "flex-1 py-2 px-4 text-xs font-bold rounded-lg transition duration-150 bg-blue-600 text-white shadow-sm";
                    panel.classList.remove('hidden');
                } else {
                    btn.className = "flex-1 py-2 px-4 text-xs font-bold rounded-lg transition duration-150 text-slate-600 hover:bg-slate-100";
                    panel.classList.add('hidden');
                }
            });
            if (tabName === 'vendors') {
                setTimeout(initVendorChart, 150);
            }
        }

        function loadLogs() {
            fetch('/api/logs')
                .then(r => r.json())
                .then(data => {
                    const logsView = document.getElementById('logs-view');
                    logsView.textContent = data.logs.join('\\n');
                    logsView.scrollTop = logsView.scrollHeight;
                    document.getElementById('kpi-logs-count').textContent = data.logs.length;
                });
        }

        function loadAllReports() {
            // Load GL
            fetch('/api/reports/category')
                .then(r => r.json())
                .then(data => {
                    if(data.status === 'success') {
                        renderGLTree(data.data);
                        
                        // Update KPIs
                        const bs = data.data.balance_sheet_summary;
                        document.getElementById('kpi-assets').textContent = formatCurrency(bs.total_assets);
                        document.getElementById('kpi-liabilities').textContent = formatCurrency(bs.total_liabilities);
                        document.getElementById('kpi-networth').textContent = formatCurrency(bs.net_worth);
                    }
                });

            // Load Fixed Assets
            fetch('/api/reports/fixed_assets')
                .then(r => r.json())
                .then(data => {
                    if(data.status === 'success') {
                        renderFixedAssets(data.data.hierarchical_data);
                    }
                });

            // Load Vendors
            fetch('/api/reports/vendors')
                .then(r => r.json())
                .then(data => {
                    if(data.status === 'success') {
                        renderVendors(data.data.hierarchical_data);
                        if (document.getElementById('panel-vendors').classList.contains('hidden') === false) {
                            initVendorChart();
                        }
                    }
                });
        }

        function postSimulatedTx(txType) {
            const alertBox = document.getElementById('tx-success-alert');
            const alertMsg = document.getElementById('tx-success-msg');
            alertBox.classList.add('hidden');

            fetch('/api/trigger', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ type: txType })
            })
            .then(r => r.json())
            .then(data => {
                if (data.status === 'success') {
                    alertMsg.textContent = `Posted! Debit: ${data.data.debit_account}, Amount: $${data.data.amount.toLocaleString()}`;
                    alertBox.classList.remove('hidden');
                    alertBox.className = "mt-3 p-2 bg-emerald-50 border border-emerald-200 text-emerald-800 text-xs rounded-lg flex items-center space-x-2";
                    
                    // Refresh data
                    loadAllReports();
                    loadLogs();
                } else {
                    alertMsg.textContent = `Error: ${data.message}`;
                    alertBox.classList.remove('hidden');
                    alertBox.className = "mt-3 p-2 bg-rose-50 border border-rose-200 text-rose-800 text-xs rounded-lg flex items-center space-x-2";
                }
            });
        }

        function renderGLTree(report) {
            const container = document.getElementById('gl-tree-container');
            container.innerHTML = '';
            
            const hData = report.hierarchical_data;
            for (const [cat, info] of Object.entries(hData)) {
                const catCard = document.createElement('div');
                catCard.className = "border border-slate-200 rounded-lg overflow-hidden";
                
                const catHeader = `
                    <div class="bg-slate-50 px-4 py-3 flex justify-between items-center font-bold text-slate-700 cursor-pointer hover:bg-slate-100 select-none" onclick="toggleAccordion('gl-child-${cat}')">
                        <div class="flex items-center space-x-2">
                            <span>📁</span>
                            <span>${cat}</span>
                            <span class="text-xs font-normal text-slate-400">(${info.description})</span>
                        </div>
                        <span class="font-mono text-blue-700">${formatCurrency(info.total)}</span>
                    </div>
                `;
                
                let subcatRows = '';
                for (const [subcat, subinfo] of Object.entries(info.subcategories)) {
                    let accRows = '';
                    subinfo.accounts.forEach(acc => {
                        accRows += `
                            <div class="flex justify-between items-center py-1.5 pl-8 pr-4 text-xs hover:bg-slate-50 border-b border-slate-100 last:border-0 font-medium">
                                <span class="text-slate-500 font-mono">[${acc.account_number}] ${acc.name}</span>
                                <span class="font-mono text-slate-700">${formatCurrency(acc.balance)}</span>
                            </div>
                        `;
                    });
                    
                    subcatRows += `
                        <div class="border-b border-slate-200 last:border-0">
                            <div class="bg-slate-50/50 px-4 py-2 flex justify-between items-center text-xs font-bold text-slate-600">
                                <span>📂 ${subcat}</span>
                                <span class="font-mono text-slate-700">${formatCurrency(subinfo.total)}</span>
                            </div>
                            <div class="divide-y divide-slate-100 bg-white">
                                ${accRows}
                            </div>
                        </div>
                    `;
                }
                
                catCard.innerHTML = `
                    ${catHeader}
                    <div id="gl-child-${cat}" class="transition-all duration-200">
                        ${subcatRows}
                    </div>
                `;
                container.appendChild(catCard);
            }
        }

        function renderFixedAssets(assetsData) {
            const container = document.getElementById('assets-container');
            container.innerHTML = '';

            for (const [cat, info] of Object.entries(assetsData)) {
                const catSection = document.createElement('div');
                catSection.className = "space-y-3";

                let rows = '';
                for (const [subcat, subinfo] of Object.entries(info.subcategories)) {
                    subinfo.assets.forEach(asset => {
                        // Calculate percentage depreciated
                        const pctDepr = asset.purchase_value > 0 ? (asset.accumulated_depreciation / asset.purchase_value) * 100 : 0;
                        rows += `
                            <tr class="hover:bg-slate-50 text-xs text-slate-700">
                                <td class="px-4 py-3 font-mono font-bold">${asset.code}</td>
                                <td class="px-4 py-3 font-medium text-slate-900">${asset.name}</td>
                                <td class="px-4 py-3 text-slate-400">${subcat}</td>
                                <td class="px-4 py-3 text-right font-mono">${formatCurrency(asset.purchase_value)}</td>
                                <td class="px-4 py-3 text-right font-mono text-slate-400">${formatCurrency(asset.accumulated_depreciation)}</td>
                                <td class="px-4 py-3 text-right font-mono font-bold text-slate-800">${formatCurrency(asset.net_book_value)}</td>
                                <td class="px-4 py-3 w-[150px]">
                                    <div class="w-full bg-slate-100 rounded-full h-1.5">
                                        <div class="bg-blue-600 h-1.5 rounded-full" style="width: ${pctDepr}%"></div>
                                    </div>
                                    <div class="text-[9px] text-right text-slate-400 mt-1 font-semibold">${pctDepr.toFixed(0)}% Depr.</div>
                                </td>
                            </tr>
                        `;
                    });
                }

                catSection.innerHTML = `
                    <div class="flex justify-between items-center bg-slate-100/80 px-4 py-2 rounded-lg">
                        <span class="text-xs font-bold text-slate-700">📁 Category: ${cat}</span>
                        <div class="text-xs space-x-3 text-slate-500 font-semibold">
                            <span>Cost: <strong class="text-slate-800">${formatCurrency(info.total_purchase_value)}</strong></span>
                            <span>Net Book: <strong class="text-slate-800">${formatCurrency(info.total_net_book_value)}</strong></span>
                        </div>
                    </div>
                    <table class="min-w-full divide-y divide-slate-200 border border-slate-200 rounded-lg overflow-hidden">
                        <thead class="bg-slate-50 text-slate-500 uppercase tracking-wider text-[10px] font-bold">
                            <tr>
                                <th class="px-4 py-2 text-left">Code</th>
                                <th class="px-4 py-2 text-left">Asset</th>
                                <th class="px-4 py-2 text-left">Subcategory</th>
                                <th class="px-4 py-2 text-right">Cost</th>
                                <th class="px-4 py-2 text-right">Accum Depr</th>
                                <th class="px-4 py-2 text-right">Net Book Value</th>
                                <th class="px-4 py-2 text-left">Depr Status</th>
                            </tr>
                        </thead>
                        <tbody class="bg-white divide-y divide-slate-200">
                            ${rows}
                        </tbody>
                    </table>
                `;
                container.appendChild(catSection);
            }
        }

        function renderVendors(vendorData) {
            const container = document.getElementById('vendors-container');
            container.innerHTML = '';

            for (const [cat, info] of Object.entries(vendorData)) {
                const catHeader = `
                    <div class="flex justify-between items-center py-1.5 border-b border-slate-200 font-bold text-slate-700 text-xs">
                        <span>📁 Category: ${cat}</span>
                        <span class="font-mono text-blue-700">Spend: ${formatCurrency(info.total_spend)}</span>
                    </div>
                `;

                let vendorLines = '';
                for (const [subcat, subinfo] of Object.entries(info.subcategories)) {
                    subinfo.vendors.forEach(v => {
                        vendorLines += `
                            <div class="flex justify-between items-center py-2 pl-4 text-xs text-slate-600 border-b border-slate-100 last:border-0">
                                <div>
                                    <div class="font-bold text-slate-800">${v.name}</div>
                                    <div class="text-[10px] text-slate-400 font-medium">Terms: ${v.terms} | Subcat: ${subcat}</div>
                                </div>
                                <div class="text-right font-mono">
                                    <div class="font-bold text-slate-800">${formatCurrency(v.simulated_spend)}</div>
                                    <div class="text-[10px] text-slate-400">Current Owed: ${formatCurrency(v.current_outstanding)}</div>
                                </div>
                            </div>
                        `;
                    });
                }

                const catDiv = document.createElement('div');
                catDiv.className = "bg-white p-3 rounded-lg border border-slate-200 shadow-sm space-y-2";
                catDiv.innerHTML = `
                    ${catHeader}
                    <div class="divide-y divide-slate-100">
                        ${vendorLines}
                    </div>
                `;
                container.appendChild(catDiv);
            }
        }

        function initVendorChart() {
            fetch('/api/reports/vendors')
                .then(r => r.json())
                .then(data => {
                    if (data.status !== 'success') return;
                    
                    const labels = [];
                    const spends = [];
                    
                    for (const [cat, info] of Object.entries(data.data.hierarchical_data)) {
                        labels.push(cat);
                        spends.push(info.total_spend);
                    }
                    
                    const ctx = document.getElementById('vendorSpendChart').getContext('2d');
                    
                    if(vendorChartInstance) {
                        vendorChartInstance.destroy();
                    }
                    
                    vendorChartInstance = new Chart(ctx, {
                        type: 'doughnut',
                        data: {
                            labels: labels,
                            datasets: [{
                                data: spends,
                                backgroundColor: ['#2563eb', '#10b981', '#f59e0b', '#ec4899', '#6366f1'],
                                borderWidth: 1
                            }]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            plugins: {
                                legend: {
                                    display: false
                                }
                            }
                        }
                    });
                });
        }

        function toggleAccordion(id) {
            const element = document.getElementById(id);
            element.classList.toggle('hidden');
        }

        function formatCurrency(val) {
            return '$' + parseFloat(val).toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
        }

        function downloadReport(type, format) {
            window.open(`/api/reports/export?type=${type}&format=${format}`, '_blank');
        }
    </script>
</body>
</html>
"""

class AuraLedgerHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Suppress command line log clutter
        pass

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(HTML_DASHBOARD.encode('utf-8'))
            
        elif self.path == '/api/logs':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            
            log_lines = []
            log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'auraledger_audit.log')
            if os.path.exists(log_path):
                try:
                    with open(log_path, 'r', encoding='utf-8') as f:
                        log_lines = f.readlines()[-30:] # Fetch last 30 logs for complexity
                except Exception:
                    log_lines = ["Error reading audit log file."]
            else:
                log_lines = ["No transactions recorded. Trigger simulated entries on the left panel."]
                
            response = {"logs": [line.strip() for line in log_lines]}
            self.wfile.write(json.dumps(response).encode('utf-8'))
            
        elif self.path == '/api/reports/category':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            try:
                reporter = CategoryReporter()
                report = reporter.generate_gl_category_report()
                formatted = reporter.format_ascii_tree(report)
                response = {"status": "success", "data": report, "formatted": formatted}
            except Exception as e:
                response = {"status": "error", "message": str(e)}
            self.wfile.write(json.dumps(response).encode('utf-8'))
            
        elif self.path == '/api/reports/fixed_assets':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            try:
                reporter = CategoryReporter()
                report = reporter.generate_fixed_assets_category_report()
                response = {"status": "success", "data": report}
            except Exception as e:
                response = {"status": "error", "message": str(e)}
            self.wfile.write(json.dumps(response).encode('utf-8'))
            
        elif self.path == '/api/reports/vendors':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            try:
                reporter = CategoryReporter()
                report = reporter.generate_vendor_spend_category_report()
                response = {"status": "success", "data": report}
            except Exception as e:
                response = {"status": "error", "message": str(e)}
            self.wfile.write(json.dumps(response).encode('utf-8'))
            
        elif self.path.startswith('/api/reports/export'):
            # Parse query params
            from urllib.parse import urlparse, parse_qs
            parsed = urlparse(self.path)
            queries = parse_qs(parsed.query)
            rep_type = queries.get('type', ['gl'])[0]
            rep_format = queries.get('format', ['csv'])[0]
            
            reporter = CategoryReporter()
            if rep_type == 'gl':
                report = reporter.generate_gl_category_report()
            elif rep_type == 'fixed_assets':
                report = reporter.generate_fixed_assets_category_report()
            else:
                report = reporter.generate_vendor_spend_category_report()
                
            self.send_response(200)
            
            if rep_format == 'csv':
                self.send_header('Content-Type', 'text/csv')
                self.send_header('Content-Disposition', f'attachment; filename={rep_type}_category_report.csv')
                self.end_headers()
                csv_data = reporter.export_report_to_csv(rep_type, report)
                self.wfile.write(csv_data.encode('utf-8'))
            else:
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Disposition', f'attachment; filename={rep_type}_category_report.json')
                self.end_headers()
                self.wfile.write(json.dumps(report, indent=2).encode('utf-8'))
        else:
            self.send_error(404, "File not found")

    def do_POST(self):
        if self.path == '/api/trigger':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode('utf-8')
            
            try:
                payload = json.loads(post_data) if post_data else {}
                tx_type = payload.get('type', 'aws')
                
                # Execute transaction simulator directly into the db_instance tables!
                token = auth_service.authenticate("admin")
                
                if tx_type == 'aws':
                    # AWS invoice posting: Debit Hosting Cost (Expense), Credit Accounts Payable (Liability)
                    aws_cost = 18200.00
                    # Load Aws AWS account & AP account
                    gl_accounts = db_instance.query("general_ledger_account")
                    aws_acc = next((a for a in gl_accounts if a['account_number'] == '5010'), None)
                    ap_acc = next((a for a in gl_accounts if a['account_number'] == '2010'), None)
                    
                    if aws_acc and ap_acc:
                        db_instance.begin()
                        aws_acc['balance'] = float(aws_acc['balance']) + aws_cost
                        ap_acc['balance'] = float(ap_acc['balance']) + aws_cost
                        db_instance.update("general_ledger_account", '5010', aws_acc)
                        db_instance.update("general_ledger_account", '2010', ap_acc)
                        db_instance.commit()
                        
                        audit_log("general_ledger", f"POST: AWS Invoice #INV-AWS-827 - Debited AWS Hosting Cost (5010) and Credited Accounts Payable (2010) for ${aws_cost:,.2f}", "INFO")
                        
                        response = {
                            "status": "success",
                            "data": {
                                "debit_account": "[5010] AWS Hosting Costs",
                                "credit_account": "[2010] Trade Accounts Payable",
                                "amount": aws_cost
                            }
                        }
                    else:
                        raise Exception("Required accounts for AWS Invoice transaction not found.")
                        
                elif tx_type == 'saas_rev':
                    # SaaS subscription receipt: Debit Operating Account (Asset), Credit Software Revenue (Revenue)
                    rev_amount = 45000.00
                    gl_accounts = db_instance.query("general_ledger_account")
                    cash_acc = next((a for a in gl_accounts if a['account_number'] == '1020'), None)
                    rev_acc = next((a for a in gl_accounts if a['account_number'] == '4010'), None)
                    
                    if cash_acc and rev_acc:
                        db_instance.begin()
                        cash_acc['balance'] = float(cash_acc['balance']) + rev_amount
                        rev_acc['balance'] = float(rev_acc['balance']) + rev_amount
                        db_instance.update("general_ledger_account", '1020', cash_acc)
                        db_instance.update("general_ledger_account", '4010', rev_acc)
                        db_instance.commit()
                        
                        audit_log("general_ledger", f"POST: SaaS Subscriptions billing collection batch - Debited Operating cash (1020) and Credited SaaS Revenue (4010) for ${rev_amount:,.2f}", "INFO")
                        
                        response = {
                            "status": "success",
                            "data": {
                                "debit_account": "[1020] Chase Operating Account",
                                "credit_account": "[4010] Software SaaS Subscriptions",
                                "amount": rev_amount
                            }
                        }
                    else:
                        raise Exception("Required accounts for SaaS Subscription revenue not found.")
                        
                elif tx_type == 'machinery':
                    # Purchase computer server equipment: Debit Fixed Assets (Asset), Credit Cash (Asset)
                    cost = 15000.00
                    gl_accounts = db_instance.query("general_ledger_account")
                    fa_acc = next((a for a in gl_accounts if a['account_number'] == '1600'), None)
                    cash_acc = next((a for a in gl_accounts if a['account_number'] == '1020'), None)
                    
                    if fa_acc and cash_acc:
                        db_instance.begin()
                        fa_acc['balance'] = float(fa_acc['balance']) + cost
                        cash_acc['balance'] = float(cash_acc['balance']) - cost
                        db_instance.update("general_ledger_account", '1600', fa_acc)
                        db_instance.update("general_ledger_account", '1020', cash_acc)
                        
                        # Add a new asset to fixed assets table!
                        asset_id = f"custom_asset_{int(datetime.now().timestamp())}"
                        new_asset = {
                            "code": "AST-COMP-099",
                            "name": "PowerEdge R750 Virtualization Host",
                            "purchase_value": cost,
                            "salvage_value": 1500.00,
                            "useful_life_years": 5
                        }
                        db_instance.insert("fixed_assets_asset", asset_id, new_asset)
                        db_instance.commit()
                        
                        audit_log("fixed_assets", f"CAPEX: Purchased PowerEdge R750 Rack Server - Capitalized under Category Equipment (1600) for ${cost:,.2f}", "INFO")
                        
                        response = {
                            "status": "success",
                            "data": {
                                "debit_account": "[1600] Warehouse Machinery / Hardware",
                                "credit_account": "[1020] Chase Operating Account (Cash)",
                                "amount": cost
                            }
                        }
                    else:
                        raise Exception("Required accounts for equipment capex not found.")
                        
                elif tx_type == 'salaries':
                    # Engineering salaries: Debit Engineering salaries (Expense), Credit Cash (Asset)
                    sal_cost = 145000.00
                    gl_accounts = db_instance.query("general_ledger_account")
                    sal_acc = next((a for a in gl_accounts if a['account_number'] == '5100'), None)
                    cash_acc = next((a for a in gl_accounts if a['account_number'] == '1020'), None)
                    
                    if sal_acc and cash_acc:
                        db_instance.begin()
                        sal_acc['balance'] = float(sal_acc['balance']) + sal_cost
                        cash_acc['balance'] = float(cash_acc['balance']) - sal_cost
                        db_instance.update("general_ledger_account", '5100', sal_acc)
                        db_instance.update("general_ledger_account", '1020', cash_acc)
                        db_instance.commit()
                        
                        audit_log("general_ledger", f"POST: Monthly payroll dispatch - Debited Salaries & Wages Expense (5100) and Credited Operating Cash (1020) for ${sal_cost:,.2f}", "INFO")
                        
                        response = {
                            "status": "success",
                            "data": {
                                "debit_account": "[5100] Engineering Salaries",
                                "credit_account": "[1020] Chase Operating Account",
                                "amount": sal_cost
                            }
                        }
                    else:
                        raise Exception("Required accounts for payroll dispatch not found.")
                else:
                    raise Exception("Unsupported transaction type simulator.")
                    
            except Exception as e:
                response = {"status": "error", "message": str(e)}
                
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_error(404, "Endpoint not found")

def start_server():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), AuraLedgerHTTPHandler) as httpd:
        print(f"==================================================")
        print(f"  Auraledger Finance & Accounting Server Running  ")
        print(f"  Localhost URL: http://localhost:{PORT}          ")
        print(f"==================================================")
        print("Press Ctrl+C to terminate.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")

if __name__ == '__main__':
    start_server()
