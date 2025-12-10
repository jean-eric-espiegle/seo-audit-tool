<template>
	<NuxtLayout>
		<NuxtPage />
	</NuxtLayout>
</template>

<style>
/* GLOBAL RESET */
* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
	font-family: "Inter", system-ui, sans-serif;
}

html {
	transition: background 0.3s ease, color 0.3s ease;
}

body {
	background: var(--bg);
	color: var(--text);
	padding: 32px;
}

/* LIGHT THEME VARIABLES */
:root {
	--bg: #f5f6fa;
	--text: #1f2937;
	--card-bg: #ffffff;
	--card-shadow: rgba(0, 0, 0, 0.06);
	--border: #cbd5e1;
	--input-bg: #ffffff;

	--primary: #2563eb;
	--primary-dark: #1e40af;
	--good: #16a34a;
	--bad: #dc2626;

	--tag-bg: #e0edff;
	--tag-text: #1d4ed8;
}

/* DARK MODE OVERRIDES */
.dark {
	--bg: #0d1117;
	--text: #d1d5db;
	--card-bg: #161b22;
	--card-shadow: rgba(0, 0, 0, 0.4);
	--border: #30363d;
	--input-bg: #0f141a;

	--primary: #3b82f6;
	--primary-dark: #1d4ed8;
	--good: #22c55e;
	--bad: #f87171;

	--tag-bg: #233876;
	--tag-text: #93c5fd;
}

/* GENERAL STYLES */
.container {
	max-width: 1100px;
	margin: auto;
}

.card {
	background: var(--card-bg);
	border-radius: 16px;
	padding: 24px;
	margin-bottom: 24px;
	box-shadow: 0px 4px 30px var(--card-shadow);
}

.input {
	padding: 14px;
	border-radius: 12px;
	border: 1px solid var(--border);
	background: var(--input-bg);
	color: var(--text);
	width: 100%;
	transition: 0.2s ease;
}

.input:focus {
	border-color: var(--primary);
	box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.3);
}

.btn {
	background: var(--primary);
	color: white;
	padding: 14px 26px;
	border-radius: 12px;
	border: none;
	cursor: pointer;
	font-weight: 500;
	transition: 0.2s;
}

.btn:hover {
	background: var(--primary-dark);
}

.btn:disabled {
	background: #6b7280;
	cursor: not-allowed;
}

.grid {
	display: grid;
	gap: 20px;
}

.grid-2 {
	grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
}

.tag {
	background: var(--tag-bg);
	color: var(--tag-text);
	padding: 6px 14px;
	border-radius: 20px;
	display: inline-block;
	font-size: 14px;
}

.good {
	color: var(--good);
	font-weight: 600;
}
.bad {
	color: var(--bad);
	font-weight: 600;
}

</style>
